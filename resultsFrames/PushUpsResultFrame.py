import tkinter as tk

class PushUpsResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.PushUpLabel = tk.Label(self)
        self.PushUpLabel["text"] = "Push Ups"
        self.PushUpLabel.grid(row=0, column=0)

        self.PushUpNumLabel = tk.Label(self)
        self.PushUpNumLabel["text"] = ("Number: " + person.pushUpNum)
        self.PushUpNumLabel.grid(row=1, column=0)
