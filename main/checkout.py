import functools


class Checkout(object):
    """
        Checkout system
    """

    def __init__(self, promotion_rules=[]):
        """
            Initialize checkout class
            :param promotion_rules:
        """
        self.promo_rules = promotion_rules
        self.co_products = []  # products already scanned

        # check validation of promotion rules and raise error if any
        self.validate_promotion_rules()

    def scan(self, product):
        """
            Scan product adding to checkout system
            :param product:
            :return: bool
        """
        self.co_products.append(product)
        return True

    def subtotal(self):
        """
            Subtotal price without
            applying promotion code
            :return: float
        """
        return functools.reduce(lambda sum, cal: sum + float(cal.price), self.co_products, 0)

    def total(self):
        """
            Total price after promotion rule
            :return: float
        """
        if not self.promo_rules:
            return round(self.subtotal(), 2)

        promo_rules_for_item = list(filter(lambda rule: rule.promotion_type == 'on_item_price', self.promo_rules))
        promo_rule_for_total = next(rule for rule in self.promo_rules if rule.promotion_type == 'on_total_price')
        total_price_without_promo = self.subtotal()

        # apply promotion code for each item of promo_rules_for_item
        for rule in promo_rules_for_item:
            for product in self.co_products:
                co_qty = len(list(filter(lambda p: p.product_code == product.product_code, self.co_products)))
                if not rule.applicable(product=product, quantity=co_qty):
                    continue
                # set promotion price for the product if rule can apply on this product
                product.price = rule.promotion_price

        # recalculate total price with promotion for item
        total_price = self.subtotal()
        # apply promotion code for total price of promo_rule_for_total
        if promo_rule_for_total.applicable(total_price=total_price_without_promo):
            total_price -= (promo_rule_for_total.discount_rate / 100 * total_price)
        return round(total_price, 2)

    def validate_promotion_rules(self):
        """
            Validate promoting rule
            :return:
        """
        if all([rule.valid() for rule in self.promo_rules]):
            for rule in self.promo_rules:
                if not rule.valid():
                    raise ValueError(f"Promotion {rule.promotion_name} is not valid,\n{rule.error_messages}")
