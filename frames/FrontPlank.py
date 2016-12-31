import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class FrontPlank(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.FrPlank = tk.Label(self)
       self.FrPlank["text"] = "Front Plank"
       self.FrPlank.grid(row=0, column=0)

       self.FrPlankRate = tk.Label(self)
       self.FrPlankRate["text"] = "Rating(0-3): "
       self.FrPlankRate.grid(row=1, column=0)

       self.FrPlankRate = tk.Text(self)
       self.FrPlankRate["height"] = 1
       self.FrPlankRate["width"] = 5
       self.FrPlankRate.grid(row=1, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)
