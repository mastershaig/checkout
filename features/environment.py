from main.product import Product
from main.promotion_rule import PromotionRule


def before_scenario(context, scenario):
    """
    Create products and promotion rules before each scenario
    """
    context.product_1 = Product(product_code="001", name="Curry Sauce", price=1.95)
    context.product_2 = Product(product_code="002", name="Pizza", price=5.99)
    context.product_3 = Product(product_code="003", name="Men’s T-Shirt", price=25.00)

    # Promotion rules
    context.promotion_rule_1 = PromotionRule(promotion_name="spend over €30, you get 10% off", promotion_type="on_total_price",
                                             min_price=30.0, discount_rate=10)

    # Rule when you buy 2 or more pizzas, the price for each drops to €3.99.
    context.promotion_rule_2 = PromotionRule(promotion_name="promotion Pizza x2", promotion_type="on_item_price",
                                             promotion_price=3.99, min_quantity=2)
    context.promotion_rule_2.add_product(context.product_2)
