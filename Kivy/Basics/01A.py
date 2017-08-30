""" Python3: Hello World App """
from kivy.app import App
from kivy.uix.label import Label

class HelloWorld(App):  # Inherits from 'App' class
    def build(self):
        return Label(text='Hello World!')
if __name__ == '__main__':
    HelloWorld().run()
