import tkinter as tk

class BMIResultFrame(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.BMIresult = tk.Label(self)
       self.BMIresult["text"] = ("BMI: " + str(self.controller.person.getBMI()))
       
       self.BMIresult.pack()
