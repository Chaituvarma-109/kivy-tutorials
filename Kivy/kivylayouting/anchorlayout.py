# Sample Python application demonstrating
# the working of AnchorLayout in Kivy

# Module imports

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# The AnchorLayout aligns its children to a border
# (top, bottom, left, right) or center
from kivy.uix.anchorlayout import AnchorLayout

# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the childrens at the desired location.
from kivy.uix.boxlayout import BoxLayout

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button


# A Kivy app demonstrating the working of anchor layout
class AnchorLayoutApp(App):

    def build(self):
        # Anchor Layout1
        layout = AnchorLayout(
            anchor_x='center', anchor_y='center')
        btn = Button(text='Hello World',
                     size_hint=(.3, .3),
                     background_color=(1.0, 0.0, 0.0, 1.0))

        layout.add_widget(btn)
        return layout


# creating the object root for AnchorLayoutApp() class
root = AnchorLayoutApp()
# Run the Kivy app
root.run()
