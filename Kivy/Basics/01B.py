"""
Python3: Hello World App using kv stylesheet 
  Uses 'HelloWorld.kv' for style-info.
"""
from kivy.app import App
from kivy.uix.label import Label

class HelloWorld(App):  # Inherits from 'App' class
    def build(self):
        return Label()
if __name__ == '__main__':
    HelloWorld().run()
