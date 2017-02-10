import tkinter as tk

class DeepSquatResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row=1
        self.deepSquatAssessLabel = tk.Label(self)
        self.deepSquatAssessLabel["text"] = "Deep Squat Assessment"
        self.deepSquatAssessLabel.grid(row=0, column=0)

        self.deepSquatRatingLabel = tk.Label(self)
        self.deepSquatRatingLabel["text"] = ("Rating: " + person.deepSquatRate)
        self.deepSquatRatingLabel.grid(row=self.row, column=0)
        self.row += 1
