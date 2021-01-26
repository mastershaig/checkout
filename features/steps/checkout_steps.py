# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from main.product import Product


@given('mass assignment')
def step_impl(context):
    product_list = []
    for row in context.table.rows:
        product = Product(product_code=row[0], name=row[1], price=float(row[2]))
        product_list.append(product)
    context.product_list = product_list


@when('something happen')
def step_impl(context):
    assert len(context.product_list) == 3
