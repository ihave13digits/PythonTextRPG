magic = {
        ### Offensive
        # Grade 3
        "firestorm"         : {"burned" : True, "damage" : 100, "cost" : 25},
        "lightning barrage" : {"stunned" : True, "damage" : 100, "cost" : 25},
        "tsunami"           : {"confused" : True, "damage" : 100, "cost" : 25},
        "earthquake"        : {"stunned" : True, "damage" : 100, "cost" : 25},
        "destroy"           : {"confused" : True, "damage" : 100, "cost" : 25},
        #Grade 2
        "fire blast"        : {"damage" : 50, "cost" : 10},
        "lightning"         : {"damage" : 50, "cost" : 10},
        "flash flood"       : {"damage" : 50, "cost" : 10},
        "fissure"           : {"damage" : 50, "cost" : 10},
        "kill"              : {"damage" : 50, "cost" : 10},
        # Grade 1
        "fireball"          : {"damage" : 10, "cost" : 5},
        "lightning bolt"    : {"damage" : 10, "cost" : 5},
        "water burst"       : {"damage" : 10, "cost" : 5},
        "ground collapse"   : {"damage" : 10, "cost" : 5},
        "harm"              : {"damage" : 10, "cost" : 5},
        
        ### Offensive Strategy
        "burn"              : {"burned" : True, "damage" : 10, "cost" : 10},
        "electric shock"    : {"stunned" : True, "damage" : 10, "cost" : 10},
        "poison rain"       : {"poisoned" : True, "damage" : 10, "cost" : 10},
        "tremor"            : {"stunned" : True, "damage" : 10, "cost" : 10},
        "decay"             : {"confused" : True, "damage" : 10, "cost" : 10},
        
        ### Defensive
        "heal"              : {"hp" : 10, "cost" : 5},
        "heal all"          : {"hp" : 100, "cost" : 25},
        "cure"              : {"burned" : False, "stunned" : False, "confused" : False, "poisoned" : False, "cost" : 10},
        "cure all"          : {"burned" : False, "stunned" : False, "confused" : False, "poisoned" : False, "hp" : 100, "cost" : 25},
        "cure poison"       : {"poisoned" : False, "cost" : 5},
        "cure confusion"    : {"confused" : False, "cost" : 5},
        "cure stun"         : {"stunned" : False, "cost" : 5},
        "cure burn"         : {"burned" : False, "cost" : 5},
        
        ### Strategy
        "inflict poison"    : {"poisoned" : True, "cost" : 5},
        "inflict confusion" : {"confused" : True, "cost" : 5},
        "inflict stun"      : {"stunned" : True, "cost" : 5},
        "inflict burn"      : {"burned" : True, "cost" : 5},
    }
