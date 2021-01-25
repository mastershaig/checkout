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


    def applicable(self, product=None, quantity=0, total_price=0):

        if self.promotion_type == 'on_item_price':
            result = []
            for item in self.products:
                if item.product_code == product.product_code:
                    result.append(product)
            return result and quantity >= self.min_quantity
        elif self.promotion_type == 'on_total_price':
            return total_price >= self.min_price

    def valid(self):
        if self.error():
            return False
        else:
            return True

    def error(self):
        errors = []
        if self.promotion_type == 'on_item_price':
            if not self.products:
                errors.append("products is required")
            if not self.min_quantity:
                errors.append("min_quantity is required")
        elif self.promotion_type == 'on_total_price':
            if not self.min_price:
                errors.append("min_price is required")

        self.error_messages = errors
        return errors