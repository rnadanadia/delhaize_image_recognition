
import kivy
import time
kivy.require("1.9.1")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.app import App

Config.set('graphics', 'resizable', True )
Builder.load_string('''               
<MyLayout>:
    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        padding: 50
        spacing: 20
                                
        Label:
            id: my_label
            text: "Hello World"
            font_size: 32

            Button:
                size_hint: .15, .12
                pos_hint: {'center_x' : 0.5}
                background_color: (0, 0, 0, 0)

                Image:
                    id: my_image
                    source: '/Users/nadanadia/Documents/GitHub/delhaize_image_recognition/imageicon.png'
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    ''')


class MyLayout(Widget):
    def create_icon(self):
        self.ids.my_image.source = '/Users/nadanadia/Documents/GitHub/delhaize_image_recognition/imageicon.png'
    
class LayoutApp(App):
    def create_icon(self):
        return MyLayout


if __name__ == "__main__" :
    LayoutApp().run()

