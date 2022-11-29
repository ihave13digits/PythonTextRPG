# GnarledPass     Elder'sPeak     NorthKingdom    Teaksborough


# Glutton'sBay    Baggerton       Brisby          Albak


# Port Grace      Fairlanding     RuinedForest    Rolnhelm


# Cold Flats      Ditherton       Smeade          Osgard

world = {
        'North Kingdom' : {
            'mobs' : ['human','gnome','gnome','elf','elf','elf'],
            'restock' : 20, 'shop' : {'gold' : 10000, 'markup' : 2.0, 'inventory' : {}},
            'travel' : {'north':'', 'south':'Brisby', 'east':'Teaksborough', 'west':"Elder's Peak"}
            },
        'Brisby' : {
            'mobs' : ['human','gnome','gnome','elf','elf','elf'],
            'restock' : 15, 'shop' : {'gold' : 5000, 'markup' : 1.5, 'inventory' : {}},
            'travel' : {'north':'North Kingdom', 'south':'Ruined Forest', 'east':'Albak', 'west':'Baggerton'}
            },
        'Teaksborough' : {
            'mobs' : ['human','gnome','gnome','elf','elf','elf'],
            'restock' : 15, 'shop' : {'gold' : 5000, 'markup' : 1.5, 'inventory' : {}},
            'travel' : {'south':'Albak', 'west':'North Kingdom'}
            },
        "Elder's Peak" : {
            'mobs' : ['human','human','gnome','dwarf','dwarf','giant'],
            'restock' : 15, 'shop' : {'gold' : 5000, 'markup' : 1.5, 'inventory' : {}},
            'travel' : {'south':'Baggerton', 'east':'North Kingdom', 'west':'Gnarled Pass'}
            },
        'Gnarled Pass' : {
            'mobs' : ['dwarf','dwarf','dwarf','dwarf','giant','giant'],
            'restock' : 10, 'shop' : {'gold' : 1000, 'markup' : 1.0, 'inventory' : {}},
            'travel' : {'south':"Glutton's Bay", 'east':"Elder's Peak"}
            },
        "Glutton's Bay" : {
            'mobs' : ['human','dwarf','gnome','orc','elf','giant'],
            'restock' : 10, 'shop' : {'gold' : 1000, 'markup' : 1.0, 'inventory' : {}},
            'travel' : {'north':'Gnarled Pass', 'south':'Port Grace', 'east':'Baggerton'}
            },
        'Baggerton' : {
            'mobs' : ['human','human','gnome','orc','elf'],
            'restock' : 7, 'shop' : {'gold' : 750, 'markup' : 0.75, 'inventory' : {}},
            'travel' : {'north':"Elder's Peak", 'south':'Fairlanding', 'east':'Brisby', 'west':"Glutton's Bay"}
            },
        'Port Grace' : {
            'mobs' : ['human','gnome','gnome','elf'],
            'restock' : 7, 'shop' : {'gold' : 750, 'markup' : 0.75, 'inventory' : {}},
            'travel' : {'north':"Glutton's Bay", 'south':'Cold Flats', 'east':'Fairlanding'}
            },
        'Fairlanding' : {
            'mobs' : ['human','human','human','gnome','elf'],
            'restock' : 5, 'shop' : {'gold' : 500, 'markup' : 0.5, 'inventory' : {}},
            'travel' : {'north':'Baggerton', 'south':'Ditherton', 'east':'Ruined Forest', 'west':'Port Grace'}
            },
        'Cold Flats' : {
            'mobs' : ['goblin','ogre','ogre','orc','orc','orc'],
            'restock' : 10, 'shop' : {'gold' : 1000, 'markup' : 1.0, 'inventory' : {}},
            'travel' : {'north':'Port Grace', 'east':'Ditherton'}
            },
        'Ruined Forest' : {
            'mobs' : ['human','orc','orc','elf','elf'],
            'restock' : 10, 'shop' : {'gold' : 1000, 'markup' : 1.0, 'inventory' : {}},
            'travel' : {'north':'Brisby', 'south':'Smeade', 'east':'Rolnhelm', 'west':'Fairlanding'}
            },
        'Albak' : {
            'mobs' : ['human','human','human','orc','goblin','goblin'],
            'restock' : 12, 'shop' : {'gold' : 2500, 'markup' : 1.25, 'inventory' : {}},
            'travel' : {'north':'Teaksborough', 'south':'Rolnhelm', 'west':'Brisby'}
            },
        'Ditherton' : {
            'mobs' : ['human','gnome','gnome','gnome','elf'],
            'restock' : 7, 'shop' : {'gold' : 750, 'markup' : 0.75, 'inventory' : {}},
            'travel' : {'north':'Fairlanding', 'east':'Smeade', 'west':'Cold Flats'}
            },
        'Smeade' : {
            'mobs' : ['human','orc','goblin','elf'],
            'restock' : 10, 'shop' : {'gold' : 1000, 'markup' : 1.0, 'inventory' : {}},
            'travel' : {'north':'Ruined Forest', 'east':'Osgard', 'west':'Ditherton'}
            },
        'Rolnhelm' : {
            'mobs' : ['human'],
            'restock' : 15, 'shop' : {'gold' : 5000, 'markup' : 1.5, 'inventory' : {}},
            'travel' : {'north':'Albak', 'south':'Osgard', 'west':'Ruined Forest'}
            },
        'Osgard' : {
            'mobs' : ['ogre','goblin','goblin','orc','orc','orc'],
            'restock' : 12, 'shop' : {'gold' : 2500, 'markup' : 1.25, 'inventory' : {}},
            'travel' : {'north':'Rolnhelm', 'west':'Smeade'}
            },
    }
