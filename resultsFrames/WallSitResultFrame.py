import tkinter as tk

class WallSitResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.WallSitLabel = tk.Label(self)
        self.WallSitLabel["text"] = "Wall Sit"
        self.WallSitLabel.grid(row=0, column=0)

        self.WallSitTime = tk.Label(self)
        self.WallSitTime["text"] = ("Time(sec.): " + person.wallSitTime)
        self.WallSitTime.grid(row=1, column=0)
