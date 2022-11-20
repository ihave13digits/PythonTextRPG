import random

from mob import *
from item import *
from magic import *

class Entity():

    def __init__(self, NAME, RACE, AI=True):
        self.is_ai = AI
        self.name = NAME
        self.race = RACE
        self.job = ""
        self.level = 1
        self.points = 0
        self.exp = 0
        self.level_up = mobs[RACE]['lup']
        self.experience = 0
        self.poisoned = False
        self.confused = False
        self.stunned = False
        self.burned = False
        
        self.hp = mobs[RACE]['hp']
        self.HP = mobs[RACE]['hp']
        self.mp = mobs[RACE]['mp']
        self.MP = mobs[RACE]['mp']
        self.magic = mobs[RACE]['mag']
        self.attack = mobs[RACE]['atk']
        self.defense = mobs[RACE]['def']

        self.gold = 100

        self.equip = {
                "left hand"  : 'nothing',
                "right hand" : 'nothing',
                "head"       : 'nothing',
                "neck"       : 'nothing',
                "shoulders"  : 'nothing',
                "torso"      : 'shirt',
                "waist"      : 'nothing',
                "arms"       : 'nothing',
                "legs"       : 'pants',
                "hands"      : 'nothing',
                "feet"       : 'nothing',
            }
        self.spells = {}
        self.inventory = {}

    def get_data(self):
        return {
                "name"       : self.name,
                "race"       : self.race,
                "job"        : self.job,
                "points"     : self.points,
                "level"      : self.level,
                "exp"        : self.exp,
                "level_up"   : self.level_up,
                "experience" : self.experience,
                "hp"         : self.hp,
                "HP"         : self.HP,
                "mp"         : self.mp,
                "MP"         : self.MP,
                "magic"      : self.magic,
                "attack"     : self.attack,
                "defense"    : self.defense,
                "gold"       : self.gold,
                "equip"      : self.equip,
                "spells"     : self.spells,
                "inventory"  : self.inventory,
            }

    def set_data(self, data):
        self.name = data["name"]
        self.race = data["race"]
        self.job = data["job"]
        self.points = data["points"]
        self.level = data["level"]
        self.exp = data["exp"]
        self.level_up = data["level_up"]
        self.experience = data["experience"]
        self.hp = data["hp"]
        self.HP = data["HP"]
        self.mp = data["mp"]
        self.MP = data["MP"]
        self.magic = data["magic"]
        self.attack = data["attack"]
        self.defense = data["defense"]
        self.gold = data["gold"]
        self.equip = data["equip"]
        self.spells = data["spells"]
        self.inventory = data["inventory"]

    def get_magic_bonus(self):
        bonus = 0
        for i in self.equip:
            bonus += items[self.equip[i]].get('magic', 0)
        return bonus

    def get_attack_bonus(self):
        return items[self.equip['left hand']]['attack']+items[self.equip['right hand']]['attack']

    def get_defense_bonus(self):
        bonus = 0
        for i in self.equip:
            bonus += items[self.equip[i]].get('defense', 0)
        return bonus

    def get_magic_damage(self, spell):
        return magic[spell]['damage']+self.get_magic_bonus()

    def get_damage(self, hand):
        return self.attack+items[self.equip[hand]]['attack']

    def get_armor(self):
        return self.defense+self.get_defense_bonus()

    def take_damage(self, dmg):
        self.hp -= max(dmg-self.get_armor(), 1)

    def add_spell(self, spell):
        if spell in self.spells:
            self.spells[spell] += 1
        else:
            self.spells[spell] = 1

    def use_spell(self, spell, entity):
        if self.mp >= magic[spell]['cost']:
            if "hp" in magic[spell]: entity.hp = min(entity.hp+(magic[spell]["hp"]+self.get_magic_bonus()), entity.HP)
            if "damage" in magic[spell]: entity.take_damage(self.get_magic_attack(spell))
            if "poisoned" in magic[spell]: self.poisoned = magic[spell]['poisoned']
            if "confused" in magic[spell]: self.confused = magic[spell]['confused']
            if "stunned" in magic[spell]: self.stunned = magic[spell]['stunned']
            if "burned" in magic[spell]: self.burned = magic[spell]['burned']
            self.mp -= magic[spell]['cost']

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

    def equip_item(self, item, slot):
        if self.equip[slot] != "nothing":
            self.add_item(self.equip[slot])
        self.del_item(item)
        self.equip[slot] = item

    def use_item(self, item):
        can_delete = False
        if "hp" in items[item]:
            can_delete = True
            self.hp = min(self.hp+items[item]['hp'], self.HP)
        if "mp" in items[item]:
            can_delete = True
            self.mp = min(self.mp+items[item]['mp'], self.MP)
        if "HP" in items[item]:
            can_delete = True
            self.HP += items[item]['HP']
        if "MP" in items[item]:
            can_delete = True
            self.MP += items[item]['MP']
        if "mag" in items[item]:
            can_delete = True
            self.magic += items[item]['mag']
        if "atk" in items[item]:
            can_delete = True
            self.attack += items[item]['atk']
        if "def" in items[item]:
            can_delete = True
            self.defense += items[item]['def']
        if "spell" in items[item]:
            can_delete = True
            self.add_spell(items[item]['spell'])
        #if "" in items[item]:
        #    pass
        if can_delete:
            self.del_item(item)

    def can_craft_item(self, item):
        can_craft = True
        for i in crafting[item]['take']:
            if i in self.inventory:
                if self.inventory[i] < crafting[item]['take'][i]:
                    can_craft = False
            else:
                can_craft = False
        return can_craft

    def craft_item(self, item):
        if self.can_craft_item(item):
            for i in crafting[item]['take']:
                for n in range(crafting[item]['take'][i]):
                    self.del_item(i)
            for i in crafting[item]['give']:
                for n in range(crafting[item]['give'][i]):
                    self.add_item(i)

    def reward(self, stat, value):
        if stat == "gold":
            self.gold += value
        elif stat == "exp":
            self.exp += value
        elif stat == "hp":
            self.hp += value
        elif stat == "mp":
            self.mp += value
        elif stat == "HP":
            self.HP += value
        elif stat == "MP":
            self.MP += value
        elif stat == "mag":
            self.magic += value
        elif stat == "atk":
            self.attack += value
        elif stat == "def":
            self.defense += value
        elif stat == "spell":
            self.add_spell(value)

    def gain_experience(self, xp):
        self.exp = int(self.exp+xp)
        while self.exp >= self.level_up:
            self.increase_level()

    def increase_level(self):
        self.experience = int(self.experience+self.exp)
        self.exp = int(self.exp-self.level_up)
        self.level += 1
        self.level_up = int(self.level_up*mobs[self.race]['curve'])
        if self.level % mobs[self.race]['point'] == 0:
            self.points += 1
            if self.is_ai:
                self.auto_level()
            else:
                input("{} leveled up!".format(self.name))
    
    def auto_level(self):
        while self.points > 0:
            stat = random.randint(0, 4)
            if stat == 0:
                self.magic += 1
            elif stat == 1:
                self.attack += 1
            elif stat == 2:
                self.defense += 1
            elif stat == 3:
                self.HP += 1
                self.hp += 1
            elif stat == 4:
                self.MP += 1
                self.mp += 1
            else:
                self.HP += 1
                self.hp += 1
            self.points -= 1

    def auto_equip(self):
        to_equip = []
        for i in self.inventory:
            for slot in self.equip:
                if 'slot' in items[i]:
                    if items[i]['slot'] in slot:
                        to_equip.append([i, slot])
        for i in to_equip:
            self.equip_item(i[0], i[1])

    def randomize(self):
        self.hp = self.HP
        self.mp = self.MP
        self.inventory = {}
        self.gold += random.randint(0, 15)*10
        for i in items:
            if i != "nothing":
                if random.randint(0, 1500) < items[i]['rarity']:
                    M = int(items[i]['count']/2)
                    if M > 1:
                        self.inventory[i] = random.randint(1, M)
        self.auto_equip()
