items = {}
crafting = {}
magic = {}
jobs = {}
mobs = {}
names = {}
world = {}
quest = {}
playable_mobs = []

import json
from os import path
#global items, crafting, magic, mobs, jobs, names, world, quest, playable_mobs
quest_list = []
with open(path.join(path.join(path.dirname(__file__), "data/quest"), "QuestList.json"),"r") as f:
    qd = json.loads(f.read().strip())
    for q in qd:
        if qd[q]: quest_list.append(q)
for q in quest_list:
    data_file = "{}.json".format(q)
    data_path = path.join(path.join(path.dirname(__file__), "data/quest"), data_file)
    try:
        with open(data_path,"r") as f:
            q_data = json.loads(f.read().strip())
            quest[q] = q_data
    except FileNotFoundError:
        T.text("Quest File at path '{}' Not Found".format(data_path))
with open(path.join(path.join(path.dirname(__file__), "data/game_data"), "item.json"),"r") as f:
    items = json.loads(f.read().strip())
with open(path.join(path.join(path.dirname(__file__), "data/game_data"), "craft.json"),"r") as f:
    crafting = json.loads(f.read().strip())
with open(path.join(path.join(path.dirname(__file__), "data/game_data"), "magic.json"),"r") as f:
    magic = json.loads(f.read().strip())
with open(path.join(path.join(path.dirname(__file__), "data/game_data"), "mob.json"),"r") as f:
    mobs = json.loads(f.read().strip())
with open(path.join(path.join(path.dirname(__file__), "data/game_data"), "job.json"),"r") as f:
    jobs = json.loads(f.read().strip())
with open(path.join(path.join(path.dirname(__file__), "data/game_data"), "names.json"),"r") as f:
    names = json.loads(f.read().strip())
with open(path.join(path.join(path.dirname(__file__), "data/game_data"), "world.json"),"r") as f:
    world = json.loads(f.read().strip())
playable_mobs = mobs['playable_mobs']
