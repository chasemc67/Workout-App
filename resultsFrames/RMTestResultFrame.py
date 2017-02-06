import tkinter as tk

class RMTestResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person
        self.row = 1

        self.RMTestResultLabel = tk.Label(self)
        self.RMTestResultLabel["text"] = "1RM Test"
        self.RMTestResultLabel.grid(row=0, column=1)

        if (person.RMTestExA != "\n" and person.RMTestExAWeight != "\n"):
            self.RMTestExALabel = tk.Label(self)
            self.RMTestExALabel["text"] = ("Exercise: " + person.RMTestExA)
            self.RMTestExALabel.grid(row=self.row, column=0)

            self.RMTestExAWeightLabel = tk.Label(self)
            self.RMTestExAWeightLabel["text"] = ("1 Rep Max: " + person.RMTestExAWeight)
            self.RMTestExAWeightLabel.grid(row=self.row, column=1)

            self.row += 1

        if (person.RMTestExB != "\n" and person.RMTestExBWeight != "\n"):
            self.RMTestExBLabel = tk.Label(self)
            self.RMTestExBLabel["text"] = ("Exercise: " + person.RMTestExB)
            self.RMTestExBLabel.grid(row=self.row, column=0)

            self.RMTestExBWeightLabel = tk.Label(self)
            self.RMTestExBWeightLabel["text"] = ("1 Rep Max: " + person.RMTestExBWeight)
            self.RMTestExBWeightLabel.grid(row=self.row, column=1)

            self.row += 1
