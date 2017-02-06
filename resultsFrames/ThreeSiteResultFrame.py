import tkinter as tk

class ThreeSiteResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1

        if (person.threeSiteFemaleSupra != "\n" and person.threeSiteFemaleTricep != "\n" and person.threeSiteFemaleThigh != "\n"):
            self.threeSiteBDMaleLabel = tk.Label(self)
            #self.threeSiteBDMaleLabel["text"] = ("Body Density: " + str(person.getThreeSiteMale()))
            self.threeSiteBDMaleLabel["text"] = ("Body Density: " + "100" )
            self.threeSiteBDMaleLabel.grid(row=self.row, column=0)

            self.row += 1

            self.threeSiteBFMaleLabel = tk.Label(self)
            #self.threeSiteBFMaleLabel["text"] = ("Body Fat %: " + str(person.getBodyFatThreeMale()))
            self.threeSiteBFMaleLabel["text"] = ("Body Fat %: " + "100")
            self.threeSiteBFMaleLabel.grid(row=self.row, column=0)

            self.row += 1

        if (person.threeSiteMaleChest != "\n" and person.threeSiteMaleAb != "\n" and person.threeSiteMaleThigh != "\n"):
            self.threeSiteBDFemaleLabel = tk.Label(self)
            #self.threeSiteBDFemaleLabel["text"] = ("Body Density: " + str(person.getThreeSiteFemale()))
            self.threeSiteBDFemaleLabel["text"] = ("Body Density: " + "100")
            self.threeSiteBDFemaleLabel.grid(row=self.row, column=0)

            self.row += 1

            self.threeSiteBFFemaleLabel = tk.Label(self)
            #self.threeSiteBFFemaleLabel["text"] = ("Body Fat %: " + str(person.getBodyFatThreeFemale()))
            self.threeSiteBFFemaleLabel["text"] = ("Body Fat %: " + "100")
            self.threeSiteBFFemaleLabel.grid(row=self.row, column=0)

            self.row += 1
