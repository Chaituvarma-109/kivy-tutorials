import kivy

# base Class of your App inherits from the App class.	
# app:always refers to the instance of your application
from kivy.app import App

from kivy.uix.dropdown import DropDown

# module consists the floatlayout
# to work with FloatLayout first
# you have to import it
from kivy.uix.floatlayout import FloatLayout

# The Button is a Label with associated actions that
# are triggered when the button is pressed (
# or released after a click / touch).
from kivy.uix.button import Button


class CustomDropDown(DropDown):
    pass


class DropdownDemo(FloatLayout):
    '''The code of the application itself.'''

    def __init__(self, **kwargs):
        '''The button at the opening of the window is created here,
		not in kv
		'''
        super(DropdownDemo, self).__init__(**kwargs)
        self.dropdown = CustomDropDown()

        # Creating a self widget button
        self.mainbutton = Button(text='Do you in college?', size_hint_x=0.6, size_hint_y=0.15)

        # Added button to FloatLayout so inherits this class
        self.add_widget(self.mainbutton)

        # Adding actions
        # If click
        self.mainbutton.bind(on_release=self.dropdown.open)

        # root.select on_select called
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select=self.callback)

    def callback(self, instance, x):
        '''x is self.mainbutton.text refreshed'''
        print("The chosen mode is: {0}".format(x))


class myapp(App):
    '''The build function returns root,
	here root = DropdownDemo ().
	root can only be called in the kv file.
	'''

    def build(self):
        return DropdownDemo()


if __name__ == '__main__':
    myapp().run()
