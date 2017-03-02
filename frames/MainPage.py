import tkinter as tk
from buttons.NextButton import NextButton
from buttons.QuitButton import QuitButton
from buttons.PlaceholderTextBox import PlaceholderTextBox
import datetime

class MainPage(tk.Frame):

   def focus_next_window(self, event):
      event.widget.tk_focusNext().focus()
      return("break")

   def focus_last_window(self, event):
      event.widget.tk_focusPrev().focus()
      return("break")

   def validateInput(self):
      validationSuccess = True

      if self.nameText.get(1.0, tk.END).strip() != "":
            self.nameText.config(highlightbackground="white")
      else:
            self.nameText.config(highlightbackground="red")
            validationSuccess = False

      try:
            datetime.datetime.strptime(self.testDateText.get(1.0, tk.END).strip(), '%m/%d/%Y')
            self.testDateText.config(highlightbackground="white")
      except Exception as e:
            print(e)
            self.testDateText.config(highlightbackground="red")
            validationSuccess = False
      
      try:
            datetime.datetime.strptime(self.birthDateText.get(1.0, tk.END).strip(), '%m/%d/%Y')
            self.birthDateText.config(highlightbackground="white")
      except:
            self.birthDateText.config(highlightbackground="red")
            validationSuccess = False
      
      try:
            float(self.restHRText.get(1.0, tk.END).strip())
            self.restHRText.config(highlightbackground="white")
      except:
            self.restHRText.config(highlightbackground="red")
            validationSuccess = False
      
      try:
            float(self.restBPText.get(1.0, tk.END).strip())
            self.restBPText.config(highlightbackground="white")
      except:
            self.restBPText.config(highlightbackground="red")
            validationSuccess = False
      
      try:
            float(self.heightText.get(1.0, tk.END).strip())
            self.heightText.config(highlightbackground="white")
      except:
            self.heightText.config(highlightbackground="red")
            validationSuccess = False
      
      try:
            float(self.weightText.get(1.0, tk.END).strip())
            self.weightText.config(highlightbackground="white")
      except:
            self.weightText.config(highlightbackground="red")
            validationSuccess = False

      return validationSuccess



   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.labelName = tk.Label(self)
       self.labelName["text"] = "Name: "
       self.labelName.grid(row=0, column=0)

       self.nameText = tk.Text(self)
       self.nameText["height"] = 1
       self.nameText["width"] = 15
       self.nameText.bind("<Tab>", self.focus_next_window)
       self.nameText.bind("<Shift-Tab>", self.focus_last_window)
       self.nameText.grid(row=0, column=1)

       self.labelDateOfTest = tk.Label(self)
       self.labelDateOfTest["text"] = "Date of Test: "
       self.labelDateOfTest.grid(row=0, column=2)

       self.testDateText = PlaceholderTextBox(self, placeholder="mm/dd/yyyy")
       self.testDateText["height"] = 1
       self.testDateText["width"] = 15
       self.testDateText.bind("<Tab>", self.focus_next_window)
       self.testDateText.bind("<Shift-Tab>", self.focus_last_window)
       self.testDateText.grid(row=0, column=3)

       self.labelGender = tk.Label(self)
       self.labelGender["text"] = "Gender: "
       self.labelGender.grid(row=0, column=4)

       self.genderVariable = tk.StringVar(self)
       self.genderVariable.set("Male")
       if self.controller.person.gender.strip() != "":
            self.genderVariable.set(self.controller.person.gender)
       self.genderText = tk.OptionMenu(self, self.genderVariable, "Male", "Female")
       self.genderText["height"] = 1
       self.genderText["width"] = 15
       self.genderText.bind("<Tab>", self.focus_next_window)
       self.genderText.bind("<Shift-Tab>", self.focus_last_window)
       self.genderText.grid(row=0, column=5)

       self.labelDOB = tk.Label(self)
       self.labelDOB["text"] = "Date of Birth: "
       self.labelDOB.grid(row=0, column=6)

       self.birthDateText = PlaceholderTextBox(self, placeholder="mm/dd/yyyy")
       self.birthDateText["height"] = 1
       self.birthDateText["width"] = 15
       self.birthDateText.bind("<Tab>", self.focus_next_window)
       self.birthDateText.bind("<Shift-Tab>", self.focus_last_window)
       self.birthDateText.grid(row=0, column=7)

       self.labelPhoneNumber = tk.Label(self)
       self.labelPhoneNumber["text"] = "Phone Number: "
       self.labelPhoneNumber.grid(row=1, column=0)

       self.phoneNumberText = tk.Text(self)
       self.phoneNumberText["height"] = 1
       self.phoneNumberText["width"] = 15
       self.phoneNumberText.bind("<Tab>", self.focus_next_window)
       self.phoneNumberText.bind("<Shift-Tab>", self.focus_last_window)
       self.phoneNumberText.grid(row=1, column=1)

       self.labelRestHR = tk.Label(self)
       self.labelRestHR["text"] = "Heart Rate: "
       self.labelRestHR.grid(row=1, column=2)

       self.restHRText = tk.Text(self)
       self.restHRText["height"] = 1
       self.restHRText["width"] = 15
       self.restHRText.bind("<Tab>", self.focus_next_window)
       self.restHRText.bind("<Shift-Tab>", self.focus_last_window)
       self.restHRText.grid(row=1, column=3,padx=0, pady=3)

       self.labelRestBP = tk.Label(self)
       self.labelRestBP["text"] = "Blood Pressure "
       self.labelRestBP.grid(row=1, column=4)

       self.restBPText = tk.Text(self)
       self.restBPText["height"] = 1
       self.restBPText["width"] = 15
       self.restBPText.bind("<Tab>", self.focus_next_window)
       self.restBPText.bind("<Shift-Tab>", self.focus_last_window)
       self.restBPText.grid(row=1, column=5)

       self.labelHeight = tk.Label(self)
       self.labelHeight["text"] = "Height (cm): "
       self.labelHeight.grid(row=1, column=6)

       self.heightText = tk.Text(self)
       self.heightText["height"] = 1
       self.heightText["width"] = 15
       self.heightText.bind("<Tab>", self.focus_next_window)
       self.heightText.bind("<Shift-Tab>", self.focus_last_window)
       self.heightText.grid(row=1, column=7)

       self.labelWeight = tk.Label(self)
       self.labelWeight["text"] = "Weight (kg): "
       self.labelWeight.grid(row=2, column=0)

       self.weightText = tk.Text(self)
       self.weightText["height"] = 1
       self.weightText["width"] = 15
       self.weightText.bind("<Tab>", self.focus_next_window)
       self.weightText.bind("<Shift-Tab>", self.focus_last_window)
       self.weightText.grid(row=2, column=1)

       self.labelBodyComp = tk.Label(self)
       self.labelBodyComp["text"] = "Body Composition Assessments: "
       self.labelBodyComp.grid(row=3, column=0)

       self.checkCircumference = tk.Checkbutton(self, text="Circumferences", command = lambda: self.boxChecked("Circumference"))
       self.checkCircumference.grid(row=4, column=0)
       

       self.checkThreeSkinfold = tk.Checkbutton(self, text="3-Site Skinfold", command = lambda: self.boxChecked("ThreeSiteSkinfold"))
       self.checkThreeSkinfold.grid(row=4, column=1)
       

       self.checkSevenSkinfold = tk.Checkbutton(self, text="7-Site Skinfold", command = lambda: self.boxChecked("SvnSiteSkinfold"))
       self.checkSevenSkinfold.grid(row=4, column=2)

       self.labelAerobicTest = tk.Label(self)
       self.labelAerobicTest["text"] = "Maximal/Submaximal VO2 Max Assessments: "
       self.labelAerobicTest.grid(row=5, column=0)

       self.checkModAstrand = tk.Checkbutton(self, text="Modified Astrand Cycle Test", command = lambda: self.boxChecked("ModAst"))
       self.checkModAstrand.grid(row=6, column=0)

       self.checkEbelling = tk.Checkbutton(self, text="Ebbeling Treadmill Test", command = lambda: self.boxChecked("Ebelling"))
       self.checkEbelling.grid(row=6, column=1)

       self.checkRockport = tk.Checkbutton(self, text="Rockport 1 Mile Walk Test", command = lambda: self.boxChecked("Rockport"))
       self.checkRockport.grid(row=6, column=2)

       self.checkCoopers = tk.Checkbutton(self, text="Coopers Run Test", command = lambda: self.boxChecked ("Coopers"))
       self.checkCoopers.grid(row=6, column=3)

       self.labelPower = tk.Label(self)
       self.labelPower["text"] = "Power Tests: "
       self.labelPower.grid(row=7, column=0)

       self.checkMBToss = tk.Checkbutton(self, text="Seated Med. Ball Toss", command = lambda: self.boxChecked("MBtoss"))
       self.checkMBToss.grid(row=8, column=0)

       self.checkVertJump = tk.Checkbutton(self, text="Vertical Jump Test", command = lambda: self.boxChecked("VertJump"))
       self.checkVertJump.grid(row=8, column=1)

       self.labelMaxStrength = tk.Label(self)
       self.labelMaxStrength["text"] = "Max Strength Tests: "
       self.labelMaxStrength.grid(row=9, column=0)

       self.checkRepMaxTest = tk.Checkbutton(self, text="1 Rep Max (Tested)", command = lambda: self.boxChecked("RMtest"))
       self.checkRepMaxTest.grid(row=10, column=0)

       self.checkRepMaxPredict = tk.Checkbutton(self, text="1 Rep Max (Predicted)", command = lambda: self.boxChecked("RMpredict"))
       self.checkRepMaxPredict.grid(row=10, column=1)

       self.checkGripStr = tk.Checkbutton(self, text="Grip Strength", command = lambda: self.boxChecked("GripStrength"))
       self.checkGripStr.grid(row=10, column=2)

       self.labelEndurance = tk.Label(self)
       self.labelEndurance["text"] = "Muscular Endurance Tests: "
       self.labelEndurance.grid(row=11, column=0)

       self.checkPushUp = tk.Checkbutton(self, text="Push Ups", command = lambda: self.boxChecked("PushUps"))
       self.checkPushUp.grid(row=12, column=0)

       self.checkCurlUp = tk.Checkbutton(self, text="10cm Curl Up", command = lambda: self.boxChecked("CurlUps"))
       self.checkCurlUp.grid(row=12, column=1)

       self.checkPlankTime = tk.Checkbutton(self, text="Front Plank", command = lambda: self.boxChecked("PlankEnd"))
       self.checkPlankTime.grid(row=12, column=2)

       self.checkWallSit = tk.Checkbutton(self, text="Wall Sit", command = lambda: self.boxChecked("WallSit"))
       self.checkWallSit.grid(row=12, column=3)

       self.labelFlexibility = tk.Label(self)
       self.labelFlexibility["text"] = "Flexibility Tests: "
       self.labelFlexibility.grid(row=13, column=0)

       self.checkSitReach = tk.Checkbutton(self, text="Sit and Reach", command = lambda: self.boxChecked("FlexTests"))
       self.checkSitReach.grid(row=14, column=0)

       self.labelMobility = tk.Label(self)
       self.labelMobility ["text"] = "Mobility/Movement Screening: "
       self.labelMobility.grid(row=15, column=0)

       self.checkStance = tk.Checkbutton(self, text="Single Leg Stance Test", command = lambda: self.boxChecked("SLstance"))
       self.checkStance.grid(row=16, column=0)

       self.checkSquat = tk.Checkbutton(self, text="Deep Squat Assessment", command = lambda: self.boxChecked("DeepSquat"))
       self.checkSquat.grid(row=16, column=1)

       self.checkWallSlide = tk.Checkbutton(self, text="Wall Slide", command = lambda: self.boxChecked("WallSlide"))
       self.checkWallSlide.grid(row=16, column=2)

       self.checkHipHinge = tk.Checkbutton(self, text="Hip Hinge", command = lambda: self.boxChecked("HipHinge"))
       self.checkHipHinge.grid(row=16, column=3)

       self.checkPlankAssess = tk.Checkbutton(self, text="Front Plank Assessment", command = lambda: self.boxChecked("FrontPlank"))
       self.checkPlankAssess.grid(row=16, column=4)

       self.Next = NextButton(self, self.controller, self.saveData, self.validateInput)
       self.Next.grid(row=17, column=0)

       self.Quit = QuitButton(self, self.controller)
       self.Quit.grid(row=17, column=2)

   def boxChecked(self, text):
       if text in self.controller.person.framesChecked:
           self.controller.person.framesChecked.remove(text)
       else:
           self.controller.person.framesChecked.append(text)


   def loadData(self, person):
       self.nameText.delete(1.0, tk.END)
       self.nameText.insert(tk.END, self.controller.person.name)

       if self.controller.person.testDate.strip() != "":
             self.testDateText.delete(1.0, tk.END)
             self.testDateText.insert(tk.END, self.controller.person.testDate)

       if self.controller.person.birthDate.strip() != "":
            self.birthDateText.delete(1.0, tk.END)
            self.birthDateText.insert(tk.END, self.controller.person.birthDate)

       self.phoneNumberText.delete(1.0, tk.END)
       self.phoneNumberText.insert(tk.END, self.controller.person.phoneNumber)

       self.restHRText.delete(1.0, tk.END)
       self.restHRText.insert(tk.END, self.controller.person.restHR)

       self.restBPText.delete(1.0, tk.END)
       self.restBPText.insert(tk.END, self.controller.person.restBP)

       self.heightText.delete(1.0, tk.END)
       self.heightText.insert(tk.END, self.controller.person.height)

       self.weightText.delete(1.0, tk.END)
       self.weightText.insert(tk.END, self.controller.person.weight)

       if "Circumference" in self.controller.person.framesChecked:
            self.checkCircumference.select()
       if "ThreeSiteSkinfold" in self.controller.person.framesChecked:
            self.checkThreeSkinfold.select()
       if "SvnSiteSkinfold" in self.controller.person.framesChecked:
            self.checkSevenSkinfold.select()
       if "ModAst" in self.controller.person.framesChecked:
            self.checkModAstrand.select()
       if "Ebelling" in self.controller.person.framesChecked:
            self.checkEbelling.select()
       if "Rockport" in self.controller.person.framesChecked:
            self.checkRockport.select()
       if "Coopers" in self.controller.person.framesChecked:
            self.checkCoopers.select()
       if "MBtoss" in self.controller.person.framesChecked:
            self.checkMBToss.select()
       if "VertJump" in self.controller.person.framesChecked:
            self.checkVertJump.select()
       if "RMtest" in self.controller.person.framesChecked:
            self.checkRepMaxTest.select()
       if "RMpredict" in self.controller.person.framesChecked:
            self.checkRepMaxPredict.select()
       if "GripStrength" in self.controller.person.framesChecked:
            self.checkGripStr.select()
       if "PushUps" in self.controller.person.framesChecked:
            self.checkPushUp.select()
       if "CurlUps" in self.controller.person.framesChecked:
            self.checkCurlUp.select()
       if "PlankEnd" in self.controller.person.framesChecked:
            self.checkPlankTime.select()
       if "WallSit" in self.controller.person.framesChecked:
            self.checkWallSit.select()
       if "FlexTests" in self.controller.person.framesChecked:
            self.checkSitReach.select()
       if "SLstance" in self.controller.person.framesChecked:
            self.checkStance.select()
       if "DeepSquat" in self.controller.person.framesChecked:
            self.checkSquat.select()
       if "WallSlide" in self.controller.person.framesChecked:
            self.checkWallSlide.select()
       if "HipHinge" in self.controller.person.framesChecked:
            self.checkHipHinge.select()
       if "FrontPlank" in self.controller.person.framesChecked:
            self.checkPlankAssess.select()


   def saveData(self, person):
       print("Saving new user with name " + str(self.nameText.get(1.0, tk.END)))

       self.controller.person.name = self.nameText.get(1.0, tk.END).strip()
       #self.controller.person.testDate = datetime.strptime(self.testDateText.get(1.0, tk.END).strip(), '%m/%d/%Y')
       self.controller.person.testDate = self.testDateText.get(1.0, tk.END).strip()
       self.controller.person.gender = str(self.genderVariable.get())
       self.controller.person.birthDate = self.birthDateText.get(1.0, tk.END).strip()
       self.controller.person.phoneNumber = self.phoneNumberText.get(1.0, tk.END).strip()
       self.controller.person.restHR = self.restHRText.get(1.0, tk.END).strip()
       self.controller.person.restBP = self.restBPText.get(1.0, tk.END).strip()
       self.controller.person.height = self.heightText.get(1.0, tk.END).strip()
       self.controller.person.weight = self.weightText.get(1.0, tk.END).strip()

