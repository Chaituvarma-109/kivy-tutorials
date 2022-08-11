# Program to Show how to create a switch
# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# The Switch widget is active or inactive
# The state transition of a switch is from
# either on to off or off to on.
from kivy.uix.switch import Switch

# The GridLayout arranges children in a matrix.
# It takes the available space and
# divides it into columns and rows,
# then adds widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout

# The Label widget is for rendering text.
from kivy.uix.label import Label


# A Gridlayout with a label a switch
# A class which contains all stuff about the switch
class SimpleSwitch(GridLayout):

    # Defining __init__ constructor
    def __init__(self, **kwargs):
        # super function can be used to gain access
        # to inherited methods from a parent or sibling class
        # that has been overwritten in a class object.
        super(SimpleSwitch, self).__init__(**kwargs)

        # no of columns
        self.cols = 2

        # Adding label to the Switch
        self.add_widget(Label(text="Switch"))

        # Initially switch is Off i.e active = False
        self.settings_sample = Switch(active=False)

        # Add widget
        self.add_widget(self.settings_sample)


# Defining the App Class
class SwitchApp(App):
    # define build function
    def build(self):
        # return the switch class
        return SimpleSwitch()


# Run the kivy app
if __name__ == '__main__':
    SwitchApp().run()
