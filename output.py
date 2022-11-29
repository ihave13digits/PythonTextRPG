from os import system
from sys import stdout, platform
import textwrap, time

from color import *

class Text():

    def __init__(self):
        self.text_speed = 0.06
        self.text_pause = 1.2
        self.menu_width = 48
        self.text_margin = 3
        self.clear_cmd = ""

        if platform.startswith('win32'):
            self.clear_cmd = 'cls'
        else:
            self.clear_cmd = 'clear'

    def clear_text(self):
        system(self.clear_cmd)

    def get_colored_text(self, txt, c=Color(255, 255, 255)):
        if self.clear_cmd == "clear":
            return "\x1b[{};2;{};{};{}m".format(38, c.r, c.g, c.b) + str(txt) + '\x1b[0m'
        else:
            return txt

    def expanded_text(self, a, b, g=" "):
        print("{}{}{}".format(a, g*(self.menu_width-(len(a)+len(b))), b))

    def print(self, txt="", end="\n", c=Color(255,255,255)):
        print(self.get_colored_text(txt, c), end)

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

T = Text()
