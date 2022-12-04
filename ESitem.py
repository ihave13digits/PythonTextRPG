from var import *
from output import *

def player_item():
    sel = V.inventory_selection(V.player.inventory, "inventory_menu")
    if sel != "nothing":
        V.player.use_item(sel)
        T.text("{} used {}".format(V.player.name, sel))

def craft_item():
    T.clear_text()
    for i in crafting:
        if V.player.can_craft_item(i):
            T.print("{}".format(i), "\n", V.c_text2)
    T.print("(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0":
        V.state = "inventory_menu"
        return
    if sel in crafting and V.player.can_craft_item(sel):
        V.player.craft_item(sel)



def equip():
    part = ""
    T.clear_text()
    for part in V.player.equip:
        T.print("({}){}{}".format(part," "*(T.menu_width-(len(part)+len(V.player.equip[part]))),V.player.equip[part]), "\n", V.c_text2)
    T.print("(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0":
        V.state = "inventory_menu"
        return
    if sel in V.player.equip:
        part = sel
    T.clear_text()
    for i in V.player.inventory:
        if 'slot' in items[i]:
            if items[i]['slot'] in part:
                margin = T.menu_width - ( len(i) + len(str(V.player.inventory[i])) + len(str(items[i]['value'])) )
                T.print("[{}] {}{}{}".format(V.player.inventory[i], i, " "*margin, items[i]['value']), "\n", V.c_text2)
    T.print("(1) nothing\n(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0":
        V.state = "equip"
        return
    if sel == "1": sel = "nothing"
    if sel in V.player.inventory or sel == "nothing":
        if part != "":
            V.player.equip_item(sel, part)
