import tkinter as tk

class HipHingeResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1

        self.hipHingeLabel = tk.Label(self)
        self.hipHingeLabel["text"] = "Hip Hinge Assessment"
        self.hipHingeLabel.grid(row=0, column=0)

        self.hipHingeRatingLabel = tk.Label(self)
        self.hipHingeRatingLabel["text"] = ("Rating: " + person.hipHingeRate)
        self.hipHingeRatingLabel.grid(row=self.row, column=0)

        self.row += 1
