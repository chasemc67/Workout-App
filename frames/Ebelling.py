import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class Ebelling(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Ebelling = tk.Label(self)
       self.Ebelling["text"] = "Ebelling Treadmill Test"
       self.Ebelling.grid(row=0, column=0)

       self.EbellingWU = tk.Label(self)
       self.EbellingWU["text"] = "Warm Up Speed"
       self.EbellingWU.grid(row=1, column=0)

       self.EbellingWU = tk.Text(self)
       self.EbellingWU["height"] = 1
       self.EbellingWU["width"] = 5
       self.EbellingWU.grid(row=1, column=1)

       self.EbellingWork = tk.Label(self)
       self.EbellingWork["text"] = "Workload Speed"
       self.EbellingWork.grid(row=2, column=0)

       self.EbellingWork = tk.Text(self)
       self.EbellingWork["height"] = 1
       self.EbellingWork["width"] = 5
       self.EbellingWork.grid(row=2, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)
