# import kivy module
import kivy

# this restricts the kivy version i.e
# below this kivy version you cannot use the app or software
# kivy.require("1.9.1")
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# if you not import label and use it it through error
from kivy.uix.label import Label


# defining the App class
class MyLabelApp(App):
    def build(self):
        # label display the text on screen
        # lbl = # text colour
        lbl = Label(text="Label is Added on screen !!:)", font_size='40sp', color=[0.41, 0.42, 0.74, 1], markup=True)
        return lbl


# creating the object
label = MyLabelApp()
# run the window
label.run()
