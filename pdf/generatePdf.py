#https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor

def generatePdfForPerson(person):
	doc = SimpleDocTemplate('form.pdf', rightMarge=72, leftMargin=72, topMargin=72, bottomMargin=18)
	Story=[]
	logo = 'pdf/macewan-university-logo.png'		

	im = Image(logo, 3*inch, 1*inch)
	Story.append(im)

	styles = getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, borderWidth=1, borderColor=HexColor('#800020'), borderPadding=3))
	ptext = '<font size=12>%s</font>' % person.testDate

	Story.append(Paragraph(ptext, styles["Justify"]))
	Story.append(Spacer(1, 12))
	 
	Story.append(Spacer(1, 12))
	ptext = '<font size=12>Name: %s</font>' % person.name
	Story.append(Paragraph(ptext, styles["Justify"]))
	Story.append(Spacer(1, 12))
	 

	if "BMIframe" in person.framesChecked: 
		ptext = '<font size=12>BMI: %s</font>' % str(person.getBMI())
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))

	if "Circumference" in person.framesChecked:
		ptext = '<font size=12>Circumference:</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Hip Circ (cm):%s</font>' % str(person.hipCirc)
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Waist Circ (cm):%s</font>' % str(person.waistCirc)
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Arm Circ (cm):%s</font>' % str(person.armCirc)
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Thigh Circ (cm):%s</font>' % str(person.thighCirc)
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))
		

	if "Coopers" in person.framesChecked:
		ptext = '<font size=12>Coopers Run Test:</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>VO2max (ml/kg/min):%s</font>' % str(person.getCooperAerobic())
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))
		

	if "CurlUps" in person.framesChecked:
		ptext = '<font size=12>Curl Ups: %s</font>' % str(person.curlUpNum)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		

	if "DeepSquat" in person.framesChecked:
		ptext = '<font size=12>Deep Squat Assessment Rating(0-3): %s</font>' % str(person.deepSquatRate)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		

	if "Ebelling" in person.framesChecked:
		ptext = '<font size=12>Ebelling Treadmill Test:</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>VO2max (ml/kg/min): %s</font>' % str(person.getEbellingAerobic())
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))

	if "FlexTests" in person.framesChecked:
		ptext = '<font size=12>Sit & Reach Distance(cm): %s</font>' % str(person.sitReachDist)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))

	if "FrontPlank" in person.framesChecked:
		ptext = '<font size=12>Front Plank Assessment Rating(0-3): %s</font>' % str(person.frontPlankRate)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		

	if "GripStrength" in person.framesChecked:
		ptext = '<font size=12>GripStrength: </font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Left Hand(kg): %s</font>' % str(person.gripStrengthLeft)
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Right Hand(kg): %s</font>' % str(person.gripStrengthRight)
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))

	if "HipHinge" in person.framesChecked:
		ptext = '<font size=12>Hip Hinge Assessment Rating(0-3): %s</font>' % str(person.hipHingeRate)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		

	if "MBtoss" in person.framesChecked:
		ptext = '<font size=12>Med. Ball Toss Distance(cm): %s</font>' % str(person.seatMBDist)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		

	if "ModAst" in person.framesChecked:
		ptext = '<font size=12>Modified Astrand Cycle Test:</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>VO2max(ml/kg/min): %s </font>' % str(person.modAstAerobic)
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))
		

	if "PlankEnd" in person.framesChecked:
		ptext = '<font size=12>Front Plank Time(sec.): %s</font>' % str(person.plankTime)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		

	if "PushUps" in person.framesChecked:
		ptext = '<font size=12>Push Ups: %s</font>' % str(person.pushUpNum)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		

	if "RMpredict" in person.framesChecked:
		ptext = '<font size=12>1 Rep Max (Predicted) </font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Exercise: %s </font>' % str(person.RMPredictEx)
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>1 Rep Max Weight: %s </font>' % str(person.getRepMaxPredict())
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))
		

	if "RMtest" in person.framesChecked:
		ptext = '<font size=12>1 Rep Max (Tested):</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		if (person.RMTestExA.strip() != "" and person.RMTestExAWeight.strip() != ""):
			ptext = '<font size=12>Exercise: %s</font>' % str(person.RMTestExA)
			Story.append(Paragraph(ptext, styles["Justify"]))

			ptext = '<font size=12>1 Rep Max Weight: %s</font>' % str(person.RMTestExAWeight)
			Story.append(Paragraph(ptext, styles["Justify"]))

		if (person.RMTestExB.strip() != "" and person.RMTestExBWeight.strip() != ""):
			ptext = '<font size=12>Exercise: %s</font>' % str(person.RMTestExB)
			Story.append(Paragraph(ptext, styles["Justify"]))

			ptext = '<font size=12>1 Rep Max Weight: %s</font>' % str(person.RMTestExBWeight)
			Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))

	if "Rockport" in person.framesChecked:
		ptext = '<font size=12>Rockport 1 Mile Walk Test:</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>VO2max(ml/kg/min): %s</font>' % str(person.getRockportAerobic())
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))
		

	if "SLstance" in person.framesChecked:
		ptext = '<font size=12>Single Leg Stance Test:</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Left Leg Eyes Open Time(sec.): %s</font>' % str(person.SLOpenLeft)
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Right Leg Eyes Open Time(sec.): %s</font>' % str(person.SLOpenRight)
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Left Leg Eyes Closed Time(sec.): %s</font>' % str(person.SLCloseLeft)
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Right Leg Eyes Closed Time(sec.): %s</font>' % str(person.SLCloseRight)
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))

	if "SvnSiteSkinfold" in person.framesChecked:
		ptext = '<font size=12>Seven Site Skinfold:</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Body Density: %s</font>' % str(person.getSevenSiteDensity())
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Body Fat %%: %s</font>' % str(person.getBodyFatSeven())
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))

	if "ThreeSiteSkinfold" in person.framesChecked:
		ptext = '<font size=12>Three Site Skinfold:</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		if (person.threeSiteFemaleSupra.strip() != "" and person.threeSiteFemaleTricep.strip() != "" and person.threeSiteFemaleThigh.strip() != ""):
			ptext = '<font size=12>Body Density: %s</font>' % str(person.getThreeSiteMale())
			Story.append(Paragraph(ptext, styles["Justify"]))

			ptext = '<font size=12>Body Fat %%: %s</font>' % str(person.getBodyFatThreeMale())
			Story.append(Paragraph(ptext, styles["Justify"]))

		if (person.threeSiteMaleChest.strip() != "" and person.threeSiteMaleAb.strip() != "" and person.threeSiteMaleThigh.strip() != ""):
			ptext = '<font size=12>Body Density: %s</font>' % str(person.getThreeSiteFemale())
			Story.append(Paragraph(ptext, styles["Justify"]))

			ptext = '<font size=12>Body Fat %%: %s</font>' % str(person.getBodyFatThreeFemale())
			Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))

	if "VertJump" in person.framesChecked:
		ptext = '<font size=12>Vertical Jump Test:</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Stand and Reach(cm): %s</font>' % str(person.vertJumpSR)
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Best Jump(cm): %s</font>' % str(person.getVertJumpBest())
		Story.append(Paragraph(ptext, styles["Justify"]))

		ptext = '<font size=12>Peak Power(W): %s</font>' % str(person.getVertJumpPower())
		Story.append(Paragraph(ptext, styles["Justify"]))

		Story.append(Spacer(1, 12))
		

	if "WallSit" in person.framesChecked:
		ptext = '<font size=12>Wall Sit Time(sec.): %s</font>' % str(person.wallSitTime)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		

	if "WallSlide" in person.framesChecked:
		ptext = '<font size=12> Wall Slide Assessment Rating(0-3):%s</font>' % str(person.wallSlideRate)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))

	doc.build(Story)
	print("PDF created")




