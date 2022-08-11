from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    my_text = StringProperty("1")
    count = 1
    btn_state = BooleanProperty(False)
    text_inp_str = StringProperty("foo")
    # slider_value_txt = StringProperty("Value")

    def on_button_press(self):
        if self.btn_state:
            print("Button Clicked...")
            self.count += 1
            self.my_text = str(self.count)

    def on_state_toggle_btn(self, widget):
        print(f"toggle state: {widget.state}")
        if widget.state == "normal":
            widget.text = "OFF"
            self.btn_state = False
        else:
            widget.text = "ON"
            self.btn_state = True

    def text_validate(self, widget):
        self.text_inp_str = widget.text

    # def on_switch_active(self, widget):
    #     print(f"Switch: {str(widget.active)}")

    # def on_slider_value(self, widget):
    #     print(f"Switch: {int(widget.value)}")
        # self.slider_value_txt = str(int(widget.value))


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(100):
            # size = dp(100)+i*10
            size = dp(100)
            b = Button(text=str(i), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
