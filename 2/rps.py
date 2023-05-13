def outcome(O,M):
    outcomeNum = M-O
    if outcomeNum == 0:
        return 3
    elif outcomeNum == 1 or outcomeNum == -2:
        return 6
    else:
        return 0


strat = open('strategy_guide.txt','r')
score = 0
OMoves = ['A', 'B', 'C']
MMoves = ['X', 'Y', 'Z']
for i in strat:
    moveScore = MMoves.index(i[2])+1
    outcomeScore = outcome(OMoves.index(i[0]),MMoves.index(i[2]))
    #print(f'Score = {score+moveScore+outcomeScore} = {score} + {moveScore} + {outcomeScore}')
    score += moveScore+outcomeScore

print(score)
