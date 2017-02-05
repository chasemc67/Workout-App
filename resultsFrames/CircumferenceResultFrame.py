import tkinter as tk

class CircumferenceResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1
        self.circumferenceResult = tk.Label(self)
        self.circumferenceResult["text"] = ("Circumferences: ")
        self.circumferenceResult.grid(row=0, column=0)

        if person.hipCirc != "":
            self.hipCircLabel = tk.Label(self)
            self.hipCircLabel["text"] = ("Hip Circumference(cm): " + person.hipCirc)
            self.hipCircLabel.grid(row=self.row, column=0)
            self.row += 1

        if person.waistCirc != "":
            self.waistCircLabel = tk.Label(self)
            self.waistCircLabel["text"] = ("Waist Circumference(cm): " + person.waistCirc)
            self.waistCircLabel.grid(row=self.row, column=0)
            self.row += 1

        if person.armCirc != "":
            self.armCircLabel = tk.Label(self)
            self.armCircLabel["text"] = ("Arm Circumference(cm): " + person.armCirc)
            self.armCircLabel.grid(row=self.row, column =0)
            self.row += 1

        if person.thighCirc != "":
            self.thighCircLabel = tk.Label(self)
            self.thighCircLabel["text"] = ("Thigh Circumference(cm): " + person.thighCirc)
            self.thighCircLabel.grid(row=self.row, column=0)
            self.row += 1

        if person.chestCirc != "":
            self.chestCircLabel = tk.Label(self)
            self.chestCircLabel["text"] = ("Chest Circumference(cm): " + person.chestCirc)
            self.chestCircLabel.grid(row=self.row, column=0)
            self.row += 1
