from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class MainApp(App):

    def __init__(self):
        super().__init__()
        self.label_1 = Label(text="Введите сообщение:", size_hint=(1, .2), halign = "left", valign="middle")
        self.label_1.bind(size=self.label_1.setter('text_size'))
        self.label_2 = Label(text="Введите ключ от 0 до 32:", size_hint=(1, .2), halign = "left", valign="middle")
        self.label_2.bind(size=self.label_2.setter('text_size'))
        self.label_3 = Label(text="(Рас)шифрованное сообщение:", size_hint=(1, .2), halign = "left", valign="middle")
        self.label_3.bind(size=self.label_3.setter('text_size'))
        self.input_massage = TextInput()
        self.input_key = TextInput()
        self.label = TextInput(readonly=True)
        self.button = Button(text="Зашифровать")
        self.button.bind(on_press=self.btn_press)
        self.button_dec = Button(text="Дешифровать")
        self.button_dec.bind(on_press=self.btn_dec_press)
        self.popup = Popup(title='Test popup',
                           content=Label(text='Hello world'),
                           size_hint=(None, None), size=(400, 400))

    def btn_press(self, *args):
        alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        itog = ''
        massage = self.input_massage.text.upper()
        key = int(self.input_key.text)
        for i in massage:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto + key
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
        self.label.text = itog

    def btn_dec_press(self, *args):
        alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        itog = ''
        massage = self.input_massage.text.upper()
        key = int(self.input_key.text)
        for i in massage:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto - key
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
        self.label.text = itog

    def build(self):
        box = BoxLayout(orientation='vertical', padding=10, spacing=5)
        gl = GridLayout(cols=2)
        gl.add_widget(self.button)
        gl.add_widget(self.button_dec)
        box.add_widget(self.label_1)
        box.add_widget(self.input_massage)
        box.add_widget(self.label_2)
        box.add_widget(self.input_key)
        box.add_widget(self.label_3)
        box.add_widget(self.label)
        box.add_widget(gl)

        return box


if __name__ == '__main__':
    MainApp().run()

