import tkinter as tk

class Coopers(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Cooper = tk.Label(self)
       self.Cooper["text"] = "Coopers Run"
       self.Cooper.grid(row=0, column=0)

       self.CooperDist = tk.Label(self)
       self.CooperDist["text"] = "Distance(miles): "
       self.CooperDist.grid(row=1, column=0)

       self.CooperDist = tk.Text(self)
       self.CooperDist["height"] = 1
       self.CooperDist["width"] = 5
       self.CooperDist.grid(row=1, column=1)

       self.NextC = tk.Button(self)
       self.NextC["text"] = "Next"
       self.NextC["fg"] = "black"
       self.NextC["command"] = lambda: controller.next_page()
       self.NextC.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitC = tk.Button(self)
       self.QuitC["text"] = "Quit"
       self.QuitC["fg"] = "black"
       self.QuitC["command"] = lambda: controller.show_frame("MainPage")
       self.QuitC.grid(row=2, column=1)