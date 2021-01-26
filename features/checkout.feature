Feature: CheckoutSystem
  Scenario: spending over £60 and buy 2 or more Curry
    Given payment by default promotion rules
    When spending over £60 and buy 2 or more Curry
    Then return total price should equal to "66.78"

  Scenario: no apply any promotions
    Given payment by default promotion rules
    When no apply any promotions
    Then return total price should equal to "74.2"