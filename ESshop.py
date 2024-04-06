from var import *
from output import *

def shop_item_buy(sel, val):
    T.text("How many?")
    amnt = int(T.input(": "))
    for i in range(amnt+1):
        if V.player.gold >= (i*val):
            limit = i
    for i in range(limit):
        V.shop.del_item(sel)
        V.shop.gold += val
        V.player.add_item(sel)
        V.player.gold -= val
    T.text("{} bought {} ({}) for {} gold.".format(V.player.name, sel, limit, limit*val))
    world[V.location]['shop'] = V.shop.get_data()

def shop_item_sell(sel, val):
    T.text("How many?")
    amnt = int(T.input(": "))
    for i in range(amnt+1):
        if V.shop.gold >= (i*val):
            limit = i
    for i in range(limit):
        V.player.del_item(sel)
        V.player.gold += val
        V.shop.add_item(sel)
        V.shop.gold -= val
    T.text("{} sold {} ({}) for {} gold.".format(V.player.name, sel, limit, limit*val))
    world[V.location]['shop'] = V.shop.get_data()

def shop_buy():
    skill_offset = V.player.skills['barter']*0.01
    value_offset = V.shop.markup
    sel = V.inventory_selection(V.shop.inventory, "shop_menu", "{}'s Gold: {}".format(V.player.name, V.player.gold), value_offset)
    if sel != "nothing":
        val = int(items[sel]['value']*value_offset)
        if V.player.gold >= val:
            shop_item_buy(sel, val)

def shop_sell():
    skill_offset = V.player.skills['barter']*0.01
    value_offset = skill_offset
    sel = V.inventory_selection(V.player.inventory, "shop_menu", "Shop's Gold: {}".format(V.shop.gold), value_offset)
    if sel != "nothing":
        val = int(items[sel]['value']*value_offset)
        if V.shop.gold >= val:
            shop_item_sell(sel, val)

def shop_menu():
    T.clear_text()
    T.print("(1) Buy\n(2) Sell\n(0) Leave", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0": V.state = "location_menu"
    elif sel == "1":
        V.state = "shop_buy"
        text_option = random.choice(phrases[V.state])
        T.text(text_option)
    elif sel == "2":
        V.state = "shop_sell"
        text_option = random.choice(phrases[V.state])
        T.text(text_option)
