Feature: CheckoutSystem
  Scenario: payment by default promotion rules 1
    Given product code: 001, 002, 003
    When spending over £60 and buy 2 or more Curry
    Then total price equals to "66.78"


  Scenario: payment by default promotion rules 2
    Given product code: 001, 002, 003
    When not apply any promotions
    Then total price equals to "74.2"


  Scenario: payment by default promotion rules 3
    Given product code: 001, 003, 001
    When spending over £60 and buy 2 or more Curry
    Then total price equals to "36.95"


  Scenario: payment by default promotion rules 4
    Given product code: 001, 003, 001
    When not apply any promotions
    Then total price equals to "38.45"


  Scenario: payment by default promotion rules 5
    Given product code: 001, 002, 001, 003
    When spending over £60 and buy 2 or more Curry
    Then total price equals to "73.75"


  Scenario: payment by default promotion rules 6
    Given product code: 001, 002, 001, 003
    When not apply any promotions
    Then total price equals to "83.45"


  Scenario: payment by default promotion rules 7
    Given product code: 001, 003
    When spending over £60 and buy 2 or more Curry
    Then total price equals to "29.2"


  Scenario: payment by default promotion rules 8
    Given product code: 001, 003
    When not apply any promotions
    Then total price equals to "29.2"


  Scenario: payment by custom promotion rules 9
    Given product code: 001, 003, 003, 003
    When spending over £60 and buy 3 or more T-Shirt
    Then total price equals to "48.83"


  Scenario: payment by custom promotion rules 10
    Given product code: 001, 003, 003, 003
    When not apply any promotions
    Then total price equals to "69.1"