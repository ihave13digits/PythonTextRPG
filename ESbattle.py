from var import *
from output import *

def battle_stats():
    entity = V.player
    T.clear_text()
    T.print("(1) {}\n(2) {}\n(0) Back".format(V.player.name, V.mob.name), "\n", V.c_text2)
    select = T.input(": ")
    if select == "0": return
    if select == "1": entity = V.player
    if select == "2": entity = V.mob
    V.entity_stats(entity, "battle")

def battle_attack():
    hand = "right hand"
    T.clear_text()
    T.print("(1) Left Hand\n(2) Right Hand\n(0) Back", "\n", V.c_text2)
    select = T.input(": ")
    if select == "0": return
    if select == "1": hand = "left hand"
    if select == "2": hand = "right hand"
    if V.roll_skill(V.player, "combat"):
        dmg = V.player.get_damage(hand)
        V.mob.take_damage(dmg)
        T.text("{} attacked {} for {} damage".format(V.player.name, V.mob.name, max(1, dmg-V.mob.get_armor())))
    else:
        T.text("{} missed".format(V.player.name))
    V.player.take_stat_damage()
    V.ai_turn = True
    V.state = "battle"

def battle_magic():
    entity = V.mob
    T.clear_text()
    T.print("(1) {}\n(2) {}\n(0) Back".format(V.player.name, V.mob.name), "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0":
        V.state = "battle"
        return
    if sel == "1": entity = V.player
    if sel == "2": entity = V.mob
    T.clear_text()
    T.print("Select a spell to use", "\n", V.c_text1)
    for i in magic:
        if i in V.player.spells:
            margin = T.menu_width - ( len(i) + len(str(V.player.spells[i])) + len(str(magic[i]['cost'])) )
            T.print("[{}] {}{}{}".format(V.player.spells[i], i, " "*margin, magic[i]['cost']), "\n", V.c_text2)
    T.print("(0) Back", "\n", V.c_text2)

    sel = T.input(": ")
    if sel == "0":
        V.state = "battle"
        return
    elif sel in V.player.spells:
        if V.roll_skill(V.player, 'cast'):
            V.player.use_spell(sel, entity)
            T.text("{} used {} on {}".format(V.player.name, sel, entity.name))
        else:
            T.text("{} miscasted {} on {}".format(V.player.name, sel, entity.name))
        V.player.take_stat_damage()
        V.ai_turn = True
        V.state = "battle"

def battle_item(self):
    sel = V.inventory_selection(V.player.inventory, "battle")
    if sel != "nothing":
        V.player.use_item(sel)
        T.text("{} used {}".format(V.player.name, sel))
        V.state = "battle"

def battle_win():
    exp_bonus = int(mobs[V.mob.race]['exp']*(V.mob.level*mobs[V.mob.race]['curve']))
    V.player.gain_experience(exp_bonus)
    gold = int(V.mob.gold*0.75)
    V.player.gold = int(V.player.gold+gold)
    V.mob.gold = int(V.mob.gold-gold)
    if V.player.confused: V.player.confused = False
    if V.player.stunned: V.player.stunned = False
    T.text("{} won the battle, gaining {} experience and {} gold".format(V.player.name, exp_bonus, gold))
    for item in V.mob.equip:
        if V.mob.equip[item] != "nothing":
            V.mob.add_item(V.mob.equip[item])
    for item in V.mob.inventory:
        T.print("(1) Take {}\n(0) Skip".format(item), "\n", V.c_text2)
        sel = T.input(": ")
        if sel == "0": pass
        else:
            plural = ""
            if V.mob.inventory[item] > 1: plural = "s"
            for i in range(V.mob.inventory[item]):
                V.player.add_item(item)
            T.text("{} looted {} {}{} from {}".format(V.player.name, V.mob.inventory[item], item, plural, V.mob.name))
    V.state = "main_menu"

def battle_lose():
    gold = int(V.player.gold*0.75)
    V.player.gold = int(V.player.gold-gold)
    V.mob.gold = int(V.mob.gold+gold)
    V.player.hp = V.player.HP
    V.player.mp = V.player.MP
    if V.player.poisoned: V.player.poisoned = False
    if V.player.confused: V.player.confused = False
    if V.player.stunned: V.player.stunned = False
    if V.player.burned: V.player.burned = False
    T.text("{} lost the battle, losing {} gold".format(V.player.name, gold))
    V.state = "main_menu"

def battle_ai():
    affliction = ""
    can_perform_action = True
    if V.mob.stunned:
        if random.randint(0, 100) < 10:
            affiction = "being stunned"
            can_perform_action = False
    if V.mob.confused:
        if random.randint(0, 100) < 10:
            affiction = "confusion"
            can_perform_action = False
    
    if can_perform_action:
        if V.mob.hp < V.mob.HP/2:
            try:
                for i in V.mob.inventory:
                    if 'hp' in items[i] and not 'mp' in items[i]:
                        if V.mob.hp+items[i]['hp'] <= V.mob.HP:
                            V.mob.use_item(i)
                            T.text("{} used {}".format(V.mob.name, i))
            except: pass
        elif V.mob.mp < V.mob.MP/2:
            try:
                for i in V.mob.inventory:
                    if 'mp' in items[i] and not 'hp' in items[i]:
                        if V.mob.mp+items[i]['mp'] <= V.mob.MP:
                            V.mob.use_item(i)
                            T.text("{} used {}".format(V.mob.name, i))
            except: pass
        elif V.mob.hp < V.mob.HP/2 and V.mob.mp < V.mob.MP/2:
            try:
                for i in V.mob.inventory:
                    if 'hp' in items[i] and 'mp' in items[i]:
                        if V.mob.hp+items[i]['hp'] <= V.mob.HP or V.mob.mp+items[i]['mp'] <= V.mob.MP:
                            V.mob.use_item(i)
                            T.text("{} used {}".format(V.mob.name, i))
            except: pass
        can_cast = bool(random.randint(0, V.mob.MP) < V.mob.mp)
        if len(V.mob.spells) > 0:
            if can_cast:
                spell = "nothing"
                entity = V.mob
                for s in V.mob.spells:
                    if magic[s]['cost'] <= V.mob.mp:
                        can_cast = True
                        if 'damage' in magic[s]:
                            entity = V.player
                        if 'hp' in magic[s]:
                            entity = V.mob
                        spell = s
                if can_cast and spell != "nothing":
                    if V.roll_skill(V.mob, 'cast'):
                        V.mob.use_spell(spell, entity)
                        T.text("{} casted {} on {}".format(V.mob.name, spell, entity.name))
                    else:
                        T.text("{} miscasted {} on {}".format(V.mob.name, spell, entity.name))
                    V.mob.take_stat_damage()
                    V.ai_turn = False
        if not can_cast:
            hand = "right hand"
            if V.mob.equip['left hand'] != "nothing": hand = "left hand"
            elif V.mob.equip['right hand'] != "nothing": hand = "right hand"
            if V.roll_skill(V.mob, 'combat'):
                dmg = V.mob.get_damage(hand)
                V.player.take_damage(dmg)
                T.text("{} attacked {} for {} damage".format(V.mob.name, V.player.name, max(1, dmg-V.player.get_armor())))
            else:
                T.text("{} missed".format(V.mob.name))
            V.mob.take_stat_damage()
            V.ai_turn = False
    elif not can_perform_action:
        T.text("{} couldn't attack due to {}".format(V.mob.name, affliction))
        V.mob.take_stat_damage()
        V.ai_turn = False

    
def battle_player():
    T.print("(1) Attack\n(2) Stats\n(3) Magic\n(4) Item\n(0) Run", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0": V.state = "main_menu"
    elif sel == "1": battle_attack()
    elif sel == "2": battle_stats()
    elif sel == "3": battle_magic()
    elif sel == "4": battle_item()

def battle():
    T.clear_text()
    p_health = "HP:{}/{}".format(V.player.hp, V.player.HP)
    m_health = "HP:{}/{}".format(V.mob.hp, V.mob.HP)
    p_mana = "MP:{}/{}".format(V.player.mp, V.player.MP)
    m_mana = "MP:{}/{}".format(V.mob.mp, V.mob.MP)
    health_margin = T.menu_width-(len(V.player.name)+len(V.mob.name))
    T.print("{}{}{}".format(V.player.name," "*(T.menu_width-(len(V.player.name)+len(V.mob.name))),V.mob.name), "\n", V.c_text1)
    T.print("{}{}{}".format(p_health," "*(T.menu_width-(len(p_health)+len(m_health))),m_health), "\n", V.c_text1)
    T.print("{}{}{}".format(p_mana," "*(T.menu_width-(len(p_mana)+len(m_mana))),m_mana), "\n", V.c_text1)
    print()
    if V.player.hp <= 0:
        V.battle_lose()
        return
    if V.mob.hp <= 0:
        battle_win()
        return
    if V.ai_turn: battle_ai()
    else: battle_player()

def prepare_battle():
    V.ai_turn = random.choice([True, False])
    V.randomize_mob()
    txt = ""
    if V.ai_turn: txt = "{} is engaging {}".format(V.mob.race.capitalize(), V.player.name)
    else: txt = "{} is engaging {}".format(V.player.name, V.mob.race)
    T.clear_text()
    T.text(txt)
    chcs = ""
    if not V.ai_turn:
        T.print("(1) Engage\n(0) Retreat", "\n", V.c_text2)
        sel = T.input(": ")
        if not V.ai_turn and sel == "0":
            V.state = "main_menu"
            return
    V.state = "battle"
