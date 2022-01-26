import string

class spinsCards:
    def __init__(self, pins):
        self.pins = pins

    # Sustituye los - por 0
    def replaceDash(self):
        self.pins = self.pins.replace("-", "0")

    def calculatePins(self):
        self.replaceDash()
        multiplier = 1
        pins = self.pins
        isSpare, isStrike = False, False
        strikesInARow = 0
        totalPuntuation = 0
        multiplierInTwo = 1
        for bowlingToss in range(len(pins)):
            framePuntuation = 0
            
            # Si es strike, spare o número
            if pins[bowlingToss] not in string.digits:
                match pins[bowlingToss]:
                    case "/":
                        framePuntuation = (10 - int(pins[bowlingToss-1])) * multiplier
                        strikesInARow = 0 
                        isSpare = True
                    case "X":
                        framePuntuation = 10 * multiplier 
                        strikesInARow += 1
                        isStrike = True
            else:
                framePuntuation = int(pins[bowlingToss]) * multiplier
                strikesInARow = 0
            
            multiplier = multiplierInTwo
            multiplierInTwo = 1

            # Tirada siguiente  a "/"
            if isSpare and pins[bowlingToss] != "/":
                framePuntuation *= 2
                isSpare = False

            # Tirada siguiente a "X"
            if isStrike:
                multiplier, multiplierInTwo = self.Strike(strikesInARow)
            else:
                multiplier = 1
            totalPuntuation += framePuntuation

        print(totalPuntuation)
        return totalPuntuation

    def Strike(self, strikesInARow):
        multiplier = 1
        multiplierInTwo = 2
        if strikesInARow >= 2:
            multiplier *= 3
        else:
            multiplier *= 2
        return multiplier, multiplierInTwo

if __name__ == '__main__':
    def prueba():
        pins = "XXXXXXXXXXX9"
        total = 299
        SpinsCards = spinsCards(pins)
        assert SpinsCards.calculatePins() == total
    prueba()