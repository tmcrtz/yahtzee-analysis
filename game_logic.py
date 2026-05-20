import random

class Dice:
    def __init__(self, value=random.randint(1,6)):
        if (1<= value <= 6):
            self.value = value
        else:
            value = random.randint(1,6)
    
    def Reroll(self):
        if (self.rerolls > 0 and self.held != 0):
            self.value = random.randint(1, 6)
            self.rerolls -= 1

    rerolls = 3
    held = 0

class ScoreBox:
    def __init__(self, d1, d2, d3, d4, d5):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5

    def FillBox(self, score):
        if (self.filled == 0):
            self.score = score
            self.filled = 1
            return 1
        else:
            return 0

    def GetConstDiceValues(self, target):
        count = 0
        for i in vars(self).values():
            if (i.value == target): 
                count += 1
        return count

    def DiceValuesToArr(self):
        arr = []
        for i in vars(self).values():
           arr.append(i.value)
        return arr

    def CountEachVal(self):
        arr = list(self.DiceValuesToArr())
        count = [0] * (len(arr) + 1)
        while len(arr) > 0:
            num = arr.pop(0)
            count[num-1] += 1
        return count

    def AddAllDiceValues(self):
        arr = list(self.DiceValuesToArr())
        total = 0
        for i in arr:
            total += i
        return total
    
    def SetOfX (self, target, greaterToo):
        count = list(self.CountEachVal())
        for i in range(len(count)):
            if (count[i] >= target and greaterToo):
                return 1
            elif (count[i] == target and not greaterToo):
                return 1
        return 0

    def CheckStraight(self, smallOrLarge):
        count = list(self.CountEachVal())
        num = 0
        for i in range(len(count)):
            if (count[i]):
                num += 1
            else:
                num = 0
            if (num == (4 + smallOrLarge)):
                return 1
        return 0
 
    filled = 0
    score = 0

class Score1(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = self.GetConstDiceValues(1)
        return score

class Score2(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)
        
    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = self.GetConstDiceValues(2)
        return score


class Score3(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)
        
    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = self.GetConstDiceValues(3)
        return score


class Score4(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = self.GetConstDiceValues(4)
        return score

class Score5(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = self.GetConstDiceValues(5)
        return score

class Score6(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = self.GetConstDiceValues(6)
        return score

class Score3OfAKind(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        if (self.SetOfX(3, 1) == 1):
            score = self.AddAllDiceValues()
        else:
            score = 0
        return score
 
class Score4OfAKind(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        if (self.SetOfX(4, 0) == 1):
            score = self.AddAllDiceValues()
        else:
            score = 0
        return score


class ScoreFullHouse(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        if ((self.SetOfX(3, 0) == 1) and (self.SetOfX(2, 0) == 1)):
            score = 25
        else:
            score = 0
        return score


class ScoreSmallStraight(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        if (self.CheckStraight(0) == 1):
            score = 30
        else:
            score = 0
        return score


class ScoreLargeStraight(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        if (self.CheckStraight(1) == 1):
            score = 30
        else:
            score = 0
        return score


class ScoreChance(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = self.AddAllDiceValues()
        return score

class ScoreYahtzee(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        if (self.SetOfX(5,0) == 1):
            score = 50
        else:
            score = 0
        return super().FillBox(score)

    def Checkmark(self):
        if ((self.SetOfX(5,0) == 1) and (self.filled == 1)):
            if (not (self.score == 0)):
                self.score += 100

    def ScoreCalc(self):


