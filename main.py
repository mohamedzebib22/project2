from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.core.window import Window
Window.clearcolor=(100/255.0,0,1)
Window.size=(400,630)

class Scr2(Screen):
    pass
class Scr3(Screen):
    pass
class Scr4(Screen):
    pass
class Pr1(Screen):
    pass
class Pr2(Screen):
    pass
class Pr3(Screen):
    pass
class Pr4(Screen):
    pass
class Pr5(Screen):
    pass
class Pr6(Screen):
    pass
class Mainscr(ScreenManager):
    pass
Kv=Builder.load_file('pro.kv')
class Myapp(App):
    def build(self):
        self.title='myApp'
        return Kv
if __name__=='__main__':
    Myapp().run()    