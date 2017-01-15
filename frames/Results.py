import tkinter as tk   # python3

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class Results(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Results = tk.Label(self)
       self.Results["text"] = "Results"
       self.Results.pack()


       self.person = self.controller.person

   def showBMIresult(self):
       self.BMIresult = tk.Label(self)
       self.BMIresult["text"] = "BMI: "
       self.BMIresult.pack()

   def showCircumferenceResult(self, person):

       if person.hipCirc != "\n":
        self.hipCircLabel = tk.Label(self)
        self.hipCircLabel["text"] = "Hip Circumference(cm): "
        self.hipCircLabel.pack()
        self.hipCircValue = tk.Label(self)
        self.hipCircValue["text"] = person.hipCirc
        self.hipCircValue.pack()

       if person.waistCirc != "\n":
        self.waistCircLabel = tk.Label(self)
        self.waistCircLabel["text"] = "Waist Circumference(cm): "
        self.waistCircLabel.pack()

       if person.armCirc != "\n":
        self.armCircLabel = tk.Label(self)
        self.armCircLabel["text"] = "Arm Circumference(cm): "
        self.armCircLabel.pack()

       if person.thighCirc != "\n":
        self.thighCircLabel = tk.Label(self)
        self.thighCircLabel["text"] = "Thigh Circumference(cm): "
        self.thighCircLabel.pack()

       if person.chestCirc != "\n":
        self.chestCircLabel = tk.Label(self)
        self.chestCircLabel["text"] = "Chest Circumference(cm): "
        self.chestCircLabel.pack()

   def showThreeSiteSkinfoldResult(self, person):
      if (person.suprailiac != "\n" and person.tricep != "\n" and person.femaleThigh != "\n"):
       self.threeSiteBDMaleLabel = tk.Label(self)
       self.threeSiteBDMaleLabel["text"] = "Body Density: "
       self.threeSiteBDMaleLabel.pack()

       self.threeSiteBFMaleLabel = tk.Label(self)
       self.threeSiteBFMaleLabel["text"] = "Body Fat %: "
       self.threeSiteBFMaleLabel.pack()

      if (person.chest != "\n" and person.ab != "\n" and person.maleThigh != "\n"):
        self.threeSiteBDFemaleLabel = tk.Label(self)
        self.threeSiteBDFemaleLabel["text"] = "Body Density: "
        self.threeSiteBDFemaleLabel.pack()

        self.threeSiteBFFemaleLabel = tk.Label(self)
        self.threeSiteBFFemaleLabel["text"] = "Body Fat %: "
        self.threeSiteBFFemaleLabel.pack()

   def showSvnSiteSkinfoldResult(self, person):
       self.SvnSiteBDLabel = tk.Label(self)
       self.SvnSiteBDLabel["text"] = "Body Density: "
       self.SvnSiteBDLabel.pack()

       self.SvnSiteBFLabel = tk.Label(self)
       self.SvnSiteBFLabel["text"] = "Body Fat %: "
       self.SvnSiteBFLabel.pack()

   def showModAstResult(self, person):
       self.ModAstCapacityLabel = tk.Label(self)
       self.ModAstCapacityLabel["text"] = "Test: Modified Astrand Cycle Test VO2max(ml/kg/min): "
       self.ModAstCapacityLabel.pack()

   def showEbbelingResult(self, person):
       self.EbbelingCapacityLabel = tk.Label(self)
       self.EbbelingCapacityLabel["text"] = "Test: Ebbeling Treadmill Test VO2max(ml/kg/min): "
       self.EbbelingCapacityLabel.pack()

   def showRockportResult(self, person):
       self.RockportCapacityLabel = tk.Label(self)
       self.RockportCapacityLabel["text"] = "Test: Rockport 1 Mile Walk VO2max(ml/kg/min): "
       self.RockportCapacityLabel.pack()

   def showCoopersResult(self, person):
       self.CoopersCapacityLabel = tk.Label(self)
       self.CoopersCapacityLabel["text"] = "Test: Coopers Run Test VO2max(ml/kg/min): "
       self.CoopersCapacityLabel.pack()

   def showMBTossResult(self, person):
       self.MBTossLabel = tk.Label(self)
       self.MBTossLabel["text"] = "Med. Ball Toss"
       self.MBTossLabel.pack()

       self.MBTossDistLabel = tk.Label(self)
       self.MBTossDistLabel["text"] = "Throw Distance(cm): "
       self.MBTossDistLabel.pack()

   def showVertJumpResult(self, person):
        self.vertJumpLabel = tk.Label(self)
        self.vertJumpLabel["text"] = "Vertical Jump"
        self.vertJumpLabel.pack()

        self.vertJumpReachLabel = tk.Label(self)
        self.vertJumpReachLabel['text'] = ("Reach: " + self.person.vertReach)
        self.vertJumpReachLabel.pack()

        self.vertJumpCalcOutputLabel = tk.Label(self)
        self.vertJumpCalcOutputLabel['text'] = "Calc output: " + str(person.getVertJump())
        self.vertJumpCalcOutputLabel.pack()

        self.vertJumpPowerLabel = tk.Label(self)
        self.vertJumpPowerLabel["text"] = "Peak Power(W): "
        self.vertJumpPowerLabel.pack()



   def loadData(self, person):
       if (person.vertJump != "\n" and person.vertReach != "\n"):
        self.showVertJumpResult()

       if (person.height != "\n" and person.weight != "\n"):
        self.showBMIresult()

       if 1==1: # change self.person.height and weight
        self.showCircumferenceResult(person)

       if 1==1:
        self.showThreeSiteSkinfoldResult(person)

       if 1==1:
        self.showSvnSiteSkinfoldResult(person)

       if 1==1:
        self.showModAstResult(person)

       if 1==1:
        self.showEbbelingResult(person)

       if 1==1:
        self.showRockportResult(person)

       if 1==1:
        self.showCoopersResult(person)

       if 1==1:
        self.showMBTossResult(person)





       self.Back = BackButton(self, self.controller)
       self.Back.pack()

       self.Quit = QuitButton(self, self.controller)
       self.Quit.pack()

   def saveData(self, person):
       person.PushUpNum = self.PushUpNumText.get(1.0, tk.END)

