import game_logic as gl

def main():
    d1 = gl.Dice(1)
    d2 = gl.Dice(2)
    d3 = gl.Dice(3)
    d4 = gl.Dice(4)
    d5 = gl.Dice(5)

    d6 = gl.Dice(3)
    d7 = gl.Dice(3)
    d8 = gl.Dice(3)
    d9 = gl.Dice(5)
    d10 = gl.Dice(5)

    d11 = gl.Dice(6)
    d12 = gl.Dice(6)
    d13 = gl.Dice(6)
    d14 = gl.Dice(6)
    d15 = gl.Dice(6)

    print("=========TEST PARENT SCOREBOX CLASS==========")

    testscore_1 = gl.ScoreBox(d1,d2,d3,d4,d5)
    print("testscore_1 d1 value: ", testscore_1.d1.value)
    print("testscore_1 d1 type:", type(testscore_1.d1.value))
    for i in vars(testscore_1).values():
        print(i.value)

    testscore_2 = gl.ScoreBox(d6,d7,d8,d9,d10)
    print("testscore_2 d1 value: ", testscore_2.d1.value)
    print("testscore_2 d1 type:", type(testscore_2.d1.value))
    for i in vars(testscore_2).values():
        print(i.value)

    testscore_3 = gl.ScoreBox(d11,d12,d13,d14, d15)
    print("testscore_3 d1 value: ", testscore_3.d1.value)
    print("testscore_3 d1 type:", type(testscore_3.d1.value))
    for i in vars(testscore_3).values():
        print(i.value)

    print("==========FUNCTION TESTS==========")

    print("ts1 GetConstDiceValues(1): ", testscore_1.GetConstDiceValues(1))

    print("ts3 GetConstDiceValues(6): ", testscore_3.GetConstDiceValues(6))

    arr = list(testscore_1.DiceValuesToArr())
    print("ts1 DiceValuesToArr: ", arr)

    print("ts1 CountEachVal: ", testscore_1.CountEachVal())
    print("ts2 CountEachVal: ", testscore_2.CountEachVal())
    print("ts3 CountEachVal: ", testscore_3.CountEachVal())

    print("ts1 AddAllDiceValues: ", testscore_1.AddAllDiceValues())

    print("ts2 SetOfX(3, 0): ", testscore_2.SetOfX(3, 0))

    print("ts1 CheckStraight(1): ", testscore_1.CheckStraight(1))

    print("ts2 CheckStraight(1): ", testscore_2.CheckStraight(1))
    
    print("ts3 CheckStraight(0): ", testscore_3.CheckStraight(0))
    print("ts3 CheckStraight(1): ", testscore_3.CheckStraight(1))

    print("ts1 FillBox(50):", testscore_1.FillBox(50))
    print("ts1 FillBox(50):", testscore_1.FillBox(1))
    print("ts1.filled: ", testscore_1.filled)
    print("ts1.score: ", testscore_1.score)

    print("==========TEST CHILD SCOREBOX CLASSES==========")

    box_score1 = gl.Score1(d1,d2,d3,d4,d5)
    print("box_score1 d1 value: ", box_score1.d1.value)
    print("box_score1 d1 type:", type(box_score1.d1.value))
    for i in vars(box_score1).values():
        print(i.value)

    print("bs1.score: ",box_score1.score)
    print("bs1.filled: ",box_score1.filled)
    print("bs1 FillBox(): ", box_score1.FillBox())
    print("bs1.score: ",box_score1.score)
    print("bs1.filled: ",box_score1.filled)
 
    box_score2 = gl.Score2(d1,d2,d3,d4,d5)
    print("bs2 FillBox(): ", box_score2.FillBox())
    print("bs2.score: ", box_score2.score)

    box_score3 = gl.Score3(d1,d2,d3,d4,d5)
    print("bs3 FillBox(): ", box_score3.FillBox())
    print("bs3.score: ", box_score3.score)
 
    box_score4 = gl.Score4(d1,d2,d3,d4,d5)
    print("bs4 FillBox(): ", box_score4.FillBox())
    print("bs4.score: ", box_score4.score)
 
    box_score5 = gl.Score5(d1,d2,d3,d4,d5)
    print("bs5 FillBox(): ", box_score5.FillBox())
    print("bs5.score: ", box_score5.score)
 
    box_score6 = gl.Score6(d1,d2,d3,d4,d5)
    print("bs6 FillBox(): ", box_score6.FillBox())
    print("bs6.score: ", box_score6.score)
 
    box_score3kind = gl.Score3OfAKind(d1,d2,d3,d4,d5)
    print("bs3kind FillBox(): ", box_score3kind.FillBox())
    print("bs3kind.score: ", box_score3kind.score)
 
    box_score4kind = gl.Score4OfAKind(d1,d2,d3,d4,d5)
    print("bs4kind FillBox(): ", box_score4kind.FillBox())
    print("bs4kind.score: ", box_score4kind.score)
 
    box_scorefh = gl.ScoreFullHouse(d1,d2,d3,d4,d5)
    print("bsfh FillBox(): ", box_scorefh.FillBox())
    print("bsfh.score: ", box_scorefh.score)
 
    box_scoress = gl.ScoreSmallStraight(d1,d2,d3,d4,d5)
    print("bsss FillBox(): ", box_scoress.FillBox())
    print("bsss.score: ", box_scoress.score)
 
    box_scorels = gl.ScoreLargeStraight(d1,d2,d3,d4,d5)
    print("bsls FillBox(): ", box_scorels.FillBox())
    print("bsls.score: ", box_scorels.score)
 
    box_scorechance = gl.ScoreChance(d1,d2,d3,d4,d5)
    print("bschance FillBox(): ", box_scorechance.FillBox())
    print("bschance.score: ", box_scorechance.score)
 
    box_scoreyaht = gl.ScoreYahtzee(d11,d12,d13,d14,d15)
    print("bsyaht FillBox(): ", box_scoreyaht.FillBox())
    print("bsyaht.score: ", box_scoreyaht.score)

    print("bsyaht FillBox(): ", box_scoreyaht.FillBox())
    print("bsyaht.score: ", box_scoreyaht.score)

    box_scoreyaht.NewDice(d1,d2,d3,d4,d5)
    print("bsyaht FillBox(): ", box_scoreyaht.FillBox())
    print("bsyaht.score: ", box_scoreyaht.score)
    print("bsyaht FillBox(): ", box_scoreyaht.FillBox())
    print("bsyaht.score: ", box_scoreyaht.score)

    box_scoreyaht.NewDice(d11,d12,d13,d14,d15)
    print("bsyaht FillBox(): ", box_scoreyaht.FillBox())
    print("bsyaht.score: ", box_scoreyaht.score)
    print("bsyaht FillBox(): ", box_scoreyaht.FillBox())
    print("bsyaht.score: ", box_scoreyaht.score)



if __name__ == "__main__":
    main()

