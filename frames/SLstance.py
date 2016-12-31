import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class SLstance(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SLStance = tk.Label(self)
       self.SLStance["text"] = "Single Leg Stance Test"
       self.SLStance.grid(row=0, column=0)

       self.SLOpenLeft = tk.Label(self)
       self.SLOpenLeft["text"] = "Eyes Open Left(sec.): "
       self.SLOpenLeft.grid(row=1, column=0)

       self.SLOpenLeft = tk.Text(self)
       self.SLOpenLeft["height"] = 1
       self.SLOpenLeft["width"] = 5
       self.SLOpenLeft.grid(row=1, column=1)

       self.SLOpenRight = tk.Label(self)
       self.SLOpenRight["text"] = "Eyes Open Right(sec.): "
       self.SLOpenRight.grid(row=1, column=2)

       self.SLOpenRight = tk.Text(self)
       self.SLOpenRight["height"] = 1
       self.SLOpenRight["width"] = 5
       self.SLOpenRight.grid(row=1, column=3)

       self.SLCloseLeft = tk.Label(self)
       self.SLCloseLeft["text"] = "Eyes Closed Left(sec.): "
       self.SLCloseLeft.grid(row=2, column=0)

       self.SLCloseLeft = tk.Text(self)
       self.SLCloseLeft["height"] = 1
       self.SLCloseLeft["width"] = 5
       self.SLCloseLeft.grid(row=2, column=1)

       self.SLCloseRight = tk.Label(self)
       self.SLCloseRight["text"] = "Eyes Closed Right(sec.): "
       self.SLCloseRight.grid(row=2, column=2)

       self.SLCloseRight = tk.Text(self)
       self.SLCloseRight["height"] = 1
       self.SLCloseRight["width"] = 5
       self.SLCloseRight.grid(row=2, column=3)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)