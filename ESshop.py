from var import *
from output import *

def shop_buy():
    value_offset = (V.shop.markup*0.5)
    sel = V.inventory_selection(V.shop.inventory, "shop_menu", "{}'s Gold: {}".format(V.player.name, V.player.gold), value_offset)
    if sel != "nothing":
        val = int(((1.0-(V.player.skills['barter']*0.01))*items[sel]['value'])*value_offset)
        if V.player.gold >= val:
            V.shop.del_item(sel)
            V.shop.gold += val
            V.player.add_item(sel)
            V.player.gold -= val
            T.text("{} bought {} for {} gold.".format(V.player.name, sel, val))
            world[V.location]['shop'] = V.shop.get_data()

def shop_sell():
    value_offset = (V.shop.markup*0.5)+(V.player.skills['barter']*0.005)
    sel = V.inventory_selection(V.player.inventory, "shop_menu", "Shop's Gold: {}".format(V.shop.gold), V.shop.markup)
    if sel != "nothing":
        val = int(((1.0-(V.player.skills['barter']*0.01))*items[sel]['value'])*value_offset)
        if V.shop.gold >= val:
            V.player.del_item(sel)
            V.player.gold += val
            V.shop.add_item(sel)
            V.shop.gold -= val
            T.text("{} sold {} for {} gold.".format(V.player.name, sel, val))
            world[V.location]['shop'] = V.shop.get_data()

def shop_menu():
    T.clear_text()
    T.print("(1) Buy\n(2) Sell\n(0) Leave", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0": V.state = "location_menu"
    elif sel == "1":
        V.state = "shop_buy"
        T.text("Let me show you what I have")
    elif sel == "2":
        T.text("Let me see what you have")
        V.state = "shop_sell"
