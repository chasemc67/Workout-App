import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class ModAst(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ModAst = tk.Label(self)
       self.ModAst["text"] = "Modified Astrand"
       self.ModAst.grid(row=1, column=0)

       self.ModAstLoadA = tk.Label(self)
       self.ModAstLoadA["text"] = "Warm-Up Load(kp): "
       self.ModAstLoadA.grid(row=2, column=0)

       self.ModAstLoadA = tk.Text(self)
       self.ModAstLoadA["height"] = 1
       self.ModAstLoadA["width"] = 5
       self.ModAstLoadA.grid(row=2, column =1)

       self.ModAstLoadB = tk.Label(self)
       self.ModAstLoadB["text"] = "Work Load(kp): "
       self.ModAstLoadB.grid(row=3, column=0)

       self.ModAstLoadB = tk.Text(self)
       self.ModAstLoadB["height"] = 1
       self.ModAstLoadB["width"] = 5
       self.ModAstLoadB.grid(row=3, column=1)

       self.ModAstHR = tk.Label(self)
       self.ModAstHR["text"] = "Average HR(bpm): "
       self.ModAstHR.grid(row=3, column=2)

       self.ModAstHR = tk.Text(self)
       self.ModAstHR["height"] = 1
       self.ModAstHR["width"] = 5
       self.ModAstHR.grid(row=3, column=3)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=4, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=4, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=4, column=2)