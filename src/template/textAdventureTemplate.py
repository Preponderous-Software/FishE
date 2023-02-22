class TextAdventureTemplate:
    def __init__(self):

        self.descriptor = "Default descriptor"
        self.prompt = "Make your choice!"
        self.optionList = []

        self.times = {
            0: "12:00 AM",
            1: "1:00 AM",
            2: "2:00 AM",
            3: "3:00 AM",
            4: "4:00 AM",
            5: "5:00 AM",
            6: "6:00 AM",
            7: "7:00 AM",
            8: "8:00 AM",
            9: "9:00 AM",
            10: "10:00 AM",
            11: "11:00 AM",
            12: "12:00 PM",
            13: "1:00 PM",
            14: "2:00 PM",
            15: "3:00 PM",
            16: "4:00 PM",
            17: "5:00 PM",
            18: "6:00 PM",
            19: "7:00 PM",
            20: "8:00 PM",
            21: "9:00 PM",
            22: "10:00 PM",
            23: "11:00 PM",
        }

    def lotsOfSpace(self):
        print("\n" * 20)

    def divider(self):
        print("\n")
        print("-" * 75)
        print("\n")

    def showOptions(
        self,
        descriptor,
        prompt,
        optionList,
        dayVariable,
        timeVariable,
        moneyVariable,
        fishVariable,
    ):
        self.descriptor = descriptor
        self.prompt = prompt
        self.optionList = optionList
        self.dayVariable = dayVariable
        self.timeVariable = timeVariable
        self.moneyVariable = moneyVariable
        self.fishVariable = fishVariable

        self.lotsOfSpace()
        self.divider()
        print(" " + self.descriptor)
        self.divider()
        print(" Day %d" % self.dayVariable)
        print(" | " + self.times[self.timeVariable])
        print(" | Money: $%d" % self.moneyVariable)
        print(" | Fish: %d" % self.fishVariable)
        print("\n " + self.prompt)
        self.divider()
        self.n = 1
        self.listOfN = []
        for option in self.optionList:
            print(" [%d] %s" % (self.n, option))
            self.listOfN.append("%d" % self.n)
            self.n += 1

        self.choice = input("\n> ")
        for i in self.listOfN:
            if self.choice == i:
                return self.choice
        self.changePrompt = "Try again!"
        return self.showOptions(
            self.descriptor,
            self.changePrompt,
            self.optionList,
            self.dayVariable,
            self.timeVariable,
            self.moneyVariable,
            self.fishVariable,
        )