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
    	pass