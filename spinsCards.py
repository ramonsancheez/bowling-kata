import string

class spinsCards:
    def __init__(self, pins):
        self.pins = pins

    # Sustituye los - por 0
    def replaceDash(self):
        self.pins = self.pins.replace("-", "0")

    def calculatePins(self):
        self.replaceDash()
        pins = self.pins
        isSpare, isStrike = False, False
        i = 0
        totalPuntuation = 0
        for bowlingToss in range(len(pins)):
            framePuntuation = 0
            
            # Si es strike, spare o número
            if pins[bowlingToss] not in string.digits:
                match pins[bowlingToss]:
                    case "/":
                        framePuntuation = 10 - int(pins[bowlingToss-1])
                        isSpare = True
                    case "X":
                        framePuntuation = 10
                        isStrike = True
            else:
                framePuntuation = int(pins[bowlingToss])
            
            # Tirada siguiente  a "/"
            if isSpare and pins[bowlingToss] != "/":
                framePuntuation *= 2
                isSpare = False

            # Tirada siguiente a "X"
            if i != 0:
                framePuntuation *= 2
                i -= 1
                
            totalPuntuation += framePuntuation

            if isStrike:
                i += 2
                isStrike = False

        print(totalPuntuation)
        return totalPuntuation

if __name__ == '__main__':
    def prueba():
        pins = "XXX"
        total = 60
        SpinsCards = spinsCards(pins)
        assert SpinsCards.calculatePins() == total
    prueba()