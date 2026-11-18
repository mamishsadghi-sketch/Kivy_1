from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.lang import Builder
from kivy.animation import Animation
import re

class RootLayout(FloatLayout):
    pass

class MyCanvas(FloatLayout):
    pass

class Bobsfangi(Widget):
    pass

class Patric(Widget):
    pass

class CodeAnims(BoxLayout):
    def start(self, text, instance=None):
        root = App.get_running_app().root     
        self.player_a = root.ids.player_a 
        self.hit = False         
        self.player_a.pos_hint = {} 

        self.player_b = root.ids.player_b
        pairs = re.findall(r"([a-zA-Z_]\w*)\s*[:=]\s*(-?\d+(?:\.\d+)?)", text)
        data = {name.lower(): float(value) for name, value in pairs}
        data_pos = [data["x"], data["y"]]

        
        print(self.player_b.size)
        self.anim=Animation(x=data["x"], y=data["y"], duration=1.5)
        self.anim.bind(on_progress=self.check_hit)
        self.anim.start(self.player_a)

        

    def check_hit(self, anim, widget, progress):
        if not self.hit and widget.collide_widget(self.player_b):
            self.hit = True
            self.anim.stop(widget)
    
class MyApp(App):
    def build(self):
        Builder.load_file("codeAnim.kv")
        return RootLayout()


MyApp().run()