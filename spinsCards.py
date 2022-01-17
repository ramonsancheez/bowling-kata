import string

class spinsCards:
    def __init__(self, pins):
        self.pins = pins
        self.totalPuntuation = self.calculatePins(pins)

    def setTotal(self, totalPuntuation):
        self.totalPuntuation = totalPuntuation

    def getTotal(self):
        return self.totalPuntuation

    def calculatePins(self, pins):
        isSpare, isStrike = False, False

        for bowlingToss in range(len(pins)):
            tossStrike = 0
            framePuntuation = 0

            # Si es strike, spare, 0 o número
            if pins[bowlingToss] not in string.digits:
                match pins[bowlingToss]:
                    case "/":
                        framePuntuation = 10 - int(pins[bowlingToss-1])
                        isSpare = True
                        break
                    case "X":
                        framePuntuation = 10
                        tossStrike += 2
                        isStrike = True
                        break
                    case "-":
                        framePuntuation = 0
                        break
            else:
                framePuntuation = int(pins[bowlingToss])
            
            # Tirada siguiente  a "/"
            if isSpare:
                framePuntuation *= 2
                isSpare = False

            # Tirada siguiente a "X"
            if tossStrike != 0:
                if isStrike:
                    framePuntuation *=3
                    isStrike = False
                else:
                    framePuntuation *=2
                    
                tossStrike -= 1

            totalPuntuation += framePuntuation

        return totalPuntuation