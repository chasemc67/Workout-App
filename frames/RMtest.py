import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class RMtest(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.RepMaxTest = tk.Label(self)
       self.RepMaxTest["text"] = "1 Rep Max.(Tested)"
       self.RepMaxTest.grid(row=0, column=0)

       self.RMTestExA = tk.Label(self)
       self.RMTestExA["text"] = "Exercise: "
       self.RMTestExA.grid(row=1, column=0)

       self.RMTestExA = tk.Text(self)
       self.RMTestExA["height"] = 1
       self.RMTestExA["width"] = 5
       self.RMTestExA.grid(row=1, column=1)

       self.RMTestExAWeight = tk.Label(self)
       self.RMTestExAWeight["text"] = "1RM(kg): "
       self.RMTestExAWeight.grid(row=1, column=2)

       self.RMTestExAWeight = tk.Text(self)
       self.RMTestExAWeight["height"] = 1
       self.RMTestExAWeight["width"] = 5
       self.RMTestExAWeight.grid(row=1, column=3)

       self.RMTestExB = tk.Label(self)
       self.RMTestExB["text"] = "Exercise: "
       self.RMTestExB.grid(row=2, column=0)

       self.RMTestExB = tk.Text(self)
       self.RMTestExB["height"] = 1
       self.RMTestExB["width"] = 5
       self.RMTestExB.grid(row=2, column=1)

       self.RMTestExBWeight = tk.Label(self)
       self.RMTestExBWeight["text"] = "1RM(kg): "
       self.RMTestExBWeight.grid(row=2, column=2)

       self.RMTestExBWeight = tk.Text(self)
       self.RMTestExBWeight["height"] = 1
       self.RMTestExBWeight["width"] = 5
       self.RMTestExBWeight.grid(row=2, column=3)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)