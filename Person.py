class Person():
    def __init__(self):
        # person attributes
        self.name = ""
        self.phoneNumber = ""
        self.testDate = ""
        self.birthDate = ""
        self.height = ""
        self.weight = ""
        self.age = ""
        self.gender = ""
        self.restHR = ""
        self.restBP = ""
        self.hipCirc = ""
        self.waistCirc = ""
        self.armCirc = ""
        self.thighCirc = ""
        self.chestCirc = ""
        self.mbToss = ""
        self.vertReach = ""
        self.vertJump = ""
        self.repMaxTestWeight = ""
        self.repMaxPredictWeight = ""
        self.gripStrengthLeft = ""
        self.gripStrenghtRight = ""
        self.pushUp = ""
        self.curlUp = ""
        self.PlankEndurance = ""
        self.WallSit = ""
        self.SitReach = ""
        self.SLstanceOpenLeft = ""
        self.SLstanceOpenRight = ""
        self.SLstanceClosedLeft = ""
        self.SLstanceClosedRight = ""
        self.deepSquatScreen = ""
        self.wallSlideScreen = ""
        self.hipHingeScreen = ""
        self.speed = ""
        self.testHR = ""
        self.PlankScreen = ""
        self.sumOfFolds= ""
        self.load = ""
        self.loadLBS = ""
        self.time = ""
        self.reps = ""
        self.repWeight = ""
        self.distance = ""
        self.distanceMiles = ""
        self.jumpHeigh = ""
        self.bodyMass = ""
        self.results = ""
        self.repWeight = ""
        self.chest = ""
        self.ab = ""
        self.maleThigh = ""
        self.suprailiac = ""
        self.tricep = ""
        self.femaleThigh = ""
        self.modAstLoadA = ""
        self.modAstLoadB = ""
        self.modAstHR = ""
        self.modAstCapacity = ""
        self.ebbelingHR = ""
        self.ebbelingLoad = ""
        self.ebbelingSpeed = ""
        self.RMTestExA = ""
        self.RMTestExB = ""
        self.RMTestExAWeight = ""
        self.RMTestExBWeight = ""

    # Calculations
    def getBMI(self):
        return float(self.weight) / (float(self.height) * float(self.height))

    def getThreeSiteMale(self):
        return 1.10938 - (0.0008267 * float(self.sumOfFolds)) + (0.0000016 * (float(self.sumOfFolds) * float(self.sumOfFolds))) - (0.0002574 * float(self.age))

    def getThreeSiteFemale(self):
        return 1.0994921 - (0.0009929 * float(self.sumOfFolds)) + (0.0000023 * (float(self.sumOfFolds) * float(self.sumOfFolds))) - (0.0001392 * float(self.age))

    def getSevenSiteMale(self):
        return 1.112 - (0.00043499 * float(self.sumOfFolds)) + (0.00000055 * (float(self.sumOfFolds) * float(self.sumOfFolds))) - (0.00028826 * float(self.age))

    def getSevenSiteFemale(self):
        return 1.097 - (0.00046971 * float(self.sumOfFolds)) + (0.00000056 * (float(self.sumOfFolds) * float(self.sumOfFolds))) - (0.00012828 * float(self.age))

    def getBodyFatThreeMale(self):
        return ((495 / float(self.getThreeSiteMale())) - 450)

    def getBodyFatThreeFemale(self):
        return ((495 / float(self.getThreeSiteFemale())) - 450)

    def getBodyFatSevenMale(self):
        return ((495 / float(self.getSevenSiteMale())) - 450)

    def getBodyFatSevenFemale(self):
        return ((495 / float(self.getSevenSiteFemale())) - 450)

    def getEbellingAerobic(self):
        if self.gender == "male" or self.gender == "Male" or self.gender == "M":
            genderModifier = 1
        else:
            genderModifier = 0
        return 15.1 + (21.8 * float(self.speed)) - (0.327 * float(self.testHR)) - (0.263 * float(self.speed) * float(self.age)) + (0.00504 * float(self.testHR) * float(self.age)) + (5.98 * float(self.genderModifier))

    def getRockportAerobic(self):
        if self.gender == "male" or self.gender == "Male" or self.gender == "M":
            genderModifier = 1
        else:
            genderModifier = 0
        return 132.853 - (0.0769 * float(self.loadLBS)) - (0.3877 * float(self.age)) + (6.315 * float(self.genderModifier)) - (0.32649 * float(self.time)) - (0.1565 * float(self.testHR))

    def getCooperAerobic(self):
        return (35.97 * float(self.distanceMiles)) - 11.29

    def getVertJump(self):
        return(60.7 * float(self.jumpHeight)) + (45.3 * float(self.bodyMass)) - 2055

    def getRepMaxPredict(self):
        return (1.0 + 0.0333 * float(self.reps)) * float(self.repWeight)
