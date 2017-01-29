class Person():
    def __init__(self):
        # person attributes
        self.armCirc = ""
        self.birthDate = ""
        self.chestCirc = ""
        self.cooperDist = ""
        self.curlUpNum = ""
        self.deepSquatRate = ""
        self.ebbelingHR = ""
        self.ebbelingWork = ""
        self.ebbelingWU = ""
        self.frontPlankRate = ""
        self.gender = ""
        self.gripStrengthRight = ""
        self.gripStrengthLeft = ""
        self.height = ""
        self.hipCirc = ""
        self.hipHingeRate = ""
        self.modAstHR = ""
        self.modAstLoadA = ""
        self.modAstLoadB = ""
        self.modAstAerobic = ""
        self.name = ""
        self.phoneNumber = ""
        self.plankTime = ""
        self.pushUpNum = ""
        self.restBP = ""
        self.restHR = ""
        self.RMTestExA = ""
        self.RMTestExAWeight = ""
        self.RMTestExB = ""
        self.RMTestExBWeight = ""
        self.RMPredictEx = ""
        self.RMPredictReps = ""
        self.RMPredictLoad = ""
        self.rockportHR = ""
        self.rockportTime = ""
        self.seatMBDist = ""
        self.sitReachDist = ""
        self.SLCloseLeft = ""
        self.SLCloseRight = ""
        self.SLOpenLeft = ""
        self.SLOpenRight = ""
        self.svnSiteChest = ""
        self.svnSiteMidAx = ""
        self.svnSiteTri = ""
        self.svnSiteScap = ""
        self.svnSiteSupra = ""
        self.svnSiteAb = ""
        self.svnSiteThigh = ""
        self.testDate = ""
        self.thighCirc = ""
        self.threeSiteMaleChest = ""
        self.threeSiteMaleAb = ""
        self.threeSiteMaleThigh = ""
        self.threeSiteFemaleSupra = ""
        self.threeSiteFemaleTricep = ""
        self.threeSiteFemaleThigh = ""
        self.vertJumpBest = ""
        self.vertJumpSR = ""
        self.waistCirc = ""
        self.wallSitTime = ""
        self.wallSlideRate = ""
        self.weight = ""

        self.framesChecked = list()


    # Database Functions
        # returns a list of names of attributes
        # Excluding the list of frames checked
    def getAttributes(self):
        #attrList = list()
        #for A in dir(self):
        #    if not A.startswith('__') and not callable(getattr(self, A)) and not A.startswith('framesChecked'):
        #        attrList.append(A)
        #return(attrList)
        return ['RMPredictEx', 'RMPredictLoad', 'RMPredictReps', 'RMTestExA', 'RMTestExAWeight', 'RMTestExB', 'RMTestExBWeight', 'SLCloseLeft', 'SLCloseRight', 'SLOpenLeft', 'SLOpenRight', 'armCirc', 'birthDate', 'chestCirc', 'cooperDist', 'curlUpNum', 'deepSquatRate', 'ebbelingHR', 'ebbelingWU', 'ebbelingWork', 'frontPlankRate', 'gender', 'gripStrengthLeft', 'gripStrengthRight', 'height', 'hipCirc', 'hipHingeRate', 'modAstAerobic', 'modAstHR', 'modAstLoadA', 'modAstLoadB', 'name', 'phoneNumber', 'plankTime', 'pushUpNum', 'restBP', 'restHR', 'rockportHR', 'rockportTime', 'seatMBDist', 'sitReachDist', 'svnSiteAb', 'svnSiteChest', 'svnSiteMidAx', 'svnSiteScap', 'svnSiteSupra', 'svnSiteThigh', 'svnSiteTri', 'testDate', 'thighCirc', 'threeSiteFemaleSupra', 'threeSiteFemaleThigh', 'threeSiteFemaleTricep', 'threeSiteMaleAb', 'threeSiteMaleChest', 'threeSiteMaleThigh', 'vertJumpBest', 'vertJumpSR', 'waistCirc', 'wallSitTime', 'wallSlideRate', 'weight']

    # todo fix this shit
    def getAge(self):
        return 20

    # Calculations
    def getBMI(self):
        return float(self.weight) / (float(self.height) * float(self.height))

    def getSumOfFolds(self):
        if self.gender.lower() == "male" or self.gender.lower() == "m":
            return float(self.threeSiteMaleChest) + float(self.threeSiteMaleAb) + float(self.threeSiteMaleThigh)
        else:
            return float(self.threeSiteFemaleSupra) + float(self.threeSiteFemaleTricep) + (self.threeSiteFemaleThigh)

    def getThreeSiteMale(self):
        return 1.10938 - (0.0008267 * float(self.sumOfFolds)) + (0.0000016 * (float(self.sumOfFolds) * float(self.sumOfFolds))) - (0.0002574 * float(self.age))

    def getThreeSiteFemale(self):
        return 1.0994921 - (0.0009929 * float(self.sumOfFolds)) + (0.0000023 * (float(self.sumOfFolds) * float(self.sumOfFolds))) - (0.0001392 * float(self.age))

    def getSevenSiteDensity(self):
        if self.gender.lower() == "male" or self.gender.lower() == "m":
            return 1.112 - (0.00043499 * float(self.sumOfFolds)) + (0.00000055 * (float(self.sumOfFolds) * float(self.sumOfFolds))) - (0.00028826 * float(self.getAge()))
        else:
            return 1.097 - (0.00046971 * float(self.sumOfFolds)) + (0.00000056 * (float(self.sumOfFolds) * float(self.sumOfFolds))) - (0.00012828 * float(self.getAge()))

    def getBodyFatThreeMale(self):
        return ((495 / float(self.getThreeSiteMale())) - 450)

    def getBodyFatThreeFemale(self):
        return ((495 / float(self.getThreeSiteFemale())) - 450)

    def getBodyFatSeven(self):
        if self.gender.lower() == "male" or self.gender.lower() == "m":
            return ((495 / float(self.getSevenSiteMale())) - 450)
        else:
            return ((495 / float(self.getSevenSiteFemale())) - 450)

    def getEbellingAerobic(self):
        if self.gender.lower() == "male" or self.gender.lower() == 'm':
            genderModifier = 1
        else:
            genderModifier = 0
        return 15.1 + (21.8 * float(self.ebbelingWork)) - (0.327 * float(self.ebbelingHR)) - (0.263 * float(self.ebbelingWork) * float(self.getAge())) + (0.00504 * float(self.ebbelingHR) * float(self.getAge())) + (5.98 * float(self.genderModifier))

    def getRockportAerobic(self):
        if self.gender.lower() == "male" or self.gender.lower() == "m":
            genderModifier = 1
        else:
            genderModifier = 0
        return 132.853 - (0.0769 * (float(self.weight) * 2.20462)) - (0.3877 * float(self.getAge())) + (6.315 * float(self.genderModifier)) - (0.32649 * float(self.rockportTime)) - (0.1565 * float(self.rockportHR))

    def getCooperAerobic(self):
        return (35.97 * float(self.cooperDist)) - 11.29

    def getVertJumpBest(self):
        return (float(self.vertJumpBest) - float(self.vertJumpSR))

    def getVertJumpPower(self):
        return (60.7 * float(self.vertJumpBest)) + (45.3 * float(self.weight)) - 2055

    def getRepMaxPredict(self):
        return (1.0 + 0.0333 * float(self.RMPredictReps)) * float(self.RMPredictLoad)
