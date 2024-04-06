from var import *
from output import *

def player_item():
    sel = V.inventory_selection(V.player.inventory, "inventory_menu")
    if sel != "nothing":
        V.player.use_item(sel)
        T.text("{} used {}".format(V.player.name, sel))

def show_recipe(r):
    T.clear_text()
    T.print(r, "\n\n", V.c_text1)
    T.print("Requires:", "\n", V.c_text1)
    for i in crafting[r]['take']:
        T.print("  {} {}".format(i, crafting[r]['take'][i]), "\n", V.c_text1)
    T.print("Produces:", "\n", V.c_text1)
    for i in crafting[r]['give']:
        T.print("  {} {}".format(i, crafting[r]['give'][i]), "\n", V.c_text1)
    T.print("\n(1) Craft\n(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0": return
    if sel == '1': V.player.craft_item(r)
    show_recipe(r)

def craft_item():
    craftable = []
    T.clear_text()
    for i in crafting:
        if V.player.can_craft_item(i):
            if not i in craftable:
                craftable.append(i)
    for i in craftable:
        T.print("{}".format(i), "\n", V.c_text2)
    T.print("(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0":
        V.state = "inventory_menu"
        return
    if sel in craftable:
        show_recipe(sel)

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
