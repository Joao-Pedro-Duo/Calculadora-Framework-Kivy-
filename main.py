# importar o App, Builder
# Criar o Aplicativo
# Criar a função build

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

GUI = Builder.load_file("interface.kv")

class Calculator(App):
    def build(self):
        return GUI


Calculator().run()