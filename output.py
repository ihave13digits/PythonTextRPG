from os import system, environ
from sys import stdin, stdout, platform
import textwrap, time
#import androidhelper

from color import *

class Text():

    def __init__(self):
        #self.droid = androidhelper.Android()
        self.text_speed = 0.03
        self.text_pause = 0.3
        self.menu_width = 48
        self.text_margin = 3
        self.clear_cmd = ""
        self.color_enabled = False
        
        self.init_color()

    def init_color(self):
        p = platform
        t = bool(hasattr(stdout, 'isatty') and stdout.isatty())
        if p.startswith('win32'):
            self.clear_cmd = 'cls'
        else:
            self.clear_cmd = 'clear'
            if ('ANSICON' not in environ or environ['TERM'] == "xterm-256color") and t:
                self.color_enabled = True

    def clear_text(self):
        system(self.clear_cmd)

    def get_colored_text(self, txt, c=Color(255, 255, 255), style=38):
        if self.color_enabled:
            return "\x1b[{};2;{};{};{}m".format(style, c.r, c.g, c.b) + str(txt) + '\x1b[0m'
        else:
            return txt

    def expand_text(self, a, width, g=" ", align='l'):
        if align == 'l':
            return "{}{}".format(a, g*(width-(len(str(a)))))
        if align == 'r':
            return "{}{}".format(g*(width-(len(str(a)))), a)

    def expanded_text(self, a, b, g=" ", c=Color(255, 255, 255)):
        self.print("{}{}{}".format(a, g*(self.menu_width-(len(str(a))+len(str(b)))), b), "\n", c)

    def print(self, txt="", end="\n", c=Color(255,255,255)):
        print(self.get_colored_text(txt, c), end=end)

    def input(self, txt, c=Color(255,255,255)):
        return input(self.get_colored_text(txt, c, 5))

    def get_char(self):
        system("stty raw -echo")
        c = stdin.read(1)
        system("stty -raw echo")
        return str(c)

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
        
        
        #self.droid.ttsSpeak(text)


T = Text()
