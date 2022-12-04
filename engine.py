import time, random
from os import path

from output import *
from world_map import *
from game_data import *

from shop import Shop
from entity import Entity

from ESbattle import *
from EScharacter import *
from ESitem import *
from ESquest import *
from ESsettings import *
from ESshop import *
from EStravel import *

class Engine():

    def __init__(self):
        pass

    ##
    ### Data
    ##

    def get_data_path(self):
        data_file = "slot-{}-{}".format(V.data_slot, V.data_file)
        return path.join(path.join(path.dirname(__file__), V.data_path), data_file)

    def load_quest_data(self):
        global quest
        import json
        quest_list = []
        with open(path.join(path.join(path.dirname(__file__), V.quest_path), "QuestList.json"),"r") as f:
            qd = json.loads(f.read().strip())
            for q in qd:
                if qd[q]: quest_list.append(q)
        for q in quest_list:
            data_file = "{}.json".format(q)
            data_path = path.join(path.join(path.dirname(__file__), V.quest_path), data_file)
            try:
                with open(data_path,"r") as f:
                    q_data = json.loads(f.read().strip())
                    quest[q] = q_data
            except FileNotFoundError:
                T.text("Quest File at path '{}' Not Found".format(data_path))
            

    def save_data(self):
        import json
        colors = {
            'text1' : [V.c_text1.r, V.c_text1.g, V.c_text1.b],
            'text2' : [V.c_text2.r, V.c_text2.g, V.c_text2.b],
            'count' : [V.c_count.r, V.c_count.g, V.c_count.b],
            'attack' : [V.c_attack.r, V.c_attack.g, V.c_attack.b],
            'defense' : [V.c_defense.r, V.c_defense.g, V.c_defense.b],
            'magic' : [V.c_magic.r, V.c_magic.g, V.c_magic.b],
            'gold' : [V.c_gold.r, V.c_gold.g, V.c_gold.b],
            }
        data = {
                'colors' : colors,
                "text_pause" : T.text_pause,
                "text_speed" : T.text_speed,
                "text_margin" : T.text_margin,
                "menu_width" : T.menu_width,
                "location" : V.location,
                "quest" : V.selected_quest,
                "quests" : quest,
                "player" : V.player.get_data(),
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
            V.location = data['location']
            V.selected_quest = data['quest']
            quest = data['quests']
            V.player.set_data(data['player'])
            world = data['world']
            colors = data['colors']
            V.c_text1.r = colors["text1"][0]
            V.c_text1.g = colors["text1"][1]
            V.c_text1.b = colors["text1"][2]
            V.c_text2.r = colors["text2"][0]
            V.c_text2.g = colors["text2"][1]
            V.c_text2.b = colors["text2"][2]
            V.c_count.r = colors["count"][0]
            V.c_count.g = colors["count"][1]
            V.c_count.b = colors["count"][2]
            V.c_attack.r = colors["attack"][0]
            V.c_attack.g = colors["attack"][1]
            V.c_attack.b = colors["attack"][2]
            V.c_defense.r = colors["defense"][0]
            V.c_defense.g = colors["defense"][1]
            V.c_defense.b = colors["defense"][2]
            V.c_magic.r = colors["magic"][0]
            V.c_magic.g = colors["magic"][1]
            V.c_magic.b = colors["magic"][2]
            V.c_gold.r = colors["gold"][0]
            V.c_gold.g = colors["gold"][1]
            V.c_gold.b = colors["gold"][2]
            f.close()
        V.state = "main_menu"

    ##
    ### Game Menus
    ##

    def main_menu(self):
        T.clear_text()
        T.print("(1) Battle\n(2) Stats\n(3) Inventory\n(4) Location\n(5) Quests\n(6) Settings\n(0) Exit", "\n", V.c_text2)
        sel = T.input(": ")
        if sel == "0": V.state = "exit"
        elif sel == "1": V.state = "prepare_battle"
        elif sel == "2": V.entity_stats(V.player, "main_menu")
        elif sel == "3": V.state = "inventory_menu"
        elif sel == "4": V.state = "location_menu"
        elif sel == "5": V.state = "quest_history"
        elif sel == "6": V.state = "settings"

    def inventory_menu(self):
        T.clear_text()
        T.print("(1) Items\n(2) Equip\n(3) Craft\n(0) Back", "\n", V.c_text2)
        sel = T.input(": ")
        if sel == "0": V.state = "main_menu"
        elif sel == "1": V.state = "item"
        elif sel == "2": V.state = "equip"
        elif sel == "3": V.state = "craft"

    def location_menu(self):
        T.clear_text()
        T.print("(1) Travel\n(2) Shop\n(0) Back", "\n", V.c_text2)
        sel = T.input(": ")
        if sel == "0": V.state = "main_menu"
        elif sel == "1": V.state = "travel_menu"
        elif sel == "2": V.state = "shop_menu"

    def exit_menu(self):
        T.text(T.get_colored_text("Are you sure you want to exit?", V.c_text1))
        T.clear_text()
        T.print("(1) Exit Without Saving\n(2) Save And Exit\n(0) Cancel", "\n", V.c_text2)
        sel = T.input(": ")
        if sel == "0": V.state = "main_menu"
        elif sel == "1": V.running = False
        elif sel == "2":
            self.save_data()
            V.running = False
        T.clear_text()

    def new_game(self):
        for l in world:
            S = Shop(world[l]['shop']['gold'], world[l]['shop']['markup'])
            world[l]['shop'] = S.get_data()
        #self.load_quest_data()
        V.state = 'quest'
        V.selected_quest = "Intro"

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
        T.print(output_menu, "\n", V.c_text2)

        sel = T.input(": ")
        if sel == "0":
            V.running = False
            T.clear_text()
        elif sel == "1": V.state = "select_race"
        elif sel == "2" and can_continue: self.load_data()

    ##
    ### Update
    ##

    def update_background(self):
        for l in world:
            if random.randint(0, 1000) < world[l]['restock']:
                S = Shop(0, 0)
                S.set_data(world[l]['shop'])
                S.restock()
                world[l]['shop'] = S.get_data()
        V.shop.set_data(world[V.location]['shop'])

    def update(self):
        self.update_background()
        #
        if V.state == "battle": battle()
        elif V.state == "prepare_battle": prepare_battle()
        #
        elif V.state == "quest": quest_menu()
        elif V.state == "quest_history": quest_history()
        #
        elif V.state == "travel_menu": travel_menu()
        #
        elif V.state == "item": player_item()
        elif V.state == "equip": equip()
        elif V.state == "craft": craft_item()
        #
        elif V.state == "shop_buy": shop_buy()
        elif V.state == "shop_sell": shop_sell()
        elif V.state == "shop_menu": shop_menu()
        #
        elif V.state == "set_speed": set_speed()
        elif V.state == "set_pause": set_pause()
        elif V.state == "set_margin": set_margin()
        elif V.state == "set_width": set_width()
        elif V.state == "set_color": set_color()
        elif V.state == "settings": settings()
        #
        elif V.state == "level_up": level_up()
        elif V.state == "select_race": select_race()
        elif V.state == "select_job": select_job()
        elif V.state == "select_sex": select_sex()
        #
        elif V.state == "inventory_menu": self.inventory_menu()
        elif V.state == "location_menu": self.location_menu()
        elif V.state == "main_menu": self.main_menu()
        elif V.state == "new_game": self.new_game()
        elif V.state == "intro": self.intro()
        elif V.state == "exit": self.exit_menu()

    def start(self):
        self.run()

    def run(self):
        while V.running:
            self.update()
