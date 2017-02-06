import tkinter as tk

class SLStanceResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.SLStanceLabel = tk.Label(self)
        self.SLStanceLabel["text"] = "Single Leg Stance Test"
        self.SLStanceLabel.grid(row=0, column=0)

        self.SLStanceLeftOpen = tk.Label(self)
        self.SLStanceLeftOpen["text"] = ("Left Leg Eyes Open Time(sec.): " + person.SLOpenLeft)
        self.SLStanceLeftOpen.grid(row=1, column=0)

        self.SLStanceRightOpen = tk.Label(self)
        self.SLStanceRightOpen["text"] = ("Right Leg Eyes Open Time(sec.): " + person.SLOpenRight)
        self.SLStanceRightOpen.grid(row=1, column=1)

        self.SLStanceLeftClosed = tk.Label(self)
        self.SLStanceLeftClosed["text"] = ("Left Leg Eyes Closed Time(sec.): " + person.SLCloseLeft)
        self.SLStanceLeftClosed.grid(row=2, column=0)

        self.SLStanceRightClosed = tk.Label(self)
        self.SLStanceRightClosed["text"] = ("Right Leg Eyes Closed Time(sec.): " + person.SLCloseRight)
        self.SLStanceRightClosed.grid(row=2, column=1)
