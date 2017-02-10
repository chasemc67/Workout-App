import tkinter as tk

class EbbelingResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1

        self.EbbelingCapacityLabel = tk.Label(self)
        #self.EbbelingCapacityLabel["text"] = ("Test: Ebbeling Treadmill Test VO2max(ml/kg/min): " + str(person.getEbellingAerobic()))
        self.EbbelingCapacityLabel["text"] = ("Test: Ebbeling Treadmill Test VO2max(ml/kg/min): " + "100")
        self.EbbelingCapacityLabel.grid(row=0, column=0)
        self.row += 1
