Feature: CheckoutSystem
  Scenario: payment by default promotion rules for product codes: 001, 002, 003
    Given product code: 001, 002, 003
    When spending over £30 and buy 2 or more pizzas
    Then total price equals to "29.65"


  Scenario: payment without promotions for product codes: 001, 002, 003
    Given product code: 001, 002, 003
    When not apply any promotions
    Then total price equals to "32.94"


  Scenario: payment by default promotion rules for product codes: 002, 001, 002
    Given product code: 002, 001, 002
    When spending over £30 and buy 2 or more pizzas
    Then total price equals to "9.93"


  Scenario: payment without promotions for product codes: 002, 001, 002
    Given product code: 002, 001, 002
    When not apply any promotions
    Then total price equals to "13.93"


  Scenario: payment by default promotion rules for product codes: product code: 002, 001, 002, 003
    Given product code: 002, 001, 002, 003
    When spending over £30 and buy 2 or more pizzas
    Then total price equals to "31.44"


  Scenario: payment without promotions for product codes: 002, 001, 002, 003
    Given product code: 002, 001, 002, 003
    When not apply any promotions
    Then total price equals to "38.93"


  Scenario: payment by default promotion rules for product codes: product code: 002, 003
    Given product code: 002, 003
    When spending over £30 and buy 2 or more pizzas
    Then total price equals to "27.89"


  Scenario: payment without promotions for product codes: 002, 003
    Given product code: 002, 003
    When not apply any promotions
    Then total price equals to "30.99"


  Scenario: payment by default promotion rules for product codes: product code: 002, 003, 003, 003
    Given product code: 002, 003, 003, 003
    When spending over £30 and buy 3 or more T-Shirt
    Then total price equals to "45.89"


  Scenario: payment without promotions for product codes: 002, 003, 003, 003
    Given product code: 002, 003, 003, 003
    When not apply any promotions
    Then total price equals to "80.99"