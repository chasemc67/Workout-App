class Person():
    def __init__(self):
        # person attributes
        self.height = 0
        self.weight = 0
        self.age = 0
        self.gender = 0
        self.restHR = 0
        self.restBP = 0
        self.hipCirc = 0
        self.waistCirc = 0
        self.armCirc = 0
        self.thighCirc = 0
        self.chestCirc = 0
        self.mbToss = 0
        self.vertReach = 0
        self.vertJump = 0
        self.repMaxTestWeight = 0
        self.repMaxPredictWeight = 0
        self.gripStrengthLeft = 0
        self.gripStrenghtRight = 0
        self.pushUp = 0
        self.curlUp = 0
        self.PlankEndurance = 0
        self.WallSit = 0
        self.SitReach = 0
        self.SLstanceOpenLeft = 0
        self.SLstanceOpenRight = 0
        self.SLstanceClosedLeft = 0
        self.SLstanceClosedRight = 0
        self.deepSquatScreen = 0
        self.wallSlideScreen = 0
        self.hipHingeScreen = 0
        self.speed = 0
        self.testHR = 0
        self.PlankScreen = 0
        self.sumOfFolds= 0
        self.load = 0
        self.loadLBS = 0
        self.time = 0
        self.reps = 0
        self.repWeight = 0
        self.distance = 0
        self.distanceMiles = 0


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
