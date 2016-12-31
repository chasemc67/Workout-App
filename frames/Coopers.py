import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class Coopers(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Cooper = tk.Label(self)
       self.Cooper["text"] = "Coopers Run"
       self.Cooper.grid(row=0, column=0)

       self.CooperDist = tk.Label(self)
       self.CooperDist["text"] = "Distance(miles): "
       self.CooperDist.grid(row=1, column=0)

       self.CooperDist = tk.Text(self)
       self.CooperDist["height"] = 1
       self.CooperDist["width"] = 5
       self.CooperDist.grid(row=1, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)
