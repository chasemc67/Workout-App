import tkinter as tk

class VertJumpResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.vertJumpLabel = tk.Label(self)
        self.vertJumpLabel["text"] = "Vertical Jump"
        self.vertJumpLabel.grid(row=0, column=0)

        self.vertJumpReachLabel = tk.Label(self)
        self.vertJumpReachLabel['text'] = ("Reach: " + person.vertJumpSR)
        self.vertJumpReachLabel.grid(row=1, column=0)

        self.vertJumpCalcOutputLabel = tk.Label(self)
        #self.vertJumpCalcOutputLabel['text'] = "Calc. output: " + str(person.getVertJumpBest())
        self.vertJumpCalcOutputLabel["text"] = ("Calc. Output: " + "100")
        self.vertJumpCalcOutputLabel.grid(row=2, column=0)

        self.vertJumpPowerLabel = tk.Label(self)
        #self.vertJumpPowerLabel["text"] = ("Peak Power(W):" + str(person.getVertJumpPower()))
        self.vertJumpPowerLabel["text"] = ("Peak Power(W): " + "100")
        self.vertJumpPowerLabel.grid(row=3, column=0)
