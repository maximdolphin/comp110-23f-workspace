"""Defining a class!"""

from __future__ import annotations

class Pizza:
    
    # attributes
    # Think of these as the variables
    # each instance of the class will have
    # <name> : <type>
    
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str):
        """My constructor"""
        self.size = inp_size

    def price(self) -> float:
     if self.size == "large":
        price: float = 6.25
     else:
        price: float = 5.00
     price += .75 * self.toppings
     if self.gluten_free:
        price += 1.00
     return price   

    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
       """Make a new pizza with existing pizza's properties and add toppings."""
       new_pizza    
