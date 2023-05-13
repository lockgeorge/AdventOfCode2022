data = open('test_data.txt','r')
food = [0]
for c in data:
    if c == '\n':
        food.append(0)
    else:
        food[len(food)-1] = food[len(food)-1]+int(c.strip('\n'))
#print(food)
mostCals = max(food)
elfNum = food.index(mostCals)+1
print(f'Elf number {elfNum} has the most food at {mostCals}')
data.close()
food.sort(reverse=True)
print(sum(food[0:3]))
    

