import tkinter as tk

class FlexResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1

        self.SitReachLabel = tk.Label(self)
        self.SitReachLabel["text"] = "Sit and Reach"
        self.SitReachLabel.grid(row=0, column=0)

        self.SitReachResult = tk.Label(self)
        self.SitReachResult["text"] = ("Max. Distance(cm): " + person.sitReachDist)
        self.SitReachResult.grid(row=self.row, column=0)
        self.row += 1
