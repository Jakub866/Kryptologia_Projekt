from plyer import filechooser
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
"""Class of the FileChooser button of Plyer Package"""

class FileChoose(Button):
    def __init__(self, **kwargs):
        super(FileChoose,self).__init__(**kwargs)

    def choose(self,*args):
        return filechooser.open_file()

    def save(self,*args):
        return filechooser.save_file()


"""Class for the max characters limited input label"""
class LimitedInput(TextInput):
    max_characters = NumericProperty(0)
    def insert_text(self, substring, from_undo=False):
        if len(self.text) > self.max_characters and self.max_characters >0:
            substring =""
        TextInput.insert_text(self,substring,from_undo)

