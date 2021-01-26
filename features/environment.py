from main.product import Product
from main.promotion_rule import PromotionRule


def before_scenario(context, scenario):
    context.product_1 = Product(product_code="001", name="Curry Sauce", price=9.25)
    context.product_2 = Product(product_code="002", name="Pizza", price=45.00)
    context.product_3 = Product(product_code="003", name="Men’s T-Shirt", price=19.95)

    context.promotion_rule_1 = PromotionRule(promotion_name="promotion 60 price", promotion_type="on_total_price",
                                             min_price=60.0, discount_rate=10)

    context.promotion_rule_2 = PromotionRule(promotion_name="promotion Curry x2", promotion_type="on_item_price",
                                             promotion_price=8.5, min_quantity=2)
    context.promotion_rule_2.add_product(context.product_1)
