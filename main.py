from os import system
from sys import stdout, platform
import time, random, textwrap

m_names = ['Aaron', 'Alexander', 'Alfred', 'Andrew', 'Antonio', 'Arnold', 'Ashton', 'Austin',
        'Barney', 'Barry', 'Ben', 'Benjamin', 'Bill', 'Billy', 'Bob', 'Bobby', 'Brandon', 'Brendon',
        'Calvin', 'Carl', 'Carlos', 'Chester', 'Chris', 'Christopher', 'Clark', 'Cletus',
        'Damian', 'Daniel', 'Dave', 'David', 'Don', 'Donald', 'Drew', 'Dustin',
        'Earl', 'Edward', 'Edwin', 'Eli', 'Elijah', 'Elliot', 'Emmett', 'Eric', 'Ernest', 'Ethan', 'Eugene', 'Evan', 'Ezekiel', 'Ezra',
        'Fabian', 'Felix', 'Fernando', 'Floyd', 'Francis', 'Francisco', 'Frank', 'Franklin', 'Freddy', 'Frederick',
        'Gabriel', 'Garrett', 'Gary', 'Gavin', 'Gene', 'George', 'Gerald', 'Gordon', 'Graham', 'Grant', 'Greg', 'Gregory', 'Gus',
        'Hal', 'Hank', 'Harold', 'Harison', 'Harry', 'Harvey', 'Henry', 'Herbert', 'Howard',
        'Ian', 'Ike', 'Immanuel', 'Isaac', 'Ivan',
        'Jake', 'James', 'Jamie', 'Jared', 'Jason', 'Javier', 'Jeremy', 'Jesse', 'Jim', 'John', 'Josh', 'Joshua', 'Justin',
        'Keith', 'Ken', 'Kenny', 'Kent', 'Kevin', 'Klaus', 'Kurt', 'Kyle',
        'Lance', 'Lawrence', 'Leonard', 'Liam', 'Logan', 'Louis', 'Lucas', 'Luke', 'Lyle',
        'Magnus', 'Marcus', 'Mark', 'Marshall', 'Martin', 'Mason', 'Matthew', 'Michael', 'Mike', 'Murphey',
        'Nathan', 'Ned', 'Nick', 'Nicolas', 'Nelson', 'Nigel', 'Nolan', 'Norman',
        'Oliver', 'Omar', 'Oscar', 'Oswald', 'Owen',
        'Patrick', 'Paul', 'Pete', 'Peter', 'Phillip',
        'Quentin', 'Quinton', 'Quincy', 'Quinn',
        'Randal', 'Randy', 'Richard', 'Robby', 'Robert', 'Rufus',
        'Sean', 'Shawn', 'Stan', 'Stanley', 'Steve', 'Steven',
        'Ted', 'Terry', 'Theo', 'Theodore', 'Timmy', 'Timothy', 'Tobias', 'Tyler',
        'Ulfric', 'Ulric',
        'Vance', 'Vincent',
        'Waldo', 'Will', 'William', 'Willy',
        'Xavier',
        'Yorick',
        'Zander'
        ]

f_names = ['Abby', 'Abegail', 'Addison', 'Alice', 'Allison', 'Allie', 'Amanda', 'Amy', 'Anna', 'Anne', 'Annette', 'Arlene', 'Aubrey', 'Audrey',
        'Barbara', 'Beckie', 'Beth', 'Bethany', 'Brandy', 'Briana',
        'Caitlin', 'Caitlyn', 'Carissa', 'Carol', 'Catherine', 'Cathy', 'Catie', 'Celine', 'Clair',
        'Dahlia', 'Daisy', 'Danielle', 'Daphne', 'Darla', 'Dawn', 'Deborah', 'Delilah', 'Denise', 'Diana', 'Donna', 'Dorothy',
        'Eleanor', 'Elena', 'Elizabeth', 'Ellen', 'Emma', 'Emilie', 'Emily', 'Erica', 'Esther', 'Eve', 'Evelyn',
        'Fae', 'Faith', 'Farrah', 'Faye', 'Felicity', 'Fiona', 'Frances', 'Francine', 'Freda',
        'Gabby', 'Gabriella', 'Gene', 'Genevieve', 'Gillian', 'Giselle', 'Gladys', 'Glenda', 'Gloria', 'Grace', 'Gretchen', 'Gwen', 'Gwendolyn',
        'Hailey', 'Hannah', 'Hariette', 'Harper', 'Hazel', 'Heather', 'Helen', 'Helena', 'Hillary', 'Hope',
        'Ida', 'Irene', 'Iris', 'Isabel', 'Isabelle', 'Ivana', 'Izzy',
        'Jamie', 'Jasmine', 'Jean', 'Jeanette', 'Jenny', 'Jessie', 'Julia', 'Justine',
        'Kaitlin', 'Kaitlyn', 'Katherine', 'Katie', 'Kathy', 'Katrina', 'Kayla', 'Kelly', 'Kelsey', 'Kendra', 'Kylie',
        'Lacey', 'Laura', 'Lauren', 'Lena', 'Leslie', 'Lindsey', 'Lily', 'Lisa', 'Lori', 'Louise', 'Lucy',
        'Madison', 'Mandy', 'Mariah', 'Marie', 'Marla', 'Mary', 'Megan', 'Melanie', 'Melissa', 'Michelle', 'Mia', 'Mildred', 'Mollie', 'Molly', 'Monica', 'Morgan',
        'Nadia', 'Natalie', 'Natasha', 'Nickie', 'Nicola', 'Nicole', 'Noelle',
        'Odelia', 'Odette', 'Olive', 'Olivia', 'Oriana',
        'Paige', 'Patricia', 'Penelope', 'Phoebe',
        'Quirina',
        'Rachael', 'Rachel', 'Rebecca', 'Roxanne',
        'Samantha', 'Sandra', 'Sandy', 'Sasha', 'Shari', 'Sherry', 'Shirley', 'Sondra', 'Sue', 'Susan', 'Suzy',
        'Tabitha', 'Tamara', 'Tania', 'Tara', 'Tatiana', 'Taylor', 'Teresa', 'Tesla', 'Tiffany', 'Toni', 'Tori', 'Tracy', 'Trinity',
        'Uma', 'Ursula',
        'Vicky', 'Victoria',
        'Wanda', 'Wendy', 'Whitney', 'Willow',
        'Xandra',
        'Yildirim',
        'Zoey'
        ]

l_names = ['Adams', 'Aimes', 'Allen', 'Anderson', 'Andrews', 'Arlington',
        'Bailey', 'Baker', 'Barnes', 'Barrows', 'Beck', 'Bell', 'Bellflower', 'Bennett', 'Black', 'Bolton', 'Bowing', 'Breyers', 'Bridges', 'Brooks', 'Brown', 'Butler',
        'Campbell', 'Carey', 'Carpenter', 'Carter', 'Carrion', 'Clark', 'Clarkson', 'Cole', 'Coleman', 'Collins', 'Conners', 'Cook', 'Cooper', 'Cox', 'Cromwell',
        'Daniels', 'Davis', 'Diaz', 'Dickens', 'Downing', 'Downs', 'Duke', 'Durden',
        'Edwards', 'Einstein', 'Eldridge', 'Ellers', 'Ellington', 'Ellis', 'Evans', 'Ewig',
        'Farley', 'Feilder', 'Feilds', 'Fisher', 'Flores', 'Ford', 'Forester', 'Foster',
        'Garcia', 'Garrison', 'Gibson', 'Glass', 'Gonzalez', 'Graham', 'Gray', 'Green', 'Grey', 'Griffin',
        'Hall', 'Harris', 'Harrison', 'Harvey', 'Hayes', 'Heins', 'Henderson', 'Hendrix', 'Hernandez', 'Heston', 'Hill', 'Howard', 'Hughes',
        'Ibanez', 'Ibarria', 'Ingram', 'Irons', 'Irvin', 'Irving', 'Irwin', 'Iverson', 'Ives', 'Ivory', 'Ivey', 'Izaguire',
        'Jackson', 'Jacobs', 'James', 'Jenkins', 'Johnson', 'Jones', 'Jordan',
        'Kane', 'Kearson', 'Keith', 'Keller', 'Kelly', 'Kendall', 'Kendrick', 'Kennedy', 'King', 'Kinney', 'Kirkland', 'Koch',
        'Leach', 'Lee', 'Leech', 'Lewis', 'Linton', 'Lopez', 'Lockhart', 'Long', 'Lott', 'Lyn',
        'Marrows', 'Martin', 'Martinez', 'McCloud', 'McDonald', 'Meadows', 'Miller', 'Mills', 'Mitchell', 'Moore', 'Morgan', 'Morris', 'Muntz', 'Murphy', 'Myers',
        'Narrows', 'Navarro', 'Neighbors', 'Nelson', 'Nolan',
        'Oakley', 'Oats', "O'Brien", 'Ochoa', "O'Connor", 'Odell', 'Oliver', 'Olson', 'Ortega', 'Osborne', 'Owens',
        'Parker', 'Patterson', 'Perez', 'Perry', 'Peterson', 'Phillips', 'Poacher', 'Powwel', 'Price', 'Prince',
        'Quaid', 'Quail', 'Quarles', 'Quarters', 'Quick', 'Quigley', 'Quimby', 'Quinn',
        'Ramirez', 'Reed', 'Richards', 'Richardson', 'Rivera', 'Robbins', 'Roberts', 'Robinson', 'Rodgers', 'Rogers', 'Rodriguez', 'Rogers', 'Ross', 'Russell',
        'Sanchez', 'Sanders', 'Scott', 'Sexton', 'Simmons', 'Simpson', 'Smith', 'Stark', 'Stewert', 'Sullivan', 'Sykes',
        'Taylor', 'Teech', 'Thomas', 'Thompson', 'Timberlake', 'Torres', 'Travis', 'Turner',
        'Underbrook', 'Underhill',
        'Vanderbeek', 'Vandyke', 'Vanguard', 'Vaughan',
        'Walker', 'Wallace', 'Wallice', 'Ward', 'Warren', 'Washington', 'Waters', 'Watson', 'Weeks', 'White', 'Williams', 'Williamson', 'Wilson', 'Wood', 'Wright',
        'Xanders',
        'Yarbrough', 'Young',
        'Zimmerman', 'Zuckerburg'
        ]

mobs = {
        'dwarf'  : {"hp" : 13, "mp" : 7, "mag" : 1, "atk" : 2, "def" : 2, "exp" : 10, "lup" : 110, "point" : 2, "curve" : 1.25},
        'human'  : {"hp" : 10, "mp" : 10, "mag" : 2, "atk" : 3, "def" : 3, "exp" : 15, "lup" : 100, "point" : 3, "curve" : 1.25},
        'giant'  : {"hp" : 12, "mp" : 12, "mag" : 3, "atk" : 3, "def" : 3, "exp" : 20, "lup" : 90, "point" : 1, "curve" : 1.25},
        'gnome'  : {"hp" : 6, "mp" : 10, "mag" : 3, "atk" : 1, "def" : 1, "exp" : 10, "lup" : 80, "point" : 2, "curve" : 1.2},
        'elf'    : {"hp" : 8, "mp" : 12, "mag" : 3, "atk" : 3, "def" : 2, "exp" : 15, "lup" : 100, "point" : 3, "curve" : 1.2},
        'troll'  : {"hp" : 12, "mp" : 12, "mag" : 2, "atk" : 3, "def" : 4, "exp" : 20, "lup" : 120, "point" : 1, "curve" : 1.2},
        'goblin' : {"hp" : 12, "mp" : 8, "mag" : 2, "atk" : 2, "def" : 1, "exp" : 10, "lup" : 40, "point" : 1, "curve" : 1.3},
        'orc'    : {"hp" : 12, "mp" : 8, "mag" : 1, "atk" : 4, "def" : 3, "exp" : 15, "lup" : 60, "point" : 2, "curve" : 1.3},
        'ogre'   : {"hp" : 12, "mp" : 8, "mag" : 1, "atk" : 4, "def" : 4, "exp" : 20, "lup" : 80, "point" : 3, "curve" : 1.3},
    }

magic = {
        "fireball"        : {"damage" : 10, "cost" : 5, "value" : 500, "rarity" : 5, "count" : 2},
        "lightning bolt"  : {"damage" : 10, "cost" : 5, "value" : 500, "rarity" : 5, "count" : 2},
        "flash flood"     : {"damage" : 10, "cost" : 5, "value" : 500, "rarity" : 5, "count" : 2},
        "ground collapse" : {"damage" : 10, "cost" : 5, "value" : 500, "rarity" : 5, "count" : 2},
        "harm"            : {"damage" : 10, "cost" : 5, "value" : 500, "rarity" : 5, "count" : 2},
        "heal"            : {"hp" : 10, "cost" : 5, "value" : 500, "rarity" : 5, "count" : 2},
    }

items = {
        ## None
        'nothing'                   : {"type" : "", "attack" : 0, "defense" : 0, "value" : 0, "rarity" : 0, "count" : 0},
        
        ## Consumable

        # Food
        'porridge'                  : {"type" : "food", "hp" : 5, "mp" : 5, "value" : 25, "rarity" : 150, "count" : 2},
        'haggis'                    : {"type" : "food", "hp" : 15, "mp" : 15, "value" : 50, "rarity" : 50, "count" : 5},
        'bread'                     : {"type" : "food", "hp" : 5, "mp" : 5, "value" : 25, "rarity" : 150, "count" : 2},
		'kebab'                     : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 50, "rarity" : 50, "count" : 5},
        'steak'                     : {"type" : "food", "hp" : 15, "mp" : 15, "value" : 50, "rarity" : 50, "count" : 5},
        'soup'                      : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 25, "rarity" : 100, "count" : 4},
        'stew'                      : {"type" : "food", "hp" : 10, "mp" : 10, "value" : 25, "rarity" : 100, "count" : 4},

        # Potion
        'health potion'             : {"type" : "potion", "hp" : 25, "value" : 100, "rarity" : 250, "count" : 10},
        'mana potion'               : {"type" : "potion", "mp" : 25, "value" : 100, "rarity" : 200, "count" : 10},
        'elixer'                    : {"type" : "potion", "hp" : 25, "mp" : 25, "value" : 250, "rarity" : 100, "count" : 5},
        'restoration potion'        : {"type" : "potion", "hp" : 10000000, "mp" : 10000000, "value" : 1000, "rarity" : 50, "count" : 2},
        'potion of blessings'       : {"type" : "potion", "mag" : 1, "atk" : 1, "def" : 1, "value" : 50000, "rarity" : 1, "count" : 2},
        'potion of magic'           : {"type" : "potion", "mag" : 1, "value" : 25000, "rarity" : 2, "count" : 2},
        'potion of attack'          : {"type" : "potion", "atk" : 1, "value" : 25000, "rarity" : 2, "count" : 2},
        'potion of defense'         : {"type" : "potion", "def" : 1, "value" : 25000, "rarity" : 2, "count" : 2},
        'potion of health'          : {"type" : "potion", "HP" : 1, "value" : 25000, "rarity" : 5, "count" : 2},
        'potion of mana'            : {"type" : "potion", "MP" : 1, "value" : 25000, "rarity" : 5, "count" : 2},

        # Scroll
        'scroll of fireball'        : {"type" : "scroll", "spell" : "fireball", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of lightning bolt'  : {"type" : "scroll", "spell" : "lightning bolt", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of flash flood'     : {"type" : "scroll", "spell" : "flash flood", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of ground collapse' : {"type" : "scroll", "spell" : "ground collapse", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of harm'            : {"type" : "scroll", "spell" : "harm", "value" : 5000, "rarity" : 2, "count" : 2},
        'scroll of heal'            : {"type" : "scroll", "spell" : "heal", "value" : 5000, "rarity" : 2, "count" : 2},

        ## Arms
        
        # Weapon
        'club'                      : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 50, "rarity" : 250, "count" : 2, "slot" : "hand_"},
        'mace'                      : {"type" : "arms", "attack" : 3, "defense" : 0, "value" : 250, "rarity" : 150, "count" : 2, "slot" : "hand_"},
        'greatmace'                 : {"type" : "arms", "attack" : 5, "defense" : 1, "value" : 1000, "rarity" : 50, "count" : 2, "slot" : "hand_"},
        'war axe'                   : {"type" : "arms", "attack" : 4, "defense" : 2, "value" : 1000, "rarity" : 100, "count" : 2, "slot" : "hand_"},
        'dagger'                    : {"type" : "arms", "attack" : 1, "defense" : 0, "value" : 250, "rarity" : 250, "count" : 2, "slot" : "hand_"},
        'shortsword'                : {"type" : "arms", "attack" : 2, "defense" : 1, "value" : 500, "rarity" : 150, "count" : 2, "slot" : "hand_"},
        'longsword'                 : {"type" : "arms", "attack" : 3, "defense" : 1, "value" : 750, "rarity" : 100, "count" : 2, "slot" : "hand_"},
        'greatsword'                : {"type" : "arms", "attack" : 4, "defense" : 2, "value" : 1000, "rarity" : 50, "count" : 2, "slot" : "hand_"},
        # Shield
        'buckler'                   : {"type" : "arms", "attack" : 1, "defense" : 2, "value" : 50, "rarity" : 100, "count" : 2, "slot" : "hand_"},
        'shield'                    : {"type" : "arms", "attack" : 1, "defense" : 3, "value" : 100, "rarity" : 50, "count" : 2, "slot" : "hand_"},
        'tower shield'              : {"type" : "arms", "attack" : 1, "defense" : 5, "value" : 250, "rarity" : 25, "count" : 2, "slot" : "hand_"},
        
        ## Armor
        
        # Head
        'coif'                      : {"type" : "armor", "attack" : 0, "defense" : 3, "value" : 250, "rarity" : 15, "count" : 2, "slot" : "head"},
        'greathelm'                 : {"type" : "armor", "attack" : 0, "defense" : 5, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "head"},
        # Neck
        'cloak'                     : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 100, "rarity" : 25, "count" : 3, "slot" : "neck"},
        'gorget'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 3, "slot" : "neck"},
        'necklace'                  : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 500, "rarity" : 5, "count" : 2, "slot" : "neck"},
        'magic necklace'            : {"type" : "armor", "magic" : 1, "attack" : 0, "defense" : 0, "value" : 2500, "rarity" : 2, "count" : 2, "slot" : "neck"},
        'blessed necklace'          : {"type" : "armor", "magic" : 1, "attack" : 1, "defense" : 1, "value" : 2500, "rarity" : 1, "count" : 2, "slot" : "neck"},
        # Shoulders
        'pauldrons'                 : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 100, "rarity" : 25, "count" : 3, "slot" : "shoulders"},
        # Torso
        'shirt'                     : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 25, "rarity" : 75, "count" : 2, "slot" : "torso"},
        'ringmail'                  : {"type" : "armor", "attack" : 0, "defense" : 6, "value" : 500, "rarity" : 15, "count" : 2, "slot" : "torso"},
        'hauberk'                   : {"type" : "armor", "attack" : 0, "defense" : 8, "value" : 750, "rarity" : 10, "count" : 2, "slot" : "torso"},
        'breastplate'               : {"type" : "armor", "attack" : 0, "defense" : 10, "value" : 1000, "rarity" : 5, "count" : 2, "slot" : "torso"},
        # Waist
        'belt'                      : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 50, "rarity" : 100, "count" : 2, "slot" : "waist"},
        'chainskirt'                : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 50, "count" : 2, "slot" : "waist"},
        'tassets'                   : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 50, "count" : 2, "slot" : "waist"},
        'fauld'                     : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "waist"},
        'chainskirt'                : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 50, "count" : 2, "slot" : "waist"},
        # Arms
        'bracers'                   : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "arms"},
        'vambrace'                  : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "arms"},
        'rerebrace'                 : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "arms"},
        'full cannon'               : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 250, "rarity" : 25, "count" : 2, "slot" : "arms"},
        # Legs
        'pants'                     : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 50, "rarity" : 50, "count" : 2, "slot" : "legs"},
        'cuisse'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "legs"},
        'poleyn'                    : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 100, "rarity" : 25, "count" : 2, "slot" : "legs"},
        'chausses'                  : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 300, "rarity" : 25, "count" : 2, "slot" : "legs"},
        # Hands
        'gloves'                    : {"type" : "armor", "attack" : 0, "defense" : 0, "value" : 150, "rarity" : 20, "count" : 2, "slot" : "hands"},
        'chain gloves'              : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 150, "rarity" : 20, "count" : 2, "slot" : "hands"},
        'gauntlets'                 : {"type" : "armor", "attack" : 1, "defense" : 2, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "hands"},
        # Feet
        'boots'                     : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 150, "rarity" : 25, "count" : 2, "slot" : "feet"},
        'chain boots'               : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
        'sabatons'                  : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
        'greaves'                   : {"type" : "armor", "attack" : 0, "defense" : 1, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
        'full greaves'              : {"type" : "armor", "attack" : 0, "defense" : 2, "value" : 250, "rarity" : 10, "count" : 2, "slot" : "feet"},
    }

crafting = {
		# Armor
        'full cannon'  : {'take':{'vambrace':1, 'rerebrace':1, 'bracers':1}, 'give':{'full cannon':1}},
        'chausses'     : {'take':{'cuisse':1, 'poleyn':1}, 'give':{'chausses':1}},
		'full greaves' : {'take':{'sabatons':1, 'greaves':1}, 'give':{'full greaves':1}},
    }

# GnarledPass     Elder'sPeak     NorthKingdom    Teaksborough


# Glutton'sBay    Baggerton       Brisby          Albak


# Port Grace      Fairlanding     RuinedForest    Rolnhelm


# Cold Flats      Ditherton       Smeade          Osgard

world = {
        'North Kingdom' : {
            'shop' : {},
            'travel' : {'north':'', 'south':'Brisby', 'east':'Teaksborough', 'west':"Elder's Peak"}
            },
        'Brisby' : {
            'shop' : {},
            'travel' : {'north':'North Kingdom', 'south':'Ruined Forest', 'east':'Albak', 'west':'Baggerton'}
            },
        'Teaksborough' : {
            'shop' : {},
            'travel' : {'south':'Albak', 'west':'North Kingdom'}
            },
        "Elder's Peak" : {
            'shop' : {},
            'travel' : {'south':'Baggerton', 'east':'North Kingdom', 'west':'Gnarled Pass'}
            },
        'Gnarled Pass' : {
            'shop' : {},
            'travel' : {'south':"Glutton's Bay", 'east':"Elder's Peak"}
            },
        "Glutton's Bay" : {
            'shop' : {},
            'travel' : {'north':'Gnarled Pass', 'south':'Port Grace', 'east':'Baggerton'}
            },
        'Baggerton' : {
            'shop' : {},
            'travel' : {'north':"Elder's Peak", 'south':'Fairlanding', 'east':'Brisby', 'west':"Glutton's Bay"}
            },
        'Port Grace' : {
            'shop' : {},
            'travel' : {'north':"Glutton's Bay", 'south':'Cold Flats', 'east':'Fairlanding'}
            },
        'Fairlanding' : {
            'shop' : {},
            'travel' : {'north':'Baggerton', 'south':'Ditherton', 'east':'Ruined Forest', 'west':'Port Grace'}
            },
        'Cold Flats' : {
            'shop' : {},
            'travel' : {'north':'Port Grace', 'east':'Ditherton'}
            },
        'Ruined Forest' : {
            'shop' : {},
            'travel' : {'north':'Brisby', 'south':'Smeade', 'east':'Rolnhelm', 'west':'Fairlanding'}
            },
        'Albak' : {
            'shop' : {},
            'travel' : {'north':'Teaksborough', 'south':'Rolnhelm', 'west':'Brisby'}
            },
        'Ditherton' : {
            'shop' : {},
            'travel' : {'north':'Fairlanding', 'east':'Smeade', 'west':'Cold Flats'}
            },
        'Smeade' : {
            'shop' : {},
            'travel' : {'north':'Ruined Forest', 'east':'Osgard', 'west':'Ditherton'}
            },
        'Rolnhelm' : {
            'shop' : {},
            'travel' : {'north':'Albak', 'south':'Osgard', 'west':'Ruined Forest'}
            },
        'Osgard' : {
            'shop' : {},
            'travel' : {'north':'Rolnhelm', 'west':'Smeade'}
            },
    }

"""
    self.text("Stranger: Adventurer, welcome to these parts.  What's your name?")
    self.player.name = input(": ")
    self.text("Stranger: A pleasure to meet you, my name is Hodan.  Just a word of advice for your stay:")
    self.text("Hodan: It's a treacherous world out there, and it would be wise to equip yourself.")
    self.text("Hodan: You can find weapons and armor, among other things in the shop down the way.")
    self.text("Hodan: You don't look like you have much gold on you.  I can't offer much, but I could spare a few coin for ye.")
    print("(1) Yes, that would help me abundantly.  Thanks.")
    print("(2) No, thank you.  I think I can manage on my own.")
    sel = input(": ")
    if sel == "2":
        self.text("Hodan: Nonsense, you don't even have a blade on ye.  Take this, it's no trouble, plus, maybe we will cross paths again when I'm the one in need.")
        self.player.gold = int(self.player.gold+150)
    else:
        self.text("Hodan: Here ye are, every bit helps.  Perhaps we will cross paths again, and ye can help out if I'm the one in need.")
        self.player.gold = int(self.player.gold+75)
    self.text("Hodan: Off ye go, I've got to get back to the wife, or I'll never hear the end of it!")
"""

quest = {
        'intro' : {
            'part' : '0',
            '0' : {'part' : '1', 'prompt' : "Stranger: Adventurer, welcome to these parts.  What's your name?"},
            '1' : {'part' : '2', 'prompt' : "Stranger: A pleasure to meet you, my name is Hodan.  Just a word of advice for your stay:"},
            '2' : {'part' : '3', 'prompt' : "Hodan: It's a treacherous world out there, and it would be wise to equip yourself."},
            '3' : {'part' : '4', 'prompt' : "Hodan: You can find weapons and armor, among other things in the shop down the way."},
            '4' : {
                'part' : '5',
                'prompt' : "Hodan: You don't look like you have much gold on you.  I can't offer much, but I could spare a few coin for ye.",
                'option' : {
                    "(1) Yes, that would help me abundantly.  Thanks.",
                    "(2) No, thank you.  I think I can manage on my own."
                    }
            },
            '5' : {'part' : '6', 'prompt' : "Hodan: Off ye go, I've got to get back to the wife, or I'll never hear the end of it!"},
            '6' : {'state' : 'main_menu'},
        },
        'quest' : {
            'part' : 0,
            '0' : {
                'prompt' : "",
                'option' : [],
            },
        },
    }

class Shop():

    def __init__(self, GOLD=1000, MARKUP=1.0, STOCK=10):
        self.gold = GOLD
        self.markup = MARKUP
        self.inventory = {}
        for i in range(STOCK):
            self.restock()

    def get_data(self):
        return {
                "gold" : self.gold,
                "markup" : self.markup,
                "inventory" : self.inventory,
            }

    def set_data(self, data):
        self.gold = data['gold']
        self.markup = data['markup']
        self.inventory = data['inventory']

    def add_item(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def del_item(self, item):
        if item in self.inventory:
            if self.inventory[item] > 1:
                self.inventory[item] -= 1
            else:
                self.inventory.pop(item, None)

    def restock(self):
        for i in items:
            if i != "nothing":
                if random.randint(0, 1000) < items[i]['rarity']:
                    self.inventory[i] = random.randint(1, items[i]['count'])



class Entity():

    def __init__(self, NAME, RACE, AI=True):
        self.is_ai = AI
        self.name = NAME
        self.race = RACE
        self.job = ""
        self.level = 1
        self.points = 0
        self.exp = 0
        self.level_up = mobs[RACE]['lup']
        self.experience = 0
        
        self.hp = mobs[RACE]['hp']
        self.HP = mobs[RACE]['hp']
        self.mp = mobs[RACE]['mp']
        self.MP = mobs[RACE]['mp']
        self.magic = mobs[RACE]['mag']
        self.attack = mobs[RACE]['atk']
        self.defense = mobs[RACE]['def']

        self.gold = 100

        self.equip = {
                "hand_r" : 'nothing',
                "hand_l" : 'nothing',
                "head" : 'nothing',
                "neck" : 'nothing',
                "torso" : 'shirt',
                "waist" : 'nothing',
                "arms" : 'nothing',
                "legs" : 'pants',
                "hands" : 'nothing',
                "feet" : 'nothing',
            }
        self.spells = {}
        self.inventory = {}

    def get_data(self):
        return {
                "name" : self.name,
                "race" : self.race,
                "job" : self.job,
                "points" : self.points,
                "level" : self.level,
                "exp" : self.exp,
                "level_up" : self.level_up,
                "experience" : self.experience,
                "hp" : self.hp,
                "HP" : self.HP,
                "mp" : self.mp,
                "MP" : self.MP,
                "magic" : self.magic,
                "attack" : self.attack,
                "defense" : self.defense,
                "gold" : self.gold,
                "equip" : self.equip,
                "spells" : self.spells,
                "inventory" : self.inventory,
            }

    def set_data(self, data):
        self.name = data["name"]
        self.race = data["race"]
        self.job = data["job"]
        self.points = data["points"]
        self.level = data["level"]
        self.exp = data["exp"]
        self.level_up = data["level_up"]
        self.experience = data["experience"]
        self.hp = data["hp"]
        self.HP = data["HP"]
        self.mp = data["mp"]
        self.MP = data["MP"]
        self.magic = data["magic"]
        self.attack = data["attack"]
        self.defense = data["defense"]
        self.gold = data["gold"]
        self.equip = data["equip"]
        self.spells = data["spells"]
        self.inventory = data["inventory"]

    def get_magic_bonus(self):
        bonus = 0
        for i in self.equip:
            bonus += items[self.equip[i]].get('magic', 0)
        return bonus

    def get_attack_bonus(self):
        return items[self.equip['hand_l']]['attack']+items[self.equip['hand_r']]['attack']

    def get_defense_bonus(self):
        bonus = 0
        for i in self.equip:
            bonus += items[self.equip[i]].get('defense', 0)
        return bonus

    def get_magic_damage(self, spell):
        return magic[spell]['damage']+self.get_magic_bonus()

    def get_damage(self, hand):
        return self.attack+items[self.equip[hand]]['attack']

    def get_armor(self):
        return self.defense+self.get_defense_bonus()

    def take_damage(self, dmg):
        self.hp -= max(dmg-self.get_armor(), 0)

    def add_spell(self, spell):
        if spell in self.spells:
            self.spells[spell] += 1
        else:
            self.spells[spell] = 1

    def use_spell(self, spell, entity):
        if self.mp >= magic[spell]['cost']:
            if "hp" in magic[spell]:
                entity.hp = min(entity.hp+(magic[spell]["hp"]+self.get_magic_bonus()), entity.HP)
            if "damage" in magic[spell]:
                entity.take_damage(self.get_magic_attack(spell))
            self.mp -= magic[spell]['cost']

    def add_item(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1

    def del_item(self, item):
        if item in self.inventory:
            if self.inventory[item] > 1:
                self.inventory[item] -= 1
            else:
                self.inventory.pop(item, None)

    def equip_item(self, item, slot):
        if self.equip[slot] != "nothing":
            self.add_item(self.equip[slot])
        self.del_item(item)
        self.equip[slot] = item

    def use_item(self, item):
        can_delete = False
        if "hp" in items[item]:
            can_delete = True
            self.hp = min(self.hp+items[item]['hp'], self.HP)
        if "mp" in items[item]:
            can_delete = True
            self.mp = min(self.mp+items[item]['mp'], self.MP)
        if "HP" in items[item]:
            can_delete = True
            self.HP += items[item]['HP']
        if "MP" in items[item]:
            can_delete = True
            self.MP += items[item]['MP']
        if "mag" in items[item]:
            can_delete = True
            self.magic += items[item]['mag']
        if "atk" in items[item]:
            can_delete = True
            self.attack += items[item]['atk']
        if "def" in items[item]:
            can_delete = True
            self.defense += items[item]['def']
        if "spell" in items[item]:
            can_delete = True
            self.add_spell(items[item]['spell'])
        #if "" in items[item]:
        #    pass
        if can_delete:
            self.del_item(item)

    def can_craft_item(self, item):
        can_craft = True
        for i in crafting[item]['take']:
            if i in self.inventory:
                if self.inventory[i] < crafting[item]['take'][i]:
                    can_craft = False
            else:
                can_craft = False
        return can_craft

    def craft_item(self, item):
        if self.can_craft_item(item):
            for i in crafting[item]['take']:
                for n in range(crafting[item]['take'][i]):
                    self.del_item(i)
            for i in crafting[item]['give']:
                for n in range(crafting[item]['give'][i]):
                    self.add_item(i)

    def gain_experience(self, xp):
        self.exp = int(self.exp+xp)
        while self.exp >= self.level_up:
            self.increase_level()

    def increase_level(self):
        self.experience = int(self.experience+self.exp)
        self.exp = int(self.exp-self.level_up)
        self.level += 1
        self.level_up = int(self.level_up*mobs[self.race]['curve'])
        if self.level % mobs[self.race]['point'] == 0:
            self.points += 1
            if self.is_ai:
                self.auto_level()
            else:
                input("{} leveled up!".format(self.name))
    
    def auto_level(self):
        while self.points > 0:
            stat = random.randint(0, 4)
            if stat == 0:
                self.magic += 1
            elif stat == 1:
                self.attack += 1
            elif stat == 2:
                self.defense += 1
            elif stat == 3:
                self.HP += 1
                self.hp += 1
            elif stat == 4:
                self.MP += 1
                self.mp += 1
            else:
                self.HP += 1
                self.hp += 1
            self.points -= 1

    def auto_equip(self):
        to_equip = []
        for i in self.inventory:
            for slot in self.equip:
                if 'slot' in items[i]:
                    if items[i]['slot'] in slot:
                        to_equip.append([i, slot])
        for i in to_equip:
            self.equip_item(i[0], i[1])

    def randomize(self):
        self.hp = self.HP
        self.mp = self.MP
        self.inventory = {}
        self.gold += random.randint(0, 15)*10
        for i in items:
            if i != "nothing":
                if random.randint(0, 1500) < items[i]['rarity']:
                    M = int(items[i]['count']/2)
                    if M > 1:
                        self.inventory[i] = random.randint(1, M)
        self.auto_equip()



class Engine():

    def __init__(self):
        self.running = True
        self.ai_turn = True
        self.clear_cmd = ""
        self.data_file = "main-PythonTextRPG-ihave13digits.json"
        self.state = "intro"
        self.location = "Fairlanding"
        self.item_type = ""
        self.text_pause = 1.2
        self.text_speed = 0.06
        self.text_margin = 3
        self.menu_width = 48
        self.player = Entity("Player", "human", False)
        self.mob = Entity("human", "human")
        self.shop = Shop()

        if platform.startswith('win32'):
            self.clear_cmd = 'cls'
        else:
            self.clear_cmd = 'clear'

    ##
    ### Data
    ##

    def save_data(self):
        import json
        data = {
                "text_pause" : self.text_pause,
                "text_speed" : self.text_speed,
                "text_margin" : self.text_margin,
                "menu_width" : self.menu_width,
                "location" : self.location,
                "player" : self.player.get_data(),
                #"shop" : self.shop.get_data(),
                "world" : world,
            }
        with open(self.data_file,"w") as f:
            json.dump(data, f)
            f.close()

    def load_data(self):
        global world
        import json
        with open(self.data_file,"r") as f:
            data = json.loads(f.read())
            self.text_pause = data['text_pause']
            self.text_speed = data['text_speed']
            self.text_margin = data['text_margin']
            self.menu_width = data['menu_width']
            self.loation = data['location']
            self.player.set_data(data['player'])
            #self.shop.set_data(data['shop'])
            world = data['world']
            f.close()
        self.state = "main_menu"

    ##
    ### Engine Tools
    ##

    def get_console_size(self):
        from os import get_terminal_size
        line = str(get_terminal_size())
        x = ""
        y = ""
        z = 0
        for c in line:
            if c == " ":
                z += 1
            if c.isdigit() == True:
                if z == 0:
                    x += c
                if z == 1:
                    y += c
        return [int(x), int(y)]

    def clear_text(self):
        system(self.clear_cmd)

    def text(self, text):
        self.clear_text()
        wrapped_text = str('\n'.join(textwrap.wrap(text, self.menu_width, break_long_words=False)))
        for c in wrapped_text:
            stdout.write(c)
            stdout.flush()
            time.sleep(self.text_speed)
        if self.text_pause != -1.0:
            time.sleep(self.text_pause)
        else:
            input(": ")
        print("\n"*self.text_margin, end="")

    def randomize_mob(self):
        races = []
        for i in mobs:
            races.append(i)
        race = random.randint(0, len(races)-1)
        first_name = random.choice(m_names)
        last_name = random.choice(l_names)
        name = "{} {}".format(first_name, last_name)
        self.mob = Entity(name, races[race])
        self.mob.randomize()
        self.mob.gain_experience(random.randint(int(self.player.experience/2), int(self.player.experience)))

    def inventory_selection(self, inventory, state, gold_txt=''):
        selecting = True
        selection = "nothing"
        while selecting:
            self.clear_text()
            print("Select an item to use")
            print("Item Type: {}\n{}\n".format(self.item_type, gold_txt))
            for i in inventory:
                if items[i]['type'] == self.item_type:
                    s_value = str(items[i]['value'])
                    s_atk = ''
                    s_def = ''
                    if "attack" in items[i]:
                        s_atk = " [{}]".format(items[i]['attack'])
                    if "defense" in items[i]:
                        s_def = " [{}]".format(items[i]['defense'])
                    margin = self.menu_width - ( len(i) + len(str(inventory[i])) + len(s_value) + len(s_atk) + len(s_def))
                    print("[{}] {}{}{}{}{}".format(inventory[i], i, " "*margin, s_value, s_atk, s_def))
            print("\n(1) Food\n(2) Potion\n(3) Scroll\n(4) Arms\n(5) Armor\n(0) Back\n")
            sel = input(": ")
            if sel == "0":
                self.state = state
                selecting = False
            elif sel == "1": self.item_type = "food"
            elif sel == "2": self.item_type = "potion"
            elif sel == "3": self.item_type = "scroll"
            elif sel == "4": self.item_type = "arms"
            elif sel == "5": self.item_type = "armor"
            elif sel in inventory:
                selection = sel
                selecting = False
        return selection

    ##
    ### Game Menus
    ##

    def intro(self):
        can_continue = False
        try:
            with open(self.data_file, "r") as f:
                f.close()
            can_continue = True
        except:
            pass
        self.clear_text()
        print("(1) New Game")
        if can_continue:
            print("(2) Continue")
        print("(0) Exit")

        sel = input(": ")
        if sel == "0": self.running = False
        elif sel == "1": self.state = "new_game"
        elif sel == "2" and can_continue:
            self.load_data()

    def new_game(self):
        for l in world:
            #GOLD, MARKUP, STOCK
            S = Shop(world[l]['shop']['gold'], world[l]['shop']['markup'], world[l]['shop']['stock'])
            world[l]['shop'] = S.get_data()
        self.text("Stranger: Adventurer, welcome to these parts.  What's your name?")
        self.player.name = input(": ")
        self.text("Stranger: A pleasure to meet you, my name is Hodan.  Just a word of advice for your stay:")
        self.text("Hodan: It's a treacherous world out there, and it would be wise to equip yourself.")
        self.text("Hodan: You can find weapons and armor, among other things in the shop down the way.")
        self.text("Hodan: You don't look like you have much gold on you.  I can't offer much, but I could spare a few coin for ye.")
        print("(1) Yes, that would help me abundantly.  Thanks.")
        print("(2) No, thank you.  I think I can manage on my own.")
        sel = input(": ")
        if sel == "2":
            self.text("Hodan: Nonsense, you don't even have a blade on ye.  Take this, it's no trouble, plus, maybe we will cross paths again when I'm the one in need.")
            self.player.gold = int(self.player.gold+150)
        else:
            self.text("Hodan: Here ye are, every bit helps.  Perhaps we will cross paths again, and ye can help out if I'm the one in need.")
            self.player.gold = int(self.player.gold+75)
        self.text("Hodan: Off ye go, I've got to get back to the wife, or I'll never hear the end of it!")
        self.state = "main_menu"

    def main_menu(self):
        self.clear_text()
        print("(1) Battle\n(2) Stats\n(3) Items\n(4) Equip\n(5) Craft\n(6) Travel\n(7) Shop\n(8) Settings\n(0) Exit")
        sel = input(": ")
        if sel == "0": self.state = "exit"
        elif sel == "1":
            self.ai_turn = random.choice([True, False])
            self.randomize_mob()
            self.state = "battle"
        elif sel == "2": self.entity_stats(self.player, "main_menu")
        elif sel == "3": self.state = "item"
        elif sel == "4": self.state = "equip"
        elif sel == "5": self.state = "craft"
        elif sel == "6": self.state = "travel_menu"
        elif sel == "7": self.state = "shop_menu"
        elif sel == "8": self.state = "settings"

    def exit_menu(self):
        self.text("Are you sure you want to exit?")
        self.clear_text()
        print("(1) Exit Without Saving\n(2) Save And Exit\n(0) Cancel")
        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.running = False
        elif sel == "2":
            self.save_data()
            self.running = False

    ##
    ### Battle
    ##

    def battle_stats(self):
        entity = self.player
        self.clear_text()
        print("(1) {}".format(self.player.name))
        print("(2) {}".format(self.mob.name))
        print("(0) Back")
        select = input(": ")
        if select == "0": return
        if select == "1": entity = self.player
        if select == "2": entity = self.mob
        self.entity_stats(entity, "battle")

    def battle_attack(self):
        hand = "hand_r"
        self.clear_text()
        print("(1) Left Hand\n(2) Right Hand\n(0) Back")
        select = input(": ")
        if select == "0": return
        if select == "1": hand = "hand_l"
        if select == "2": hand = "hand_r"
        dmg = self.player.get_damage(hand)
        self.mob.take_damage(dmg)
        self.text("{} attacked {} for {} damage".format(self.player.name, self.mob.name, dmg))
        self.ai_turn = True
        self.state = "battle"

    def battle_magic(self):
        entity = self.mob
        self.clear_text()
        print("Select a target")
        print("(1) {}".format(self.mob.name))
        print("(2) {}".format(self.player.name))
        print("(0) Back")
        sel = input(": ")
        if sel == "0":
            self.state = "battle"
            return
        if sel == "1": entity = self.mob
        if sel == "2": entity = self.player
        self.clear_text()
        print("Select a spell to use")
        for i in self.player.spells:
            margin = self.menu_width - ( len(i) + len(str(self.player.spells[i])) + len(str(magic[i]['value'])) )
            print("[{}] {}{}{}".format(self.player.spells[i], i, " "*margin, magic[i]['value']))
        print("(0) Back")

        sel = input(": ")
        if sel == "0":
            self.state = "battle"
            return
        elif sel in self.player.spells:
            self.player.use_spell(sel, entity)
            self.text("{} used {} on {}".format(self.player.name, sel, entity.name))
            self.ai_turn = True
            self.state = "battle"

    def battle_item(self):
        sel = self.inventory_selection(self.player.inventory, "battle")
        if sel != "nothing":
            self.player.use_item(sel)
            self.text("{} used {}".format(self.player.name, sel))
            self.state = "battle"

    def battle_win(self):
        exp_bonus = int(mobs[self.mob.race]['exp']*(self.mob.level*mobs[self.mob.race]['curve']))
        self.player.gain_experience(exp_bonus)
        self.shop.restock()
        gold = int(self.mob.gold*0.75)
        self.player.gold = int(self.player.gold+gold)
        self.mob.gold = int(self.mob.gold-gold)
        self.text("{} won the battle, gaining {} experience and {} gold".format(self.player.name, exp_bonus, gold))
        for item in self.mob.equip:
            if self.mob.equip[item] != "nothing":
                self.mob.add_item(self.mob.equip[item])
        for item in self.mob.inventory:
            print("(1) Take {}".format(item))
            print("(0) Skip")
            sel = input(": ")
            if sel == "0": pass
            else:
                plural = ""
                if self.mob.inventory[item] > 1: plural = "s"
                for i in range(self.mob.inventory[item]):
                    self.player.add_item(item)
                self.text("{} looted {} {}{} from {}".format(self.player.name, self.mob.inventory[item], item, plural, self.mob.name))
        self.state = "main_menu"

    def battle_lose(self):
        self.shop.restock()
        gold = int(self.player.gold*0.75)
        self.player.gold = int(self.player.gold-gold)
        self.mob.gold = int(self.mob.gold+gold)
        self.player.hp = self.player.HP
        self.player.mp = self.player.MP
        self.text("{} lost the battle, losing {} gold".format(self.player.name, gold))
        self.state = "main_menu"

    def battle_ai(self):
        if self.mob.hp < self.mob.HP/2:
            for i in self.mob.inventory:
                if 'hp' in items[i] and not 'mp' in items[i]:
                    if self.mob.hp+items[i]['hp'] <= self.mob.HP:
                        self.mob.use_item(i)
                        self.text("{} used {}".format(self.mob.name, i))
        if self.mob.mp < self.mob.MP/2:
            for i in self.mob.inventory:
                if 'mp' in items[i] and not 'hp' in items[i]:
                    if self.mob.mp+items[i]['mp'] <= self.mob.MP:
                        self.mob.use_item(i)
                        self.text("{} used {}".format(self.mob.name, i))
        if self.mob.hp < self.mob.HP/2 and self.mob.mp < self.mob.MP/2:
            for i in self.mob.inventory:
                if 'hp' in items[i] and 'mp' in items[i]:
                    if self.mob.hp+items[i]['hp'] <= self.mob.HP or self.mob.mp+items[i]['mp'] <= self.mob.MP:
                        self.mob.use_item(i)
                        self.text("{} used {}".format(self.mob.name, i))
        can_cast = bool(random.randint(0, self.mob.MP) < self.mob.mp)
        if len(self.mob.spells) > 0:
            if can_cast:
                spell = "nothing"
                entity = self.mob
                for s in self.mob.spells:
                    if magic[s]['cost'] <= self.mob.mp:
                        can_cast = True
                        if 'damage' in magic[s]:
                            entity = self.player
                        if 'hp' in magic[s]:
                            entity = self.mob
                        spell = s
                if can_cast and spell != "nothing":
                    self.mob.use_spell(spell, entity)
                    self.text("{} casted {} on {}".format(self.mob.name, spell, entity.name))
                    self.ai_turn = False
        if not can_cast:
            hand = "hand_r"
            if self.mob.equip['hand_l'] != "nothing": hand = "hand_l"
            if self.mob.equip['hand_r'] != "nothing": hand = "hand_r"
            dmg = self.mob.get_damage(hand)
            self.player.take_damage(dmg)
            self.text("{} attacked {} for {} damage".format(self.mob.name, self.player.name, dmg))
            self.ai_turn = False

    def battle_player(self):
        print("(1) Attack\n(2) Stats\n(3) Magic\n(4) Item\n(0) Run")
        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.battle_attack()
        elif sel == "2": self.battle_stats()
        elif sel == "3": self.battle_magic()
        elif sel == "4": self.battle_item()

    def battle(self):
        self.clear_text()
        p_health = "HP:{}/{}".format(self.player.hp, self.player.HP)
        m_health = "HP:{}/{}".format(self.mob.hp, self.mob.HP)
        p_mana = "MP:{}/{}".format(self.player.mp, self.player.MP)
        m_mana = "MP:{}/{}".format(self.mob.mp, self.mob.MP)
        health_margin = self.menu_width-(len(self.player.name)+len(self.mob.name))
        print("{}{}{}".format(self.player.name," "*(self.menu_width-(len(self.player.name)+len(self.mob.name))),self.mob.name))
        print("{}{}{}".format(p_health," "*(self.menu_width-(len(p_health)+len(m_health))),m_health))
        print("{}{}{}".format(p_mana," "*(self.menu_width-(len(p_mana)+len(m_mana))),m_mana))
        print()
        if self.player.hp <= 0:
            self.battle_lose()
            self.randomize_mob()
            return
        if self.mob.hp <= 0:
            self.battle_win()
            self.randomize_mob()
            return
        if self.ai_turn: self.battle_ai()
        else: self.battle_player()

    ##
    ### Stats
    ##

    def entity_stats(self, entity, menu):
        self.clear_text()
        exp = "{}/{}".format(entity.exp, entity.level_up)
        ehp = "{}/{}".format(entity.hp, entity.HP)
        emp = "{}/{}".format(entity.mp, entity.MP)
        emg = "{} [{}]".format(entity.magic, entity.get_magic_bonus())
        eat = "{} [{}]".format(entity.attack, entity.get_attack_bonus())
        edf = "{} [{}]".format(entity.defense, entity.get_defense_bonus())
        print("Name:{}{}".format(" "*(self.menu_width-(len("Name:")+len(entity.name))), entity.name))
        print("Gold:{}{}".format(" "*(self.menu_width-(len("Gold:")+len(str(entity.gold)))), entity.gold))
        print("Level:{}{}".format(" "*(self.menu_width-(len("Level:")+len(str(entity.level)))), entity.level))
        print("Points:{}{}".format(" "*(self.menu_width-(len("Points:")+len(str(entity.points)))), entity.points))
        print("Experience:{}{}".format(" "*(self.menu_width-(len("Experience:")+len(exp))), exp))
        print("Health:{}{}".format(" "*(self.menu_width-(len("Health:")+len(ehp))), ehp))
        print("Mana:{}{}".format(" "*(self.menu_width-(len("Mana:")+len(emp))), emp))
        print("Magic:{}{}".format(" "*(self.menu_width-(len("Magic:")+len(emg))), emg))
        print("Attack:{}{}".format(" "*(self.menu_width-(len("Attack:")+len(eat))), eat))
        print("Defense:{}{}".format(" "*(self.menu_width-(len("Defense:")+len(edf))), edf))
        sel = input("\n: ")
        spending_points = bool(entity.points > 0)
        while spending_points > 0:
            if entity.points <= 0:
                spending_points = False
                self.state = menu
                return
            print("(1) Increase Magic\n(2) Increase Attack\n(3) Increase Defense\n(4) Increase Health\n(5) Increase Mana\n(0) Back")
            sel = input(": ")
            if sel == "0":
                spending_points = False
            elif sel == "1":
                entity.magic += 1
                entity.points -= 1
            elif sel == "2":
                entity.attack += 1
                entity.points -= 1
            elif sel == "3":
                entity.defense += 1
                entity.points -= 1
            elif sel == "4":
                entity.HP += 1
                entity.hp += 1
                entity.points -= 1
            elif sel == "5":
                entity.MP += 1
                entity.mp += 1
                entity.points -= 1
        self.state = menu

    ##
    ### Item
    ##

    def player_item(self):
        sel = self.inventory_selection(self.player.inventory, "main_menu")
        if sel != "nothing":
            self.player.use_item(sel)
            self.text("{} used {}".format(self.player.name, sel))

    def craft_item(self):
        for i in crafting:
            if self.player.can_craft_item(i):
                print("{}".format(i))
        print("(0) Back")
        sel = input(": ")
        if sel == "0":
            self.state = "main_menu"
            return
        if sel in crafting and self.player.can_craft_item(sel):
            self.player.craft_item(sel)

    ##
    ### Equip
    ##

    def equip(self):
        part = ""
        self.clear_text()
        for part in self.player.equip:
            print("{}{}({})".format(part," "*(self.menu_width-(len(part)+len(self.player.equip[part]))),self.player.equip[part]))
        print("(0) Back")
        sel = input(": ")
        if sel == "0":
            self.state = "main_menu"
            return
        if sel in self.player.equip:
            part = sel
        self.clear_text()
        for i in self.player.inventory:
            if 'slot' in items[i]:
                if items[i]['slot'] in part:
                    margin = self.menu_width - ( len(i) + len(str(self.player.inventory[i])) + len(str(items[i]['value'])) )
                    print("[{}] {}{}{}".format(self.player.inventory[i], i, " "*margin, items[i]['value']))
        print("(1) nothing")
        print("(0) Back")
        sel = input(": ")
        if sel == "0":
            self.state = "equip"
            return
        if sel == "1": sel = "nothing"
        if sel in self.player.inventory or sel == "nothing":
            if part != "":
                self.player.equip_item(sel, part)

    ##
    ### Shop
    ##

    def shop_buy(self):
        sel = self.inventory_selection(self.shop.inventory, "shop_menu", "{}'s Gold: {}".format(self.player.name, self.player.gold))
        if sel != "nothing":
            if self.player.gold >= items[sel]['value']:
                self.shop.del_item(sel)
                self.shop.gold += items[sel]['value']
                self.player.add_item(sel)
                self.player.gold -= items[sel]['value']
                self.text("{} bought {}".format(self.player.name, sel))

    def shop_sell(self):
        sel = self.inventory_selection(self.player.inventory, "shop_menu", "Shop's Gold: {}".format(self.shop.gold))
        if sel != "nothing":
            if self.shop.gold >= items[sel]['value']:
                self.player.del_item(sel)
                self.shop.add_item(sel)
                self.shop.gold -= items[sel]['value']
                self.player.gold += items[sel]['value']
                self.text("{} sold {}".format(self.player.name, sel))

    def shop_menu(self):
        self.clear_text()
        print("(1) Buy\n(2) Sell\n(0) Leave")
        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1":
            self.state = "shop_buy"
            self.text("Let me show you what I have")
        elif sel == "2":
            self.text("Let me see what you have")
            self.state = "shop_sell"

    ##
    ### Travel
    ##

    def travel_menu(self):
        self.clear_text()
        print("\n\n")
        if 'north' in world[self.location]['travel']:
            print("(8) {}".format(world[self.location]['travel']['north']))
        if 'south' in world[self.location]['travel']:
            print("(2) {}".format(world[self.location]['travel']['south']))
        if 'east' in world[self.location]['travel']:
            print("(6) {}".format(world[self.location]['travel']['east']))
        if 'west' in world[self.location]['travel']:
            print("(4) {}".format(world[self.location]['travel']['west']))
        print("(0) Back")

        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "8" and "north" in world[self.location]['travel']:
            self.state = "main_menu"
            self.location = world[self.location]['travel']['north']
        elif sel == "2" and "south" in world[self.location]['travel']:
            self.state = "main_menu"
            self.location = world[self.location]['travel']['south']
        elif sel == "6" and "east" in world[self.location]['travel']:
            self.state = "main_menu"
            self.location = world[self.location]['travel']['east']
        elif sel == "4" and "west" in world[self.location]['travel']:
            self.state = "main_menu"
            self.location = world[self.location]['travel']['west']

    ##
    ### Settings
    ##

    def set_speed(self):
        self.clear_text()
        print("(1) Fast\n(2) Normal\n(3) Slow\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            self.text_speed = 0.01
            self.text("Sample text to show timing")
        elif sel == "2":
            self.text_speed = 0.03
            self.text("Sample text to show timing")
        elif sel == "3":
            self.text_speed = 0.06
            self.text("Sample text to show timing")

    def set_pause(self):
        self.clear_text()
        print("(1) Fast\n(2) Medium\n(3) Slow\n(4) Wait\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            self.text_pause = 0.15
            self.text("Sample text to show timing")
        elif sel == "2":
            self.text_pause = 0.225
            self.text("Sample text to show timing")
        elif sel == "3":
            self.text_pause = 0.3
            self.text("Sample text to show timing")
        elif sel == "4":
            self.text_pause = -1.0

    def set_margin(self):
        self.clear_text()
        print("(1) 1\n(2) 3\n(3) 5\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            self.text_margin = 1
            self.text("Sample text to show margin")
        elif sel == "2":
            self.text_margin = 3
            self.text("Sample text to show margin")
        elif sel == "3":
            self.text_margin = 5
            self.text("Sample text to show margin")

    def set_width(self):
        self.clear_text()
        print("(1) 32\n(2) 48\n(3) 64\n(0) Back")
        sel = input(": ")
        if sel == "0": self.state = "settings"
        elif sel == "1":
            self.menu_width = 48
            self.text("Sample text to show margin")
        elif sel == "2":
            self.menu_width = 56
            self.text("Sample text to show margin")
        elif sel == "3":
            self.menu_width = 64
            self.text("Sample text to show margin")

    def set_setting(self, setting, settings):
        for s in settings:
            print("({}) {}".format(settings[s]['select'], settings[s]['prompt']))

    def settings(self):
        self.clear_text()
        print("(1) Text Speed\n(2) Text Pause\n(3) Clear Margin\n(4) Menu Width\n(0) Back")

        sel = input(": ")
        if sel == "0": self.state = "main_menu"
        elif sel == "1": self.state = "set_speed"
        elif sel == "2": self.state = "set_pause"
        elif sel == "3": self.state = "set_margin"
        elif sel == "4": self.state = "set_width"

    def update(self):
        if self.state == "battle": self.battle()
        elif self.state == "item": self.player_item()
        elif self.state == "equip": self.equip()
        elif self.state == "craft": self.craft_item()
        elif self.state == "shop_buy": self.shop_buy()
        elif self.state == "shop_sell": self.shop_sell()
        elif self.state == "shop_menu": self.shop_menu()
        elif self.state == "travel_menu": self.travel_menu()
        elif self.state == "main_menu": self.main_menu()
        elif self.state == "set_speed": self.set_speed()
        elif self.state == "set_pause": self.set_pause()
        elif self.state == "set_margin": self.set_margin()
        elif self.state == "set_width": self.set_width()
        elif self.state == "settings": self.settings()
        elif self.state == "new_game": self.new_game()
        elif self.state == "intro": self.intro()
        elif self.state == "exit": self.exit_menu()

    def start(self):
        self.run()

    def run(self):
        while self.running:
            self.update()

if __name__ == "__main__":
    E = Engine()
    E.start()
