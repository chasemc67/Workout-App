import tkinter as tk

class FrontPlankResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.plankAssessLabel = tk.Label(self)
        self.plankAssessLabel["text"] = "Front Plank Assessment"
        self.plankAssessLabel.grid(row=0, column=0)

        self.plankRatingLabel = tk.Label(self)
        self.plankRatingLabel["text"] = ("Rating: " + person.frontPlankRate)
        self.plankRatingLabel.grid(row= 1, column=0)

