from behave import given, when, then, step
from main.promotion_rule import PromotionRule
from main.checkout import Checkout


@given('product code: 001, 002, 003')
def step_impl(context):
    context.basket = [context.product_1, context.product_2, context.product_3]


@when('spending over £60 and buy 2 or more Curry')
def step_impl(context):
    context.promotion_rules = [context.promotion_rule_1, context.promotion_rule_2]


@then('total price equals to "{price}"')
def step_impl(context, price):
    co = Checkout(context.promotion_rules)
    for val in context.basket:
        co.scan(val)

    cal = co.total()
    assert cal == float(price)


@when('not apply any promotions')
def step_impl(context):
    context.promotion_rules = []


@given('product code: 001, 003, 001')
def step_impl(context):
    context.basket = [context.product_1, context.product_3, context.product_1]


@given('product code: 001, 002, 001, 003')
def step_impl(context):
    context.basket = [context.product_1, context.product_2, context.product_1, context.product_3]


@given('product code: 001, 001')
def step_impl(context):
    context.basket = [context.product_1, context.product_1]


@given('product code: 001, 003')
def step_impl(context):
    context.basket = [context.product_1, context.product_3]


@given('product code: 001, 003, 003, 003')
def step_impl(context):
    context.basket = [context.product_1, context.product_3, context.product_3, context.product_3]


@when('spending over £60 and buy 3 or more T-Shirt')
def step_impl(context):
    promotion_rule = PromotionRule(promotion_name="promotion T-Shirt x3", promotion_type="on_item_price",
                                   promotion_price=15, min_quantity=3)
    promotion_rule.add_product(context.product_3)
    context.promotion_rules = [context.promotion_rule_1, promotion_rule]
