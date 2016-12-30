import tkinter as tk

class FlexTests(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SitReach = tk.Label(self)
       self.SitReach["text"] = "Sit & Reach"
       self.SitReach.grid(row=0, column=0)

       self.SitReachDist = tk.Label(self)
       self.SitReachDist["text"] = "Max Distance (cm): "
       self.SitReachDist.grid(row=1, column=0)

       self.SitReachDist = tk.Text(self)
       self.SitReachDist["height"] = 1
       self.SitReachDist["width"] = 5
       self.SitReachDist.grid(row=1, column=1)

       self.NextG = tk.Button(self)
       self.NextG["text"] = "Next"
       self.NextG["fg"] = "black"
       self.NextG["command"] = lambda: controller.next_page()
       self.NextG.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitG = tk.Button(self)
       self.QuitG["text"] = "Quit"
       self.QuitG["fg"] = "black"
       self.QuitG["command"] = lambda: controller.show_frame("MainPage")
       self.QuitG.grid(row=2, column=2)