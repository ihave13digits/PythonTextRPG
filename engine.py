from os import system
from sys import stdout, platform
import time, random, textwrap

from names import *
from mob import *
from magic import *
from item import *
from world import *
from quest import *

from shop import Shop
from entity import Entity

class Engine():

    def __init__(self):
        self.running = True
        self.ai_turn = True
        self.clear_cmd = ""
        self.data_file = "main-PythonTextRPG-ihave13digits.json"
        self.state = "intro"
        self.selected_quest = ""
        self.location = "Fairlanding"
        self.item_type = ""
        self.text_pause = 1.2
        self.text_speed = 0.06
        self.text_margin = 3
        self.menu_width = 48
        self.player = Entity("Player", "human", False)
        self.mob = Entity("human", "human")
        self.shop = Shop()

        if platform.startswith('win32'):
            self.clear_cmd = 'cls'
        else:
            self.clear_cmd = 'clear'

    ##
    ### Data
    ##

    def save_data(self):
        import json
        data = {
                "text_pause" : self.text_pause,
                "text_speed" : self.text_speed,
                "text_margin" : self.text_margin,
                "menu_width" : self.menu_width,
                "location" : self.location,
                "quest" : self.selected_quest,
                "player" : self.player.get_data(),
                #"shop" : self.shop.get_data(),
                "world" : world,
            }
        with open(self.data_file,"w") as f:
            json.dump(data, f)
            f.close()

    def load_data(self):
        global world
        import json
        with open(self.data_file,"r") as f:
            data = json.loads(f.read())
            self.text_pause = data['text_pause']
            self.text_speed = data['text_speed']
            self.text_margin = data['text_margin']
            self.menu_width = data['menu_width']
            self.location = data['location']
            self.selected_quest = data['quest']
            self.player.set_data(data['player'])
            world = data['world']
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

    def clear_text(self):
        system(self.clear_cmd)

    def text(self, text):
        self.clear_text()
        wrapped_text = str('\n'.join(textwrap.wrap(text, self.menu_width, break_long_words=False)))
        for c in wrapped_text:
            stdout.write(c)
            stdout.flush()
            time.sleep(self.text_speed)
        if self.text_pause != -1.0:
            time.sleep(self.text_pause)
        else:
            input(": ")
        print("\n"*self.text_margin, end="")

    def randomize_mob(self):
        races = []
        for i in mobs:
            races.append(i)
        race = random.randint(0, len(races)-1)
        first_name = random.choice(m_names)
        last_name = random.choice(l_names)
        name = "{} {}".format(first_name, last_name)
        self.mob = Entity(name, races[race])
        self.mob.randomize()
        self.mob.gain_experience(random.randint(int(self.player.experience/2), int(self.player.experience)))

    def inventory_selection(self, inventory, state, gold_txt=''):
        selecting = True
        selection = "nothing"
        while selecting:
            self.clear_text()
            print("Select an item to use")
            print("Item Type: {}\n{}\n".format(self.item_type, gold_txt))
            for i in inventory:
                if items[i]['type'] == self.item_type:
                    s_value = str(items[i]['value'])
                    s_atk = ''
                    s_def = ''
                    if "attack" in items[i]:
                        s_atk = " [{}]".format(items[i]['attack'])
                    if "defense" in items[i]:
                        s_def = " [{}]".format(items[i]['defense'])
                    margin = self.menu_width - ( len(i) + len(str(inventory[i])) + len(s_value) + len(s_atk) + len(s_def))
                    print("[{}] {}{}{}{}{}".format(inventory[i], i, " "*margin, s_value, s_atk, s_def))
            print("\n(1) Food\n(2) Potion\n(3) Scroll\n(4) Arms\n(5) Armor\n(0) Back\n")
            sel = input(": ")
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
            with open(self.data_file, "r") as f:
                f.close()
            can_continue = True
        except:
            pass
        self.clear_text()
        print("(1) New Game")
        if can_continue:
            print("(2) Continue")
        print("(0) Exit")

        sel = input(": ")
        if sel == "0": self.running = False
        elif sel == "1": self.state = "new_game"
        elif sel == "2" and can_continue:
            self.load_data()

    def new_game(self):
        for l in world:
            S = Shop(world[l]['shop']['gold'], world[l]['shop']['markup'])
            world[l]['shop'] = S.get_data()
        self.state = 'quest'
        self.selected_quest = "intro"

    def main_menu(self):
        self.clear_text()
        print("(1) Battle\n(2) Stats\n(3) Inventory\n(4) Location\n(5) Settings\n(0) Exit")
        sel = input(": ")
        if sel == "0": self.state = "exit"
        elif sel == "1":
            self.ai_turn = random.choice([True, False])
            self.randomize_mob()
            self.state = "battle"
        elif sel == "2": self.entity_stats(self.player, "main_menu")
        elif sel == "3": self.state = "inventory_menu"
        elif sel == "4": self.state = "location_menu"
        elif sel == "5": self.state = "settings"

    def inventory_menu(self):
        self.clear_text()
        print("(1) Items\n(2) Equip\n(3) Craft\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.state = "item"
        elif sel == "2": self.state = "equip"
        elif sel == "3": self.state = "craft"

    def location_menu(self):
        self.clear_text()
        print("(1) Travel\n(2) Shop\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.state = "travel_menu"
        elif sel == "2": self.state = "shop_menu"

    def exit_menu(self):
        self.text("Are you sure you want to exit?")
        self.clear_text()
        print("(1) Exit Without Saving\n(2) Save And Exit\n(0) Cancel")
        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.running = False
        elif sel == "2":
            self.save_data()
            self.running = False

    ##
    ### Quest
    ##

    def freetype(self, data):
        if data['object'] == 'player':
            if data['variable'] == "name":
                self.player.name = input(": ")

    def quest_menu(self):
        global quest
        part = quest[self.selected_quest]['part']
        if 'reward' in quest[self.selected_quest][part]:
            stat = quest[self.selected_quest][part]['reward']['stat']
            value = quest[self.selected_quest][part]['reward']['value']
            self.player.reward(stat, value)
        if 'completed' in quest[self.selected_quest][part]:
            quest[self.selected_quest]['completed'] = quest[self.selected_quest][part]['completed']
        if 'state' in quest[self.selected_quest][part]:
            self.state = quest[self.selected_quest][part]['state']
            return
        if 'freetype' in quest[self.selected_quest][part]:
            self.freetype(quest[self.selected_quest][part]['freetype'])
        self.text(quest[self.selected_quest][part]['prompt'])
        if 'option' in quest[self.selected_quest][part]:
            for o in quest[self.selected_quest][part]['option']:
                print("({}) {}".format(o, quest[self.selected_quest][part]['option'][o]['prompt']))
            sel = input(": ")
            if sel in quest[self.selected_quest][part]['option']:
                if 'reward' in quest[self.selected_quest][part]['option'][sel]:
                    stat = quest[self.selected_quest][part]['option'][sel]['reward']['stat']
                    value = quest[self.selected_quest][part]['option'][sel]['reward']['value']
                    self.player.reward(stat, value)
        quest[self.selected_quest]['part'] = quest[self.selected_quest][part]['part']

    def quest_history(self):
        for q in quest:
            if quest[q]['discovered']:
                qst = q
                if quest[q]['completed']:
                    qst = "".format()
                print()

    ##
    ### Battle
    ##

    def battle_stats(self):
        entity = self.player
        self.clear_text()
        print("(1) {}".format(self.player.name))
        print("(2) {}".format(self.mob.name))
        print("(0) Back")
        select = input(": ")
        if select == "0": return
        if select == "1": entity = self.player
        if select == "2": entity = self.mob
        self.entity_stats(entity, "battle")

    def battle_attack(self):
        hand = "hand_r"
        self.clear_text()
        print("(1) Left Hand\n(2) Right Hand\n(0) Back")
        select = input(": ")
        if select == "0": return
        if select == "1": hand = "left hand"
        if select == "2": hand = "right hand"
        dmg = self.player.get_damage(hand)
        self.mob.take_damage(dmg)
        self.text("{} attacked {} for {} damage".format(self.player.name, self.mob.name, max(1, dmg-self.mob.get_armor())))
        self.ai_turn = True
        self.state = "battle"

    def battle_magic(self):
        entity = self.mob
        self.clear_text()
        print("Select a target")
        print("(1) {}".format(self.mob.name))
        print("(2) {}".format(self.player.name))
        print("(0) Back")
        sel = input(": ")
        if sel == "0":
            self.state = "battle"
            return
        if sel == "1": entity = self.mob
        if sel == "2": entity = self.player
        self.clear_text()
        print("Select a spell to use")
        for i in self.player.spells:
            margin = self.menu_width - ( len(i) + len(str(self.player.spells[i])) + len(str(magic[i]['value'])) )
            print("[{}] {}{}{}".format(self.player.spells[i], i, " "*margin, magic[i]['value']))
        print("(0) Back")

        sel = input(": ")
        if sel == "0":
            self.state = "battle"
            return
        elif sel in self.player.spells:
            self.player.use_spell(sel, entity)
            self.text("{} used {} on {}".format(self.player.name, sel, entity.name))
            self.ai_turn = True
            self.state = "battle"

    def battle_item(self):
        sel = self.inventory_selection(self.player.inventory, "battle")
        if sel != "nothing":
            self.player.use_item(sel)
            self.text("{} used {}".format(self.player.name, sel))
            self.state = "battle"

    def battle_win(self):
        exp_bonus = int(mobs[self.mob.race]['exp']*(self.mob.level*mobs[self.mob.race]['curve']))
        self.player.gain_experience(exp_bonus)
        gold = int(self.mob.gold*0.75)
        self.player.gold = int(self.player.gold+gold)
        self.mob.gold = int(self.mob.gold-gold)
        if self.player.confused: self.player.confused = False
        if self.player.stunned: self.player.stunned = False
        self.text("{} won the battle, gaining {} experience and {} gold".format(self.player.name, exp_bonus, gold))
        for item in self.mob.equip:
            if self.mob.equip[item] != "nothing":
                self.mob.add_item(self.mob.equip[item])
        for item in self.mob.inventory:
            print("(1) Take {}".format(item))
            print("(0) Skip")
            sel = input(": ")
            if sel == "0": pass
            else:
                plural = ""
                if self.mob.inventory[item] > 1: plural = "s"
                for i in range(self.mob.inventory[item]):
                    self.player.add_item(item)
                self.text("{} looted {} {}{} from {}".format(self.player.name, self.mob.inventory[item], item, plural, self.mob.name))
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
        self.text("{} lost the battle, losing {} gold".format(self.player.name, gold))
        self.state = "main_menu"

    def battle_ai(self):
        if self.mob.burned:
            self.text("{} took {} burn damage".format(self.mob.name, 1))
            self.mob.take_damage(1)
            self.clear_text()
        if self.mob.poisoned:
            self.text("{} took {} poison damage".format(self.mob.name, 1))
            self.mob.take_damage(1)
            self.clear_text()
        if self.mob.hp < self.mob.HP/2:
            for i in self.mob.inventory:
                if 'hp' in items[i] and not 'mp' in items[i]:
                    if self.mob.hp+items[i]['hp'] <= self.mob.HP:
                        self.mob.use_item(i)
                        self.text("{} used {}".format(self.mob.name, i))
        if self.mob.mp < self.mob.MP/2:
            for i in self.mob.inventory:
                if 'mp' in items[i] and not 'hp' in items[i]:
                    if self.mob.mp+items[i]['mp'] <= self.mob.MP:
                        self.mob.use_item(i)
                        self.text("{} used {}".format(self.mob.name, i))
        if self.mob.hp < self.mob.HP/2 and self.mob.mp < self.mob.MP/2:
            for i in self.mob.inventory:
                if 'hp' in items[i] and 'mp' in items[i]:
                    if self.mob.hp+items[i]['hp'] <= self.mob.HP or self.mob.mp+items[i]['mp'] <= self.mob.MP:
                        self.mob.use_item(i)
                        self.text("{} used {}".format(self.mob.name, i))
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
                    self.text("{} casted {} on {}".format(self.mob.name, spell, entity.name))
                    self.ai_turn = False
        if not can_cast:
            hand = "hand_r"
            if self.mob.equip['left hand'] != "nothing": hand = "left hand"
            if self.mob.equip['right hand'] != "nothing": hand = "right hand"
            dmg = self.mob.get_damage(hand)
            self.player.take_damage(dmg)
            self.text("{} attacked {} for {} damage".format(self.mob.name, self.player.name, max(1, dmg-self.player.get_armor())))
            self.ai_turn = False

    def battle_player(self):
        if self.player.burned:
            self.text("{} took {} burn damage".format(self.player.name, 1))
            self.player.take_damage(1)
            self.clear_text()
        if self.player.poisoned:
            self.text("{} took {} poison damage".format(self.player.name, 1))
            self.player.take_damage(1)
            self.clear_text()
        print("(1) Attack\n(2) Stats\n(3) Magic\n(4) Item\n(0) Run")
        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.battle_attack()
        elif sel == "2": self.battle_stats()
        elif sel == "3": self.battle_magic()
        elif sel == "4": self.battle_item()

    def battle(self):
        self.clear_text()
        p_health = "HP:{}/{}".format(self.player.hp, self.player.HP)
        m_health = "HP:{}/{}".format(self.mob.hp, self.mob.HP)
        p_mana = "MP:{}/{}".format(self.player.mp, self.player.MP)
        m_mana = "MP:{}/{}".format(self.mob.mp, self.mob.MP)
        health_margin = self.menu_width-(len(self.player.name)+len(self.mob.name))
        print("{}{}{}".format(self.player.name," "*(self.menu_width-(len(self.player.name)+len(self.mob.name))),self.mob.name))
        print("{}{}{}".format(p_health," "*(self.menu_width-(len(p_health)+len(m_health))),m_health))
        print("{}{}{}".format(p_mana," "*(self.menu_width-(len(p_mana)+len(m_mana))),m_mana))
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

    ##
    ### Stats
    ##

    def entity_stats(self, entity, menu):
        self.clear_text()
        exp = "{}/{}".format(entity.exp, entity.level_up)
        ehp = "{}/{}".format(entity.hp, entity.HP)
        emp = "{}/{}".format(entity.mp, entity.MP)
        emg = "{} [{}]".format(entity.magic, entity.get_magic_bonus())
        eat = "{} [{}]".format(entity.attack, entity.get_attack_bonus())
        edf = "{} [{}]".format(entity.defense, entity.get_defense_bonus())
        print("Location:{}{}".format(" "*(self.menu_width-(len("Location:")+len(self.location))), self.location))
        print("\nName:{}{}".format(" "*(self.menu_width-(len("Name:")+len(entity.name))), entity.name))
        print("Gold:{}{}".format(" "*(self.menu_width-(len("Gold:")+len(str(entity.gold)))), entity.gold))
        print("Level:{}{}".format(" "*(self.menu_width-(len("Level:")+len(str(entity.level)))), entity.level))
        print("Points:{}{}".format(" "*(self.menu_width-(len("Points:")+len(str(entity.points)))), entity.points))
        print("Experience:{}{}".format(" "*(self.menu_width-(len("Experience:")+len(exp))), exp))
        print("\nHealth:{}{}".format(" "*(self.menu_width-(len("Health:")+len(ehp))), ehp))
        print("Mana:{}{}".format(" "*(self.menu_width-(len("Mana:")+len(emp))), emp))
        print("Magic:{}{}".format(" "*(self.menu_width-(len("Magic:")+len(emg))), emg))
        print("Attack:{}{}".format(" "*(self.menu_width-(len("Attack:")+len(eat))), eat))
        print("Defense:{}{}".format(" "*(self.menu_width-(len("Defense:")+len(edf))), edf))
        sel = input("\n: ")
        spending_points = bool(entity.points > 0)
        while spending_points > 0:
            if entity.points <= 0:
                spending_points = False
                self.state = menu
                return
            self.clear_text()
            exp = "{}/{}".format(entity.exp, entity.level_up)
            ehp = "{}/{}".format(entity.hp, entity.HP)
            emp = "{}/{}".format(entity.mp, entity.MP)
            emg = "{} [{}]".format(entity.magic, entity.get_magic_bonus())
            eat = "{} [{}]".format(entity.attack, entity.get_attack_bonus())
            edf = "{} [{}]".format(entity.defense, entity.get_defense_bonus())
            print("Location:{}{}".format(" "*(self.menu_width-(len("Location:")+len(self.location))), self.location))
            print("\nName:{}{}".format(" "*(self.menu_width-(len("Name:")+len(entity.name))), entity.name))
            print("Gold:{}{}".format(" "*(self.menu_width-(len("Gold:")+len(str(entity.gold)))), entity.gold))
            print("Level:{}{}".format(" "*(self.menu_width-(len("Level:")+len(str(entity.level)))), entity.level))
            print("Points:{}{}".format(" "*(self.menu_width-(len("Points:")+len(str(entity.points)))), entity.points))
            print("Experience:{}{}".format(" "*(self.menu_width-(len("Experience:")+len(exp))), exp))
            print("\nHealth:{}{}".format(" "*(self.menu_width-(len("Health:")+len(ehp))), ehp))
            print("Mana:{}{}".format(" "*(self.menu_width-(len("Mana:")+len(emp))), emp))
            print("Magic:{}{}".format(" "*(self.menu_width-(len("Magic:")+len(emg))), emg))
            print("Attack:{}{}".format(" "*(self.menu_width-(len("Attack:")+len(eat))), eat))
            print("Defense:{}{}".format(" "*(self.menu_width-(len("Defense:")+len(edf))), edf))
            print("(1) Increase Magic\n(2) Increase Attack\n(3) Increase Defense\n(4) Increase Health\n(5) Increase Mana\n(0) Back")
            sel = input(": ")
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
                entity.HP += 1
                entity.hp += 1
                entity.points -= 1
            elif sel == "5":
                entity.MP += 1
                entity.mp += 1
                entity.points -= 1
        self.state = menu

    ##
    ### Item
    ##

    def player_item(self):
        sel = self.inventory_selection(self.player.inventory, "inventory_menu")
        if sel != "nothing":
            self.player.use_item(sel)
            self.text("{} used {}".format(self.player.name, sel))

    def craft_item(self):
        for i in crafting:
            if self.player.can_craft_item(i):
                print("{}".format(i))
        print("(0) Back")
        sel = input(": ")
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
        self.clear_text()
        for part in self.player.equip:
            print("{}{}({})".format(part," "*(self.menu_width-(len(part)+len(self.player.equip[part]))),self.player.equip[part]))
        print("(0) Back")
        sel = input(": ")
        if sel == "0":
            self.state = "inventory_menu"
            return
        if sel in self.player.equip:
            part = sel
        self.clear_text()
        for i in self.player.inventory:
            if 'slot' in items[i]:
                if items[i]['slot'] in part:
                    margin = self.menu_width - ( len(i) + len(str(self.player.inventory[i])) + len(str(items[i]['value'])) )
                    print("[{}] {}{}{}".format(self.player.inventory[i], i, " "*margin, items[i]['value']))
        print("(1) nothing")
        print("(0) Back")
        sel = input(": ")
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
        sel = self.inventory_selection(self.shop.inventory, "shop_menu", "{}'s Gold: {}".format(self.player.name, self.player.gold))
        if sel != "nothing":
            if self.player.gold >= items[sel]['value']:
                self.shop.del_item(sel)
                self.shop.gold += items[sel]['value']
                self.player.add_item(sel)
                self.player.gold -= items[sel]['value']
                self.text("{} bought {}".format(self.player.name, sel))
                world[self.location]['shop'] = self.shop.get_data()

    def shop_sell(self):
        sel = self.inventory_selection(self.player.inventory, "shop_menu", "Shop's Gold: {}".format(self.shop.gold))
        if sel != "nothing":
            if self.shop.gold >= items[sel]['value']:
                self.player.del_item(sel)
                self.shop.add_item(sel)
                self.shop.gold -= items[sel]['value']
                self.player.gold += items[sel]['value']
                self.text("{} sold {}".format(self.player.name, sel))
                world[self.location]['shop'] = self.shop.get_data()

    def shop_menu(self):
        self.clear_text()
        print("(1) Buy\n(2) Sell\n(0) Leave")
        sel = input(": ")
        if sel == "0": self.state = "location_menu"
        elif sel == "1":
            self.state = "shop_buy"
            self.text("Let me show you what I have")
        elif sel == "2":
            self.text("Let me see what you have")
            self.state = "shop_sell"

    ##
    ### Travel
    ##

    def travel_menu(self):
        self.clear_text()
        print("\n\n")
        if 'north' in world[self.location]['travel']:
            print("(8) {}".format(world[self.location]['travel']['north']))
        if 'south' in world[self.location]['travel']:
            print("(2) {}".format(world[self.location]['travel']['south']))
        if 'east' in world[self.location]['travel']:
            print("(6) {}".format(world[self.location]['travel']['east']))
        if 'west' in world[self.location]['travel']:
            print("(4) {}".format(world[self.location]['travel']['west']))
        print("(0) Back")

        sel = input(": ")
        if sel == "0": self.state = "location_menu"
        elif sel == "8" and "north" in world[self.location]['travel']:
            self.state = "main_menu"
            self.location = world[self.location]['travel']['north']
        elif sel == "2" and "south" in world[self.location]['travel']:
            self.state = "main_menu"
            self.location = world[self.location]['travel']['south']
        elif sel == "6" and "east" in world[self.location]['travel']:
            self.state = "main_menu"
            self.location = world[self.location]['travel']['east']
        elif sel == "4" and "west" in world[self.location]['travel']:
            self.state = "main_menu"
            self.location = world[self.location]['travel']['west']

    ##
    ### Settings
    ##

    def set_speed(self):
        self.clear_text()
        print("(1) Fast\n(2) Normal\n(3) Slow\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            self.text_speed = 0.01
            self.text("Sample text to show timing")
        elif sel == "2":
            self.text_speed = 0.03
            self.text("Sample text to show timing")
        elif sel == "3":
            self.text_speed = 0.06
            self.text("Sample text to show timing")

    def set_pause(self):
        self.clear_text()
        print("(1) Fast\n(2) Medium\n(3) Slow\n(4) Wait\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            self.text_pause = 0.15
            self.text("Sample text to show timing")
        elif sel == "2":
            self.text_pause = 0.225
            self.text("Sample text to show timing")
        elif sel == "3":
            self.text_pause = 0.3
            self.text("Sample text to show timing")
        elif sel == "4":
            self.text_pause = -1.0

    def set_margin(self):
        self.clear_text()
        print("(1) 1\n(2) 3\n(3) 5\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            self.text_margin = 1
            self.text("Sample text to show margin")
        elif sel == "2":
            self.text_margin = 3
            self.text("Sample text to show margin")
        elif sel == "3":
            self.text_margin = 5
            self.text("Sample text to show margin")

    def set_width(self):
        self.clear_text()
        print("(1) 32\n(2) 48\n(3) 64\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            self.menu_width = 48
            self.text("Sample text to show margin")
        elif sel == "2":
            self.menu_width = 56
            self.text("Sample text to show margin")
        elif sel == "3":
            self.menu_width = 64
            self.text("Sample text to show margin")

    def set_setting(self, setting, settings):
        for s in settings:
            print("({}) {}".format(settings[s]['select'], settings[s]['prompt']))

    def settings(self):
        self.clear_text()
        print("(1) Text Speed\n(2) Text Pause\n(3) Clear Margin\n(4) Menu Width\n(0) Back")

        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.state = "set_speed"
        elif sel == "2": self.state = "set_pause"
        elif sel == "3": self.state = "set_margin"
        elif sel == "4": self.state = "set_width"

    def update_background(self):
        for l in world:
            if random.randint(0, 1000) < world[l]['restock']:
                gold = world[l]['shop']['gold']
                markup = world[l]['shop']['markup']
                if random.randint(0, 1000) < 2: gold += random.randint(-gold/4, gold/4)
                if random.randint(0, 1000) < 1: markup += random.randrange(-0.01, 0.01)
                S = Shop(gold, markup)
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
        elif self.state == "inventory_menu": self.inventory_menu()
        elif self.state == "location_menu": self.location_menu()
        elif self.state == "main_menu": self.main_menu()
        elif self.state == "set_speed": self.set_speed()
        elif self.state == "set_pause": self.set_pause()
        elif self.state == "set_margin": self.set_margin()
        elif self.state == "set_width": self.set_width()
        elif self.state == "settings": self.settings()
        elif self.state == "new_game": self.new_game()
        elif self.state == "intro": self.intro()
        elif self.state == "exit": self.exit_menu()

    def start(self):
        self.run()

    def run(self):
        while self.running:
            self.update()
