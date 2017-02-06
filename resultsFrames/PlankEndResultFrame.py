import tkinter as tk

class PlankEndResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.FrontPlankLabel = tk.Label(self)
        self.FrontPlankLabel["text"] = "Front Plank"
        self.FrontPlankLabel.grid(row=0,column=0)

        self.FrontPlankTime = tk.Label(self)
        self.FrontPlankTime["text"] = ("Time(sec.): " + person.plankTime)
        self.FrontPlankTime.grid(row=1, column=0)
