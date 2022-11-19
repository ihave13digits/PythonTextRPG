items = {
        ## None
        'nothing'                   : {"type" : "", "attack" : 0, "defense" : 0, "value" : 0, "rarity" : 0, "count" : 0},
        
        ## Consumable

        # Food
        'porridge'                  : {"type" : "food", "hp" : 5, "mp" : 5, "value" : 25, "rarity" : 150, "count" : 2},
        'haggis'                    : {"type" : "food", "hp" : 15, "mp" : 15, "value" : 50, "rarity" : 50, "count" : 5},
        'bread'                     : {"type" : "food", "hp" : 5, "mp" : 5, "value" : 25, "rarity" : 150, "count" : 2},
		'kebab'                     : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 50, "rarity" : 50, "count" : 5},
        'steak'                     : {"type" : "food", "hp" : 15, "mp" : 15, "value" : 50, "rarity" : 50, "count" : 5},
        'soup'                      : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 25, "rarity" : 100, "count" : 4},
        'stew'                      : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 25, "rarity" : 100, "count" : 4},

        # Potion
        'health potion'             : {"type" : "potion", "hp" : 25, "value" : 100, "rarity" : 250, "count" : 10},
        'mana potion'               : {"type" : "potion", "mp" : 25, "value" : 100, "rarity" : 200, "count" : 10},
        'elixer'                    : {"type" : "potion", "hp" : 25, "mp" : 25, "value" : 250, "rarity" : 100, "count" : 5},
        'restoration potion'        : {"type" : "potion", "hp" : 10000000, "mp" : 10000000, "value" : 1000, "rarity" : 50, "count" : 2},
        'potion of blessings'       : {"type" : "potion", "mag" : 1, "atk" : 1, "def" : 1, "value" : 50000, "rarity" : 1, "count" : 2},
        'potion of magic'           : {"type" : "potion", "mag" : 1, "value" : 25000, "rarity" : 2, "count" : 2},
        'potion of attack'          : {"type" : "potion", "atk" : 1, "value" : 25000, "rarity" : 2, "count" : 2},
        'potion of defense'         : {"type" : "potion", "def" : 1, "value" : 25000, "rarity" : 2, "count" : 2},
        'potion of health'          : {"type" : "potion", "HP" : 1, "value" : 25000, "rarity" : 5, "count" : 2},
        'potion of mana'            : {"type" : "potion", "MP" : 1, "value" : 25000, "rarity" : 5, "count" : 2},

        # Scroll
        'scroll of fireball'        : {"type" : "scroll", "spell" : "fireball", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of lightning bolt'  : {"type" : "scroll", "spell" : "lightning bolt", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of flash flood'     : {"type" : "scroll", "spell" : "flash flood", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of ground collapse' : {"type" : "scroll", "spell" : "ground collapse", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of harm'            : {"type" : "scroll", "spell" : "harm", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of heal'            : {"type" : "scroll", "spell" : "heal", "value" : 5000, "rarity" : 2, "count" : 2},

        ## Arms
        
        # Weapon
        'club'                      : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 50, "rarity" : 250, "count" : 2, "slot" : "hand_"},
        'mace'                      : {"type" : "arms", "attack" : 3, "defense" : 0, "value" : 250, "rarity" : 150, "count" : 2, "slot" : "hand_"},
        'greatmace'                 : {"type" : "arms", "attack" : 5, "defense" : 1, "value" : 1000, "rarity" : 50, "count" : 2, "slot" : "hand_"},
        'war axe'                   : {"type" : "arms", "attack" : 4, "defense" : 2, "value" : 1000, "rarity" : 100, "count" : 2, "slot" : "hand_"},
        'dagger'                    : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : "hand_"},
        'shortsword'                : {"type" : "arms", "attack" : 2, "defense" : 1, "value" : 500, "rarity" : 150, "count" : 2, "slot" : "hand_"},
        'longsword'                 : {"type" : "arms", "attack" : 3, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : "hand_"},
        'greatsword'                : {"type" : "arms", "attack" : 4, "defense" : 2, "value" : 1000, "rarity" : 50, "count" : 2, "slot" : "hand_"},
        # Shield
        'buckler'                   : {"type" : "arms", "attack" : 1, "defense" : 2, "value" : 50, "rarity" : 100, "count" : 2, "slot" : "hand_"},
        'shield'                    : {"type" : "arms", "attack" : 1, "defense" : 3, "value" : 100, "rarity" : 50, "count" : 2, "slot" : "hand_"},
        'tower shield'              : {"type" : "arms", "attack" : 1, "defense" : 5, "value" : 250, "rarity" : 25, "count" : 2, "slot" : "hand_"},
        
        ## Armor
        
        # Head
        'coif'                      : {"type" : "armor", "attack" : 0, "defense" : 3, "value" : 250, "rarity" : 15, "count" : 2, "slot" : "head"},
        'greathelm'                 : {"type" : "armor", "attack" : 0, "defense" : 5, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "head"},
        # Neck
        'cloak'                     : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 100, "rarity" : 25, "count" : 3, "slot" : "neck"},
        'gorget'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 3, "slot" : "neck"},
        'necklace'                  : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 500, "rarity" : 5, "count" : 2, "slot" : "neck"},
        'magic necklace'            : {"type" : "armor", "magic" : 1, "attack" : 0, "defense" : 0, "value" : 2500, "rarity" : 2, "count" : 2, "slot" : "neck"},
        'blessed necklace'          : {"type" : "armor", "magic" : 1, "attack" : 1, "defense" : 1, "value" : 2500, "rarity" : 1, "count" : 2, "slot" : "neck"},
        # Shoulders
        'pauldrons'                 : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 100, "rarity" : 25, "count" : 3, "slot" : "shoulders"},
        # Torso
        'shirt'                     : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 25, "rarity" : 75, "count" : 2, "slot" : "torso"},
        'ringmail'                  : {"type" : "armor", "attack" : 0, "defense" : 6, "value" : 500, "rarity" : 15, "count" : 2, "slot" : "torso"},
        'hauberk'                   : {"type" : "armor", "attack" : 0, "defense" : 8, "value" : 750, "rarity" : 10, "count" : 2, "slot" : "torso"},
        'breastplate'               : {"type" : "armor", "attack" : 0, "defense" : 10, "value" : 1000, "rarity" : 5, "count" : 2, "slot" : "torso"},
        # Waist
        'belt'                      : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 50, "rarity" : 100, "count" : 2, "slot" : "waist"},
        'chainskirt'                : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 50, "count" : 2, "slot" : "waist"},
        'tassets'                   : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 50, "count" : 2, "slot" : "waist"},
        'fauld'                     : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "waist"},
        'chainskirt'                : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 50, "count" : 2, "slot" : "waist"},
        # Arms
        'bracers'                   : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "arms"},
        'vambrace'                  : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "arms"},
        'rerebrace'                 : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "arms"},
        'full cannon'               : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 250, "rarity" : 25, "count" : 2, "slot" : "arms"},
        # Legs
        'pants'                     : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 50, "rarity" : 50, "count" : 2, "slot" : "legs"},
        'cuisse'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "legs"},
        'poleyn'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "legs"},
        'chausses'                  : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 300, "rarity" : 25, "count" : 2, "slot" : "legs"},
        # Hands
        'gloves'                    : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 150, "rarity" : 20, "count" : 2, "slot" : "hands"},
        'chain gloves'              : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 150, "rarity" : 20, "count" : 2, "slot" : "hands"},
        'gauntlets'                 : {"type" : "armor", "attack" : 1, "defense" : 2, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "hands"},
        # Feet
        'boots'                     : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 150, "rarity" : 25, "count" : 2, "slot" : "feet"},
        'chain boots'               : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
        'sabatons'                  : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
        'greaves'                   : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
        'full greaves'              : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
    }



crafting = {
		# Armor
        'full cannon'  : {'take':{'vambrace':1, 'rerebrace':1, 'bracers':1}, 'give':{'full cannon':1}},
        'chausses'     : {'take':{'cuisse':1, 'poleyn':1}, 'give':{'chausses':1}},
		'full greaves' : {'take':{'sabatons':1, 'greaves':1}, 'give':{'full greaves':1}},
    }
