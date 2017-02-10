import tkinter as tk

class SvnSiteResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.SvnSiteBDLabel = tk.Label(self)
        #self.SvnSiteBDLabel["text"] = ("Body Density: " + str(person.getSevenSiteDensity()))
        self.SvnSiteBDLabel["text"] = ("Body Density: " + "100")
        self.SvnSiteBDLabel.grid(row=0, column=0)

        self.SvnSiteBFLabel = tk.Label(self)
        #self.SvnSiteBFLabel["text"] = ("Body Fat %: " + str(person.getBodyFatSeven()))
        self.SvnSiteBFLabel["text"] = ("Body Fat %: " + "100")
        self.SvnSiteBFLabel.grid(row=1, column=0)
