import tkinter as tk

class GripStrengthResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1

        self.GripStrengthLabel = tk.Label(self)
        self.GripStrengthLabel["text"] = "Grip Strength"
        self.GripStrengthLabel.grid(row=0, column=0)

        self.GripStrengthLeftLabel = tk.Label(self)
        self.GripStrengthLeftLabel["text"] = ("Left Hand(kg): " + person.gripStrengthLeft)
        self.GripStrengthLeftLabel.grid(row=self.row, column=0)

        self.GripStrengthRightLabel = tk.Label(self)
        self.GripStrengthRightLabel["text"] = ("Right Hand(kg): " + person.gripStrengthRight)
        self.GripStrengthRightLabel.grid(row=self.row, column=1)
        self.row += 1
