import tkinter as tk

class RMtest(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.RepMaxTest = tk.Label(self)
       self.RepMaxTest["text"] = "1 Rep Max.(Tested)"
       self.RepMaxTest.grid(row=0, column=0)

       self.RMTestExA = tk.Label(self)
       self.RMTestExA["text"] = "Exercise: "
       self.RMTestExA.grid(row=1, column=0)

       self.RMTestExA = tk.Text(self)
       self.RMTestExA["height"] = 1
       self.RMTestExA["width"] = 5
       self.RMTestExA.grid(row=1, column=1)

       self.RMTestExAWeight = tk.Label(self)
       self.RMTestExAWeight["text"] = "1RM(kg): "
       self.RMTestExAWeight.grid(row=1, column=2)

       self.RMTestExAWeight = tk.Text(self)
       self.RMTestExAWeight["height"] = 1
       self.RMTestExAWeight["width"] = 5
       self.RMTestExAWeight.grid(row=1, column=3)

       self.RMTestExB = tk.Label(self)
       self.RMTestExB["text"] = "Exercise: "
       self.RMTestExB.grid(row=2, column=0)

       self.RMTestExB = tk.Text(self)
       self.RMTestExB["height"] = 1
       self.RMTestExB["width"] = 5
       self.RMTestExB.grid(row=2, column=1)

       self.RMTestExBWeight = tk.Label(self)
       self.RMTestExBWeight["text"] = "1RM(kg): "
       self.RMTestExBWeight.grid(row=2, column=2)

       self.RMTestExBWeight = tk.Text(self)
       self.RMTestExBWeight["height"] = 1
       self.RMTestExBWeight["width"] = 5
       self.RMTestExBWeight.grid(row=2, column=3)

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