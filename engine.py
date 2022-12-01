import time, random
from os import path

from names import *
from mob import *
from job import *
from magic import *
from item import *
from world import *
from quest import *
from output import *
from world_map import *

from shop import Shop
from entity import Entity

class Engine():

    def __init__(self):
        self.running = True
        self.ai_turn = True
        self.data_slot = 0
        self.data_file = "main-PythonTextRPG-ihave13digits.json"
        self.data_path = "data/data"
        self.quest_path = "data/quest"
        self.state = "intro"
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
        self.c_edit = Color(0, 0, 0)
        self.quest_hash = {
            'player_name' : self.player.name,
        }

    ##
    ### Data
    ##

    def get_data_path(self):
        data_file = "slot-{}-{}".format(self.data_slot, self.data_file)
        return path.join(path.join(path.dirname(__file__), self.data_path), data_file)

    def save_quest_data(self):
        import json
        for q in quest:
            data_file = "{}.json".format(q)
            data_path = path.join(path.join(path.dirname(__file__), self.quest_path), data_file)
            try:
                with open(data_path,"w") as f:
                    json.dump(quest[q], f)
            except FileNotFoundError:
                T.text("Quest File at path '{}' Not Found".format(data_path))

    def load_quest_data(self):
        global quest
        import json
        quest_list = []
        with open(path.join(path.join(path.dirname(__file__), self.quest_path), "QuestList.json"),"r") as f:
            qd = json.loads(f.read().strip())
            for q in qd:
                if qd[q]: quest_list.append(q)
        for q in quest_list:
            data_file = "{}.json".format(q)
            data_path = path.join(path.join(path.dirname(__file__), self.quest_path), data_file)
            try:
                with open(data_path,"r") as f:
                    q_data = json.loads(f.read().strip())
                    quest[q] = q_data
            except FileNotFoundError:
                T.text("Quest File at path '{}' Not Found".format(data_path))
            

    def save_data(self):
        import json
        colors = {
            'text1' : [self.c_text1.r, self.c_text1.g, self.c_text1.b],
            'text2' : [self.c_text2.r, self.c_text2.g, self.c_text2.b],
            'count' : [self.c_count.r, self.c_count.g, self.c_count.b],
            'attack' : [self.c_attack.r, self.c_attack.g, self.c_attack.b],
            'defense' : [self.c_defense.r, self.c_defense.g, self.c_defense.b],
            'magic' : [self.c_magic.r, self.c_magic.g, self.c_magic.b],
            'gold' : [self.c_gold.r, self.c_gold.g, self.c_gold.b],
            }
        data = {
                'colors' : colors,
                "text_pause" : T.text_pause,
                "text_speed" : T.text_speed,
                "text_margin" : T.text_margin,
                "menu_width" : T.menu_width,
                "location" : self.location,
                "quest" : self.selected_quest,
                "quests" : quest,
                "player" : self.player.get_data(),
                "world" : world,
            }
        with open(self.get_data_path(),"w") as f:
            json.dump(data, f)
            f.close()

    def load_data(self):
        global world, quest
        import json
        with open(self.get_data_path(),"r") as f:
            data = json.loads(f.read())
            T.text_pause = data['text_pause']
            T.text_speed = data['text_speed']
            T.text_margin = data['text_margin']
            T.menu_width = data['menu_width']
            self.location = data['location']
            self.selected_quest = data['quest']
            quest = data['quests']
            self.player.set_data(data['player'])
            world = data['world']
            colors = data['colors']
            self.c_text1.r = colors["text1"][0]
            self.c_text1.g = colors["text1"][1]
            self.c_text1.b = colors["text1"][2]
            self.c_text2.r = colors["text2"][0]
            self.c_text2.g = colors["text2"][1]
            self.c_text2.b = colors["text2"][2]
            self.c_count.r = colors["count"][0]
            self.c_count.g = colors["count"][1]
            self.c_count.b = colors["count"][2]
            self.c_attack.r = colors["attack"][0]
            self.c_attack.g = colors["attack"][1]
            self.c_attack.b = colors["attack"][2]
            self.c_defense.r = colors["defense"][0]
            self.c_defense.g = colors["defense"][1]
            self.c_defense.b = colors["defense"][2]
            self.c_magic.r = colors["magic"][0]
            self.c_magic.g = colors["magic"][1]
            self.c_magic.b = colors["magic"][2]
            self.c_gold.r = colors["gold"][0]
            self.c_gold.g = colors["gold"][1]
            self.c_gold.b = colors["gold"][2]
            f.close()
        self.state = "main_menu"

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

    def randomize_mob(self):
        race = world[self.location]['mobs'][random.randint(0, len(world[self.location]['mobs'])-1)]
        sex = random.choice(("m", "f"))
        name = race
        if race in playable_mobs:
            first_name = random.choice(names[race][sex])
            last_name = random.choice(names[race]['l'])
            name = "{} {}".format(first_name, last_name)
        self.mob = Entity(name, race, sex)
        first_name = random.choice(names[race]['m'])
        last_name = random.choice(names[race]['l'])
        name = "{} {}".format(first_name, last_name)
        self.mob.randomize()
        self.mob.gain_experience(random.randint(int(self.player.experience/2), int(self.player.experience)))

    def inventory_selection(self, inventory, state, gold_txt='', mrk=1.0):
        selecting = True
        selection = "nothing"
        while selecting:
            T.clear_text()
            T.print("Select an item to use", "\n", self.c_text1)
            T.print("Item Type: {}\n{}\n".format(self.item_type, gold_txt), "\n", self.c_text1)
            for i in inventory:
                if items[i]['type'] == self.item_type:
                    s_value = str(items[i]['value'])
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
                        T.get_colored_text(int(int(s_value)*mrk), self.c_gold),
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
            T.print("\n(1) Food\n(2) Potion\n(3) Scroll\n(4) Arms\n(5) Armor\n(0) Back\n", "\n", self.c_text2)
            sel = T.input(": ")
            if sel == "0":
                self.state = state
                selecting = False
            elif sel == "1": self.item_type = "food"
            elif sel == "2": self.item_type = "potion"
            elif sel == "3": self.item_type = "scroll"
            elif sel == "4": self.item_type = "arms"
            elif sel == "5": self.item_type = "armor"
            elif sel in inventory:
                selection = sel
                selecting = False
        return selection

    ##
    ### Game Menus
    ##

    def intro(self):
        can_continue = False
        try:
            with open(self.get_data_path(), "r") as f:
                f.close()
            can_continue = True
        except:
            pass
        T.clear_text()
        output_menu = "(1) New Game\n"
        if can_continue:
            output_menu += "(2) Continue\n"
        output_menu += "(0) Exit"
        T.print(output_menu, "\n", self.c_text2)

        sel = T.input(": ")
        if sel == "0":
            self.running = False
            T.clear_text()
        elif sel == "1": self.state = "select_race"
        elif sel == "2" and can_continue: self.load_data()

    def new_game(self):
        for l in world:
            S = Shop(world[l]['shop']['gold'], world[l]['shop']['markup'])
            world[l]['shop'] = S.get_data()
        self.load_quest_data()
        self.state = 'quest'
        self.selected_quest = "Intro"

    def main_menu(self):
        T.clear_text()
        T.print("(1) Battle\n(2) Stats\n(3) Inventory\n(4) Location\n(5) Quests\n(6) Settings\n(0) Exit", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "exit"
        elif sel == "1": self.state = "prepare_battle"
        elif sel == "2": self.entity_stats(self.player, "main_menu")
        elif sel == "3": self.state = "inventory_menu"
        elif sel == "4": self.state = "location_menu"
        elif sel == "5": self.state = "quest_history"
        elif sel == "6": self.state = "settings"

    def inventory_menu(self):
        T.clear_text()
        T.print("(1) Items\n(2) Equip\n(3) Craft\n(0) Back", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.state = "item"
        elif sel == "2": self.state = "equip"
        elif sel == "3": self.state = "craft"

    def location_menu(self):
        T.clear_text()
        T.print("(1) Travel\n(2) Shop\n(0) Back", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.state = "travel_menu"
        elif sel == "2": self.state = "shop_menu"

    def exit_menu(self):
        T.text(T.get_colored_text("Are you sure you want to exit?", self.c_text1))
        T.clear_text()
        T.print("(1) Exit Without Saving\n(2) Save And Exit\n(0) Cancel", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.running = False
        elif sel == "2":
            self.save_data()
            self.running = False
        T.clear_text()

    ##
    ### Quest
    ##

    def freetype(self, data):
        if data['object'] == 'player':
            if data['variable'] == "name":
                self.player.name = T.input(": ")
                self.quest_hash['player_name'] = self.player.name

    def quest_menu(self):
        global quest
        part = quest[self.selected_quest]['part']
        if 'reward' in quest[self.selected_quest][part]:
            if 'stat' in quest[self.selected_quest][part]['reward']:
                key = quest[self.selected_quest][part]['reward']['stat']
                value = quest[self.selected_quest][part]['reward']['value']
                self.player.reward('stat', key, value)
            elif 'item' in quest[self.selected_quest][part]['reward']:
                key = quest[self.selected_quest][part]['reward']['item']
                value = quest[self.selected_quest][part]['reward']['value']
                self.player.reward('item', key, value)
        if 'add_quest' in quest[self.selected_quest][part]:
            q = quest[self.selected_quest][part]['add_quest']['quest']
            quest[q]['discovered'] = True
        if 'completed' in quest[self.selected_quest][part]:
            quest[self.selected_quest]['completed'] = quest[self.selected_quest][part]['completed']
        if 'state' in quest[self.selected_quest][part]:
            self.state = quest[self.selected_quest][part]['state']
            return
        if 'freetype' in quest[self.selected_quest][part]:
            self.freetype(quest[self.selected_quest][part]['freetype'])
        
        if 'prompt' in quest[self.selected_quest][part]:
            T.text(quest[self.selected_quest][part]['prompt'])
        elif 'fprompt' in quest[self.selected_quest][part]:
            T.text(quest[self.selected_quest][part]['fprompt'].format(**self.quest_hash))
        
        if 'option' in quest[self.selected_quest][part]:
            for o in quest[self.selected_quest][part]['option']:
                T.print("({}) {}".format(o, quest[self.selected_quest][part]['option'][o]['prompt']), "\n", self.c_text1)
            sel = T.input(": ")
            if sel in quest[self.selected_quest][part]['option']:
                if 'reward' in quest[self.selected_quest][part]['option'][sel]:
                    if 'stat' in quest[self.selected_quest][part]['option'][sel]['reward']:
                        stat = quest[self.selected_quest][part]['option'][sel]['reward']['stat']
                        value = quest[self.selected_quest][part]['option'][sel]['reward']['value']
                        self.player.reward('stat', stat, value)
                    if 'item' in quest[self.selected_quest][part]['option'][sel]['reward']:
                        stat = quest[self.selected_quest][part]['option'][sel]['reward']['item']
                        value = quest[self.selected_quest][part]['option'][sel]['reward']['value']
                        self.player.reward('item', stat, value)
            if 'part' in quest[self.selected_quest][part]['option'][sel]:
                quest[self.selected_quest]['part'] = quest[self.selected_quest][part]['option'][sel]['part']
                #return
        if 'part' in quest[self.selected_quest][part]:
            quest[self.selected_quest]['part'] = quest[self.selected_quest][part]['part']

    def quest_history(self):
        T.clear_text()
        T.print("{}\n".format(self.selected_quest), "\n", self.c_text1)
        for q in quest:
            qst = ""
            if quest[q]['discovered']:
                qst = q
                cplt = "Incomplete"
                if quest[q]['completed']:
                    cplt = "Completed"
                T.print("{}{}{}| {}".format(qst, " "*(T.menu_width-(len(qst)+len(quest[q]['location'])+len(cplt)+2)), quest[q]['location'], cplt), "\n", self.c_text2)
        T.print()
        psbl = ""
        if quest[self.selected_quest]['location'] == self.location and quest[self.selected_quest]['discovered'] == True and not quest[self.selected_quest]['completed']:
            psbl = "(1) Accept Quest\n"
        T.print("{}(0) Back\n".format(psbl), "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0":
            self.state = "main_menu"
        if sel == "1" and psbl != "":
            self.state = "quest"
        if sel in quest:
            self.selected_quest = sel

    ##
    ### Battle
    ##

    def battle_stats(self):
        entity = self.player
        T.clear_text()
        T.print("(1) {}\n(2) {}\n(0) Back".format(self.player.name, self.mob.name), "\n", self.c_text2)
        select = T.input(": ")
        if select == "0": return
        if select == "1": entity = self.player
        if select == "2": entity = self.mob
        self.entity_stats(entity, "battle")

    def battle_attack(self):
        hand = "right hand"
        T.clear_text()
        T.print("(1) Left Hand\n(2) Right Hand\n(0) Back", "\n", self.c_text2)
        select = T.input(": ")
        if select == "0": return
        if select == "1": hand = "left hand"
        if select == "2": hand = "right hand"
        dmg = self.player.get_damage(hand)
        self.mob.take_damage(dmg)
        T.text("{} attacked {} for {} damage".format(self.player.name, self.mob.name, max(1, dmg-self.mob.get_armor())))
        self.player.take_stat_damage()
        self.ai_turn = True
        self.state = "battle"

    def battle_magic(self):
        entity = self.mob
        T.clear_text()
        T.print("(1) {}\n(2) {}\n(0) Back".format(self.player.name, self.mob.name), "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0":
            self.state = "battle"
            return
        if sel == "1": entity = self.mob
        if sel == "2": entity = self.player
        T.clear_text()
        T.print("Select a spell to use", "\n", self.c_text1)
        for i in self.player.spells:
            margin = T.menu_width - ( len(i) + len(str(self.player.spells[i])) + len(str(magic[i]['cost'])) )
            T.print("[{}] {}{}{}".format(self.player.spells[i], i, " "*margin, magic[i]['cost']), "\n", self.c_text2)
        T.print("(0) Back", "\n", self.c_text2)

        sel = T.input(": ")
        if sel == "0":
            self.state = "battle"
            return
        elif sel in self.player.spells:
            self.player.use_spell(sel, entity)
            T.text("{} used {} on {}".format(self.player.name, sel, entity.name))
            self.player.take_stat_damage()
            self.ai_turn = True
            self.state = "battle"

    def battle_item(self):
        sel = self.inventory_selection(self.player.inventory, "battle")
        if sel != "nothing":
            self.player.use_item(sel)
            T.text("{} used {}".format(self.player.name, sel))
            self.state = "battle"

    def battle_win(self):
        exp_bonus = int(mobs[self.mob.race]['exp']*(self.mob.level*mobs[self.mob.race]['curve']))
        self.player.gain_experience(exp_bonus)
        gold = int(self.mob.gold*0.75)
        self.player.gold = int(self.player.gold+gold)
        self.mob.gold = int(self.mob.gold-gold)
        if self.player.confused: self.player.confused = False
        if self.player.stunned: self.player.stunned = False
        T.text("{} won the battle, gaining {} experience and {} gold".format(self.player.name, exp_bonus, gold))
        for item in self.mob.equip:
            if self.mob.equip[item] != "nothing":
                self.mob.add_item(self.mob.equip[item])
        for item in self.mob.inventory:
            T.print("(1) Take {}\n(0) Skip".format(item), "\n", self.c_text2)
            sel = T.input(": ")
            if sel == "0": pass
            else:
                plural = ""
                if self.mob.inventory[item] > 1: plural = "s"
                for i in range(self.mob.inventory[item]):
                    self.player.add_item(item)
                T.text("{} looted {} {}{} from {}".format(self.player.name, self.mob.inventory[item], item, plural, self.mob.name))
        self.state = "main_menu"

    def battle_lose(self):
        gold = int(self.player.gold*0.75)
        self.player.gold = int(self.player.gold-gold)
        self.mob.gold = int(self.mob.gold+gold)
        self.player.hp = self.player.HP
        self.player.mp = self.player.MP
        if self.player.poisoned: self.player.poisoned = False
        if self.player.confused: self.player.confused = False
        if self.player.stunned: self.player.stunned = False
        if self.player.burned: self.player.burned = False
        T.text("{} lost the battle, losing {} gold".format(self.player.name, gold))
        self.state = "main_menu"

    def battle_ai(self):
        affliction = ""
        can_perform_action = True
        if self.mob.stunned:
            if random.randint(0, 100) < 10:
                affiction = "being stunned"
                can_perform_action = False
        if self.mob.confused:
            if random.randint(0, 100) < 10:
                affiction = "confusion"
                can_perform_action = False
        
        
        if can_perform_action:
            if self.mob.hp < self.mob.HP/2:
                try:
                    for i in self.mob.inventory:
                        if 'hp' in items[i] and not 'mp' in items[i]:
                            if self.mob.hp+items[i]['hp'] <= self.mob.HP:
                                self.mob.use_item(i)
                                T.text("{} used {}".format(self.mob.name, i))
                except: pass
            elif self.mob.mp < self.mob.MP/2:
                try:
                    for i in self.mob.inventory:
                        if 'mp' in items[i] and not 'hp' in items[i]:
                            if self.mob.mp+items[i]['mp'] <= self.mob.MP:
                                self.mob.use_item(i)
                                T.text("{} used {}".format(self.mob.name, i))
                except: pass
            elif self.mob.hp < self.mob.HP/2 and self.mob.mp < self.mob.MP/2:
                try:
                    for i in self.mob.inventory:
                        if 'hp' in items[i] and 'mp' in items[i]:
                            if self.mob.hp+items[i]['hp'] <= self.mob.HP or self.mob.mp+items[i]['mp'] <= self.mob.MP:
                                self.mob.use_item(i)
                                T.text("{} used {}".format(self.mob.name, i))
                except: pass
            can_cast = bool(random.randint(0, self.mob.MP) < self.mob.mp)
            if len(self.mob.spells) > 0:
                if can_cast:
                    spell = "nothing"
                    entity = self.mob
                    for s in self.mob.spells:
                        if magic[s]['cost'] <= self.mob.mp:
                            can_cast = True
                            if 'damage' in magic[s]:
                                entity = self.player
                            if 'hp' in magic[s]:
                                entity = self.mob
                            spell = s
                    if can_cast and spell != "nothing":
                        self.mob.use_spell(spell, entity)
                        T.text("{} casted {} on {}".format(self.mob.name, spell, entity.name))
                        self.mob.take_stat_damage()
                        self.ai_turn = False
            if not can_cast:
                hand = "right hand"
                if self.mob.equip['left hand'] != "nothing": hand = "left hand"
                elif self.mob.equip['right hand'] != "nothing": hand = "right hand"
                dmg = self.mob.get_damage(hand)
                self.player.take_damage(dmg)
                T.text("{} attacked {} for {} damage".format(self.mob.name, self.player.name, max(1, dmg-self.player.get_armor())))
                self.mob.take_stat_damage()
                self.ai_turn = False
        elif not can_perform_action:
            T.text("{} couldn't attack due to {}".format(self.mob.name, affliction))
            self.mob.take_stat_damage()
            self.ai_turn = False

        
    def battle_player(self):
        T.print("(1) Attack\n(2) Stats\n(3) Magic\n(4) Item\n(0) Run", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.battle_attack()
        elif sel == "2": self.battle_stats()
        elif sel == "3": self.battle_magic()
        elif sel == "4": self.battle_item()

    def battle(self):
        T.clear_text()
        p_health = "HP:{}/{}".format(self.player.hp, self.player.HP)
        m_health = "HP:{}/{}".format(self.mob.hp, self.mob.HP)
        p_mana = "MP:{}/{}".format(self.player.mp, self.player.MP)
        m_mana = "MP:{}/{}".format(self.mob.mp, self.mob.MP)
        health_margin = T.menu_width-(len(self.player.name)+len(self.mob.name))
        T.print("{}{}{}".format(self.player.name," "*(T.menu_width-(len(self.player.name)+len(self.mob.name))),self.mob.name), "\n", self.c_text1)
        T.print("{}{}{}".format(p_health," "*(T.menu_width-(len(p_health)+len(m_health))),m_health), "\n", self.c_text1)
        T.print("{}{}{}".format(p_mana," "*(T.menu_width-(len(p_mana)+len(m_mana))),m_mana), "\n", self.c_text1)
        print()
        if self.player.hp <= 0:
            self.battle_lose()
            self.randomize_mob()
            return
        if self.mob.hp <= 0:
            self.battle_win()
            self.randomize_mob()
            return
        if self.ai_turn: self.battle_ai()
        else: self.battle_player()

    def prepare_battle(self):
        self.ai_turn = random.choice([True, False])
        self.randomize_mob()
        txt = ""
        if self.ai_turn: txt = "{} is engaging {}".format(self.mob.race.capitalize(), self.player.name)
        else: txt = "{} is engaging {}".format(self.player.name, self.mob.race)
        T.clear_text()
        T.text(txt)
        chcs = ""
        if not self.ai_turn:
            T.print("(1) Engage\n(0) Retreat", "\n", self.c_text2)
            sel = T.input(": ")
            if not self.ai_turn and sel == "0":
                self.state = "main_menu"
                return
        self.state = "battle"

    ##
    ### Stats
    ##

    def display_stats(self, entity):
        T.clear_text()
        exp = "{}/{}".format(entity.exp, entity.level_up)
        ehp = "{}/{}".format(entity.hp, entity.HP)
        emp = "{}/{}".format(entity.mp, entity.MP)
        emg = "{} [{}]".format(entity.magic, entity.get_magic_bonus())
        eat = "{} [{}]".format(entity.attack, entity.get_attack_bonus())
        edf = "{} [{}]".format(entity.defense, entity.get_defense_bonus())
        T.print("Location:{}{}".format(" "*(T.menu_width-(len("Location:")+len(self.location))), self.location), "\n", self.c_text1)
        T.print("\nName:{}{}".format(" "*(T.menu_width-(len("Name:")+len(entity.name))), entity.name), "\n", self.c_text1)
        T.print("Race:{}{}".format(" "*(T.menu_width-(len("Race:")+len(entity.race))), entity.race), "\n", self.c_text1)
        T.print("Sex:{}{}".format(" "*(T.menu_width-(len("Sex:")+len(entity.sex))), entity.sex), "\n", self.c_text1)
        T.print("Job:{}{}".format(" "*(T.menu_width-(len("Job:")+len(entity.job))), entity.job), "\n", self.c_text1)
        T.print("\nGold:{}{}".format(" "*(T.menu_width-(len("Gold:")+len(str(entity.gold)))), entity.gold), "\n", self.c_text1)
        T.print("Level:{}{}".format(" "*(T.menu_width-(len("Level:")+len(str(entity.level)))), entity.level), "\n", self.c_text1)
        T.print("Points:{}{}".format(" "*(T.menu_width-(len("Points:")+len(str(entity.points)))), entity.points), "\n", self.c_text1)
        T.print("Experience:{}{}".format(" "*(T.menu_width-(len("Experience:")+len(exp))), exp), "\n", self.c_text1)
        T.print("\nHealth:{}{}".format(" "*(T.menu_width-(len("Health:")+len(ehp))), ehp), "\n", self.c_text1)
        T.print("Mana:{}{}".format(" "*(T.menu_width-(len("Mana:")+len(emp))), emp), "\n", self.c_text1)
        T.print("Magic:{}{}".format(" "*(T.menu_width-(len("Magic:")+len(emg))), emg), "\n", self.c_text1)
        T.print("Attack:{}{}".format(" "*(T.menu_width-(len("Attack:")+len(eat))), eat), "\n", self.c_text1)
        T.print("Defense:{}{}".format(" "*(T.menu_width-(len("Defense:")+len(edf))), edf), "\n", self.c_text1)
        T.print("\nStrength:{}{}".format(" "*(T.menu_width-(len("Strength:")+len(str(entity.strength)))), entity.strength), "\n", self.c_text1)
        T.print("Constitution:{}{}".format(" "*(T.menu_width-(len("Constitution:")+len(str(entity.constitution)))), entity.constitution), "\n", self.c_text1)
        T.print("Dexterity:{}{}".format(" "*(T.menu_width-(len("dexterity:")+len(str(entity.dexterity)))), entity.dexterity), "\n", self.c_text1)
        T.print("Awareness:{}{}".format(" "*(T.menu_width-(len("Awareness:")+len(str(entity.awareness)))), entity.awareness), "\n", self.c_text1)
        T.print("Intelligence:{}{}".format(" "*(T.menu_width-(len("Intelligence:")+len(str(entity.intelligence)))), entity.intelligence), "\n", self.c_text1)
        T.print("Charisma:{}{}".format(" "*(T.menu_width-(len("Charisma:")+len(str(entity.charisma)))), entity.charisma), "\n", self.c_text1)

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
            T.print("(1) Increase Magic\n(2) Increase Attack\n(3) Increase Defense\n(4) Charisma\n(5) Increase Health\n(6) Increase Mana\n(0) Back", "\n", self.c_text2)
            sel = T.input(": ")
            if sel == "0":
                spending_points = False
            elif sel == "1":
                entity.magic += 1
                entity.points -= 1
            elif sel == "2":
                entity.attack += 1
                entity.points -= 1
            elif sel == "3":
                entity.defense += 1
                entity.points -= 1
            elif sel == "4":
                entity.charisma += 1
                entity.points -= 1
            elif sel == "5":
                entity.HP += 1
                entity.hp += 1
                entity.points -= 1
            elif sel == "6":
                entity.MP += 1
                entity.mp += 1
                entity.points -= 1
        self.state = menu

    def select_race(self):
        T.clear_text()
        R = self.player.race
        T.print(R, "\n\n", self.c_text1)
        T.expanded_text("Health:", str(mobs[R]['hp']))
        T.expanded_text("Magic:", str(mobs[R]['mp']))
        T.expanded_text("Attack:", str(mobs[R]['atk']))
        T.expanded_text("Defense:", str(mobs[R]['def']))
        T.expanded_text("Strength:", str(mobs[R]['str']))
        T.expanded_text("Constitution:", str(mobs[R]['con']))
        T.expanded_text("Dexterity:", str(mobs[R]['dex']))
        T.expanded_text("Awareness:", str(mobs[R]['awa']))
        T.expanded_text("Intelligence:", str(mobs[R]['int']))
        T.expanded_text("Charisma:", str(mobs[R]['cha']))
        print()
        for p in playable_mobs:
            T.print("({})".format(p), "\n", self.c_text2)
        T.print("(0){}Continue".format(" "*(T.menu_width-(len("(0)")+len("Continue")))), "\n", self.c_text2)
        sel = T.input(": ")
        if sel in playable_mobs:
            self.player.race = sel
        if sel == "0":
            self.state = "select_sex"

    def select_sex(self):
        T.clear_text()
        T.print("(m) Male\n(f) Female", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "m" or sel == "f":
            self.player.sex = sel
            self.state = "new_game"

    """
    def select_job(self):
        T.clear_text()
        print("(0) Back")
        sel = T.input(": ")
        if sel in jobs:
            self.player.job = sel
        if sel == "0":
            self.state = "main_menu"
    """

    ##
    ### Item
    ##

    def player_item(self):
        sel = self.inventory_selection(self.player.inventory, "inventory_menu")
        if sel != "nothing":
            self.player.use_item(sel)
            T.text("{} used {}".format(self.player.name, sel))

    def craft_item(self):
        for i in crafting:
            if self.player.can_craft_item(i):
                T.print("{}".format(i), "\n", self.c_text2)
        T.print("(0) Back", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0":
            self.state = "inventory_menu"
            return
        if sel in crafting and self.player.can_craft_item(sel):
            self.player.craft_item(sel)

    ##
    ### Equip
    ##

    def equip(self):
        part = ""
        T.clear_text()
        for part in self.player.equip:
            T.print("({}){}{}".format(part," "*(T.menu_width-(len(part)+len(self.player.equip[part]))),self.player.equip[part]), "\n", self.c_text2)
        T.print("(0) Back", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0":
            self.state = "inventory_menu"
            return
        if sel in self.player.equip:
            part = sel
        T.clear_text()
        for i in self.player.inventory:
            if 'slot' in items[i]:
                if items[i]['slot'] in part:
                    margin = T.menu_width - ( len(i) + len(str(self.player.inventory[i])) + len(str(items[i]['value'])) )
                    T.print("[{}] {}{}{}".format(self.player.inventory[i], i, " "*margin, items[i]['value']), "\n", self.c_text2)
        T.print("(1) nothing\n(0) Back", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0":
            self.state = "equip"
            return
        if sel == "1": sel = "nothing"
        if sel in self.player.inventory or sel == "nothing":
            if part != "":
                self.player.equip_item(sel, part)

    ##
    ### Shop
    ##

    def shop_buy(self):
        sel = self.inventory_selection(self.shop.inventory, "shop_menu", "{}'s Gold: {}".format(self.player.name, self.player.gold), self.shop.markup)
        if sel != "nothing":
            if self.player.gold >= items[sel]['value']:
                self.shop.del_item(sel)
                self.shop.gold += items[sel]['value']
                self.player.add_item(sel)
                self.player.gold -= items[sel]['value']
                T.text("{} bought {}".format(self.player.name, sel))
                world[self.location]['shop'] = self.shop.get_data()

    def shop_sell(self):
        sel = self.inventory_selection(self.player.inventory, "shop_menu", "Shop's Gold: {}".format(self.shop.gold), self.shop.markup)
        if sel != "nothing":
            if self.shop.gold >= items[sel]['value']:
                self.player.del_item(sel)
                self.shop.add_item(sel)
                self.shop.gold -= items[sel]['value']
                self.player.gold += items[sel]['value']
                T.text("{} sold {}".format(self.player.name, sel))
                world[self.location]['shop'] = self.shop.get_data()

    def shop_menu(self):
        T.clear_text()
        T.print("(1) Buy\n(2) Sell\n(0) Leave", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "location_menu"
        elif sel == "1":
            self.state = "shop_buy"
            T.text("Let me show you what I have")
        elif sel == "2":
            T.text("Let me see what you have")
            self.state = "shop_sell"

    ##
    ### Travel
    ##

    def travel_menu(self):
        T.clear_text()
        print(world_map)
        T.expanded_text("Location:", self.location)
        n_txt = ""
        s_txt = ""
        e_txt = ""
        w_txt = ""
        if 'north' in world[self.location]['travel']: n_txt = "(8) {}".format(world[self.location]['travel']['north'])
        if 'west' in world[self.location]['travel']: w_txt = "(4) {}".format(world[self.location]['travel']['west'])
        if 'east' in world[self.location]['travel']: e_txt = "(6) {}".format(world[self.location]['travel']['east'])
        if 'south' in world[self.location]['travel']: s_txt = "(2) {}".format(world[self.location]['travel']['south'])
        n_off = int(32-int(len(n_txt)/2))
        s_off = int(32-int(len(s_txt)/2))
        ew_off = int(64-int((len(e_txt))+(len(w_txt))))
        b_off = int(32-int(len("(0) Back")/2))
        T.print("{}{}".format(" "*n_off, n_txt), "\n", self.c_text2)
        T.print("{}{}{}".format(w_txt, " "*ew_off, e_txt), "\n", self.c_text2)
        T.print("{}{}".format(" "*s_off, s_txt), "\n", self.c_text2)
        T.print("{}(0) Back".format(" "*b_off), "\n", self.c_text2)

        sel = T.input(": ")
        if sel == "0": self.state = "location_menu"
        elif sel == "8" and "north" in world[self.location]['travel']:
            self.state = "travel_menu"
            self.location = world[self.location]['travel']['north']
        elif sel == "2" and "south" in world[self.location]['travel']:
            self.state = "travel_menu"
            self.location = world[self.location]['travel']['south']
        elif sel == "4" and "west" in world[self.location]['travel']:
            self.state = "travel_menu"
            self.location = world[self.location]['travel']['west']
        elif sel == "6" and "east" in world[self.location]['travel']:
            self.state = "travel_menu"
            self.location = world[self.location]['travel']['east']
        

    ##
    ### Settings
    ##

    def set_speed(self):
        T.clear_text()
        T.print("(1) Fast\n(2) Normal\n(3) Slow\n(0) Back", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            T.text_speed = 0.01
            T.text("Sample text to show timing")
        elif sel == "2":
            T.text_speed = 0.03
            T.text("Sample text to show timing")
        elif sel == "3":
            T.text_speed = 0.06
            T.text("Sample text to show timing")

    def set_pause(self):
        T.clear_text()
        T.print("(1) Fast\n(2) Medium\n(3) Slow\n(4) Wait\n(0) Back", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            T.text_pause = 0.15
            T.text("Sample text to show timing")
        elif sel == "2":
            T.text_pause = 0.225
            T.text("Sample text to show timing")
        elif sel == "3":
            T.text_pause = 0.3
            T.text("Sample text to show timing")
        elif sel == "4":
            T.text_pause = -1.0

    def set_margin(self):
        T.clear_text()
        T.print("(1) 1\n(2) 3\n(3) 5\n(0) Back", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            T.text_margin = 1
            T.text("Sample text to show margin")
        elif sel == "2":
            T.text_margin = 3
            T.text("Sample text to show margin")
        elif sel == "3":
            T.text_margin = 5
            T.text("Sample text to show margin")

    def set_width(self):
        T.clear_text()
        T.print("(1) 32\n(2) 48\n(3) 64\n(0) Back", "\n", self.c_text2)
        sel = T.input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            T.menu_width = 48
            T.text("Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  ")
        elif sel == "2":
            T.menu_width = 56
            T.text("Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  ")
        elif sel == "3":
            T.menu_width = 64
            T.text("Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  ")

    def set_color(self):
        T.clear_text()
        T.print("(r) Red\n(g) Green\n(b) Blue\n", "\n", self.c_edit)
        T.print("(1) Text", "\n", self.c_text1)
        T.print("(2) Option", "\n", self.c_text2)
        T.print("(3) Count", "\n", self.c_count)
        T.print("(4) Attack", "\n", self.c_attack)
        T.print("(5) Defense", "\n", self.c_defense)
        T.print("(6) Magic", "\n", self.c_magic)
        T.print("(7) Gold", "\n", self.c_gold)
        T.print("(0) Back", "\n", self.c_text2)
        
        sel = T.input(": ")
        if sel == "0": self.state = "settings"
        if sel == "r":
            T.clear_text()
            v = T.input(": ")
            self.c_edit.r = int(v)
        if sel == "g":
            T.clear_text()
            v = T.input(": ")
            self.c_edit.g = int(v)
        if sel == "b":
            T.clear_text()
            v = T.input(": ")
            self.c_edit.b = int(v)
        if sel == "1": self.c_text1.reset(self.c_edit)
        if sel == "2": self.c_text2.reset(self.c_edit)
        if sel == "3": self.c_count.reset(self.c_edit)
        if sel == "4": self.c_attack.reset(self.c_edit)
        if sel == "5": self.c_defense.reset(self.c_edit)
        if sel == "6": self.c_magic.reset(self.c_edit)
        if sel == "7": self.c_gold.reset(self.c_edit)

    def settings(self):
        T.clear_text()
        T.print("(1) Text Speed\n(2) Text Pause\n(3) Clear Margin\n(4) Menu Width\n(5) Color\n(0) Back", "\n", self.c_text2)

        sel = T.input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.state = "set_speed"
        elif sel == "2": self.state = "set_pause"
        elif sel == "3": self.state = "set_margin"
        elif sel == "4": self.state = "set_width"
        elif sel == "5": self.state = "set_color"

    def update_background(self):
        for l in world:
            if random.randint(0, 1000) < world[l]['restock']:
                S = Shop(0, 0)
                S.set_data(world[l]['shop'])
                S.restock()
                world[l]['shop'] = S.get_data()
        self.shop.set_data(world[self.location]['shop'])

    def update(self):
        self.update_background()
        if self.state == "battle": self.battle()
        elif self.state == "quest": self.quest_menu()
        elif self.state == "item": self.player_item()
        elif self.state == "equip": self.equip()
        elif self.state == "craft": self.craft_item()
        elif self.state == "shop_buy": self.shop_buy()
        elif self.state == "shop_sell": self.shop_sell()
        elif self.state == "shop_menu": self.shop_menu()
        elif self.state == "travel_menu": self.travel_menu()
        elif self.state == "quest_history": self.quest_history()
        elif self.state == "inventory_menu": self.inventory_menu()
        elif self.state == "location_menu": self.location_menu()
        elif self.state == "main_menu": self.main_menu()
        elif self.state == "set_speed": self.set_speed()
        elif self.state == "set_pause": self.set_pause()
        elif self.state == "set_margin": self.set_margin()
        elif self.state == "set_width": self.set_width()
        elif self.state == "set_color": self.set_color()
        elif self.state == "settings": self.settings()
        elif self.state == "prepare_battle": self.prepare_battle()
        elif self.state == "select_race": self.select_race()
        elif self.state == "select_sex": self.select_sex()
        elif self.state == "new_game": self.new_game()
        elif self.state == "intro": self.intro()
        elif self.state == "exit": self.exit_menu()

    def start(self):
        self.run()

    def run(self):
        while self.running:
            self.update()
