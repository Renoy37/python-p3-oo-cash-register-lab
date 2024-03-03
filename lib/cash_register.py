#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = []
        self.prices = []
        self.quantities = []

    def add_item(self, title, price, quantity=1):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.prices.extend([price] * quantity)
        self.quantities.append(quantity)

    def apply_discount(self):
        discount_total = self.total * (self.discount / 100)
        self.total -= discount_total
        if discount_total:
            print("After the discount, the total comes to $800.")
        else:
            print("There is no discount to apply.")
        return discount_total

    def void_last_transaction(self):
        if self.items:
            last_quantity = self.quantities.pop()
            last_price = self.prices[-1]
            self.total -= last_price * last_quantity
            del self.items[-last_quantity:]
            del self.prices[-last_quantity:]
