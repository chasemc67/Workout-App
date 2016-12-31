import tkinter as tk
from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class Circumference(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self,parent)
       self.controller = controller

       self.Circumference = tk.Label(self)
       self.Circumference["text"] = "Circumferences"
       self.Circumference.grid(row=0, column=0)

       self.HipCirc = tk.Label(self)
       self.HipCirc["text"] = "Hip(cm): "
       self.HipCirc.grid(row=1, column=0)

       self.HipCirc = tk.Text(self)
       self.HipCirc["height"] = 1
       self.HipCirc["width"] = 5
       self.HipCirc.grid(row=1, column=1)

       self.WaistCirc = tk.Label(self)
       self.WaistCirc["text"] = "Waist(cm): "
       self.WaistCirc.grid(row=2, column=0)

       self.WaistCirc = tk.Text(self)
       self.WaistCirc["height"] = 1
       self.WaistCirc["width"] = 5
       self.WaistCirc.grid(row=2, column=1)

       self.ArmCirc = tk.Label(self)
       self.ArmCirc["text"] = "Arm(cm): "
       self.ArmCirc.grid(row=3, column=0)

       self.ArmCirc = tk.Text(self)
       self.ArmCirc["height"] = 1
       self.ArmCirc["width"] = 5
       self.ArmCirc.grid(row=3, column=1)

       self.ThighCirc = tk.Label(self)
       self.ThighCirc["text"] = "Thigh(cm): "
       self.ThighCirc.grid(row=4, column=0)

       self.ThighCirc = tk.Text(self)
       self.ThighCirc["height"] = 1
       self.ThighCirc["width"] = 5
       self.ThighCirc.grid(row=4, column=1)

       self.ChestCirc = tk.Label(self)
       self.ChestCirc["text"] = "Chest(cm): "
       self.ChestCirc.grid(row=5, column=0)

       self.ChestCirc = tk.Text(self)
       self.ChestCirc["height"] = 1
       self.ChestCirc["width"] = 5
       self.ChestCirc.grid(row=5, column=1)

       self.Next = NextButton(self, controller)
       self.Next.grid(row=6, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=6, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=6, column=2)
