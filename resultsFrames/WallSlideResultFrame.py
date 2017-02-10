import tkinter as tk

class WallSlideResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.wallSlideLabel = tk.Label(self)
        self.wallSlideLabel["text"] = "Wall Slide Assessment"
        self.wallSlideLabel.grid(row=0, column=0)

        self.wallSlideRatingLabel = tk.Label(self)
        self.wallSlideRatingLabel["text"] = ("Rating: " + person.wallSlideRate)
        self.wallSlideRatingLabel.grid(row=1, column=0)
