from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def getvalue(self):
        slider_value = self.ids.height_value
        print(slider_value)


    pass

class MainApp(MDApp):
    def __init__(self):
        Window.size = (400,600)
        super().__init__()

MainApp().run()