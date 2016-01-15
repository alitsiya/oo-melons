"""This file should have our order classes in it."""
from random import randint
from datetime import datetime
from datetime import date

class AbstractMelonOrder(object):
    """Parent class for all orders"""


    def __init__(self, species, qty, country_code, tax, order_type):
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.order_type = order_type
        self.tax = tax

        self.shipped = False
        self.passed_inspection = None
        self.order_datetime = datetime.now()
        self.hour = self.order_datetime.hour
        self.day_of_the_week = datetime.weekday(self.order_datetime)


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        if self.qty < 10 and self.order_type == 'international':
            total += 3.00

        if (self.day_of_the_week in range(0,5)) and (self.hour in range(8,24)):
            total += 4.00

        return total

    def get_base_price(self):

        base_price = randint(5,9)

        return base_price


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True 


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, country_code=None, tax=0.08, order_type='domestic')
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, country_code, tax=0.17, order_type='international')

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(GovernmentMelonOrder, self).__init__(species, qty, country_code=None, tax=0, order_type='government')
        

    def inspect_melons(self):
      
        self.passed_inspection = True 


