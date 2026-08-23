import random

class Dice:
    def __init__(self, value=random.choice(range(1, 7))):
        if (1<= value <= 6):
            self.value = value

    held = 0

def RerollDice(self):
    pass

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
            if (type(i) != Dice):
                break
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

    def NewDice(self, d1, d2, d3, d4, d5):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
 
    filled = 0
    score = 0

class Score1(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = 1 * self.GetConstDiceValues(1)
        return score

class Score2(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)
        
    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = 2 * self.GetConstDiceValues(2)
        return score


class Score3(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)
        
    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = 3 * self.GetConstDiceValues(3)
        return score


class Score4(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = 4 * self.GetConstDiceValues(4)
        return score

class Score5(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = 5 * self.GetConstDiceValues(5)
        return score

class Score6(ScoreBox):
    def __init__(self, d1, d2, d3, d4, d5):
        super().__init__(d1, d2, d3, d4, d5)

    def FillBox(self, score=None):
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        score = 6 * self.GetConstDiceValues(6)
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
        if (self.SetOfX(4, 1) == 1):
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
        score = self.ScoreCalc()
        return super().FillBox(score)

    def ScoreCalc(self):
        if (self.SetOfX(5,0) == 1):
            score = 50 # score = 50 if first time filling
            if (self.filled == 1 and self.score != 0):  # if not first time filling and didnt fill in 0, add 100 to the filled in score and return that
                score = self.score + 100
                self.filled = 0 # needed so box can be refilled
        else:
            score = 0
        return score

class GameSetup:
    def __init__(self):
        dice_values = random.choices(range(1,7), k = 5)
        d1 = Dice(dice_values[0])
        d2 = Dice(dice_values[1])
        d3 = Dice(dice_values[2])
        d4 = Dice(dice_values[3])
        d5 = Dice(dice_values[4])
        self.dice = [d1, d2, d3, d4, d5]

        s1 = Score1(*self.dice)
        s2 = Score2(*self.dice)
        s3 = Score3(*self.dice)
        s4 = Score4(*self.dice)
        s5 = Score5(*self.dice)
        s6 = Score6(*self.dice)
        s3k = Score3OfAKind(*self.dice)
        s4k = Score4OfAKind(*self.dice)
        sfh = ScoreFullHouse(*self.dice)
        sss = ScoreSmallStraight(*self.dice)
        sls = ScoreLargeStraight(*self.dice)
        sc = ScoreChance(*self.dice)
        sy = ScoreYahtzee(*self.dice)
        self.scores = [s1, s2, s3, s4, s5, s6, s3k, s4k, sfh, sss, sls, sc, sy]
        
    def ScoreCalcAll(self):
        class Node:
            def __init__(self, data: ScoreBox):
                self.data = {"type": type(data), "data": data.ScoreCalc()}
                self.left = None
                self.right = None
                self.count = 1

        def insert(root: Node, data: ScoreBox):
            score = data.ScoreCalc()
            #print("score: ", score, " type: ", type(data))
            if (root == None):
                #print(type(data), " inserted!")
                return Node(data)
            elif (root.data["data"] > score):         # if current node's calculated score is greater than new scorebox's calculated
                #print(root.data["type"],"data: ", root.data["data"], " is larger than ", type(data), "data: ", score)
                root.left = insert(root.left, data) # score, pass that same scorebox down.
            elif (root.data["data"] < score):
                #print(root.data["type"],"data: ", root.data["data"], " is smaller than ", type(data), "data: ", score)
                root.right = insert(root.right, data)
            elif (root.data["data"] == score):
                root.count += 1                                                 # if multiple scoreboxes have the same score
                if (type(root.data["type"]) is not set):                        # then we can keep track of which are similar without
                    root.data.update({"type": {root.data["type"], type(data)}}) # making the tree larger
                root.data["type"].add(type(data))
                #print(type(data), " added to node with ", root.data["type"])
            return root

        def inorder(root):
            if root:
                inorder(root.left)
                print("data: ", root.data["data"], "count: ", root.count, "type: ", root.data["type"])
                inorder(root.right)

        bst = None
        for box in self.scores:
            #print("Inserting: ", type(box))
            bst = insert(bst, box)
            #print()
        inorder(bst)

class Turn():
    turn_count = 1
    def __init__(self):
        pass

    def new_turn(self):
        rerolls = 3


