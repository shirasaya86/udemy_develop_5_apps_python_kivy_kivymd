from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
import math
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)

class HomeScreen(Screen):
    weight = NumericProperty(50)


    def getvalue(self):
        slider_value = self.ids.height_value

    
    def increase(self):
        self.weight = self.weight + 1
        
    def decrease(self):
        self.weight = self.weight - 1

    def calculate_bmi(self):
        height = round(self.ids.height_value.value) / 100
        square = height * height
        bmi = round(self.weight / square)
        dialog = MDDialog(
            MDDialogHeadlineText(
                text="BMI",
            ),
            MDDialogSupportingText(
                text=f"Your BMI is {bmi}",
            )
        )
        dialog.open()

        # dialog.open()
    pass



class MainApp(MDApp):
    def __init__(self):
        Window.size = (400,600)
        super().__init__()

MainApp().run()