import tkinter as tk

class Rockport(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Rockport = tk.Label(self)
       self.Rockport["text"] = "Rockport 1-Mile Walk"
       self.Rockport.grid(row=0, column=0)

       self.RockportHR = tk.Label(self)
       self.RockportHR["text"] = "Post Test HR: "
       self.RockportHR.grid(row=1, column=0)

       self.RockportHR = tk.Text(self)
       self.RockportHR["height"] = 1
       self.RockportHR["width"] = 5
       self.RockportHR.grid(row=1, column=1)

       self.RockportTime = tk.Label(self)
       self.RockportTime["text"] = "Time(min): "
       self.RockportTime.grid(row=2, column=0)

       self.RockportTime = tk.Text(self)
       self.RockportTime["height"] = 1
       self.RockportTime["width"] = 5
       self.RockportTime.grid(row=2, column=1)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=3, column=2)