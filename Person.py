class Person():
    def __init__(self):
        # person attributes
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

    # Calculations
    def getBMI(self):
        return self.weight / (self.height * self.height)

    def getThreeSiteMale(self):
        return 1.10938 - (0.0008267 * self.sumOfFolds) + (0.0000016 * (self.sumOfFolds * self.sumOfFolds)) - (0.0002574 * self.age)

    def getThreeSiteFemale(self):
        return 1.0994921 - (0.0009929 * self.sumOfFolds) + (0.0000023 * (self.sumOfFolds * self.sumOfFolds)) - (0.0001392 * self.age)

    def getSevenSiteMale(self):
        return 1.112 - (0.00043499 * self.sumOfFolds) + (0.00000055 * (self.sumOfFolds * self.sumOfFolds)) - (0.00028826 * self.age)

    def getSevenSiteFemale(self):
        return 1.097 - (0.00046971 * self.sumOfFolds) + (0.00000056 * (self.sumOfFolds * self.sumOfFolds)) - (0.00012828 * self.age)

    def getBodyFatThreeMale(self):
        return (495 / self.getThreeSiteMale())

    def getBodyFatThreeFemale(self):
        return (495 / self.getThreeSiteFemale())

    def getBodyFatSevenMale(self):
        return (495 / self.getSevenSiteMale())

    def getBodyFatSevenFemale(self):
        return (495 / self.getSevenSiteFemale())

    def getEbellingAerobic(self):
        if self.gender == "male" or self.gender == "Male" or self.gender == "M":
            genderModifier = 1
        else:
            genderModifier = 0
        return 15.1 + (21.8 * self.speed) - (0.327 * self.testHR) - (0.263 * self.speed * self.age) + (0.00504 * self.testHR * self.age) + (5.98 * self.genderModifier)

    def getRockportAerobic(self):
        if self.gender == "male" or self.gender == "Male" or self.gender == "M":
            genderModifier = 1
        else:
            genderModifier = 0
        return 132.853 - (0.0769 * self.loadLBS) - (0.3877 * self.age) + (6.315 * self.genderModifier) - (0.32649 * self.time) - (0.1565 * self.testHR)

    def getCooperAerobic(self):
        return (35.97 * self.distanceMiles) - 11.29

    def getRepMaxPredict(self):
        return (1.0 + 0.0333 * self.reps) * self.repWeight
