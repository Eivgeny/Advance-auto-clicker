from inventory import Inv
from pyautogui import position, pixelMatchesColor, click
from threading import Thread
from recorder import start_recording
from file_manager import loadfile
from additional import tracker
import time

# global variables
stop = False
inv = None
# play responsible for running all the recorded records till the use decide to stop


class AdvClicker:
    def start_app(self, records):
        # Creating 2 threads, one that run the records and other that stops the first one by user choice
        global stop, inv
        stop = False
        if inv is None:
            print('please record inventory first')
            AdvClicker.set_inv()
            print('press s - to start')
        else:
            print('The auto clicker is about to start!\n')
            print('type e - to exit\n')
            time.sleep(4)
            Thread(target=self.runnable_function, args=(records,)).start()  # running the records
            Thread(target=self.stop_function).start()  # checking user input to stop runnable_function

    @staticmethod
    def set_inv():
        print('\n\tto capture the last item in the inventory\n'
              'please point the mouse and press f')
        global inv
        inv = Inv()
        while True:
            key = tracker()
            if key == 'f':
                inv.set_color(position())
                break

    def runnable_function(self, records):
        # run the records and use the global variable 'stop' to check the user input
        global stop, inv
        while True:
            for record in records:
                self.action(act=record)
                time.sleep(1)
                if stop:
                    break

            if stop:
                print('=======STOP=======\n')
                break

    @staticmethod
    def stop_function():
        # check the user input and update the global variable 'stop' if the user decide to stop the threads from running
        global stop
        while True:
            key = tracker()
            if key == 'e':
                stop = True
                break

    @staticmethod
    def load_file() -> list:
        return loadfile()

    @staticmethod
    def start_recording():
        start_recording()

    def action(self, act):
        if act['action'] == 'move':
            self.move(act)
        if act['action'] == 'cut':
            self.tree_cut(act)

    @staticmethod
    def move(act):
        while True:
            if stop:
                break
            if pixelMatchesColor(act['check'][0], act['check'][1], act['color']):
                click(act['click'][0], act['click'][1])
                break
            else:
                time.sleep(2)

    @staticmethod
    def tree_cut(act):
        global inv, stop
        while True:
            if stop:
                break
            if inv.check_color():
                break
            if pixelMatchesColor(act['check'][0], act['check'][1], act['color']):
                click(act['click'][0], act['click'][1])
                break
            else:
                time.sleep(1)

    @staticmethod
    def color_check(pos, color):
        return pixelMatchesColor(pos[0], pos[1], color)
