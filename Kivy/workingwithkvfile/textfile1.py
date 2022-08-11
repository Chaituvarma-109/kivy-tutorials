# code how to use .kv file in kivy

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App


# define the App class
# and just pass rest write on kvfile
# not necessary to pass
# can also define function in it
class kvfileApp(App):
    pass


kv = kvfileApp()
kv.run()
