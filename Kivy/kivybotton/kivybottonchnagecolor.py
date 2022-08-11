# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application

from kivy.app import App

# BoxLayout arranges children
# in a vertical or horizontal box.
from kivy.uix.boxlayout import BoxLayout

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

from kivy.uix.label import Label

# this restricts the kivy version i.e.
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")


# class in which we are defining action on click
# class RootWidget(BoxLayout):
#
#     def btn_clk(self):
#         self.lbl.text = "You have been pressed"


# creating action class and calling
# Root-widget by returning it

class ActionApp(App):

    def btn_clk(self, value):
        self.lbl = Label(text="Label is Added on screen !!:):)")
        # lbl.text = "You have been pressed"
        # return lbl

    # def build(self):
    #     return RootWidget()

    def build(self):
        btn = Button(text="Push Me !", font_size="20sp", background_color=(1, 1, 1, 1), size=(32, 32),
                     size_hint=(.2, .2), pos=(300, 250))
        btn.bind(on_press=self.btn_clk)
        return btn


# creating the myApp root for ActionApp() class
myApp = ActionApp()

# run function runs the whole program
# i.e. run() method which calls the
# target function passed to the constructor.
myApp.run()
