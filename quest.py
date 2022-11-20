quest = {
        'intro' : {
            'discovered' : True,
            'completed' : False,
            'part' : '0',
            '0' : {'part' : '1', 'prompt' : "Stranger: Adventurer, welcome to these parts.  What's your name?"},
            '1' : {
                'part' : '2',
                'prompt' : "Stranger: A pleasure to meet you, my name is Hodan.  Just a word of advice for your stay:",
                'freetype' : {'object':'player', 'variable':'name'},
            },
            '2' : {'part' : '3', 'prompt' : "Hodan: It's a treacherous world out there, and it would be wise to equip yourself."},
            '3' : {'part' : '4', 'prompt' : "Hodan: You can find weapons and armor, among other things in the shop down the way."},
            '4' : {
                'part' : '5',
                'prompt' : "Hodan: You don't look like you have much gold on you.  I can't offer much, but I could spare a few coin for ye.",
                'option' : {
                    "1" : {'prompt' : "Yes, that would help me abundantly.  Thanks.", 'reward' : {'stat':'gold', 'value':75}},
                    "2" : {'prompt' : "No, thank you.  I think I can manage on my own.", 'reward' : {'stat':'gold', 'value':150}}
                    }
            },
            '5' : {'part' : '6', 'prompt' : "Hodan: Off ye go, I've got to get back to the wife, or I'll never hear the end of it!"},
            '6' : {'completed' : True, 'state' : 'main_menu', 'reward' : {'stat':'exp', 'value':50}},
        },
        'quest' : {
            'discovered' : False,
            'completed' : False,
            'part' : '0',
            '0' : {
                'prompt' : "",
                'option' : [],
            },
        },
    }
