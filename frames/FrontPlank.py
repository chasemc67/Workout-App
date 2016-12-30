import tkinter as tk

class FrontPlank(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.FrPlank = tk.Label(self)
       self.FrPlank["text"] = "Front Plank"
       self.FrPlank.grid(row=0, column=0)

       self.FrPlankRate = tk.Label(self)
       self.FrPlankRate["text"] = "Rating(0-3): "
       self.FrPlankRate.grid(row=1, column=0)

       self.FrPlankRate = tk.Text(self)
       self.FrPlankRate["height"] = 1
       self.FrPlankRate["width"] = 5
       self.FrPlankRate.grid(row=1, column=1)

       self.NextH = tk.Button(self)
       self.NextH["text"] = "Next"
       self.NextH["fg"] = "black"
       self.NextH["command"] = lambda: controller.next_page()
       self.NextH.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitH = tk.Button(self)
       self.QuitH["text"] = "Quit"
       self.QuitH["fg"] = "black"
       self.QuitH["command"] = lambda: controller.show_frame("MainPage")
       self.QuitH.grid(row=2, column=2)