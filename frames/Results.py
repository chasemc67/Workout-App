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
       self.Results.grid(row=0, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.PushUpNumText.delete(1.0, tk.END)
       self.PushUpNumText.insert(tk.END, person.PushUpNum)

   def saveData(self, person):
       person.PushUpNum = self.PushUpNumText.get(1.0, tk.END)

