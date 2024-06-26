items = {}
crafting = {}
magic = {}
jobs = {}
mobs = {}
names = {}
world = {}
quest = {}
playable_mobs = []
selectable_jobs = []
quest_list = []
phrases = {
       "shop_buy" : [
           "Take a look at my wares.",
           "I'll show you what I have in stock.",
           "Here's what I have for sale.",
           "I hope you are pleased with my selection.",
           "Here's what I have in stock.",
           "Have a look at my inventory.",
           "Take a gander at my selection.",
           "Let me show you what I have in store.",
           "Let me show you what I have in stock.",
           ],
       "shop_sell" : [
           "Let's see what you have.",
           "Show me what you have.",
           "What are you offering?",
           "what are you trying to sell?",
           "Show me what you have to sell.",
           "Let me take a look at your inventory.",
           "What goods do you have for sale?",
           "Let me see what you have.",
           "Let me see what you've got.",
           ],
}
startup_anim = [
"""
###
## #
###
##
##
""",
"""
###   ## #
## #  ## #
###    ##
##     ##
##     ##
""",
"""
###   ## #  ####
## #  ## #   ##
###    ##    ##
##     ##    ##
##     ##    ##
""",
"""
###   ## #  ####  ## #
## #  ## #   ##   ## #
###    ##    ##   ####
##     ##    ##   ## #
##     ##    ##   ## #
""",
"""
###   ## #  ####  ## #   ##
## #  ## #   ##   ## #  ## #
###    ##    ##   ####  ## #
##     ##    ##   ## #  ## #
##     ##    ##   ## #   ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####
       ##
       ##
       ##
       ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####
       ##   ##
       ##   ###
       ##   ##
       ##   ####
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##
       ##   ##    ## ##
       ##   ###     #
       ##   ##    ## ##
       ##   ####  ## ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###
   ## #
   ###
   ## #
   ## #
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###
   ## #  ## #
   ###   ###
   ## #  ##
   ## #  ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##
   ## #  ## #  ##
   ###   ###   ## ##
   ## #  ##    ## #
   ## #  ##      ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##
   ## #  ## #  ##     ##
   ###   ###   ## ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##
   ## #  ## #  ##     ##  ##
   ###   ###   ## ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           b
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by i
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ih
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by iha
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihav
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave1
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13d
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13di
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13dig
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13digi
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13digit
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13digits
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13digits
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13digits
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13digits
""",
"""
###   ## #  ####  ## #   ##   ### #
## #  ## #   ##   ## #  ## #  ### #
###    ##    ##   ####  ## #  #####
##     ##    ##   ## #  ## #  ## ##
##     ##    ##   ## #   ##   ## ##

      ####  ####  ## ##  ####
       ##   ##    ## ##   ##
       ##   ###     #     ##
       ##   ##    ## ##   ##
       ##   ####  ## ##   ##

   ###   ###     ##   ##  ##  ##
   ## #  ## #  ##     ##  ##  ##
   ###   ###   ## ##  ##  ##  ##
   ## #  ##    ## #
   ## #  ##      ##   ##  ##  ##
           by ihave13digits
""",
]

import json
from os import path

def read_game_data(_file):
    with open(path.join(path.join(path.dirname(__file__), "data/game_data"), "{}.json".format(_file)),"r") as f:
        return json.loads(f.read().strip())

items = read_game_data("item")
crafting = read_game_data("craft")
magic = read_game_data("magic")
mobs = read_game_data("mob")
jobs = read_game_data("job")
names = read_game_data("names")
world = read_game_data("world")
playable_mobs = mobs['playable_mobs']

for i in jobs['selectable_jobs']:
    selectable_jobs.append(i)
jobs.pop('selectable_jobs')
