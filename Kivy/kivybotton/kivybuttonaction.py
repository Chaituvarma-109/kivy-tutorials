# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# BoxLayout arranges children
# in a vertical or horizontal box.
from kivy.uix.boxlayout import BoxLayout

# this restricts the kivy version i.e.
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")


# class in which we are defining action on click
class RootWidget(BoxLayout):

    def btn_clk(self):
        self.lbl.text = "You have been pressed"


# creating action class and calling
# Root-widget by returning it
class ActionApp(App):

    def build(self):
        return RootWidget()


# creating the myApp root for ActionApp() class
myApp = ActionApp()

# run function runs the whole program
# i.e. run() method which calls the
# target function passed to the constructor.
myApp.run()
