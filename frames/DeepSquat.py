import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class DeepSquat(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.DeepSquat = tk.Label(self)
       self.DeepSquat["text"] = "Deep Squat"
       self.DeepSquat.grid(row=0, column=0)

       self.DeepSquatRate = tk.Label(self)
       self.DeepSquatRate["text"] = "Rating(0-3): "
       self.DeepSquatRate.grid(row=1, column=0)

       self.DeepSquatRate = tk.Text(self)
       self.DeepSquatRate["height"] = 1
       self.DeepSquatRate["width"] = 5
       self.DeepSquatRate.grid(row=1, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=2, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=2, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=2, column=2)