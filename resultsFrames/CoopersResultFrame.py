import tkinter as tk

class CoopersResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1
        self.CoopersCapacityLabel = tk.Label(self)
        self.CoopersCapacityLabel["text"] = ("Test: Coopers Run Test VO2max(ml/kg/min): " + str(person.getCooperAerobic()))
        self.CoopersCapacityLabel.grid(row=self.row, column=0)
        self.row += 1
