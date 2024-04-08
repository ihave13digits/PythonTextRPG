import random

from game_data import *

class Shop():

    def __init__(self, GOLD=1000, MARKUP=1.0, STOCK=10):
        self.gold = GOLD
        self.markup = MARKUP
        self.inventory = {}
        self.item_types = []
        for i in range(STOCK):
            self.restock()

    def get_data(self):
        return {
                "gold" : self.gold,
                "markup" : self.markup,
                "inventory" : self.inventory,
                "item_types" : self.item_types,
            }

    def set_data(self, data):
        self.gold = data['gold']
        self.markup = data['markup']
        self.inventory = data['inventory']
        self.item_types = data['item_types']
        #input(self.item_types)

    def get_item_value(self, item):
        return items[item]['value']*self.markup

    def add_item(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def del_item(self, item):
        if item in self.inventory:
            if self.inventory[item] > 1:
                self.inventory[item] -= 1
            else:
                self.inventory.pop(item, None)

    def trade(self, shop):
        for i in items:
            if i != "nothing":
                if i in shop.inventory:
                    diff = self.inventory[i] - shop.inventory[i]
                    if diff < 0:
                        pass

    def restock(self):
        for i in items:
            if i != "nothing":
                if random.randint(0, 1000) < items[i]['rarity']:
                    self.inventory[i] = random.randint(1, items[i]['count'])
