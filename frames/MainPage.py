import tkinter as tk

class MainPage(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.labelName = tk.Label(self)
       self.labelName["text"] = "Name: "
       self.labelName.grid(row=0, column=0)

       self.Name = tk.Text(self)
       self.Name["height"] = 1
       self.Name["width"] = 15
       self.Name.grid(row=0, column=1)

       self.labelDateOfTest = tk.Label(self)
       self.labelDateOfTest["text"] = "Date of Test: "
       self.labelDateOfTest.grid(row=0, column=2)

       self.DateOfTest = tk.Text(self)
       self.DateOfTest["height"] = 1
       self.DateOfTest["width"] = 15
       self.DateOfTest.grid(row=0, column=3)

       self.labelGender = tk.Label(self)
       self.labelGender["text"] = "Gender: "
       self.labelGender.grid(row=0, column=4)

       self.Gender = tk.Text(self)
       self.Gender["height"] = 1
       self.Gender["width"] = 15
       self.Gender.grid(row=0, column=5)

       self.labelDOB = tk.Label(self)
       self.labelDOB["text"] = "Date of Birth: "
       self.labelDOB.grid(row=0, column=6)

       self.DateOfBirth = tk.Text(self)
       self.DateOfBirth["height"] = 1
       self.DateOfBirth["width"] = 15
       self.DateOfBirth.grid(row=0, column=7)

       self.labelPhoneNumber = tk.Label(self)
       self.labelPhoneNumber["text"] = "Phone Number: "
       self.labelPhoneNumber.grid(row=1, column=0)

       self.PhoneNumber = tk.Text(self)
       self.PhoneNumber["height"] = 1
       self.PhoneNumber["width"] = 15
       self.PhoneNumber.grid(row=1, column=1)

       self.labelRestHR = tk.Label(self)
       self.labelRestHR["text"] = "Heart Rate: "
       self.labelRestHR.grid(row=1, column=2)

       self.RestHR = tk.Text(self)
       self.RestHR["height"] = 1
       self.RestHR["width"] = 15
       self.RestHR.grid(row=1, column=3,padx=0, pady=3)

       self.labelRestBP = tk.Label(self)
       self.labelRestBP["text"] = "Blood Pressure "
       self.labelRestBP.grid(row=1, column=4)

       self.RestBP = tk.Text(self)
       self.RestBP["height"] = 1
       self.RestBP["width"] = 15
       self.RestBP.grid(row=1, column=5)

       self.labelHeight = tk.Label(self)
       self.labelHeight["text"] = "Height: "
       self.labelHeight.grid(row=1, column=6)

       self.Height = tk.Text(self)
       self.Height["height"] = 1
       self.Height["width"] = 15
       self.Height.grid(row=1, column=7)

       self.labelWeight = tk.Label(self)
       self.labelWeight["text"] = "Weight: "
       self.labelWeight.grid(row=2, column=0)

       self.Weight = tk.Text(self)
       self.Weight["height"] = 1
       self.Weight["width"] = 15
       self.Weight.grid(row=2, column=1)

       self.labelBodyComp = tk.Label(self)
       self.labelBodyComp["text"] = "Body Composition Assessments: "
       self.labelBodyComp.grid(row=3, column=0)

       self.checkBMI = tk.Checkbutton(self, text="BMI", command = lambda: self.boxChecked("BMIframe"))
       self.checkBMI.grid(row=4, column=0)

       self.checkCircumference = tk.Checkbutton(self, text="Circumferences", command = lambda: self.boxChecked("Circumference"))
       self.checkCircumference.grid(row=4, column=1)

       self.checkThreeSkinfold = tk.Checkbutton(self, text="3-Site Skinfold", command = lambda: self.boxChecked("ThreeSiteSkinfold"))
       self.checkThreeSkinfold.grid(row=4, column=2)

       self.checkSevenSkinfold = tk.Checkbutton(self, text="7-Site Skinfold", command = lambda: self.boxChecked("SvnSiteSkinfold"))
       self.checkSevenSkinfold.grid(row=4, column=3)

       self.labelAerobicTest = tk.Label(self)
       self.labelAerobicTest["text"] = "Maximal/Submaximal VO2 Max Assessments: "
       self.labelAerobicTest.grid(row=5, column=0)

       self.checkModAstrand = tk.Checkbutton(self, text="Modified Astrand Cycle Test", command = lambda: self.boxChecked("ModAst"))
       self.checkModAstrand.grid(row=6, column=0)

       self.checkEbelling = tk.Checkbutton(self, text="Ebelling Treadmill Test", command = lambda: self.boxChecked("Ebelling"))
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

       self.NextA = tk.Button(self)
       self.NextA["text"] = "Next"
       self.NextA["fg"]   = "black"
       self.NextA["command"] =  lambda: controller.next_page()
       self.NextA.grid(row=17, column=0)

       self.SaveA = tk.Button(self)
       self.SaveA["text"] = "Save"
       self.SaveA["fg"] = "black"
       self.SaveA["command"] = self.SaveA
       self.SaveA.grid(row=17, column=1)

       self.QuitA = tk.Button(self)
       self.QuitA["text"] = "Quit"
       self.QuitA["fg"] = "black"
       self.QuitA["command"] = lambda: controller.show_frame("MainPage")
       self.QuitA.grid(row=17, column=2)

   def boxChecked(self, text):
       if text in self.controller.framesToCycle:
           self.controller.framesToCycle.remove(text)
       else:
           self.controller.framesToCycle.append(text)