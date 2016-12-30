import tkinter as tk

class BMIframe(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.BMIresult = tk.Label(self)
       self.BMIresult["text"] = "BMI"
       self.BMIresult.grid(row=1, column=0)

       self.BMIresult = tk.Text(self)
       self.BMIresult["height"] = 1
       self.BMIresult["width"] = 5
       self.BMIresult.grid(row=1, column=1)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=2, column=2)