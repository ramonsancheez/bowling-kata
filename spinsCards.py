import string
class SpinsCards:
    def __init__(self, pins):
        self.pins = pins

    # Sustituye los - por 0 y elimina los espacios en blanco
    def replaceDash(self):
        self.pins = self.pins.replace("-", "0")
        self.pins = self.pins.replace(" ", "")

    # Calcula la tirada de bolos
    def calculatePins(self):
        self.replaceDash()
        pins = self.pins
        isSpare, isStrike = False, False
        strikesInARow, totalPuntuation, frame = 0, 0, 0
        multiplier, multiplierInTwo = 1, 1

        for bowlingToss in range(len(pins)):
            framePuntuation = 0
            
            # Si es strike, spare o número
            match pins[bowlingToss]:
                case "/":
                    framePuntuation = (10 - int(pins[bowlingToss-1])) * multiplier
                    strikesInARow = 0 
                    frame += 0.5
                    isSpare = True
                case "X":
                    framePuntuation = 10 * multiplier 
                    strikesInARow += 1
                    frame += 1
                    isStrike = True
                case _:
                    framePuntuation = int(pins[bowlingToss]) * multiplier
                    strikesInARow = 0
                    frame += 0.5
            
            multiplier = multiplierInTwo
            multiplierInTwo = 1

            # Tirada siguiente  a "/"
            if isSpare and pins[bowlingToss] != "/" and frame <= 10:
                framePuntuation *= 2
                isSpare = False

            # Tirada siguiente a "X"
            if isStrike and frame <= 9:
                multiplier, multiplierInTwo = self.strike(strikesInARow)
            else:
                pass
            isStrike = False

            totalPuntuation += framePuntuation

        return totalPuntuation

    # Si es strike:
    def strike(self, strikesInARow):
        multiplier = 1
        multiplierInTwo = 2
        if strikesInARow >= 2:
            multiplier *= 3
        else:
            multiplier *= 2
        return multiplier, multiplierInTwo

if __name__ == '__main__':
    def prueba():
        pins = "12345123451234512345"
        total = 60
        spinsCards = SpinsCards(pins)
        assert spinsCards.calculatePins() == total
    prueba()