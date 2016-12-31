import tkinter as tk


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