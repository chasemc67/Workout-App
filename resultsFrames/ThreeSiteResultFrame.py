import tkinter as tk

class ThreeSiteResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        person = self.controller.person

        self.row = 1

        if (person.threeSiteFemaleSupra.strip() != "" and person.threeSiteFemaleTricep.strip() != "" and person.threeSiteFemaleThigh.strip() != ""):
            self.threeSiteBDMaleLabel = tk.Label(self)
            self.threeSiteBDMaleLabel["text"] = ("Body Density: " + str(person.getThreeSiteMale()))
            self.threeSiteBDMaleLabel.grid(row=self.row, column=0)

            self.row += 1

            self.threeSiteBFMaleLabel = tk.Label(self)
            self.threeSiteBFMaleLabel["text"] = ("Body Fat %: " + str(person.getBodyFatThreeMale()))
            self.threeSiteBFMaleLabel.grid(row=self.row, column=0)

            self.row += 1

        if (person.threeSiteMaleChest.strip() != "" and person.threeSiteMaleAb.strip() != "" and person.threeSiteMaleThigh.strip() != ""):
            self.threeSiteBDFemaleLabel = tk.Label(self)
            self.threeSiteBDFemaleLabel["text"] = ("Body Density: " + str(person.getThreeSiteFemale()))
            self.threeSiteBDFemaleLabel.grid(row=self.row, column=0)

            self.row += 1

            self.threeSiteBFFemaleLabel = tk.Label(self)
            self.threeSiteBFFemaleLabel["text"] = ("Body Fat %: " + str(person.getBodyFatThreeFemale()))
            self.threeSiteBFFemaleLabel.grid(row=self.row, column=0)

            self.row += 1
