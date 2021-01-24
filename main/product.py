class Product(object):
    """
        Product class
    """

    def __init__(self, **kwargs):
        self.product_code = kwargs.get("product_code")
        self.name = kwargs.get('name')
        self.price = kwargs.get('price')
