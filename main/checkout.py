import functools


class Checkout(object):

    def __init__(self, promotion_rules=[]):
        self.promo_rules = promotion_rules
        self.co_products = []

        self.validate_promotion_rules()

    def scan(self, product):
        self.co_products.append(product)
        return True

    def subtotal(self):
        return functools.reduce(lambda sum, cal: sum + cal.price, self.co_products)


    def validate_promotion_rules(self):
        if all([rule.valid() for rule in self.promo_rules]):
            for rule in self.promo_rules:
                if not rule.valid():
                    raise ValueError(f"Promotion {rule.promotion_name} is not valid,\n{rule.error_messages}")

    def total(self):
        if not self.promo_rules:
            return self.subtotal()

        promo_rules_for_item = list(filter(lambda rule: rule.promotion_type == 'on_item_price', self.promo_rules))
        promo_rule_for_total = next(rule for rule in self.promo_rules if rule.promotion_type == 'on_total_price')
        total_price_without_promo = self.subtotal()

        for rule in promo_rules_for_item:
            for product in self.co_products:
                co_qty = len(list(filter(lambda p: p.product_code == product.product_code, self.co_products)))
                if rule.applicable(product=product, quantity=co_qty):
                    continue
                product.price = rule.promotion_price

        total_price = self.subtotal()
        if promo_rule_for_total.applicable(total_price=total_price_without_promo):
            total_price -= (promo_rule_for_total.discount_rate / 100 * total_price)
        return round(total_price, 2)