import tkinter as tk   # python3

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class Results(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Results = tk.Label(self)
       self.Results["text"] = "Results"
       self.Results.pack()


       self.person = self.controller.person

   def loadData(self, person):
       if (self.person.vertJump != "" and self.person.vertReach != ""):
        self.vertJumpLabel = tk.Label(self)
        self.vertJumpLabel["text"] = "VertJump (W):"
        self.vertJumpLabel.pack()

        self.vertJumpReachLabel = tk.Label(self)
        self.vertJumpReachLabel['text'] = ("Reach: " + self.person.vertReach)
        self.vertJumpReachLabel.pack()

        self.vertJumpCalcOutput = tk.Label(self)
        self.vertJumpCalcOutput['text'] = "Calc output: " + str(person.getVertJump())
        self.vertJumpCalcOutput.pack()

       self.Back = BackButton(self, self.controller)
       self.Back.pack()

       self.Quit = QuitButton(self, self.controller)
       self.Quit.pack()

   def saveData(self, person):
       person.PushUpNum = self.PushUpNumText.get(1.0, tk.END)

