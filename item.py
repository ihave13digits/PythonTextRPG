items = {
        ## None
        'nothing'                   : {"type" : "", "attack" : 0, "defense" : 0, "value" : 0, "rarity" : 0, "count" : 0},
        
        ## Consumable

        # Food
        'porridge'                  : {"type" : "food", "hp" : 5, "mp" : 5, "value" : 25, "rarity" : 150, "count" : 2},
        'haggis'                    : {"type" : "food", "hp" : 15, "mp" : 15, "value" : 50, "rarity" : 50, "count" : 5},
        'bread'                     : {"type" : "food", "hp" : 5, "mp" : 5, "value" : 25, "rarity" : 150, "count" : 2},
		'kebab'                     : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 50, "rarity" : 50, "count" : 5},
        'fish'                      : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 25, "rarity" : 50, "count" : 5},
        'steak'                     : {"type" : "food", "hp" : 15, "mp" : 15, "value" : 50, "rarity" : 50, "count" : 5},
        'soup'                      : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 25, "rarity" : 100, "count" : 4},
        'stew'                      : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 25, "rarity" : 100, "count" : 4},

        # Potion
        'minor health potion'       : {"type" : "potion", "hp" : 10, "value" : 500, "rarity" : 250, "count" : 10},
        'health potion'             : {"type" : "potion", "hp" : 25, "value" : 250, "rarity" : 100, "count" : 5},
        'major health potion'       : {"type" : "potion", "hp" : 50, "value" : 100, "rarity" : 50, "count" : 2},
        'minor mana potion'         : {"type" : "potion", "mp" : 10, "value" : 500, "rarity" : 250, "count" : 10},
        'mana potion'               : {"type" : "potion", "mp" : 25, "value" : 250, "rarity" : 100, "count" : 5},
        'major mana potion'         : {"type" : "potion", "mp" : 50, "value" : 100, "rarity" : 50, "count" : 2},
        'elixer'                    : {"type" : "potion", "hp" : 25, "mp" : 25, "value" : 250, "rarity" : 100, "count" : 5},
        'restoration potion'        : {"type" : "potion", "hp" : 10000000, "mp" : 10000000, "value" : 1000, "rarity" : 50, "count" : 2},
        'potion of blessings'       : {"type" : "potion", "mag" : 1, "atk" : 1, "def" : 1, "value" : 50000, "rarity" : 1, "count" : 2},
        'potion of magic'           : {"type" : "potion", "mag" : 1, "value" : 25000, "rarity" : 2, "count" : 2},
        'potion of attack'          : {"type" : "potion", "atk" : 1, "value" : 25000, "rarity" : 2, "count" : 2},
        'potion of defense'         : {"type" : "potion", "def" : 1, "value" : 25000, "rarity" : 2, "count" : 2},
        'potion of health'          : {"type" : "potion", "HP" : 1, "value" : 25000, "rarity" : 5, "count" : 2},
        'potion of mana'            : {"type" : "potion", "MP" : 1, "value" : 25000, "rarity" : 5, "count" : 2},

        # Scroll
        #
        'scroll of firestorm'         : {"type" : "scroll", "spell" : "firestorm", "value" : 5000, "rarity" : 5, "count" : 2},
        'scroll of lightning barrage' : {"type" : "scroll", "spell" : "lightning barrage", "value" : 5000, "rarity" : 5, "count" : 2},
        'scroll of tsunami'           : {"type" : "scroll", "spell" : "tsunami", "value" : 5000, "rarity" : 5, "count" : 2},
        'scroll of earthquake'        : {"type" : "scroll", "spell" : "earthquake", "value" : 5000, "rarity" : 5, "count" : 2},
        'scroll of destroy'           : {"type" : "scroll", "spell" : "destroy", "value" : 5000, "rarity" : 5, "count" : 2},
        #
        'scroll of fireblast'         : {"type" : "scroll", "spell" : "fireblast", "value" : 2500, "rarity" : 10, "count" : 2},
        'scroll of lightning'         : {"type" : "scroll", "spell" : "lightning", "value" : 2500, "rarity" : 10, "count" : 2},
        'scroll of flash flood'       : {"type" : "scroll", "spell" : "flash flood", "value" : 2500, "rarity" : 10, "count" : 2},
        'scroll of fissure'           : {"type" : "scroll", "spell" : "fissure", "value" : 2500, "rarity" : 10, "count" : 2},
        'scroll of kill'              : {"type" : "scroll", "spell" : "kill", "value" : 2500, "rarity" : 10, "count" : 2},
        #
        'scroll of fireball'          : {"type" : "scroll", "spell" : "fireball", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of lightning bolt'    : {"type" : "scroll", "spell" : "lightning bolt", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of water burst'       : {"type" : "scroll", "spell" : "water burst", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of ground collapse'   : {"type" : "scroll", "spell" : "ground collapse", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of harm'              : {"type" : "scroll", "spell" : "harm", "value" : 1000, "rarity" : 25, "count" : 2},
        #
        'scroll of burn'              : {"type" : "scroll", "spell" : "burn", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of electric shock'    : {"type" : "scroll", "spell" : "electric shock", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of poison rain'       : {"type" : "scroll", "spell" : "poison rain", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of tremor'            : {"type" : "scroll", "spell" : "tremor", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of decay'             : {"type" : "scroll", "spell" : "decay", "value" : 1000, "rarity" : 25, "count" : 2},
        #
        'scroll of heal'              : {"type" : "scroll", "spell" : "heal", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of heal all'          : {"type" : "scroll", "spell" : "heal all", "value" : 2500, "rarity" : 5, "count" : 2},
        'scroll of cure'              : {"type" : "scroll", "spell" : "cure", "value" : 2500, "rarity" : 10, "count" : 2},
        'scroll of cure all'          : {"type" : "scroll", "spell" : "cure all", "value" : 5000, "rarity" : 5, "count" : 2},
        'scroll of cure poison'       : {"type" : "scroll", "spell" : "cure poison", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of cure confusion'    : {"type" : "scroll", "spell" : "cure confusion", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of cure stun'         : {"type" : "scroll", "spell" : "cure stun", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of cure burn'         : {"type" : "scroll", "spell" : "cure burn", "value" : 1000, "rarity" : 25, "count" : 2},
        #
        'scroll of inflict poison'    : {"type" : "scroll", "spell" : "inflict poison", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of inflict confusion' : {"type" : "scroll", "spell" : "inflict confusion", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of inflict stun'      : {"type" : "scroll", "spell" : "inflict stun", "value" : 1000, "rarity" : 25, "count" : 2},
        'scroll of inflict burn'      : {"type" : "scroll", "spell" : "inflict burn", "value" : 1000, "rarity" : 25, "count" : 2},
        
        ## Arms
        
        # Bludgeon
        'club'                      : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 50, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'spiked club'               : {"type" : "arms", "attack" : 2, "defense" : 0, "value" : 100, "rarity" : 200, "count" : 2, "slot" : " hand"},
        'mace'                      : {"type" : "arms", "attack" : 3, "defense" : 0, "value" : 250, "rarity" : 150, "count" : 2, "slot" : " hand"},
        'greatmace'                 : {"type" : "arms", "attack" : 5, "defense" : 2, "value" : 1000, "rarity" : 50, "count" : 2, "slot" : " hand"},
        'morning star'              : {"type" : "arms", "attack" : 4, "defense" : 1, "value" : 750, "rarity" : 50, "count" : 2, "slot" : " hand"},
        'war hammer'                : {"type" : "arms", "attack" : 4, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        # Axe
        'war axe'                   : {"type" : "arms", "attack" : 4, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'great war axe'             : {"type" : "arms", "attack" : 5, "defense" : 1, "value" : 1000, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'igorot'                    : {"type" : "arms", "attack" : 4, "defense" : 1, "value" : 1000, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'lochaber axe'              : {"type" : "arms", "attack" : 4, "defense" : 1, "value" : 1000, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'bardiche'                  : {"type" : "arms", "attack" : 5, "defense" : 2, "value" : 1000, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'halberd'                   : {"type" : "arms", "attack" : 5, "defense" : 2, "value" : 1000, "rarity" : 100, "count" : 2, "slot" : " hand"},
        # Dagger
        'dagger'                    : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'athame'                    : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'pugio'                     : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'cinquedea'                 : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'dirk'                      : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'acinaces'                  : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'anelace'                   : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        # Knife
        'kiridashi'                 : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'karambit'                  : {"type" : "arms", "attack" : 2, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'puuko'                     : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'sgian dubh'                : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'tanto'                     : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'kirpan'                    : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'seax'                      : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'kukri'                     : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        'machete'                   : {"type" : "arms", "attack" : 2, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : " hand"},
        # Sword
        'bastardsword'              : {"type" : "arms", "attack" : 3, "defense" : 2, "value" : 500, "rarity" : 150, "count" : 2, "slot" : " hand"},
        'shortsword'                : {"type" : "arms", "attack" : 2, "defense" : 1, "value" : 500, "rarity" : 150, "count" : 2, "slot" : " hand"},
        'longsword'                 : {"type" : "arms", "attack" : 3, "defense" : 2, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'rapier'                    : {"type" : "arms", "attack" : 3, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'sabre'                     : {"type" : "arms", "attack" : 3, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'falchion'                  : {"type" : "arms", "attack" : 4, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'scimitar'                  : {"type" : "arms", "attack" : 4, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'kopesh'                    : {"type" : "arms", "attack" : 3, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'kopis'                     : {"type" : "arms", "attack" : 3, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'katana'                    : {"type" : "arms", "attack" : 4, "defense" : 2, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        # Great Sword
        'uchigatana'                : {"type" : "arms", "attack" : 5, "defense" : 2, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'greatsword'                : {"type" : "arms", "attack" : 4, "defense" : 2, "value" : 1000, "rarity" : 50, "count" : 2, "slot" : " hand"},
        'claymore'                  : {"type" : "arms", "attack" : 4, "defense" : 2, "value" : 1000, "rarity" : 50, "count" : 2, "slot" : " hand"},
        'flamberge'                 : {"type" : "arms", "attack" : 5, "defense" : 2, "value" : 1000, "rarity" : 50, "count" : 2, "slot" : " hand"},
        # Shield
        'buckler'                   : {"type" : "arms", "attack" : 1, "defense" : 1, "value" : 50, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'shield'                    : {"type" : "arms", "attack" : 1, "defense" : 2, "value" : 100, "rarity" : 50, "count" : 2, "slot" : " hand"},
        'tower shield'              : {"type" : "arms", "attack" : 1, "defense" : 4, "value" : 250, "rarity" : 25, "count" : 2, "slot" : " hand"},
        # Ranged
        'flintlock pistol'          : {"type" : "arms", "attack" : 6, "defense" : 0, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'revolver'                  : {"type" : "arms", "attack" : 6, "defense" : 0, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'flintlock rifle'           : {"type" : "arms", "attack" : 8, "defense" : 0, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        'revolver rifle'            : {"type" : "arms", "attack" : 8, "defense" : 0, "value" : 750, "rarity" : 100, "count" : 2, "slot" : " hand"},
        
        ## Armor
        
        # Head
        'coif'                      : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 200, "rarity" : 15, "count" : 2, "slot" : "head"},
        'cervelliere'               : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 150, "rarity" : 15, "count" : 2, "slot" : "head"},
        'nasal helm'                : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 150, "rarity" : 15, "count" : 2, "slot" : "head"},
        'sallet'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 200, "rarity" : 15, "count" : 2, "slot" : "head"},
        'barbute'                   : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 250, "rarity" : 15, "count" : 2, "slot" : "head"},
        'greathelm'                 : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "head"},
        'bassinet'                  : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 250, "rarity" : 15, "count" : 2, "slot" : "head"},
        'close helm'                : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 250, "rarity" : 15, "count" : 2, "slot" : "head"},
        # Neck
        'cloak'                     : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 100, "rarity" : 25, "count" : 3, "slot" : "neck"},
        'bevor'                     : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 3, "slot" : "neck"},
        'gorget'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 3, "slot" : "neck"},
        'necklace'                  : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 500, "rarity" : 5, "count" : 2, "slot" : "neck"},
        'magic necklace'            : {"type" : "armor", "magic" : 1, "attack" : 0, "defense" : 0, "value" : 2500, "rarity" : 2, "count" : 2, "slot" : "neck"},
        'blessed necklace'          : {"type" : "armor", "magic" : 1, "attack" : 1, "defense" : 1, "value" : 2500, "rarity" : 1, "count" : 2, "slot" : "neck"},
        # Shoulders
        'spaulders'                 : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 3, "slot" : "shoulders"},
        'pauldrons'                 : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 100, "rarity" : 25, "count" : 3, "slot" : "shoulders"},
        # Torso
        'shirt'                     : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 25, "rarity" : 75, "count" : 2, "slot" : "torso"},
        'ringmail'                  : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 500, "rarity" : 15, "count" : 2, "slot" : "torso"},
        'hauberk'                   : {"type" : "armor", "attack" : 0, "defense" : 3, "value" : 750, "rarity" : 10, "count" : 2, "slot" : "torso"},
        'breastplate'               : {"type" : "armor", "attack" : 0, "defense" : 5, "value" : 1000, "rarity" : 5, "count" : 2, "slot" : "torso"},
        'coat of plates'            : {"type" : "armor", "attack" : 0, "defense" : 4, "value" : 750, "rarity" : 5, "count" : 2, "slot" : "torso"},
        'cuirass'                   : {"type" : "armor", "attack" : 0, "defense" : 4, "value" : 750, "rarity" : 5, "count" : 2, "slot" : "torso"},
        'leather cuirass'           : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 500, "rarity" : 5, "count" : 2, "slot" : "torso"},
        'studded leather cuirass'   : {"type" : "armor", "attack" : 0, "defense" : 3, "value" : 750, "rarity" : 5, "count" : 2, "slot" : "torso"},
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
        'full cannon'               : {"type" : "armor", "attack" : 0, "defense" : 3, "value" : 250, "rarity" : 25, "count" : 2, "slot" : "arms"},
        # Legs
        'pants'                     : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 50, "rarity" : 50, "count" : 2, "slot" : "legs"},
        'cuisse'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "legs"},
        'poleyn'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "legs"},
        'chausses'                  : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 300, "rarity" : 25, "count" : 2, "slot" : "legs"},
        # Hands
        'gloves'                    : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 150, "rarity" : 20, "count" : 2, "slot" : "hands"},
        'leather gloves'            : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 150, "rarity" : 20, "count" : 2, "slot" : "hands"},
        'chain gloves'              : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 150, "rarity" : 20, "count" : 2, "slot" : "hands"},
        'gauntlets'                 : {"type" : "armor", "attack" : 1, "defense" : 2, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "hands"},
        # Feet
        'boots'                     : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 150, "rarity" : 25, "count" : 2, "slot" : "feet"},
        'chain boots'               : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 200, "rarity" : 10, "count" : 2, "slot" : "feet"},
        'sabatons'                  : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
        'greaves'                   : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
        'full greaves'              : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 300, "rarity" : 10, "count" : 2, "slot" : "feet"},
    }



crafting = {
		# Armor
        'full cannon'  : {'take':{'vambrace':1, 'rerebrace':1, 'bracers':1}, 'give':{'full cannon':1}},
        'chausses'     : {'take':{'cuisse':1, 'poleyn':1}, 'give':{'chausses':1}},
		'full greaves' : {'take':{'sabatons':1, 'greaves':1}, 'give':{'full greaves':1}},
    }
