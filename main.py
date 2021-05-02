import kivy

from kivy.app import App

kivy.require('2.0.0')

# Import for buttons
from kivy.uix.gridLayout import GridLayout

# For size of window
from kivy.config import Config

#Set size to resizeable
Config.set('graphics', 'resizable', 1)

calcApp = CalculatorApp()
calcApp.run()

#Making layout class
class CalcGridLayout(GridLayout):

    #Function is called when equal sign is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                #Solve formula and display it in entry which is pointed at by display
                self.display.text = str(eval(calculation))

            except Exception:
                self.display.text = "Error"

#Making App class
class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()
