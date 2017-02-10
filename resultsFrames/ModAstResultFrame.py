import tkinter as tk

class ModAstResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1

        self.ModAstCapacityLabel = tk.Label(self)
        self.ModAstCapacityLabel["text"] = ("Test: Modified Astrand Cycle Test VO2max(ml/kg/min): " + person.modAstAerobic)
        self.ModAstCapacityLabel.grid(row=0, column=0)
