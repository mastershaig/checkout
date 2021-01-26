Feature: CheckoutSystem
  Scenario: payment by default promotion rules 1
    Given product code: 001, 002, 003
    When spending over £30 and buy 2 or more pizzas
    Then total price equals to "29.65"


  Scenario: payment by default promotion rules 2
    Given product code: 001, 002, 003
    When not apply any promotions
    Then total price equals to "32.94"


  Scenario: payment by default promotion rules 3
    Given product code: 002, 001, 002
    When spending over £30 and buy 2 or more pizzas
    Then total price equals to "9.93"


  Scenario: payment by default promotion rules 4
    Given product code: 002, 001, 002
    When not apply any promotions
    Then total price equals to "13.93"


  Scenario: payment by default promotion rules 5
    Given product code: 002, 001, 002, 003
    When spending over £30 and buy 2 or more pizzas
    Then total price equals to "31.44"


  Scenario: payment by default promotion rules 6
    Given product code: 002, 001, 002, 003
    When not apply any promotions
    Then total price equals to "38.93"


  Scenario: payment by default promotion rules 7
    Given product code: 002, 003
    When spending over £30 and buy 2 or more pizzas
    Then total price equals to "27.89"


  Scenario: payment by default promotion rules 8
    Given product code: 002, 003
    When not apply any promotions
    Then total price equals to "30.99"


  Scenario: payment by custom promotion rules 9
    Given product code: 002, 003, 003, 003
    When spending over £30 and buy 3 or more T-Shirt
    Then total price equals to "45.89"


  Scenario: payment by custom promotion rules 10
    Given product code: 002, 003, 003, 003
    When not apply any promotions
    Then total price equals to "80.99"