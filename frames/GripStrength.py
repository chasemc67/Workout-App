import tkinter as tk

class GripStrength(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.GripStr = tk.Label(self)
       self.GripStr["text"] = "Grip Strength"
       self.GripStr.grid(row=0, column=0)

       self.GripStrLeft = tk.Label(self)
       self.GripStrLeft["text"] = "Max. Left Hand(kg): "
       self.GripStrLeft.grid(row=1, column=0)

       self.GripStrLeft = tk.Text(self)
       self.GripStrLeft["height"] = 1
       self.GripStrLeft["width"] = 5
       self.GripStrLeft.grid(row=1, column=1)

       self.GripStrRight = tk.Label(self)
       self.GripStrRight["text"] = "Max. Right Hand(kg): "
       self.GripStrRight.grid(row=2, column=0)

       self.GripStrRight = tk.Text(self)
       self.GripStrRight["height"] = 1
       self.GripStrRight["width"] = 5
       self.GripStrRight.grid(row=2, column=1)

       self.NextD = tk.Button(self)
       self.NextD["text"] = "Next"
       self.NextD["fg"] = "black"
       self.NextD["command"] = lambda: controller.next_page()
       self.NextD.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitD = tk.Button(self)
       self.QuitD["text"] = "Quit"
       self.QuitD["fg"] = "black"
       self.QuitD["command"] = lambda: controller.show_frame("MainPage")
       self.QuitD.grid(row=3, column=2)