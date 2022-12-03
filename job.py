#"barter":0, "bluff":0, "build":0, "cast":0, "climb":0, "combat":0, "craft":0, "dodge":0,
#"forage":0, "heal":0, "hide":0, "hunt":0, "persuade":0, "search":0, "sneak":0, "travel":0

jobs = {
    '' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {},
        'require' : {}},
    # Teir 1
    'fighter' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"combat":15,"dodge":10,}},
    'rogue' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"bluff":5,"dodge":5,"hide":10,"persuade":5,}},
    'hunter' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"forage":10,"hide":5,"hunt":10,}},
    # Teir 2
    'knight' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"combat":30,"dodge":20,},
        'require' : {"fighter":10}},
    'barbarian' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"climb":5,"combat":10,"dodge":10,"forage":10,"hide":5,"hunt":10,},
        'require' : {"choice":{"fighter":10, "hunter":10}}},
    'pickpocket' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"barter":10,"bluff":10,"dodge":10,"hide":10,"persuade":10,},
        'require' : {"rogue":10}},
    'cleric' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"cast":15,"combat":15,"dodge":10,"heal":10,},
        'require' : {"fighter":10}},
    'scout' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"bluff":10,"dodge":10,"hide":10,"hunt":10,"travel":10},
        'require' : {"choice":{"rogue":10, "hunter":10}}},
    'druid' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"bluff":5,"cast":15,"dodge":5,"forage":10,"hide":5,"hunt":5,"persuade":5,},
        'require' : {"rogue":10}},
    'sorcerer' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"bluff":10,"cast":10,"dodge":10,"hide":10,"persuade":10,},
        'require' : {"rogue":10}},
    # Teir 3
    'paladin' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"combat":45,"dodge":30,},
        'require' : {"knight":10, "fighter":10}},
    'ranger' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"bluff":10,"climb":10,"combat":10,"dodge":10,"forage":15,"hide":10,"hunt":10,},
        'require' : {"rogue":10, "hunter":10}},
    'theif' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"barter":10,"bluff":10,"climb":10,"combat":10,"dodge":10,"forage":5,"hide":10,"persuade":10,},
        'require' : {"pickpocket":10, "rogue":10}},
    'wizard' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"bluff":15,"cast":15,"dodge":15,"hide":15,"persuade":15,},
        'require' : {"sorcerer":10, "rogue":10}},
    # Teir 4
    'assassin' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"barter":10,"bluff":10,"climb":10,"combat":20,"dodge":10,"forage":10,"hide":10,"hunt":10,"persuade":10,},
        'require' : {"choice":{"ranger":10, "theif":10}, "rogue":10, "fighter":10}},
    'warlord' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"combat":50,"dodge":30,"persuade":20,},
        'require' : {"paladin":10, "knight":10, "fighter":10}},
    'warmage' : {
        'stat' : {"hp" : 0, "mp" : 0, "mag" : 0, "atk" : 0, "def" : 0, "cha" : 0, "point" : 0},
        'skill' : {"bluff":20,"cast":20,"dodge":20,"hide":20,"persuade":20,},
        'require' : {"choice":{"wizard":10, "sorcerer":10}, "rogue":10, "fighter":10}},
}
