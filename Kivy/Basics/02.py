""" Python3: Logging Screen """
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):  # Inherits from 'GridLayout' class
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        # Username-Widget
        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        # Password-Widget
        self.add_widget(Label(text='Password:'))
        self.password = TextInput(multiline=False,password=True)
        self.add_widget(self.password)
class Kivy_Test(App):  # Inherits from 'App' class
    def build(self):
        return LoginScreen()
if __name__ == '__main__':
    Kivy_Test().run()
