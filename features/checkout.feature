Feature: CheckoutSystem

  Scenario: Run a simple test
    Given mass assignment
     | Product code | Name          | Price |
     | 001          | Curry Sauce   | 1.95  |
     | 002          | Pizza         | 5.99  |
     | 003          | Men's T-Shirt | 25.00 |
    When something happen
