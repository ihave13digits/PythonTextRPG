# GnarledPass     Elder'sPeak     NorthKingdom    Teaksborough


# Glutton'sBay    Baggerton       Brisby          Albak


# Port Grace      Fairlanding     RuinedForest    Rolnhelm


# Cold Flats      Ditherton       Smeade          Osgard

world = {
        'North Kingdom' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'', 'south':'Brisby', 'east':'Teaksborough', 'west':"Elder's Peak"}
            },
        'Brisby' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'North Kingdom', 'south':'Ruined Forest', 'east':'Albak', 'west':'Baggerton'}
            },
        'Teaksborough' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'south':'Albak', 'west':'North Kingdom'}
            },
        "Elder's Peak" : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'south':'Baggerton', 'east':'North Kingdom', 'west':'Gnarled Pass'}
            },
        'Gnarled Pass' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'south':"Glutton's Bay", 'east':"Elder's Peak"}
            },
        "Glutton's Bay" : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'Gnarled Pass', 'south':'Port Grace', 'east':'Baggerton'}
            },
        'Baggerton' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':"Elder's Peak", 'south':'Fairlanding', 'east':'Brisby', 'west':"Glutton's Bay"}
            },
        'Port Grace' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':"Glutton's Bay", 'south':'Cold Flats', 'east':'Fairlanding'}
            },
        'Fairlanding' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'Baggerton', 'south':'Ditherton', 'east':'Ruined Forest', 'west':'Port Grace'}
            },
        'Cold Flats' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'Port Grace', 'east':'Ditherton'}
            },
        'Ruined Forest' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'Brisby', 'south':'Smeade', 'east':'Rolnhelm', 'west':'Fairlanding'}
            },
        'Albak' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'Teaksborough', 'south':'Rolnhelm', 'west':'Brisby'}
            },
        'Ditherton' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'Fairlanding', 'east':'Smeade', 'west':'Cold Flats'}
            },
        'Smeade' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'Ruined Forest', 'east':'Osgard', 'west':'Ditherton'}
            },
        'Rolnhelm' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'Albak', 'south':'Osgard', 'west':'Ruined Forest'}
            },
        'Osgard' : {
            'shop' : {'gold' : 1000, 'markup' : 1.0},
            'travel' : {'north':'Rolnhelm', 'west':'Smeade'}
            },
    }
