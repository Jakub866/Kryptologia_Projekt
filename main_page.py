import threading

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.clock import mainthread
from kivy.app import App

from algorithms.blocks import FileChoose,LimitedInput
from binread import *

"""Global variables watching use of threads, previous sites, localisations of file and algorithms type"""
global workThread
global Previous

global path_load
global path_save

global enc_or_dec


"""Init screen manager for fluenty changing pages in app"""
class WindowManager(ScreenManager):
    pass

"""Main frame of all of the applications windows"""
class Page(Screen):
    def on_enter(self):
        global Previous
        Previous = self.manager.current
        self.ids.directoryCheckbox.active = True

    def refresh(self):
        ids_list = [self.ids.loadDirectory,self.ids.saveDirectory,
                    self.ids.keyphrase, self.ids.input, self.ids.output, self.ids.status]
        for i in ids_list:
            i.text = ""

    def status(self,status):
        self.ids.status.text = status

    def set_load(self):
        try:
            global path_load
            path_load = str(FileChoose.choose(FileChoose))
            self.ids.loadDirectory.text = path_load[2:len(path_load)-2]
            self.status("File loaded.")
        except:
            self.status("Wrong directory")

    def checkbox_click(self, instance, value,type):
        if value is True:
            match type:
                case 1:
                    self.ids.output.disabled = True
                    self.ids.input.disabled = True
                    self.ids.output.text = ""
                    self.ids.input.text = ""
                    self.ids.inputCheckbox.active = False

                    self.ids.input.background_color = (0, 0, 0, 0.1)
                    self.ids.output.background_color = (0, 0, 0, 0.1)
                case 2:
                    self.ids.fileLoad.disabled = True
                    self.ids.fileSave.disabled = True
                    self.ids.loadDirectory.text = ""
                    self.ids.saveDirectory.text = ""
                    self.ids.directoryCheckbox.active = False

        else:
            match type:
                case 1:
                    self.ids.output.disabled = False
                    self.ids.input.disabled = False
                    self.ids.input.background_color = (0, 0, 0, 0)
                    self.ids.output.background_color = (0, 0, 0, 0)

                case 2:
                    self.ids.fileLoad.disabled = False
                    self.ids.fileSave.disabled = False
                    self.ids.loadDirectory.background_color = (0, 0, 0, 0)
                    self.ids.saveDirectory.background_color = (0, 0, 0, 0)



    def set_save(self):
        try:
            global path_save
            path_save = str(FileChoose.save(FileChoose))
            self.ids.saveDirectory.text = path_save[2:len(path_save)-2]
            self.status("Saving directory loaded.")

        except:
            self.status("Error when choosing a path to save")



    def enc_dec_algorithm(self, keyphrase, plaintext, algorithm, type):
        global enc_or_dec
        enc_or_dec = type

        input_functions = {1:handle_input_dec, 2: handle_input_enc}
        directory_functions ={1:reading_decrypting, 2: saving_encrypting}

        if keyphrase == "":
            self.status("Wrong keyspace")

        if self.ids.loadDirectory.text == self.ids.saveDirectory.text != "":
            self.status("Saving and loading directory are the same!")

        if self.ids.loadDirectory.text and self.ids.saveDirectory.text:
            try:
                self.status("")
                global workThread

                workThread = threading.Thread(
                        target=directory_functions[type],
                        args=(algorithm,self.ids.loadDirectory.text,self.ids.saveDirectory.text,keyphrase))

                workThread.start()
                self.status("Algorithm done.")


            except:
                self.status("Wrong keyspace. Check Help")

        if self.ids.loadDirectory.text and not self.ids.saveDirectory.text:
            self.status("There is no save directory")

        if not self.ids.loadDirectory.text and self.ids.saveDirectory.text:
            self.status("There is no load directory")
        if not keyphrase and not self.ids.loadDirectory.text and not self.ids.input.text:
            self.status("Wrong input")

        if keyphrase and not plaintext.text:
            self.status("There is no input text")

        try:
            plaintext = input_functions[type](algorithm, plaintext.text, keyphrase)
            self.ids.output.text = plaintext
            self.status("Completed")

        except:
            self.status("Wrong keyspace. Check Help")





class Main_page(Screen):
    Window.size = (800, 950)
    Window.clearcolor = (1, 1, 1, 1)


class Atbash_Page(Page):
    pass

class Vigenere_Page(Page):
    pass

class Caesar_Page(Page):
    pass

class Substitution_Page(Page):
    pass

class Enigma_Page(Page):
    def keyphrase_creator(self, rotor1, rotor2 ,rotor3 ,plugboard, posRotors, rotateRotor, plaintext, algorithm, type):
        try:
            tupleRotor = tuple(map(int, rotateRotor))

            plugboard = plugboard.text.split()
            max_len = 2
            if all(len(elem) == max_len for elem in plugboard):
                keyphrase = [int(rotor1.text), int(rotor2.text), int(rotor3.text), plugboard, posRotors.text,
                             tupleRotor]
                self.enc_dec_algorithm(keyphrase, plaintext, algorithm, type)
            else:
                self.status("Wrong dimension of plugboard")

        except:
            self.status("Wrong keyspace")

    def refresh(self):
        ids_list = [self.ids.loadDirectory,self.ids.saveDirectory,self.ids.plugboard,self.ids.posRotors,
                    self.ids.rotateRotor1,self.ids.rotateRotor2,self.ids.rotateRotor3,
                    self.ids.input, self.ids.output, self.ids.status]
        for i in ids_list:
            i.text = ""

    def set_dec(self, block):
        tmp = int(block.text)
        block.text = "5" if ((tmp - 1) % 6) == 0 else str(((tmp - 1) % 6))


    def set_inc(self, block):
        tmp = int(block.text)
        block.text = "1" if ((tmp + 1) % 6) == 0 else str(((tmp + 1) % 6))

class Loading_Page(Screen):
    local = ""

    def animationThread(self):
        # Initiate the animation
        anim= Animation(pos_hint = {"center_x":0.1}, duration= 1.5)
        anim+= Animation(pos_hint = {"center_x":0.9}, duration = 1.5)
        anim.repeat = True
        anim.start(self.loading_image)

        # Waiting for the end of the Enc/Dec thread
        while workThread.is_alive():
            time.sleep(3)
        anim.stop(self.loading_image)
        self.edit()


    def on_enter(self):
        # init loading labels
        self.loading_label = Label(text="Loading...",
                                   size_hint=(1, 0.1),
                                   font_size=50,
                                   pos_hint={"center_x": 0.5},
                                   )
        self.loading_image = Image(source="images//pad.png",
                                   size_hint=(.2, .2),
                                   pos_hint={"center_x": 0.9},
                                   )

        self.ids.loadingLayout.add_widget(self.loading_label)
        self.ids.loadingLayout.add_widget(self.loading_image)

        Loading_Thread = threading.Thread(target=self.animationThread, daemon=True)
        Loading_Thread.start()

    @mainthread
    def get_back(self, *args):
        # delete response label
        self.ids.loadingLayout.remove_widget(self.response_label)
        self.ids.loadingLayout.remove_widget(self.response_button)
        self.ids.loadingLayout.remove_widget(self.histogram_button)

        self.manager.current = Previous

    def move(self,*args):
        # delete response label
        self.ids.loadingLayout.remove_widget(self.response_label)
        self.ids.loadingLayout.remove_widget(self.response_button)
        self.ids.loadingLayout.remove_widget(self.histogram_button)
        self.manager.current = "histogram"


    @mainthread
    def edit(self):
        # Deleting old widgets
        self.ids.loadingLayout.remove_widget(self.loading_label)
        self.ids.loadingLayout.remove_widget(self.loading_image)
        # Init of response
        self.response_button = Button(text="Finish",
                                 size_hint=(1,.2),
                                 font_size = 25,
                             )
        self.histogram_button = Button(text="Show the histogram",
                                      size_hint=(1,.2),
                                      font_size = 25,
                                      )
        self.response_label = Label(text="Algorithm was succesfully completed",
                               font_size = 50,
                               text_size= (self.width,None),
                               halign = 'center',
                               valign = 'center',
                               )
        # Add new response to Loading Page
        self.ids.loadingLayout.add_widget(self.response_label)
        self.ids.loadingLayout.add_widget(self.response_button)
        self.ids.loadingLayout.add_widget(self.histogram_button)

        self.response_button.bind(on_press=self.get_back)
        self.histogram_button.bind(on_press=self.move)


from algorithms.plot import Histogram
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg


class Histogram_Page(Screen):
    def on_enter(self, *args):
        print(enc_or_dec)
        print(path_save[2:len(path_save)-2],path_load[2:len(path_load)-2])
        self.data = Histogram(path_load[2:len(path_load) - 2], path_save[2:len(path_save) - 2], enc_or_dec)
        self.data = self.data.visualization()
        self.data = FigureCanvasKivyAgg(self.data)
        self.ids.loadingLayout.add_widget(self.data)

    @mainthread
    def get_back(self):
        self.ids.loadingLayout.remove_widget(self.data)
        self.manager.current = Previous

kv = Builder.load_file('kivy_files\\page.kv')
sm = ScreenManager()
sm.add_widget(Main_page(name='main'))
sm.add_widget(Caesar_Page(name ='cezar'))
sm.add_widget(Atbash_Page(name ='atbash'))
sm.add_widget(Vigenere_Page(name ='vigenere'))
sm.add_widget(Substitution_Page(name ="substit"))
sm.add_widget(Enigma_Page(name ="enigma"))
sm.add_widget(Loading_Page(name="loading"))
sm.add_widget(Histogram_Page(name="histogram"))
class PageApp(App):

    def build(self):
        return sm


if __name__ == "__main__":
    PageApp().run()

