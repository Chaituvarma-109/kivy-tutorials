# Sample Python application demonstrating that
# how to create button using image in kivy

##################################################
# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# to change the kivy default settings we use this module config
from kivy.config import Config

# this restricts the kivy version i.e.
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)


# class in which we are creating the image button
class ButtonApp(App):

    def build(self):
        # create an image a button
        # Adding images normal.png image as button
        # decided its position and size
        btn = Button(color=(1, 0, .65, 1),
                     background_normal='cat3.png',
                     background_down='down.png',
                     size_hint=(.3, .3),
                     pos_hint={"x": 0.35, "y": 0.3}
                     )

        return btn


# creating the object root for ButtonApp() class
root = ButtonApp()

# run function runs the whole program
# i.e run() method which calls the target
# function passed to the constructor.
root.run()
