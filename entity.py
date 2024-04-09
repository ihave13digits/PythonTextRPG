import random

from game_data import *
from output import *

class Entity():

    def __init__(self, NAME, RACE, SEX, AI=True):
        self.is_ai = AI
        self.name = NAME
        self.race = RACE
        self.sex = SEX
        self.job = "fighter"
        self.level = 1
        self.points = 0
        self.skill_points = 0
        self.job_points = 0
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
        self.skills = {
                "barter"   : 0,
                "bluff"    : 0,
                "build"    : 0,
                "cast"     : 0,
                "climb"    : 0,
                "combat"   : 0,
                "craft"    : 0,
                "dodge"    : 0,
                "forage"   : 0,
                "heal"     : 0,
                "hide"     : 0,
                "hunt"     : 0,
                "persuade" : 0,
                "search"   : 0,
                "sneak"    : 0,
                "travel"   : 0,
            }
        self.skill_mod = {
                "barter"   : 0,
                "bluff"    : 0,
                "build"    : 0,
                "cast"     : 0,
                "climb"    : 0,
                "combat"   : 0,
                "craft"    : 0,
                "dodge"    : 0,
                "forage"   : 0,
                "heal"     : 0,
                "hide"     : 0,
                "hunt"     : 0,
                "persuade" : 0,
                "search"   : 0,
                "sneak"    : 0,
                "travel"   : 0,
            }
        self.jobs = {}
        self.spells = {}
        self.inventory = {}
        self.proficiency = {}

        self.calculate_derived()
        self.hp = self.HP
        self.mp = self.MP

    def get_data(self):
        return {
                "name"         : self.name,
                "race"         : self.race,
                "sex"          : self.sex,
                "job"          : self.job,
                "points"       : self.points,
                "skill_points" : self.skill_points,
                "job_points"   : self.job_points,
                "level"        : self.level,
                "exp"          : self.exp,
                "level_up"     : self.level_up,
                "experience"   : self.experience,
                "hp"           : self.hp,
                "HP"           : self.HP,
                "mp"           : self.mp,
                "MP"           : self.MP,
                "poisoned"     : self.poisoned,
                "confused"     : self.confused,
                "stunned"      : self.stunned,
                "burned"       : self.burned,
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
                "skills"       : self.skills,
                "skill_mod"    : self.skill_mod,
                "jobs"         : self.jobs,
                "spells"       : self.spells,
                "inventory"    : self.inventory,
                "proficiency"    : self.proficiency,
            }

    def set_data(self, data):
        self.name = data["name"]
        self.race = data["race"]
        self.sex = data['sex']
        self.job = data["job"]
        self.points = data["points"]
        self.skill_points = data["skill_points"]
        self.job_points = data["job_points"]
        self.level = data["level"]
        self.exp = data["exp"]
        self.level_up = data["level_up"]
        self.experience = data["experience"]
        self.hp = data["hp"]
        self.HP = data["HP"]
        self.mp = data["mp"]
        self.MP = data["MP"]
        self.poisoned = data["poisoned"]
        self.confused = data["confused"]
        self.stunned = data["stunned"]
        self.burned = data["burned"]
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
        self.skills = data["skills"]
        self.skill_mod = data["skill_mod"]
        self.jobs = data["jobs"]
        self.spells = data["spells"]
        self.inventory = data["inventory"]
        self.proficiency = data["proficiency"]

    def get_skill(self, skill):
        bonus = 0
        if skill in jobs[self.job]['skill']:  bonus = jobs[self.job]['skill'][skill]
        return int(self.skills[skill]+self.skill_mod[skill]+bonus)

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

    def rest(self, duration):
        d = min(duration, 8)/8
        self.hp = int(self.hp + (self.HP-self.hp) * d)
        self.mp = int(self.mp + (self.MP-self.mp) * d)
        if d > 0.00:
            self.confused = False
        if d > 0.25:
            self.stunned = False
        if d > 0.50:
            self.poisoned = False
        if d > 0.75:
            self.burned = False

    def take_stat_damage(self):
        if self.burned:
            T.text("{} took {} burn damage".format(self.name, 1))
            self.take_damage(1)
        if self.poisoned:
            T.text("{} took {} poison damage".format(self.name, 1))
            self.take_damage(1)

    def take_damage(self, dmg):
        self.hp -= max(dmg-self.get_armor(), 1)

    def add_job(self, j):
        if j in self.jobs: self.jobs[j] += 1
        else: self.jobs[j] = 1

    def add_spell(self, spell):
        if spell in self.spells: self.spells[spell] += 1
        else: self.spells[spell] = 1

    def use_spell(self, spell, entity):
        if self.mp >= magic[spell]['cost']:
            if "hp" in magic[spell]: entity.hp = min(entity.hp+(int(magic[spell]["hp"]*(self.spells[spell]*0.2))+self.get_magic_bonus()), entity.HP)
            if "damage" in magic[spell]: entity.take_damage(int(self.get_magic_damage(spell)*(self.spells[spell])))
            if "poisoned" in magic[spell]: entity.poisoned = magic[spell]['poisoned']
            if "confused" in magic[spell]: entity.confused = magic[spell]['confused']
            if "stunned" in magic[spell]: entity.stunned = magic[spell]['stunned']
            if "burned" in magic[spell]: entity.burned = magic[spell]['burned']
            self.mp -= magic[spell]['cost']

    def add_item(self, item):
        if item in self.inventory: self.inventory[item] += 1
        else: self.inventory[item] = 1

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
        if self.skills['craft'] < crafting[item]['craft']:
            return False
        for i in crafting[item]['take']:
            if i in self.inventory:
                if self.inventory[i] < crafting[item]['take'][i]:
                    return False
            else:
                return False
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
            if key == "gold": self.gold += value
            elif key == "exp": self.gain_experience(value)
            elif key == "hp": self.hp += value
            elif key == "mp": self.mp += value
            elif key == "HP": self.HP += value
            elif key == "MP": self.MP += value
            elif key == "mag": self.magic += value
            elif key == "atk": self.attack += value
            elif key == "def": self.defense += value
            elif key == "spell":
                self.add_spell(value)
                passed = True
        elif mode == 'skill':
            if key in self.skills:
                self.skills[key] += value
        elif mode == 'item':
            if key in items:
                for i in range(value):
                    self.add_item(key)

    def require(self, mode, key, value):
        passed = False
        if mode == 'stat':
            if key == "gold" and self.gold >= value:
                self.gold -= value
                passed = True
            elif key == "exp" and self.exp >= value: passed = True
            elif key == "hp" and self.hp >= value: passed = True
            elif key == "mp" and self.mp >= value: passed = True
            elif key == "HP" and self.HP >= value: passed = True
            elif key == "MP" and self.MP >= value: passed = True
            elif key == "mag" and self.magic >= value: passed = True
            elif key == "atk" and self.attack >= value: passed = True
            elif key == "def" and self.defense >= value: passed = True
            elif key == "spell" and value in self.spells:
                self.use_spell(value, Entity("Mob", "human", "m"))
                passed = True
        elif mode == 'skill':
            if key in self.skills:
                if self.skills[key] >= value:
                    passed = True
        elif mode == 'item':
            if key in self.items:
                if self.items[key] >= value:
                    for i in range(value):
                        self.del_item(key)
                    passed = True
        return passed

    def calculate_derived(self):
        self.HP = int(mobs[self.race]['hp']*(((self.strength*0.5)+(self.constitution*0.5))*0.25)*(self.level*0.125))
        self.MP = int(mobs[self.race]['mp']*(((self.awareness*0.5)+(self.intelligence*0.5))*0.25)*(self.level*0.125))
        self.magic = int(mobs[self.race]['mag']*(((self.awareness*0.11)+(self.intelligence*0.22)+(self.dexterity*0.11))*0.25))
        self.attack = int(mobs[self.race]['atk']*(((self.strength*0.22)+(self.constitution*0.11)+(self.dexterity*0.11))*0.25))
        self.defense = int(mobs[self.race]['def']*(((self.strength*0.11)+(self.constitution*0.11)+(self.dexterity*0.22))*0.25))

        self.skills['barter'] = int(self.charisma*1.5)
        self.skills['bluff'] = int(self.charisma*0.5)+(self.constitution*0.5)
        self.skills['build'] = int(self.dexterity*0.5)+(self.constitution*0.25)+(self.strength*0.25)
        self.skills['cast'] = int(self.magic*0.5)+(self.dexterity*0.25)+(self.intelligence*0.25)
        self.skills['climb'] = int(self.awareness*0.2)+(self.strength*0.4)+(self.dexterity*0.4)
        self.skills['combat'] = int(self.awareness*0.25)+(self.attack*0.25)+(self.defense*0.25)+(self.dexterity*0.25)
        self.skills['craft'] = int(self.dexterity*0.5)+(self.intelligence*0.5)
        self.skills['dodge'] = int(self.awareness*0.5)+(self.dexterity*0.5)
        self.skills['forage'] = int(self.awareness*0.5)+(self.dexterity*0.5)
        self.skills['heal'] = int(self.awareness*0.5)+(self.dexterity*0.5)
        self.skills['hide'] = int(self.awareness*0.5)+(self.intelligence*0.5)
        self.skills['hunt'] = int(self.awareness*0.5)+(self.dexterity*0.5)
        self.skills['persuade'] = int(self.awareness*0.5)+(self.charisma*0.5)
        self.skills['search'] = int(self.awareness*0.5)+(self.intelligence*0.5)
        self.skills['sneak'] = int(self.awareness*0.5)+(self.dexterity*0.5)
        self.skills['travel'] = int(self.awareness*1.5)

    def weapon_proficiency(self, hand):
        i = self.equip[hand]
        if i in self.proficiency:
            if self.proficiency[i] < 100:
                self.proficiency[i] += 1
        else:
            self.proficiency[i] = 1

    def gain_experience(self, xp):
        self.exp = int(self.exp+xp)
        while self.exp >= self.level_up:
            self.increase_level()

    def increase_level(self):
        self.experience = int(self.experience+self.exp)
        self.exp = int(self.exp-self.level_up)
        self.level += 1
        self.level_up = int(self.level_up*mobs[self.race]['curve'])
        self.skill_points += int((self.intelligence*0.75)+(self.awareness*0.25)*0.5)
        if self.level % mobs[self.race]['point'] == 0:
            self.points += 1
        self.job_points += 1
        if self.is_ai:
            self.auto_level()
        self.calculate_derived()

    def auto_level(self):
        skills = []
        for s in self.skills:
            skills.append(s)
        while self.points > 0:
            stat = random.randint(0, 5)
            if stat ==   0: self.strength += 1
            elif stat == 1: self.constitution += 1
            elif stat == 2: self.dexterity += 1
            elif stat == 3: self.awareness += 1
            elif stat == 4: self.intelligence += 1
            elif stat == 5: self.charisma += 1
            self.points -= 1
        while self.skill_points > 0:
            self.skills[random.choice(skills)] += 1
            self.skill_points -= 1
        while self.job_points > 0:
            self.job = random.choice(selectable_jobs)
            self.job_points -= 1

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
        self.hp = self.HP
        self.mp = self.MP
        self.inventory = {}
        misc = []
        scrolls = []
        if self.race in playable_mobs:
            equip_head = []
            equip_neck = []
            equip_shoulders = []
            equip_torso = []
            equip_waist = []
            equip_arms = []
            equip_hands = []
            equip_legs = []
            equip_feet = []
            weapons = []
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
        else:
            self.equip["torso"] = "nothing"
            self.equip["legs"] = "nothing"
            for i in items:
                if i != "nothing":
                    if random.randint(0, 2500) < items[i]['rarity']:
                        if items[i]['type'] == "material": misc.append(i)
        # Food / Potions
        for i in misc:
            if random.randint(0, 100) < 50: self.add_item(i)
        self.auto_equip()
        # Magic
        for i in range(self.magic):
            s = random.randint(0, len(scrolls))
            if random.randint(0, 100) < 50:
                try:
                    self.add_spell(items[scrolls[s]]['spell'])
                    self.add_item(scrolls[s])
                    scrolls.remove(s)
                except: pass
