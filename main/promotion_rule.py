class PromotionRule(object):


    def __init__(self, **kwargs):

        self.promotion_name = kwargs.get('promotion_name')
        self.promotion_type = kwargs.get('promotion_type')
        self.min_price = kwargs.get('min_price')
        self.min_quantity = kwargs.get('min_quantity')
        self.promotion_price = kwargs.get('promotion_price')
        self.discount_rate = kwargs.get('discount_rate')
        self.status = kwargs.get('status', 'active')
        self.products = []

    def add_product(self, product):

        self.products.append(product)
        return True
