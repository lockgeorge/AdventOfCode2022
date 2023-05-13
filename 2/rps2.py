def move(O,Outcome):
    move = O + Outcome - 1
    #print(move)
    if move == -1:
        move = 2
    elif move == 3:
        move = 0
    return move

strat = open('strategy_guide.txt','r')
score = 0
OMoves = ['A', 'B', 'C']
Outcomes = ['X', 'Y', 'Z']
for i in strat:
    outcomeScore = Outcomes.index(i[2])*3
    moveScore = move(OMoves.index(i[0]),Outcomes.index(i[2]))+1
    #print(f'Score = {score+moveScore+outcomeScore} = {score} + {moveScore} + {outcomeScore}')
    score += moveScore+outcomeScore

print(score)
