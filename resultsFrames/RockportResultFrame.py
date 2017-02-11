import tkinter as tk

class RockportResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.RockportCapacityLabel = tk.Label(self)
        #self.RockportCapacityLabel["text"] = ("Rockport 1 Mile Walk VO2max(ml/kg/min): " + str(person.getRockportAerobic()))
        self.RockportCapacityLabel["text"] = ("Rockport 1 Mile Walk VO2max(ml/kg/min): " + "100")
        self.RockportCapacityLabel.grid(row=0, column=0)
