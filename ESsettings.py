from var import *
from output import *

def set_speed():
    T.clear_text()
    T.print("(1) Fastest\n(2) Fast\n(3) Normal\n(4) Slow\n(5) Slowest\n(6) Custom\n(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0": V.state = "settings"
    elif sel == "1":
        T.text_speed = 0.010
        T.text("Sample text to show timing")
    elif sel == "2":
        T.text_speed = 0.020
        T.text("Sample text to show timing")
    elif sel == "3":
        T.text_speed = 0.030
        T.text("Sample text to show timing")
    elif sel == "4":
        T.text_speed = 0.045
        T.text("Sample text to show timing")
    elif sel == "5":
        T.text_speed = 0.060
        T.text("Sample text to show timing")
    elif sel == "6":
        custom_speed = ""
        while True:
            custom_speed = T.input(": ")
            try:
                _test = float(custom_speed)
                if _test < 1.0:
                    T.text_speed = _test
                else:
                    T.print("Invalid Input.  Enter Decimal Value Greater Than 0.0 And Less Than 1.0.")
                break
            except:
                T.print("Invalid Input.  Enter Decimal Value Greater Than 0.0 And Less Than 1.0.")
        T.text_speed = float(custom_speed)
        T.text("Sample text to show timing")

def set_pause():
    T.clear_text()
    T.print("(1) Fast\n(2) Medium\n(3) Slow\n(4) Wait\n(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0": V.state = "settings"
    elif sel == "1":
        T.text_pause = 0.15
        T.text("Sample text to show timing")
    elif sel == "2":
        T.text_pause = 0.225
        T.text("Sample text to show timing")
    elif sel == "3":
        T.text_pause = 0.3
        T.text("Sample text to show timing")
    elif sel == "4":
        T.text_pause = -1.0

def set_margin():
    T.clear_text()
    T.print("(1) 1\n(2) 3\n(3) 5\n(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0": V.state = "settings"
    elif sel == "1":
        T.text_margin = 1
        T.text("Sample text to show margin")
    elif sel == "2":
        T.text_margin = 3
        T.text("Sample text to show margin")
    elif sel == "3":
        T.text_margin = 5
        T.text("Sample text to show margin")

def set_width():
    T.clear_text()
    T.print("(1) 32\n(2) 48\n(3) 64\n(0) Back", "\n", V.c_text2)
    sel = T.input(": ")
    if sel == "0": V.state = "settings"
    elif sel == "1":
        T.menu_width = 48
        T.text("Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  ")
    elif sel == "2":
        T.menu_width = 56
        T.text("Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  ")
    elif sel == "3":
        T.menu_width = 64
        T.text("Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  Sample text to show margin.  ")

def set_color():
    T.clear_text()
    T.print("(r) Red\n(g) Green\n(b) Blue\n", "\n", V.c_edit)
    T.print("(1) Text", "\n", V.c_text1)
    T.print("(2) Option", "\n", V.c_text2)
    T.print("(3) Count", "\n", V.c_count)
    T.print("(4) Attack", "\n", V.c_attack)
    T.print("(5) Defense", "\n", V.c_defense)
    T.print("(6) Magic", "\n", V.c_magic)
    T.print("(7) Gold", "\n", V.c_gold)
    T.print("(0) Back", "\n", V.c_text2)

    sel = T.input(": ")
    if sel == "0": V.state = "settings"
    if sel == "r":
        T.clear_text()
        T.print("Input range (0-255)", "\n", V.c_text1)
        v = T.input(": ")
        V.c_edit.r = int(v)
    if sel == "g":
        T.clear_text()
        T.print("Input range (0-255)", "\n", V.c_text1)
        v = T.input(": ")
        V.c_edit.g = int(v)
    if sel == "b":
        T.clear_text()
        T.print("Input range (0-255)", "\n", V.c_text1)
        v = T.input(": ")
        V.c_edit.b = int(v)
    if sel == "1": V.c_text1.reset(V.c_edit)
    if sel == "2": V.c_text2.reset(V.c_edit)
    if sel == "3": V.c_count.reset(V.c_edit)
    if sel == "4": V.c_attack.reset(V.c_edit)
    if sel == "5": V.c_defense.reset(V.c_edit)
    if sel == "6": V.c_magic.reset(V.c_edit)
    if sel == "7": V.c_gold.reset(V.c_edit)

def settings():
    T.clear_text()
    T.print("(1) Text Speed\n(2) Text Pause\n(3) Clear Margin\n(4) Menu Width\n(5) Color\n(0) Back", "\n", V.c_text2)

    sel = T.input(": ")
    if sel == "0": V.state = "main_menu"
    elif sel == "1": V.state = "set_speed"
    elif sel == "2": V.state = "set_pause"
    elif sel == "3": V.state = "set_margin"
    elif sel == "4": V.state = "set_width"
    elif sel == "5": V.state = "set_color"
