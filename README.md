# Problem Description

Implement a checkout system that can scan items in any order and apply certain promotional campaigns to give discounts. The system needs to be flexible regarding the promotional rules.

Here is an example of what the products could be and what they could look like. You're free to define your own representation. The easy addition of new products is a requirement of the system.


Product code  | Name           | Price
--------------|----------------|------------------
001           | Curry Sauce         | 1.95 €
002           | Pizza | 5.99 €
003           | Men’s T-Shirt          | 25.00 €

The following promotional rules are only used for the example. You're free to define your own ones.

- If you spend over €30, you get 10% off your purchase.
- If you buy 2 or more pizzas, the price for each drops to €3.99.

## Installation
- Open a command line window and go to the project's directory.

- `pip install -r requirements.txt`

## Usage

- run `behave` to run all behavior tests

## Test Results
![ScreenShot](https://i.ibb.co/52W9KVs/Screen-Shot-2021-01-26-at-07-20-25.png" )
