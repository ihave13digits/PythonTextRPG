import random

from mob import *
from job import *
from item import *
from magic import *
from output import *

class Entity():

    def __init__(self, NAME, RACE, SEX, AI=True):
        self.is_ai = AI
        self.name = NAME
        self.race = RACE
        self.sex = SEX
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
        self.strength = mobs[RACE]['str']
        self.constitution = mobs[RACE]['con']
        self.dexterity = mobs[RACE]['dex']
        self.awareness = mobs[RACE]['awa']
        self.intelligence = mobs[RACE]['int']
        self.charisma = mobs[RACE]['cha']

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
                "ring0"      : 'nothing',
                "ring1"      : 'nothing',
                "ring2"      : 'nothing',
                "ring3"      : 'nothing',
                "ring4"      : 'nothing',
                "ring5"      : 'nothing',
                "ring6"      : 'nothing',
                "ring7"      : 'nothing',
            }
        self.spells = {}
        self.inventory = {}

    def get_data(self):
        return {
                "name"         : self.name,
                "race"         : self.race,
                "sex"          : self.sex,
                "job"          : self.job,
                "points"       : self.points,
                "level"        : self.level,
                "exp"          : self.exp,
                "level_up"     : self.level_up,
                "experience"   : self.experience,
                "hp"           : self.hp,
                "HP"           : self.HP,
                "mp"           : self.mp,
                "MP"           : self.MP,
                "magic"        : self.magic,
                "attack"       : self.attack,
                "defense"      : self.defense,
                "strength"     : self.strength,
                "constitution" : self.constitution,
                "dexterity"    : self.dexterity,
                "awareness"    : self.awareness,
                "intelligence" : self.intelligence,
                "charisma"     : self.charisma,
                "gold"         : self.gold,
                "equip"        : self.equip,
                "spells"       : self.spells,
                "inventory"    : self.inventory,
            }

    def set_data(self, data):
        self.name = data["name"]
        self.race = data["race"]
        self.sex = data['sex']
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
        self.strength = data['strength']
        self.consitution = data['constitution']
        self.dexterity = data['dexterity']
        self.awareness = data['awareness']
        self.intelligence = data['intelligence']
        self.charisma = data['charisma']
        self.gold = data["gold"]
        self.equip = data["equip"]
        self.spells = data["spells"]
        self.inventory = data["inventory"]

    def get_magic_bonus(self):
        bonus = int(((self.awareness*0.25)+(self.intelligence*0.5)+(self.dexterity*0.25))*0.1)
        for i in self.equip:
            bonus += items[self.equip[i]].get('magic', 0)
        return bonus

    def get_attack_bonus(self):
        bonus = int(((self.constitution*0.25)+(self.strength*0.5)+(self.dexterity*0.25))*0.1)
        return items[self.equip['left hand']]['attack']+items[self.equip['right hand']]['attack']+bonus

    def get_defense_bonus(self):
        bonus = int(((self.constitution*0.5)+(self.strength*0.25)+(self.dexterity*0.25))*0.1)
        for i in self.equip:
            bonus += items[self.equip[i]].get('defense', 0)
        return bonus

    def get_magic_damage(self, spell):
        return magic[spell]['damage']+self.get_magic_bonus()

    def get_damage(self, hand):
        return self.attack+items[self.equip[hand]]['attack']

    def get_armor(self):
        return self.defense+self.get_defense_bonus()

    def take_stat_damage(self):
        if self.burned:
            T.text("{} took {} burn damage".format(self.name, 1))
            self.take_damage(1)
        if self.poisoned:
            T.text("{} took {} poison damage".format(self.name, 1))
            self.take_damage(1)

    def take_damage(self, dmg):
        self.hp -= max(dmg-self.get_armor(), 1)

    def add_spell(self, spell):
        if spell in self.spells:
            self.spells[spell] += 1
        else:
            self.spells[spell] = 1

    def use_spell(self, spell, entity):
        if self.mp >= magic[spell]['cost']:
            if "hp" in magic[spell]: entity.hp = min(entity.hp+(int(magic[spell]["hp"]*(self.spells[spell]*0.2))+self.get_magic_bonus()), entity.HP)
            if "damage" in magic[spell]: entity.take_damage(int(self.get_magic_damage(spell)*(self.spells[spell]*0.2)))
            if "poisoned" in magic[spell]: entity.poisoned = magic[spell]['poisoned']
            if "confused" in magic[spell]: entity.confused = magic[spell]['confused']
            if "stunned" in magic[spell]: entity.stunned = magic[spell]['stunned']
            if "burned" in magic[spell]: entity.burned = magic[spell]['burned']
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

    def reward(self, mode, key, value):
        if mode == 'stat':
            if key == "gold":
                self.gold += value
            elif key == "exp":
                self.exp += value
            elif key == "hp":
                self.hp += value
            elif key == "mp":
                self.mp += value
            elif key == "HP":
                self.HP += value
            elif key == "MP":
                self.MP += value
            elif key == "mag":
                self.magic += value
            elif key == "atk":
                self.attack += value
            elif key == "def":
                self.defense += value
            elif key == "spell":
                self.add_spell(value)
        elif mode == 'item':
            if key in items:
                for i in range(value):
                    self.add_item(key)

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
        to_cull = []
        to_equip = []
        for i in self.inventory:
            for slot in self.equip:
                if 'slot' in items[i]:
                    if items[i]['slot'] in slot:
                        to_equip.append([i, slot])
        for i in range(len(to_equip)):
            for j in range(len(to_equip)):
                if to_equip[i][0] == to_equip[j][0] and to_equip[i][1] == to_equip[j][1] :
                    to_cull = to_equip[i]
                    break
        if to_cull:
            to_equip.remove(to_cull)
        for i in to_equip:
            self.equip_item(i[0], i[1])

    def randomize(self):
        equip_head = []
        equip_neck = []
        equip_shoulders = []
        equip_torso = []
        equip_waist = []
        equip_arms = []
        equip_hands = []
        equip_legs = []
        equip_feet = []
        scrolls = []
        weapons = []
        misc = []
        self.hp = self.HP
        self.mp = self.MP
        self.inventory = {}
        self.gold += random.randint(0, 15)*10
        for i in items:
            if i != "nothing":
                if random.randint(0, 2500) < items[i]['rarity']:
                    if items[i]['type'] == "scroll": scrolls.append(i)
                    elif items[i]['type'] == "arms": weapons.append(i)
                    elif items[i]['type'] == "food" or items[i]['type'] == "potion": misc.append(i)
                    elif items[i]['type'] == "armor":
                        if items[i]['slot'] == "head": equip_head.append(i)
                        if items[i]['slot'] == "neck": equip_neck.append(i)
                        if items[i]['slot'] == "shoulders": equip_shoulders.append(i)
                        if items[i]['slot'] == "torso": equip_torso.append(i)
                        if items[i]['slot'] == "waist": equip_waist.append(i)
                        if items[i]['slot'] == "arms": equip_arms.append(i)
                        if items[i]['slot'] == "hands": equip_hands.append(i)
                        if items[i]['slot'] == "legs": equip_legs.append(i)
                        if items[i]['slot'] == "feet": equip_feet.append(i)
        # Food / Potions
        for i in misc:
            if random.randint(0, 100) < 50: self.add_item(i)
        # Magic
        for i in range(self.magic):
            s = random.randint(0, len(scrolls))
            if random.randint(0, 100) < 50:
                try:
                    self.add_spell(items[scrolls[s]]['spell'])
                    self.add_item(scrolls[s])
                    scrolls.remove(s)
                except: pass
        # Weapon
        if random.randint(0, 100) < 75 and weapons: self.add_item(random.choice(weapons))
        # Armor
        if random.randint(0, 100) < 75 and equip_head: self.add_item(random.choice(equip_head))
        if random.randint(0, 100) < 75 and equip_neck: self.add_item(random.choice(equip_neck))
        if random.randint(0, 100) < 75 and equip_shoulders: self.add_item(random.choice(equip_shoulders))
        if random.randint(0, 100) < 75 and equip_torso: self.add_item(random.choice(equip_torso))
        if random.randint(0, 100) < 75 and equip_waist: self.add_item(random.choice(equip_waist))
        if random.randint(0, 100) < 75 and equip_arms: self.add_item(random.choice(equip_arms))
        if random.randint(0, 100) < 75 and equip_hands: self.add_item(random.choice(equip_hands))
        if random.randint(0, 100) < 75 and equip_legs: self.add_item(random.choice(equip_legs))
        if random.randint(0, 100) < 75 and equip_feet: self.add_item(random.choice(equip_feet))
        
        self.auto_equip()
