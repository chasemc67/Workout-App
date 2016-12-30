import tkinter as tk

class ModAst(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ModAst = tk.Label(self)
       self.ModAst["text"] = "Modified Astrand"
       self.ModAst.grid(row=1, column=0)

       self.ModAstLoadA = tk.Label(self)
       self.ModAstLoadA["text"] = "Warm-Up Load(kp): "
       self.ModAstLoadA.grid(row=2, column=0)

       self.ModAstLoadA = tk.Text(self)
       self.ModAstLoadA["height"] = 1
       self.ModAstLoadA["width"] = 5
       self.ModAstLoadA.grid(row=2, column =1)

       self.ModAstLoadB = tk.Label(self)
       self.ModAstLoadB["text"] = "Work Load(kp): "
       self.ModAstLoadB.grid(row=3, column=0)

       self.ModAstLoadB = tk.Text(self)
       self.ModAstLoadB["height"] = 1
       self.ModAstLoadB["width"] = 5
       self.ModAstLoadB.grid(row=3, column=1)

       self.ModAstHR = tk.Label(self)
       self.ModAstHR["text"] = "Average HR(bpm): "
       self.ModAstHR.grid(row=3, column=2)

       self.ModAstHR = tk.Text(self)
       self.ModAstHR["height"] = 1
       self.ModAstHR["width"] = 5
       self.ModAstHR.grid(row=3, column=3)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=4, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=4, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=4, column=2)