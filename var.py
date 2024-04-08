import random
from os import path

from world_map import *
from game_data import *
from output import *

from shop import Shop
from entity import Entity
from color import Color

class Var():

    def __init__(self):
        self.running = True
        self.ai_turn = True
        self.data_slot = 1
        self.frame_count = 0
        self.data_file = "main-PythonTextRPG-ihave13digits.json"
        self.data_path = "data/data"
        self.quest_path = "data/quest"
        self.game_path = "data/game_data"
        self.state = "startup"
        self.selected_quest = ""
        self.location = "Fairlanding"
        self.item_type = ""
        self.player = Entity("Player", "human", "m", False)
        self.mob = Entity("human", "human", "m")
        self.shop = Shop()
        self.c_text1 = Color(255, 255, 255)
        self.c_text2 = Color(100, 100, 100)
        self.c_count = Color(80, 80, 80)
        self.c_attack = Color(225, 80, 0)
        self.c_defense = Color(80, 225, 0)
        self.c_magic = Color(0, 80, 225)
        self.c_gold = Color(225, 225, 0)
        self.c_edit = Color(255, 255, 255)
        self.quest_hash = {
            'player_name' : self.player.name,
        }

    ##
    ### Engine Tools
    ##

    def get_console_size(self):
        from os import get_terminal_size
        line = str(get_terminal_size())
        x = ""
        y = ""
        z = 0
        for c in line:
            if c == " ":
                z += 1
            if c.isdigit() == True:
                if z == 0:
                    x += c
                if z == 1:
                    y += c
        return [int(x), int(y)]

    def rest_player(self, duration):
        self.player.rest(duration)

    def randomize_mob(self):
        race = world[V.location]['mobs'][random.randint(0, len(world[self.location]['mobs'])-1)]
        sex = random.choice(("m", "f"))
        name = race
        if race in playable_mobs:
            first_name = random.choice(names[race][sex])
            last_name = random.choice(names[race]['l'])
            name = "{} {}".format(first_name, last_name)
        self.mob = Entity(name, race, sex)
        self.mob.randomize()
        self.mob.gain_experience(random.randint(int(self.player.experience/2), int(self.player.experience*1.5)))
        self.mob.rest(8)

    def inventory_selection(self, inventory, state, gold_txt='', mrk=1.0):
        selecting = True
        selection = "nothing"
        while selecting:
            T.clear_text()
            T.print("Select an item to use", "\n", self.c_text1)
            T.print("Item Type: {}\n{}\n".format(self.item_type, gold_txt), "\n", self.c_text1)
            for i in inventory:
                if items[i]['type'] == self.item_type:
                    s_value = str(int(items[i]['value']*mrk))
                    s_hp = ''
                    s_mp = ''
                    s_HP = ''
                    s_MP = ''
                    s_a = ''
                    s_d = ''
                    s_m = ''
                    s_atk = ''
                    s_def = ''
                    s_mgc = ''
                    if "hp" in items[i]:
                        s_hp = " [{}]".format(items[i]['hp'])
                    if "mp" in items[i]:
                        s_mp = " [{}]".format(items[i]['mp'])
                    if "HP" in items[i]:
                        s_hp = " [{}]".format(items[i]['HP'])
                    if "MP" in items[i]:
                        s_mp = " [{}]".format(items[i]['MP'])
                    if "atk" in items[i]:
                        s_a = " [{}]".format(items[i]['atk'])
                    if "def" in items[i]:
                        s_d = " [{}]".format(items[i]['def'])
                    if "mag" in items[i]:
                        s_m = " [{}]".format(items[i]['mag'])
                    if "attack" in items[i]:
                        s_atk = " [{}]".format(items[i]['attack'])
                    if "defense" in items[i]:
                        s_def = " [{}]".format(items[i]['defense'])
                    if "magic" in items[i]:
                        s_mgc = " [{}]".format(items[i]['magic'])
                    margin = T.menu_width-(len(i)+len(str(inventory[i]))+(
                        len(s_value)+len(s_hp)+len(s_mp)+len(s_HP)+len(s_MP)+len(s_a)+len(s_d)+len(s_m)+len(s_atk)+len(s_def)+len(s_mgc)))
                    print("[{}] {}{}{}{}{}{}{}{}{}{}{}{}{}".format(
                        T.get_colored_text(inventory[i], self.c_count),
                        T.get_colored_text(i, self.c_text1),
                        " "*margin,
                        T.get_colored_text(int((int(s_value))), self.c_gold),
                        T.get_colored_text(s_hp, self.c_attack),
                        T.get_colored_text(s_mp, self.c_magic),
                        T.get_colored_text(s_HP, self.c_attack),
                        T.get_colored_text(s_MP, self.c_magic),
                        T.get_colored_text(s_a, self.c_attack),
                        T.get_colored_text(s_d, self.c_defense),
                        T.get_colored_text(s_m, self.c_magic),
                        T.get_colored_text(s_atk, self.c_attack),
                        T.get_colored_text(s_def, self.c_defense),
                        T.get_colored_text(s_mgc, self.c_magic)
                        ))
            T.print("\n(1) Material\n(2) Food\n(3) Potion\n(4) Scroll\n(5) Arms\n(6) Armor\n(0) Back\n", "\n", self.c_text2)
            sel = T.input(": ")
            if sel == "0":
                self.state = state
                selecting = False
            elif sel == "1": V.item_type = "material"
            elif sel == "2": V.item_type = "food"
            elif sel == "3": V.item_type = "potion"
            elif sel == "4": V.item_type = "scroll"
            elif sel == "5": V.item_type = "arms"
            elif sel == "6": V.item_type = "armor"
            elif sel in inventory:
                selection = sel
                selecting = False
        return selection

    def roll_skill(self, entity, skill, rate=100):
        T.print()
        input("Skill ({}) success: {}/{}".format(skill, entity.get_skill(skill), rate))
        return bool(random.randint(0, rate) < entity.get_skill(skill))

    ##
    ### Entity Tools
    ##

    def display_entity(self, entity, menu):
        entity.gain_experience(0)
        self.display_stats(entity)
        sel = T.input("\n: ")
        T.clear_text()
        T.print("Skills")
        self.display_skills(entity)
        sel = T.input("\n: ")
        T.clear_text()
        T.print("Spells")
        self.display_spells(entity)
        sel = T.input("\n: ")
        T.clear_text()
        T.print("Jobs")
        self.display_jobs(entity)
        sel = T.input("\n: ")
        spending_points = bool(entity.points > 0 or entity.skill_points > 0)
        if spending_points:
            self.state = "level_up"

    def entity_stats(self, entity, menu):
        self.display_stats(entity)
        sel = T.input("\n: ")
        spending_points = bool(entity.points > 0)
        while spending_points > 0:
            if entity.points <= 0:
                spending_points = False
                self.state = menu
                return
            self.display_stats(entity)
            T.print("(1) Strength\n(2) Constitution\n(3) Dexterity\n(4) Awareness\n(5) Intelligence\n(6) Charisma\n(0) Back", "\n", self.c_text2)
            sel = T.input(": ")
            if sel == "0":
                spending_points = False
            elif sel == "1":
                entity.strength += 1
                entity.points -= 1
            elif sel == "2":
                entity.constitution += 1
                entity.points -= 1
            elif sel == "3":
                entity.dexterity += 1
                entity.points -= 1
            elif sel == "4":
                entity.awareness += 1
                entity.points -= 1
            elif sel == "5":
                entity.intelligence += 1
                entity.points -= 1
            elif sel == "6":
                entity.charisma += 1
                entity.points -= 1
            entity.calculate_derived()
        self.state = menu

    def entity_skills(self, entity, menu):
        T.clear_text()
        for s in entity.skill_mod:
            T.expanded_text("({})".format(s), entity.get_skill(s), " ", self.c_text2)
        while entity.skill_points > 0:
            T.clear_text()
            for s in entity.skill_mod:
                T.expanded_text("({})".format(s), entity.get_skill(s), " ", self.c_text2)
            T.print("(0) Done")
            T.print("Remaining Points: {}".format(entity.skill_points))
            sel = T.input(": ")
            if sel == "0":
                self.state = menu
                break
            else:
                if sel in entity.skill_mod and entity.skill_points > 0:
                    entity.skill_mod[sel] += 1
                    entity.skill_points -= 1

    def display_text(self, value, text):
        T.print("{}:{}{}".format(text, " "*(T.menu_width-(len("{}:".format(text))+len(value))), value), "\n", self.c_text1)

    def display_stats(self, entity):
        T.clear_text()
        exp = "{}/{}".format(entity.exp, entity.level_up)
        ehp = "{}/{}".format(entity.hp, entity.HP)
        emp = "{}/{}".format(entity.mp, entity.MP)
        emg = "{} [{}]".format(entity.magic, entity.get_magic_bonus())
        eat = "{} [{}]".format(entity.attack, entity.get_attack_bonus())
        edf = "{} [{}]".format(entity.defense, entity.get_defense_bonus())
        self.display_text(V.location, "Location")
        self.display_text(entity.name, "Name")
        self.display_text(entity.race, "Race")
        self.display_text(entity.sex, "Sex")
        self.display_text(entity.job, "Job")
        print()
        self.display_text(str(entity.gold), "Gold")
        self.display_text(str(entity.level), "Level")
        self.display_text(str(entity.points), "Points")
        self.display_text(str(entity.skill_points), "Skill Points")
        self.display_text(exp, "Experience")
        print()
        self.display_text(ehp, "Health")
        self.display_text(emp, "Mana")
        self.display_text(emg, "Magic")
        self.display_text(eat, "Attack")
        self.display_text(edf, "Defense")
        print()
        self.display_text(str(entity.strength), "Strength")
        self.display_text(str(entity.constitution), "Constitution")
        self.display_text(str(entity.dexterity), "Dexterity")
        self.display_text(str(entity.awareness), "Awareness")
        self.display_text(str(entity.intelligence), "Intelligence")
        self.display_text(str(entity.charisma), "Charisma")

    def display_skills(self, entity):
        T.print()
        count = 0
        limit = int(T.menu_width/12)
        for s in entity.skills:
            count += 1
            skl = "{}{}".format(T.expand_text("| {}".format(s), 12, ' ', 'l'), T.expand_text(entity.get_skill(s), 4, ' ', 'r'))
            T.print(skl, "", V.c_text1)
            if count % limit == 0:
                T.print()
        T.print()

    def display_spells(self, entity):
        T.print()
        for s in entity.spells:
            T.print("{}{}{}".format(s," "*(T.menu_width-(len(s)+len(str(entity.spells[s])))), entity.spells[s]), "\n", self.c_text1)

    def display_jobs(self, entity):
        T.print()
        for j in entity.jobs:
            T.print("{}{}{}".format(j," "*(T.menu_width-(len(j)+len(str(entity.jobs[j])))), entity.jobs[j]), "\n", self.c_text1)

V = Var()
