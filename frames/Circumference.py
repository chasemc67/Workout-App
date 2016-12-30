import tkinter as tk

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

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=6, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=6, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=6, column=2)