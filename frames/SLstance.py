import tkinter as tk

class SLstance(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SLStance = tk.Label(self)
       self.SLStance["text"] = "Single Leg Stance Test"
       self.SLStance.grid(row=0, column=0)

       self.SLOpenLeft = tk.Label(self)
       self.SLOpenLeft["text"] = "Eyes Open Left(sec.): "
       self.SLOpenLeft.grid(row=1, column=0)

       self.SLOpenLeft = tk.Text(self)
       self.SLOpenLeft["height"] = 1
       self.SLOpenLeft["width"] = 5
       self.SLOpenLeft.grid(row=1, column=1)

       self.SLOpenRight = tk.Label(self)
       self.SLOpenRight["text"] = "Eyes Open Right(sec.): "
       self.SLOpenRight.grid(row=1, column=2)

       self.SLOpenRight = tk.Text(self)
       self.SLOpenRight["height"] = 1
       self.SLOpenRight["width"] = 5
       self.SLOpenRight.grid(row=1, column=3)

       self.SLCloseLeft = tk.Label(self)
       self.SLCloseLeft["text"] = "Eyes Closed Left(sec.): "
       self.SLCloseLeft.grid(row=2, column=0)

       self.SLCloseLeft = tk.Text(self)
       self.SLCloseLeft["height"] = 1
       self.SLCloseLeft["width"] = 5
       self.SLCloseLeft.grid(row=2, column=1)

       self.SLCloseRight = tk.Label(self)
       self.SLCloseRight["text"] = "Eyes Closed Right(sec.): "
       self.SLCloseRight.grid(row=2, column=2)

       self.SLCloseRight = tk.Text(self)
       self.SLCloseRight["height"] = 1
       self.SLCloseRight["width"] = 5
       self.SLCloseRight.grid(row=2, column=3)

       self.NextH = tk.Button(self)
       self.NextH["text"] = "Next"
       self.NextH["fg"] = "black"
       self.NextH["command"] = lambda: controller.next_page()
       self.NextH.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitH = tk.Button(self)
       self.QuitH["text"] = "Quit"
       self.QuitH["fg"] = "black"
       self.QuitH["command"] = lambda: controller.show_frame("MainPage")
       self.QuitH.grid(row=3, column=2)