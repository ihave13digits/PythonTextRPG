from var import *
from output import *

def freetype(data):
    if data['object'] == 'player':
        if data['variable'] == "name":
            V.player.name = T.input(": ")
            V.quest_hash['player_name'] = V.player.name

def quest_menu():
    global quest
    passed = True
    part = quest[V.selected_quest]['part']
    if 'require' in quest[V.selected_quest][part]:
        if 'stat' in quest[V.selected_quest][part]['require']:
            stat = quest[V.selected_quest][part]['require']['stat']
            value = quest[V.selected_quest][part]['require']['value']
            if not V.player.require('stat', stat, value):
                passed = False
        elif 'skill' in quest[V.selected_quest][part]['option'][sel]['reward']:
            stat = quest[V.selected_quest][part]['option'][sel]['reward']['skill']
            value = quest[V.selected_quest][part]['option'][sel]['reward']['value']
            V.player.require('skill', stat, value)
        elif 'item' in quest[V.selected_quest][part]['require']:
            stat = quest[V.selected_quest][part]['require']['item']
            value = quest[V.selected_quest][part]['require']['value']
            if not V.player.require('item', stat, value):
                passed = False
    if 'reward' in quest[V.selected_quest][part]:
        if 'stat' in quest[V.selected_quest][part]['reward']:
            key = quest[V.selected_quest][part]['reward']['stat']
            value = quest[V.selected_quest][part]['reward']['value']
            V.player.reward('stat', key, value)
        elif 'skill' in quest[V.selected_quest][part]['reward']:
            key = quest[V.selected_quest][part]['reward']['skill']
            value = quest[V.selected_quest][part]['reward']['value']
            V.player.reward('skill', key, value)
        elif 'item' in quest[V.selected_quest][part]['reward']:
            key = quest[V.selected_quest][part]['reward']['item']
            value = quest[V.selected_quest][part]['reward']['value']
            V.player.reward('item', key, value)
    if 'add_quest' in quest[V.selected_quest][part]:
        q = quest[V.selected_quest][part]['add_quest']['quest']
        quest[q]['discovered'] = True
    if 'completed' in quest[V.selected_quest][part]:
        quest[V.selected_quest]['completed'] = quest[V.selected_quest][part]['completed']
    if 'state' in quest[V.selected_quest][part]:
        V.state = quest[V.selected_quest][part]['state']
        return
    if 'freetype' in quest[V.selected_quest][part]:
        freetype(quest[V.selected_quest][part]['freetype'])
    
    if 'prompt' in quest[V.selected_quest][part]:
        T.text(quest[V.selected_quest][part]['prompt'])
    elif 'fprompt' in quest[V.selected_quest][part]:
        T.text(quest[V.selected_quest][part]['fprompt'].format(**V.quest_hash))
    
    if 'option' in quest[V.selected_quest][part]:
        for o in quest[V.selected_quest][part]['option']:
            T.print("({}) {}".format(o, quest[V.selected_quest][part]['option'][o]['prompt']), "\n", V.c_text1)
        sel = T.input(": ")
        if sel in quest[V.selected_quest][part]['option']:
            if 'require' in quest[V.selected_quest][part]['option'][sel]:
                if 'stat' in quest[V.selected_quest][part]['option'][sel]['require']:
                    stat = quest[V.selected_quest][part]['option'][sel]['require']['stat']
                    value = quest[V.selected_quest][part]['option'][sel]['require']['value']
                    if not V.player.require('stat', stat, value):
                        passed = False
                elif 'skill' in quest[V.selected_quest][part]['option'][sel]['reward']:
                    stat = quest[V.selected_quest][part]['option'][sel]['reward']['skill']
                    value = quest[V.selected_quest][part]['option'][sel]['reward']['value']
                    V.player.require('skill', stat, value)
                elif 'item' in quest[V.selected_quest][part]['option'][sel]['require']:
                    stat = quest[V.selected_quest][part]['option'][sel]['require']['item']
                    value = quest[V.selected_quest][part]['option'][sel]['require']['value']
                    if not V.player.require('item', stat, value):
                        passed = False
            if 'reward' in quest[V.selected_quest][part]['option'][sel]:
                if 'stat' in quest[V.selected_quest][part]['option'][sel]['reward']:
                    stat = quest[V.selected_quest][part]['option'][sel]['reward']['stat']
                    value = quest[V.selected_quest][part]['option'][sel]['reward']['value']
                    V.player.reward('stat', stat, value)
                elif 'skill' in quest[V.selected_quest][part]['option'][sel]['reward']:
                    stat = quest[V.selected_quest][part]['option'][sel]['reward']['skill']
                    value = quest[V.selected_quest][part]['option'][sel]['reward']['value']
                    V.player.reward('skill', stat, value)
                elif 'item' in quest[V.selected_quest][part]['option'][sel]['reward']:
                    stat = quest[V.selected_quest][part]['option'][sel]['reward']['item']
                    value = quest[V.selected_quest][part]['option'][sel]['reward']['value']
                    V.player.reward('item', stat, value)
            if 'part' in quest[V.selected_quest][part]['option'][sel] and passed:
                quest[V.selected_quest]['part'] = quest[V.selected_quest][part]['option'][sel]['part']
            elif 'part' in quest[V.selected_quest][part]['option'][sel] and not passed:
                V.state = "main_menu"
    if 'part' in quest[V.selected_quest][part] and passed:
        quest[V.selected_quest]['part'] = quest[V.selected_quest][part]['part']
    elif 'part' in quest[V.selected_quest][part] and not passed:
        V.state = "main_menu"

def quest_history():
    T.clear_text()
    T.print("{}\n".format(V.selected_quest), "\n", V.c_text1)
    for q in quest:
        qst = ""
        if quest[q]['discovered']:
            qst = q
            cplt = "Incomplete"
            if quest[q]['completed']:
                cplt = "Completed"
            T.print("{}{}{}| {}".format(qst, " "*(T.menu_width-(len(qst)+len(quest[q]['location'])+len(cplt)+2)), quest[q]['location'], cplt), "\n", V.c_text2)
    T.print()
    psbl = ""
    if quest[V.selected_quest]['location'] == V.location and quest[V.selected_quest]['discovered'] == True and not quest[V.selected_quest]['completed']:
        psbl = "(1) Accept Quest\n"
    T.print("{}(0) Back\n".format(psbl), "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0":
        V.state = "main_menu"
    if sel == "1" and psbl != "":
        V.state = "quest"
    if sel in quest:
        V.selected_quest = sel
