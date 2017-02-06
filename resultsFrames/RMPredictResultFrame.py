import tkinter as tk

class RMPredictResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.RMPredictResultLabel = tk.Label(self)
        self.RMPredictResultLabel["text"] = "1RM Predicted"
        self.RMPredictResultLabel.grid(row=0, column=0)

        self.RMPredictExLabel = tk.Label(self)
        self.RMPredictExLabel["text"] = ("Exercise: " + person.RMPredictEx)
        self.RMPredictExLabel.grid(row=1, column=0)

        self.RMPredictWeightLabel = tk.Label(self)
        self.RMPredictWeightLabel["text"] = ("1 Rep Max: " + str(person.getRepMaxPredict()))
        self.RMPredictWeightLabel.grid(row=2, column=0)
