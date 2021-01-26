from behave import given, when, then, step
from main.product import Product
from main.promotion_rule import PromotionRule
from main.checkout import Checkout

product_1 = Product(product_code="001", name="Curry Sauce", price=9.25)
product_2 = Product(product_code="002", name="Pizza", price=45.00)
product_3 = Product(product_code="003", name="Men’s T-Shirt", price=19.95)

promotion_rule_1 = PromotionRule(promotion_name="promotion 60 price", promotion_type="on_total_price",
                                 min_price=60.0, discount_rate=10)

promotion_rule_2 = PromotionRule(promotion_name="promotion Curry x2", promotion_type="on_item_price",
                                 promotion_price=8.5, min_quantity=2)
promotion_rule_2.add_product(product_1)


@given('payment by default promotion rules')
def step_impl(context):
    context.basket = [product_1, product_2, product_3]


@when('spending over £60 and buy 2 or more Curry')
def step_impl(context):
    context.promotion_rules = [promotion_rule_1, promotion_rule_2]


@then('return total price should equal to "{price}"')
def step_impl(context, price):
    co = Checkout(context.promotion_rules)
    for val in context.basket:
        co.scan(val)
    assert co.total() == float(price)

