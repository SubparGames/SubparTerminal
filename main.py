from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init(**kwargs)


class SubparTerminal(App):
    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect)

        self.root.add_widget(TextInput())

        with root.canvas.before:
            Color(0, 0, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


SubparTerminal().run()
