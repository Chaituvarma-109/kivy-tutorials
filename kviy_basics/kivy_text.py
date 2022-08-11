# import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class TutorialApp(App):

    def build(self):
        b = BoxLayout(orientation='vertical')

        # Adding the text input
        t = TextInput(font_size=20,
                      size_hint_y=None,
                      height=100)

        f = FloatLayout()

        # By this you are able to move the
        # Text on the screen to anywhere you want
        s = Scatter()
        la = Label(text="Hello !", font_size=20)

        f.add_widget(s)
        s.add_widget(la)

        b.add_widget(t)
        b.add_widget(f)

        # Binding it with the label
        t.bind(text=la.setter('text'))

        return b


if __name__ == "__main__":
    TutorialApp().run()
