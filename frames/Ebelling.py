import tkinter as tk

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