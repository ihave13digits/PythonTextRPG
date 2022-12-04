from var import *
from output import *

def travel_menu():
    T.clear_text()
    print(world_map)
    T.expanded_text("Location:", V.location)
    n_txt = ""
    s_txt = ""
    e_txt = ""
    w_txt = ""
    if 'north' in world[V.location]['travel']: n_txt = "(8) {}".format(world[V.location]['travel']['north'])
    if 'west' in world[V.location]['travel']: w_txt = "(4) {}".format(world[V.location]['travel']['west'])
    if 'east' in world[V.location]['travel']: e_txt = "(6) {}".format(world[V.location]['travel']['east'])
    if 'south' in world[V.location]['travel']: s_txt = "(2) {}".format(world[V.location]['travel']['south'])
    n_off = int(32-int(len(n_txt)/2))
    s_off = int(32-int(len(s_txt)/2))
    ew_off = int(64-int((len(e_txt))+(len(w_txt))))
    b_off = int(32-int(len("(0) Back")/2))
    T.print("{}{}".format(" "*n_off, n_txt), "\n", V.c_text2)
    T.print("{}{}{}".format(w_txt, " "*ew_off, e_txt), "\n", V.c_text2)
    T.print("{}{}".format(" "*s_off, s_txt), "\n", V.c_text2)
    T.print("{}(0) Back".format(" "*b_off), "\n", V.c_text2)

    sel = T.input(": ")
    if sel == "0": V.state = "location_menu"
    elif sel == "8" and "north" in world[V.location]['travel']:
        if V.roll_skill(V.player, 'travel'):
            V.state = "travel_menu"
            V.location = world[V.location]['travel']['north']
        else: V.state = "prepare_battle"
    elif sel == "2" and "south" in world[V.location]['travel']:
        if V.roll_skill(V.player, 'travel'):
            V.state = "travel_menu"
            V.location = world[V.location]['travel']['south']
        else: V.state = "prepare_battle"
    elif sel == "4" and "west" in world[V.location]['travel']:
        if V.roll_skill(V.player, 'travel'):
            V.state = "travel_menu"
            V.location = world[V.location]['travel']['west']
        else: V.state = "prepare_battle"
    elif sel == "6" and "east" in world[V.location]['travel']:
        if V.roll_skill(V.player, 'travel'):
            V.state = "travel_menu"
            V.location = world[V.location]['travel']['east']
        else: V.state = "prepare_battle"
