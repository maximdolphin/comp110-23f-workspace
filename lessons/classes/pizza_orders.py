"""Instantiating A Class."""

from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza() # constructor
my_pizza.size = "medium"
my_pizza.toppings = 3
my_pizza.gluten_free = False

def price(input_pizza: Pizza) -> float:
    """Calculates the price"""
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price