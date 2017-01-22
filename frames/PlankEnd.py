import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class PlankEnd(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Plank = tk.Label(self)
       self.Plank["text"] = "Front Plank"
       self.Plank.grid(row=0, column=0)

       self.PlankTime = tk.Label(self)
       self.PlankTime["text"] = "Time(sec.)"
       self.PlankTime.grid(row=1, column=0)

       self.PlankTimeText = tk.Text(self)
       self.PlankTimeText["height"] = 1
       self.PlankTimeText["width"] = 5
       self.PlankTimeText.grid(row=1, column=1)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)

   def loadData(self, person):

       self.PlankTimeText.delete(1.0, tk.END)
       self.PlankTimeText.insert(tk.END, person.plankTime)

   def saveData(self, person):
       person.plankTime = self.PlankTimeText.get(1.0, tk.END)
