from var import *
from output import *

def select_race():
    T.clear_text()
    R = V.player.race
    T.print(R, "\n\n", V.c_text1)
    T.expanded_text("Health:", str(mobs[R]['hp']), " ", V.c_text1)
    T.expanded_text("Magic:", str(mobs[R]['mp']), " ", V.c_text1)
    T.expanded_text("Attack:", str(mobs[R]['atk']), " ", V.c_text1)
    T.expanded_text("Defense:", str(mobs[R]['def']), " ", V.c_text1)
    T.expanded_text("Strength:", str(mobs[R]['str']), " ", V.c_text1)
    T.expanded_text("Constitution:", str(mobs[R]['con']), " ", V.c_text1)
    T.expanded_text("Dexterity:", str(mobs[R]['dex']), " ", V.c_text1)
    T.expanded_text("Awareness:", str(mobs[R]['awa']), " ", V.c_text1)
    T.expanded_text("Intelligence:", str(mobs[R]['int']), " ", V.c_text1)
    T.expanded_text("Charisma:", str(mobs[R]['cha']), " ", V.c_text1)
    T.print()
    for p in playable_mobs:
        T.print("({})".format(p), "\n", V.c_text2)
    T.print("(0){}Continue".format(" "*(T.menu_width-(len("(0)")+len("Continue")))), "\n", V.c_text2)
    sel = T.input(": ")
    if sel in playable_mobs:
        V.player.race = sel
    if sel == "0":
        V.state = "select_sex"

def select_sex():
    T.clear_text()
    T.print("(m) Male\n(f) Female", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "m" or sel == "f":
        V.player.sex = sel
        V.state = "new_game"

def select_job():
    T.clear_text()
    for j in jobs:
        can_job = True
        if 'require' in jobs[j]:
            for r in jobs[j]['require']:
                if r in V.player.jobs:
                    if V.player.jobs[r] < jobs[j]['require'][r]:
                        can_job = False
                else:
                    can_job = False
        if can_job:
            T.print("({})".format(j), "\n", V.c_text2)
    T.print("(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel in jobs:
        V.player.job = sel
        if V.player.job in V.player.jobs:
            V.player.jobs[sel] += 1
            V.player.job_points -= 1
        else:
            V.player.jobs[sel] = 1
            V.player.job_points -= 1
        
    if sel == "0" and V.player.job != "":
        V.state = "level_up"

def level_up():
    T.clear_text()
    count = 1
    p_txt = ""
    if V.player.points > 0:
        p_txt = "(1) Points\n"
    s_txt = ""
    if V.player.skill_points > 0:
        s_txt = "(2) Skills\n"
    j_txt = ""
    if V.player.job_points > 0:
        j_txt = "(3) Job\n"
    T.print("{}{}{}(0) Done".format(p_txt,s_txt,j_txt), "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0" and V.player.job_points <= 0: V.state = "main_menu"
    if sel == "1" and V.player.points > 0: V.entity_stats(V.player, "level_up")
    if sel == "2" and V.player.skill_points > 0: V.entity_skills(V.player, "level_up")
    if sel == "3" and V.player.job_points > 0: select_job()
