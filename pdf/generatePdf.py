#https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def generatePdfForPerson(person):
	doc = SimpleDocTemplate('form.pdf', rightMarge=72, leftMargin=72, topMargin=72, bottomMargin=18)
	Story=[]
	logo = 'pdf/macewan-university-logo.png'		

	im = Image(logo, 4*inch, 2*inch)
	Story.append(im)

	styles = getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	ptext = '<font size=12>%s</font>' % person.testDate

	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(1, 12))
	 
	Story.append(Spacer(1, 12))
	ptext = '<font size=12>Name %s:</font>' % person.name
	Story.append(Paragraph(ptext, styles["Normal"]))
	Story.append(Spacer(1, 12))
	 

	if "BMIframe" in person.framesChecked: 
		ptext = '<font size=12>BMI %s:</font>' % str(person.getBMI())
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))

	if "Circumference" in person.framesChecked:
		ptext = '<font size=12>Circumference: %s</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))

		ptext = '<font size=12>arm circ: %s</font>' % str(person.armCirc)
		Story.append(Paragraph(ptext, styles["Normal"]))

		Story.append(Spacer(1, 12))
		

	if "Coopers" in person.framesChecked:
		ptext = '<font size=12>Coopers %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "CurlUps" in person.framesChecked:
		ptext = '<font size=12>CurlUps %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "DeepSquat" in person.framesChecked:
		ptext = '<font size=12>DeepSquat %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "Ebelling" in person.framesChecked:
		ptext = '<font size=12>Ebelling %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "FlexTests" in person.framesChecked:
		ptext = '<font size=12>FlexTests %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "FrontPlank" in person.framesChecked:
		ptext = '<font size=12>FrontPlank %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "GripStrength" in person.framesChecked:
		ptext = '<font size=12>GripStrength: </font>'
		Story.append(Paragraph(ptext, styles["Normal"]))

		ptext = '<font size=12>Left Hand(kg): %s</font>' % str(person.GripStrengthLeft)
		Story.append(Paragraph(ptext, styles["Normal"]))

		ptext = '<font size=12>Right Hand(kg): %s</font>' % str(person.GripStrengthRight)
		Story.append(Paragraph(ptext, styles["Normal"]))

		Story.append(Spacer(1, 12))
		

	if "HipHinge" in person.framesChecked:
		ptext = '<font size=12>HipHinge %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "MBtoss" in person.framesChecked:
		ptext = '<font size=12>MBtoss %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "ModAst" in person.framesChecked:
		ptext = '<font size=12>ModAst %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "PlankEnd" in person.framesChecked:
		ptext = '<font size=12>PlankEnd %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "PushUps" in person.framesChecked:
		ptext = '<font size=12>PushUps %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "RMpredict" in person.framesChecked:
		ptext = '<font size=12>RMpredict %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "RMtest" in person.framesChecked:
		ptext = '<font size=12>RMtest %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "Rockport" in person.framesChecked:
		ptext = '<font size=12>Rockport %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "SLstance" in person.framesChecked:
		ptext = '<font size=12>SLstance %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "SvnSiteSkinfold" in person.framesChecked:
		ptext = '<font size=12>SvnSiteSkinfold %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "ThreeSiteSkinfold" in person.framesChecked:
		ptext = '<font size=12>ThreeSiteSkinfold %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "VertJump" in person.framesChecked:
		ptext = '<font size=12>VertJump %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "WallSit" in person.framesChecked:
		ptext = '<font size=12>WallSit %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		

	if "WallSlide" in person.framesChecked:
		ptext = '<font size=12>WallSlide %s:</font>' % str("TODO fill in code")
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))


	doc.build(Story)
	print("PDF created")




