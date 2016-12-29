import tkinter as tk   # python3
#import Tkinter as tk   # python

TITLE_FONT = ("Helvetica", 18, "bold")

framesToCycle = list()
currentFrameIndex = list()
currentFrameIndex.append(0)

class SampleApp(tk.Tk):

   def __init__(self, *args, **kwargs):
       tk.Tk.__init__(self, *args, **kwargs)
       # the container is where we'll stack a bunch of frames
       # on top of each other, then the one we want visible
       # will be raised above the others
       container = tk.Frame(self)
       container.pack(side="top", fill="both", expand=True)
       container.grid_rowconfigure(0, weight=1)
       container.grid_columnconfigure(0, weight=1)

       self.frames = {}
       for F in (MainPage, BMIframe, Circumference, ThreeSiteSkinfold, SvnSiteSkinfold, ModAst, Ebelling, Rockport, Coopers, MBtoss, VertJump, RMtest, RMpredict, GripStrength, PushUps, CurlUps, PlankEnd, WallSit, FlexTests, SLstance, DeepSquat, WallSlide, HipHinge, FrontPlank):
           page_name = F.__name__
           frame = F(parent=container, controller=self)
           self.frames[page_name] = frame

           # put all of the pages in the same location;
           # the one on the top of the stacking order
           # will be the one that is visible.
           frame.grid(row=0, column=0, sticky="nsew")

       self.show_frame("MainPage")


   def show_frame(self, page_name):
       '''Show a frame for the given page name'''
       currentFrameIndex[0] = 0
       frame = self.frames[page_name]
       frame.tkraise()

   def next_page(self):
       frame = self.frames[framesToCycle[currentFrameIndex[0]]]
       currentFrameIndex[0] += 1
       frame.tkraise()

   def prev_page(self):
       frame = self.frames[framesToCycle[currentFrameIndex[0]-1]]
       currentFrameIndex[0] -= 1
       frame.tkraise()

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
       if text in framesToCycle:
           framesToCycle.remove(text)
       else:
           framesToCycle.append(text)

class StartPage(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller
       label = tk.Label(self, text="This is the start page", font=TITLE_FONT)
       label.pack(side="top", fill="x", pady=10)

       button1 = tk.Button(self, text="BMIframe",
                           command=lambda: controller.show_frame("BMIframe"))
       button2 = tk.Button(self, text="ThreeSiteSkinfold",
                           command=lambda: controller.show_frame("PageTwo"))
       button3 = tk.Button(self, text="SevenSiteSkinfold",
                           command=lambda: controller.show_frame("BMIframe"))
       button4 = tk.Button(self, text="ModAst",
                           command=lambda: controller.show_frame("ModAst"))
       button5 = tk.Button(self, text="Ebelling",
                           command=lambda: controller.show_frame("Ebelling"))
       button6 = tk.Button(self, text="Rockport",
                           command=lambda: controller.show_frame("Rockport"))
       button7 = tk.Button(self, text="Coopers",
                           command=lambda: controller.show_frame("Coopers"))
       button8 = tk.Button(self, text="RMtest",
                           command=lambda: controller.show_frame("RMtest"))
       button9 = tk.Button(self, text="RMpredict",
                           command=lambda: controller.show_frame("RMpredict"))
       button10 = tk.Button(self, text="MainPage",
                           command=lambda: controller.show_frame("MainPage"))
       button11 = tk.Button(self, text="GripStrength",
                            command=lambda: controller.show_frame("GripStrength"))
       button12 = tk.Button(self, text="PushUps",
                           command=lambda: controller.show_frame("PushUps"))
       button13 = tk.Button(self, text="CurlUps",
                           command=lambda: controller.show_frame("CurlUps"))
       button14 = tk.Button(self, text="PlankEnd",
                            command=lambda: controller.show_frame("PlankEnd"))
       button15 = tk.Button(self, text="WallSit",
                            command=lambda: controller.show_frame("WallSit"))
       button16 = tk.Button(self, text="FlexTests",
                            command=lambda: controller.show_frame("FlexTests"))
       button17 = tk.Button(self, text="SLstance",
                            command=lambda: controller.show_frame("SLstance"))
       button18 = tk.Button(self, text="DeepSquat",
                           command=lambda: controller.show_frame("DeepSquat"))
       button19 = tk.Button(self, text="WallSlide",
                           command=lambda: controller.show_frame("WallSlide"))
       button20 = tk.Button(self, text="HipHinge",
                            command=lambda: controller.show_frame("HipHinge"))
       button21 = tk.Button(self, text="FrontPlank",
                            command=lambda: controller.show_frame("FrontPlank"))
       button22 = tk.Button(self, text="Circumference",
                            command=lambda: controller.show_frame("Circumference"))


       button1.pack()
       button2.pack()
       button3.pack()
       button4.pack()
       button5.pack()
       button6.pack()
       button7.pack()
       button8.pack()
       button9.pack()
       button10.pack()
       button11.pack()
       button12.pack()
       button13.pack()
       button14.pack()
       button15.pack()
       button16.pack()
       button17.pack()
       button18.pack()
       button19.pack()
       button20.pack()
       button21.pack()
       button22.pack()

class PageOne(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller
       label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
       label.pack(side="top", fill="x", pady=10)
       button = tk.Button(self, text="Go to the start page",
                          command=lambda: controller.show_frame("MainPage"))
       button.pack()


class PageTwo(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller
       label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
       label.pack(side="top", fill="x", pady=10)
       button = tk.Button(self, text="Go to the start page",
                          command=lambda: controller.show_frame("MainPage"))
       button.pack()

class BMIframe(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.BMIresult = tk.Label(self)
       self.BMIresult["text"] = "BMI"
       self.BMIresult.grid(row=1, column=0)

       self.BMIresult = tk.Text(self)
       self.BMIresult["height"] = 1
       self.BMIresult["width"] = 5
       self.BMIresult.grid(row=1, column=1)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=2, column=2)

class Circumference(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self,parent)
       self.controller = controller

       self.Circumference = tk.Label(self)
       self.Circumference["text"] = "Circumferences"
       self.Circumference.grid(row=0, column=0)

       self.HipCirc = tk.Label(self)
       self.HipCirc["text"] = "Hip(cm): "
       self.HipCirc.grid(row=1, column=0)

       self.HipCirc = tk.Text(self)
       self.HipCirc["height"] = 1
       self.HipCirc["width"] = 5
       self.HipCirc.grid(row=1, column=1)

       self.WaistCirc = tk.Label(self)
       self.WaistCirc["text"] = "Waist(cm): "
       self.WaistCirc.grid(row=2, column=0)

       self.WaistCirc = tk.Text(self)
       self.WaistCirc["height"] = 1
       self.WaistCirc["width"] = 5
       self.WaistCirc.grid(row=2, column=1)

       self.ArmCirc = tk.Label(self)
       self.ArmCirc["text"] = "Arm(cm): "
       self.ArmCirc.grid(row=3, column=0)

       self.ArmCirc = tk.Text(self)
       self.ArmCirc["height"] = 1
       self.ArmCirc["width"] = 5
       self.ArmCirc.grid(row=3, column=1)

       self.ThighCirc = tk.Label(self)
       self.ThighCirc["text"] = "Thigh(cm): "
       self.ThighCirc.grid(row=4, column=0)

       self.ThighCirc = tk.Text(self)
       self.ThighCirc["height"] = 1
       self.ThighCirc["width"] = 5
       self.ThighCirc.grid(row=4, column=1)

       self.ChestCirc = tk.Label(self)
       self.ChestCirc["text"] = "Chest(cm): "
       self.ChestCirc.grid(row=5, column=0)

       self.ChestCirc = tk.Text(self)
       self.ChestCirc["height"] = 1
       self.ChestCirc["width"] = 5
       self.ChestCirc.grid(row=5, column=1)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=6, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=6, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=6, column=2)


class ThreeSiteSkinfold(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ThreeSiteMaleCalc = tk.Label(self)
       self.ThreeSiteMaleCalc["text"] = "3-Site Skinfold (Male)"
       self.ThreeSiteMaleCalc.grid(row=2, column=0)

       self.ThreeSiteMaleChest = tk.Label(self)
       self.ThreeSiteMaleChest["text"] = "Chest: "
       self.ThreeSiteMaleChest.grid(row=2, column=1)

       self.ThreeSiteMaleChestInput = tk.Text(self)
       self.ThreeSiteMaleChestInput["height"] = 1
       self.ThreeSiteMaleChestInput["width"] = 5
       self.ThreeSiteMaleChestInput.grid(row=2, column=2)

       self.ThreeSiteMaleAb = tk.Label(self)
       self.ThreeSiteMaleAb["text"] = "Abdomen: "
       self.ThreeSiteMaleAb.grid(row=2, column=3)

       self.ThreeSiteMaleAbInput = tk.Text(self)
       self.ThreeSiteMaleAbInput["height"] = 1
       self.ThreeSiteMaleAbInput["width"] = 5
       self.ThreeSiteMaleAbInput.grid(row=2, column=4)

       self.ThreeSiteMaleThigh = tk.Label(self)
       self.ThreeSiteMaleThigh["text"] = "Thigh: "
       self.ThreeSiteMaleThigh.grid(row=2, column=5)

       self.ThreeSiteMaleChestThigh = tk.Text(self)
       self.ThreeSiteMaleChestThigh["height"] = 1
       self.ThreeSiteMaleChestThigh["width"] = 5
       self.ThreeSiteMaleChestThigh.grid(row=2, column=6)

       self.ThreeSiteFemaleCalc = tk.Label(self)
       self.ThreeSiteFemaleCalc["text"] = "3-Site Skinfold (Female)"
       self.ThreeSiteFemaleCalc.grid(row=3, column=0)

       self.ThreeSiteFemaleSupra = tk.Label(self)
       self.ThreeSiteFemaleSupra["text"] = "Suprailiac: "
       self.ThreeSiteFemaleSupra.grid(row=3, column=1)

       self.ThreeSiteFemaleSupra = tk.Text(self)
       self.ThreeSiteFemaleSupra["height"] = 1
       self.ThreeSiteFemaleSupra["width"] = 5
       self.ThreeSiteFemaleSupra.grid(row=3, column=2)

       self.ThreeSiteFemaleTricep = tk.Label(self)
       self.ThreeSiteFemaleTricep["text"] = "Tricep: "
       self.ThreeSiteFemaleTricep.grid(row=3, column=3)

       self.ThreeSiteFemaleTricep = tk.Text(self)
       self.ThreeSiteFemaleTricep["height"] = 1
       self.ThreeSiteFemaleTricep["width"] = 5
       self.ThreeSiteFemaleTricep.grid(row=3, column=4)

       self.ThreeSiteFemaleThigh = tk.Label(self)
       self.ThreeSiteFemaleThigh["text"] = "Thigh: "
       self.ThreeSiteFemaleThigh.grid(row=3, column=5)

       self.ThreeSiteFemaleThigh = tk.Text(self)
       self.ThreeSiteFemaleThigh["height"] = 1
       self.ThreeSiteFemaleThigh["width"] = 5
       self.ThreeSiteFemaleThigh.grid(row=3, column=6)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=4, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=4, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=4, column=2)

class SvnSiteSkinfold(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SvnSiteSkFold = tk.Label(self)
       self.SvnSiteSkFold["text"] = "7-Site Skin Folds"
       self.SvnSiteSkFold.grid(row=0, column=0)

       self.SvnSiteChest = tk.Label(self)
       self.SvnSiteChest["text"] = "Chest: "
       self.SvnSiteChest.grid(row=1, column=0)

       self.SvnSiteChest = tk.Text(self)
       self.SvnSiteChest["height"] = 1
       self.SvnSiteChest["width"] = 5
       self.SvnSiteChest.grid(row=1, column=1)

       self.SvnSiteMidAx = tk.Label(self)
       self.SvnSiteMidAx["text"] = "Mid-Axillary: "
       self.SvnSiteMidAx.grid(row=1, column=2)

       self.SvnSiteMidAx = tk.Text(self)
       self.SvnSiteMidAx["height"] = 1
       self.SvnSiteMidAx["width"] = 5
       self.SvnSiteMidAx.grid(row=1, column=3)

       self.SvnSiteTri = tk.Label(self)
       self.SvnSiteTri["text"] = "Triceps: "
       self.SvnSiteTri.grid(row=1, column=4)

       self.SvnSiteTri = tk.Text(self)
       self.SvnSiteTri["height"] = 1
       self.SvnSiteTri["width"] = 5
       self.SvnSiteTri.grid(row=1, column=5)

       self.SvnSiteScap = tk.Label(self)
       self.SvnSiteScap["text"] = "Subscapular: "
       self.SvnSiteScap.grid(row=1, column=6)

       self.SvnSiteScap = tk.Text(self)
       self.SvnSiteScap["height"] = 1
       self.SvnSiteScap["width"] = 5
       self.SvnSiteScap.grid(row=1, column=7)

       self.SvnSiteSupra = tk.Label(self)
       self.SvnSiteSupra["text"] = "Suprailiac: "
       self.SvnSiteSupra.grid(row=1, column=8)

       self.SvnSiteSupra = tk.Text(self)
       self.SvnSiteSupra["height"] = 1
       self.SvnSiteSupra["width"] = 5
       self.SvnSiteSupra.grid(row=1, column=9)

       self.SvnSiteAb = tk.Label(self)
       self.SvnSiteAb["text"] = "Abdomen: "
       self.SvnSiteAb.grid(row=1, column=10)

       self.SvnSiteAb = tk.Text(self)
       self.SvnSiteAb["height"] = 1
       self.SvnSiteAb["width"] = 5
       self.SvnSiteAb.grid(row=1, column=11)

       self.SvnSiteThigh = tk.Label(self)
       self.SvnSiteThigh["text"] = "Thigh: "
       self.SvnSiteThigh.grid(row=1, column=12)

       self.SvnSiteThigh = tk.Text(self)
       self.SvnSiteThigh["height"] = 1
       self.SvnSiteThigh["width"] = 5
       self.SvnSiteThigh.grid(row=1, column=13)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=2, column=2)


class ModAst(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.ModAst = tk.Label(self)
       self.ModAst["text"] = "Modified Astrand"
       self.ModAst.grid(row=1, column=0)

       self.ModAstLoadA = tk.Label(self)
       self.ModAstLoadA["text"] = "Warm-Up Load(kp): "
       self.ModAstLoadA.grid(row=2, column=0)

       self.ModAstLoadA = tk.Text(self)
       self.ModAstLoadA["height"] = 1
       self.ModAstLoadA["width"] = 5
       self.ModAstLoadA.grid(row=2, column =1)

       self.ModAstLoadB = tk.Label(self)
       self.ModAstLoadB["text"] = "Work Load(kp): "
       self.ModAstLoadB.grid(row=3, column=0)

       self.ModAstLoadB = tk.Text(self)
       self.ModAstLoadB["height"] = 1
       self.ModAstLoadB["width"] = 5
       self.ModAstLoadB.grid(row=3, column=1)

       self.ModAstHR = tk.Label(self)
       self.ModAstHR["text"] = "Average HR(bpm): "
       self.ModAstHR.grid(row=3, column=2)

       self.ModAstHR = tk.Text(self)
       self.ModAstHR["height"] = 1
       self.ModAstHR["width"] = 5
       self.ModAstHR.grid(row=3, column=3)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=4, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=4, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=4, column=2)

class Ebelling(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Ebelling = tk.Label(self)
       self.Ebelling["text"] = "Ebelling Treadmill Test"
       self.Ebelling.grid(row=0, column=0)

       self.EbellingWU = tk.Label(self)
       self.EbellingWU["text"] = "Warm Up Speed"
       self.EbellingWU.grid(row=1, column=0)

       self.EbellingWU = tk.Text(self)
       self.EbellingWU["height"] = 1
       self.EbellingWU["width"] = 5
       self.EbellingWU.grid(row=1, column=1)

       self.EbellingWork = tk.Label(self)
       self.EbellingWork["text"] = "Workload Speed"
       self.EbellingWork.grid(row=2, column=0)

       self.EbellingWork = tk.Text(self)
       self.EbellingWork["height"] = 1
       self.EbellingWork["width"] = 5
       self.EbellingWork.grid(row=2, column=1)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=3, column=2)

class Rockport(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Rockport = tk.Label(self)
       self.Rockport["text"] = "Rockport 1-Mile Walk"
       self.Rockport.grid(row=0, column=0)

       self.RockportHR = tk.Label(self)
       self.RockportHR["text"] = "Post Test HR: "
       self.RockportHR.grid(row=1, column=0)

       self.RockportHR = tk.Text(self)
       self.RockportHR["height"] = 1
       self.RockportHR["width"] = 5
       self.RockportHR.grid(row=1, column=1)

       self.RockportTime = tk.Label(self)
       self.RockportTime["text"] = "Time(min): "
       self.RockportTime.grid(row=2, column=0)

       self.RockportTime = tk.Text(self)
       self.RockportTime["height"] = 1
       self.RockportTime["width"] = 5
       self.RockportTime.grid(row=2, column=1)

       self.NextB = tk.Button(self)
       self.NextB["text"] = "Next"
       self.NextB["fg"] = "black"
       self.NextB["command"] = lambda: controller.next_page()
       self.NextB.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitB = tk.Button(self)
       self.QuitB["text"] = "Quit"
       self.QuitB["fg"] = "black"
       self.QuitB["command"] = lambda: controller.show_frame("MainPage")
       self.QuitB.grid(row=3, column=2)

class Coopers(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Cooper = tk.Label(self)
       self.Cooper["text"] = "Coopers Run"
       self.Cooper.grid(row=0, column=0)

       self.CooperDist = tk.Label(self)
       self.CooperDist["text"] = "Distance(miles): "
       self.CooperDist.grid(row=1, column=0)

       self.CooperDist = tk.Text(self)
       self.CooperDist["height"] = 1
       self.CooperDist["width"] = 5
       self.CooperDist.grid(row=1, column=1)

       self.NextC = tk.Button(self)
       self.NextC["text"] = "Next"
       self.NextC["fg"] = "black"
       self.NextC["command"] = lambda: controller.next_page()
       self.NextC.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitC = tk.Button(self)
       self.QuitC["text"] = "Quit"
       self.QuitC["fg"] = "black"
       self.QuitC["command"] = lambda: controller.show_frame("MainPage")
       self.QuitC.grid(row=2, column=1)

class MBtoss(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SeatMB = tk.Label(self)
       self.SeatMB["text"] = "Seated Med. Ball Toss"
       self.SeatMB.grid(row=0, column=0)

       self.SeatMBDist = tk.Label(self)
       self.SeatMBDist["text"] = "Max. Distance(cm): "
       self.SeatMBDist.grid(row=1, column=0)

       self.SeatMBDist = tk.Text(self)
       self.SeatMBDist["height"] = 1
       self.SeatMBDist["width"] = 5
       self.SeatMBDist.grid(row=1, column=1)

       self.NextE = tk.Button(self)
       self.NextE["text"] = "Next"
       self.NextE["fg"] = "black"
       self.NextE["command"] = lambda: controller.next_page()
       self.NextE.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitE = tk.Button(self)
       self.QuitE["text"] = "Quit"
       self.QuitE["fg"] = "black"
       self.QuitE["command"] = lambda: controller.show_frame("MainPage")
       self.QuitE.grid(row=2, column=2)

class VertJump(tk.Frame):
   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.VertJump = tk.Label(self)
       self.VertJump["text"] = "Vertical Jump"
       self.VertJump.grid(row=0, column=0)

       self.VertJumpSR = tk.Label(self)
       self.VertJumpSR["text"] = "Standing Reach(ft/inch): "
       self.VertJumpSR.grid(row=1, column=0)

       self.VertJumpSR = tk.Text(self)
       self.VertJumpSR["height"] = 1
       self.VertJumpSR["width"] = 5
       self.VertJumpSR.grid(row=1, column=1)

       self.VertJumpBest = tk.Label(self)
       self.VertJumpBest["text"] = "Best Attempt(ft/inch): "
       self.VertJumpBest.grid(row=2, column=0)

       self.VertJumpBest = tk.Text(self)
       self.VertJumpBest["height"] = 1
       self.VertJumpBest["width"] = 5
       self.VertJumpBest.grid(row=2, column=1)

       self.NextE = tk.Button(self)
       self.NextE["text"] = "Next"
       self.NextE["fg"] = "black"
       self.NextE["command"] = lambda: controller.next_page()
       self.NextE.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitE = tk.Button(self)
       self.QuitE["text"] = "Quit"
       self.QuitE["fg"] = "black"
       self.QuitE["command"] = lambda: controller.show_frame("MainPage")
       self.QuitE.grid(row=3, column=2)

class RMtest(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.RepMaxTest = tk.Label(self)
       self.RepMaxTest["text"] = "1 Rep Max.(Tested)"
       self.RepMaxTest.grid(row=0, column=0)

       self.RMTestExA = tk.Label(self)
       self.RMTestExA["text"] = "Exercise: "
       self.RMTestExA.grid(row=1, column=0)

       self.RMTestExA = tk.Text(self)
       self.RMTestExA["height"] = 1
       self.RMTestExA["width"] = 5
       self.RMTestExA.grid(row=1, column=1)

       self.RMTestExAWeight = tk.Label(self)
       self.RMTestExAWeight["text"] = "1RM(kg): "
       self.RMTestExAWeight.grid(row=1, column=2)

       self.RMTestExAWeight = tk.Text(self)
       self.RMTestExAWeight["height"] = 1
       self.RMTestExAWeight["width"] = 5
       self.RMTestExAWeight.grid(row=1, column=3)

       self.RMTestExB = tk.Label(self)
       self.RMTestExB["text"] = "Exercise: "
       self.RMTestExB.grid(row=2, column=0)

       self.RMTestExB = tk.Text(self)
       self.RMTestExB["height"] = 1
       self.RMTestExB["width"] = 5
       self.RMTestExB.grid(row=2, column=1)

       self.RMTestExBWeight = tk.Label(self)
       self.RMTestExBWeight["text"] = "1RM(kg): "
       self.RMTestExBWeight.grid(row=2, column=2)

       self.RMTestExBWeight = tk.Text(self)
       self.RMTestExBWeight["height"] = 1
       self.RMTestExBWeight["width"] = 5
       self.RMTestExBWeight.grid(row=2, column=3)

       self.NextD = tk.Button(self)
       self.NextD["text"] = "Next"
       self.NextD["fg"] = "black"
       self.NextD["command"] = lambda: controller.next_page()
       self.NextD.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitD = tk.Button(self)
       self.QuitD["text"] = "Quit"
       self.QuitD["fg"] = "black"
       self.QuitD["command"] = lambda: controller.show_frame("MainPage")
       self.QuitD.grid(row=3, column=2)

class RMpredict(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.RMPredict = tk.Label(self)
       self.RMPredict["text"] = "1 Rep Max.(Predicted)"
       self.RMPredict.grid(row=0, column=0)

       self.RMPredictEx = tk.Label(self)
       self.RMPredictEx["text"] = "Exercise: "
       self.RMPredictEx.grid(row=1, column=0)

       self.RMPredictEx = tk.Text(self)
       self.RMPredictEx["height"] = 1
       self.RMPredictEx["width"] = 5
       self.RMPredictEx.grid(row=1, column=1)

       self.RMPredictReps = tk.Label(self)
       self.RMPredictReps["text"] = "Reps: "
       self.RMPredictReps.grid(row=2, column=0)

       self.RMPredictReps = tk.Text(self)
       self.RMPredictReps["height"] = 1
       self.RMPredictReps["width"] = 5
       self.RMPredictReps.grid(row=2, column=1)

       self.RMPredictEst = tk.Label(self)
       self.RMPredictEst["text"] = "Estimated 1RM(kg): "
       self.RMPredictEst.grid(row=3, column=0)

       self.RMPredictEst = tk.Text(self)
       self.RMPredictEst["height"] = 1
       self.RMPredictEst["width"] = 5
       self.RMPredictEst.grid(row=3, column=1)

       self.NextD = tk.Button(self)
       self.NextD["text"] = "Next"
       self.NextD["fg"] = "black"
       self.NextD["command"] = lambda: controller.next_page()
       self.NextD.grid(row=4, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=4, column=1)

       self.QuitD = tk.Button(self)
       self.QuitD["text"] = "Quit"
       self.QuitD["fg"] = "black"
       self.QuitD["command"] = lambda: controller.show_frame("MainPage")
       self.QuitD.grid(row=4, column=2)

class GripStrength(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.GripStr = tk.Label(self)
       self.GripStr["text"] = "Grip Strength"
       self.GripStr.grid(row=0, column=0)

       self.GripStrLeft = tk.Label(self)
       self.GripStrLeft["text"] = "Max. Left Hand(kg): "
       self.GripStrLeft.grid(row=1, column=0)

       self.GripStrLeft = tk.Text(self)
       self.GripStrLeft["height"] = 1
       self.GripStrLeft["width"] = 5
       self.GripStrLeft.grid(row=1, column=1)

       self.GripStrRight = tk.Label(self)
       self.GripStrRight["text"] = "Max. Right Hand(kg): "
       self.GripStrRight.grid(row=2, column=0)

       self.GripStrRight = tk.Text(self)
       self.GripStrRight["height"] = 1
       self.GripStrRight["width"] = 5
       self.GripStrRight.grid(row=2, column=1)

       self.NextD = tk.Button(self)
       self.NextD["text"] = "Next"
       self.NextD["fg"] = "black"
       self.NextD["command"] = lambda: controller.next_page()
       self.NextD.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitD = tk.Button(self)
       self.QuitD["text"] = "Quit"
       self.QuitD["fg"] = "black"
       self.QuitD["command"] = lambda: controller.show_frame("MainPage")
       self.QuitD.grid(row=3, column=2)

class PushUps(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.PushUp = tk.Label(self)
       self.PushUp["text"] = "Push Ups"
       self.PushUp.grid(row=0, column=0)

       self.PushUpNum = tk.Label(self)
       self.PushUpNum["text"] = "Number: "
       self.PushUpNum.grid(row=1, column=0)

       self.PushUpNum = tk.Text(self)
       self.PushUpNum["height"] = 1
       self.PushUpNum["width"] = 5
       self.PushUpNum.grid(row=1, column=1)

       self.NextF = tk.Button(self)
       self.NextF["text"] = "Next"
       self.NextF["fg"] = "black"
       self.NextF["command"] = lambda: controller.next_page()
       self.NextF.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitF = tk.Button(self)
       self.QuitF["text"] = "Quit"
       self.QuitF["fg"] = "black"
       self.QuitF["command"] = lambda: controller.show_frame("MainPage")
       self.QuitF.grid(row=2, column=2)

class CurlUps(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.CurlUp = tk.Label(self)
       self.CurlUp["text"] = "10cm Curl Ups"
       self.CurlUp.grid(row=0, column=0)

       self.CurlUpNum = tk.Label(self)
       self.CurlUpNum["text"] = "Number: "
       self.CurlUpNum.grid(row=1, column=0)

       self.CurlUpNum = tk.Text(self)
       self.CurlUpNum["height"] = 1
       self.CurlUpNum["width"] = 5
       self.CurlUpNum.grid(row=1, column=1)

       self.NextF = tk.Button(self)
       self.NextF["text"] = "Next"
       self.NextF["fg"] = "black"
       self.NextF["command"] = lambda: controller.next_page()
       self.NextF.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitF = tk.Button(self)
       self.QuitF["text"] = "Quit"
       self.QuitF["fg"] = "black"
       self.QuitF["command"] = lambda: controller.show_frame("MainPage")
       self.QuitF.grid(row=2, column=2)

class PlankEnd(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.Plank = tk.Label(self)
       self.Plank["text"] = "Front Plank"
       self.Plank.grid(row=0, column=0)

       self.PlankTime = tk.Label(self)
       self.PlankTime["text"] = "Time(sec.)"
       self.PlankTime.grid(row=1, column=0)

       self.PlankTime = tk.Text(self)
       self.PlankTime["height"] = 1
       self.PlankTime["width"] = 5
       self.PlankTime.grid(row=1, column=1)

       self.NextF = tk.Button(self)
       self.NextF["text"] = "Next"
       self.NextF["fg"] = "black"
       self.NextF["command"] = lambda: controller.next_page()
       self.NextF.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitF = tk.Button(self)
       self.QuitF["text"] = "Quit"
       self.QuitF["fg"] = "black"
       self.QuitF["command"] = lambda: controller.show_frame("MainPage")
       self.QuitF.grid(row=2, column=2)

class WallSit(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.WallSit = tk.Label(self)
       self.WallSit["text"] = "Wall Sit"
       self.WallSit.grid(row=0, column=0)

       self.WallSitTime = tk.Label(self)
       self.WallSitTime["text"] = "Time(sec.): "
       self.WallSitTime.grid(row=1, column=0)

       self.WallSitTime = tk.Text(self)
       self.WallSitTime["height"] = 1
       self.WallSitTime["width"] = 5
       self.WallSitTime.grid(row=1, column=1)

       self.NextF = tk.Button(self)
       self.NextF["text"] = "Next"
       self.NextF["fg"] = "black"
       self.NextF["command"] = lambda: controller.next_page()
       self.NextF.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitF = tk.Button(self)
       self.QuitF["text"] = "Quit"
       self.QuitF["fg"] = "black"
       self.QuitF["command"] = lambda: controller.show_frame("MainPage")
       self.QuitF.grid(row=2, column=2)

class FlexTests(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SitReach = tk.Label(self)
       self.SitReach["text"] = "Sit & Reach"
       self.SitReach.grid(row=0, column=0)

       self.SitReachDist = tk.Label(self)
       self.SitReachDist["text"] = "Max Distance (cm): "
       self.SitReachDist.grid(row=1, column=0)

       self.SitReachDist = tk.Text(self)
       self.SitReachDist["height"] = 1
       self.SitReachDist["width"] = 5
       self.SitReachDist.grid(row=1, column=1)

       self.NextG = tk.Button(self)
       self.NextG["text"] = "Next"
       self.NextG["fg"] = "black"
       self.NextG["command"] = lambda: controller.next_page()
       self.NextG.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitG = tk.Button(self)
       self.QuitG["text"] = "Quit"
       self.QuitG["fg"] = "black"
       self.QuitG["command"] = lambda: controller.show_frame("MainPage")
       self.QuitG.grid(row=2, column=2)

class SLstance(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SLStance = tk.Label(self)
       self.SLStance["text"] = "Single Leg Stance Test"
       self.SLStance.grid(row=0, column=0)

       self.SLOpenLeft = tk.Label(self)
       self.SLOpenLeft["text"] = "Eyes Open Left(sec.): "
       self.SLOpenLeft.grid(row=1, column=0)

       self.SLOpenLeft = tk.Text(self)
       self.SLOpenLeft["height"] = 1
       self.SLOpenLeft["width"] = 5
       self.SLOpenLeft.grid(row=1, column=1)

       self.SLOpenRight = tk.Label(self)
       self.SLOpenRight["text"] = "Eyes Open Right(sec.): "
       self.SLOpenRight.grid(row=1, column=2)

       self.SLOpenRight = tk.Text(self)
       self.SLOpenRight["height"] = 1
       self.SLOpenRight["width"] = 5
       self.SLOpenRight.grid(row=1, column=3)

       self.SLCloseLeft = tk.Label(self)
       self.SLCloseLeft["text"] = "Eyes Closed Left(sec.): "
       self.SLCloseLeft.grid(row=2, column=0)

       self.SLCloseLeft = tk.Text(self)
       self.SLCloseLeft["height"] = 1
       self.SLCloseLeft["width"] = 5
       self.SLCloseLeft.grid(row=2, column=1)

       self.SLCloseRight = tk.Label(self)
       self.SLCloseRight["text"] = "Eyes Closed Right(sec.): "
       self.SLCloseRight.grid(row=2, column=2)

       self.SLCloseRight = tk.Text(self)
       self.SLCloseRight["height"] = 1
       self.SLCloseRight["width"] = 5
       self.SLCloseRight.grid(row=2, column=3)

       self.NextH = tk.Button(self)
       self.NextH["text"] = "Next"
       self.NextH["fg"] = "black"
       self.NextH["command"] = lambda: controller.next_page()
       self.NextH.grid(row=3, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=3, column=1)

       self.QuitH = tk.Button(self)
       self.QuitH["text"] = "Quit"
       self.QuitH["fg"] = "black"
       self.QuitH["command"] = lambda: controller.show_frame("MainPage")
       self.QuitH.grid(row=3, column=2)

class DeepSquat(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.DeepSquat = tk.Label(self)
       self.DeepSquat["text"] = "Deep Squat"
       self.DeepSquat.grid(row=0, column=0)

       self.DeepSquatRate = tk.Label(self)
       self.DeepSquatRate["text"] = "Rating(0-3): "
       self.DeepSquatRate.grid(row=1, column=0)

       self.DeepSquatRate = tk.Text(self)
       self.DeepSquatRate["height"] = 1
       self.DeepSquatRate["width"] = 5
       self.DeepSquatRate.grid(row=1, column=1)

       self.NextH = tk.Button(self)
       self.NextH["text"] = "Next"
       self.NextH["fg"] = "black"
       self.NextH["command"] = lambda: controller.next_page()
       self.NextH.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitH = tk.Button(self)
       self.QuitH["text"] = "Quit"
       self.QuitH["fg"] = "black"
       self.QuitH["command"] = lambda: controller.show_frame("MainPage")
       self.QuitH.grid(row=2, column=2)

class WallSlide(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.WallSlide = tk.Label(self)
       self.WallSlide["text"] = "Wall Slide"
       self.WallSlide.grid(row=0,column=0)

       self.WallSlideRate = tk.Label(self)
       self.WallSlideRate["text"] = "Rating(0-3): "
       self.WallSlideRate.grid(row=1, column=0)

       self.WallSlideRate = tk.Text(self)
       self.WallSlideRate["height"] = 1
       self.WallSlideRate["width"] = 5
       self.WallSlideRate.grid(row=1, column=1)

       self.NextH = tk.Button(self)
       self.NextH["text"] = "Next"
       self.NextH["fg"] = "black"
       self.NextH["command"] = lambda: controller.next_page()
       self.NextH.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitH = tk.Button(self)
       self.QuitH["text"] = "Quit"
       self.QuitH["fg"] = "black"
       self.QuitH["command"] = lambda: controller.show_frame("MainPage")
       self.QuitH.grid(row=2, column=2)

class HipHinge(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.HipHinge = tk.Label(self)
       self.HipHinge["text"] = "Hip Hinge"
       self.HipHinge.grid(row=0, column=0)

       self.HipHingeRate = tk.Label(self)
       self.HipHingeRate["text"] = "Rating(0-3): "
       self.HipHingeRate.grid(row=1, column=0)

       self.HipHingeRate = tk.Text(self)
       self.HipHingeRate["height"] = 1
       self.HipHingeRate["width"] = 5
       self.HipHingeRate.grid(row=1, column=1)

       self.NextH = tk.Button(self)
       self.NextH["text"] = "Next"
       self.NextH["fg"] = "black"
       self.NextH["command"] = lambda: controller.next_page()
       self.NextH.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitH = tk.Button(self)
       self.QuitH["text"] = "Quit"
       self.QuitH["fg"] = "black"
       self.QuitH["command"] = lambda: controller.show_frame("MainPage")
       self.QuitH.grid(row=2, column=2)

class FrontPlank(tk.Frame):

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.FrPlank = tk.Label(self)
       self.FrPlank["text"] = "Front Plank"
       self.FrPlank.grid(row=0, column=0)

       self.FrPlankRate = tk.Label(self)
       self.FrPlankRate["text"] = "Rating(0-3): "
       self.FrPlankRate.grid(row=1, column=0)

       self.FrPlankRate = tk.Text(self)
       self.FrPlankRate["height"] = 1
       self.FrPlankRate["width"] = 5
       self.FrPlankRate.grid(row=1, column=1)

       self.NextH = tk.Button(self)
       self.NextH["text"] = "Next"
       self.NextH["fg"] = "black"
       self.NextH["command"] = lambda: controller.next_page()
       self.NextH.grid(row=2, column=0)

       self.Back = tk.Button(self)
       self.Back["text"] = "Back"
       self.Back["fg"] = "black"
       self.Back["command"] = lambda: controller.prev_page()
       self.Back.grid(row=2, column=1)

       self.QuitH = tk.Button(self)
       self.QuitH["text"] = "Quit"
       self.QuitH["fg"] = "black"
       self.QuitH["command"] = lambda: controller.show_frame("MainPage")
       self.QuitH.grid(row=2, column=2)

if __name__ == "__main__":
   app = SampleApp()
   app.mainloop()

