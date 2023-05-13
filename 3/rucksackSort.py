elvesPerGroup = 3

def priority(item):
    dec = ord(item)
    if dec > 96:
        return dec-96
    else:
        return dec - 38

    
def compareCompartments(pack):
    compartmentSize = int(len(pack.strip('\n'))/2)
    for i in range(compartmentSize):
        testItem = pack[i]
        for j in range(compartmentSize):
            if testItem == pack[compartmentSize+j]:
                return testItem

def findBadge(packs):
    badge = set(packs[0])
    for i in range(1,elvesPerGroup):
        badge = badge & set(packs[i])
    return badge

packs = open('packingList.txt','r')
totalPriority = 0
for elf in packs:
    totalPriority += priority(compareCompartments(elf))

print(f'The total priority of items for single elves is {totalPriority}.')
packs.close()
totalPriority = 0
with open('packingList.txt','r') as packs:
    packList = packs.readlines()
    for i in range(0,len(packList),elvesPerGroup):
        groupPacks = []
        for j in range(elvesPerGroup):
            groupPacks.append(packList[i+j].strip('\n'))
        totalPriority += priority(findBadge(groupPacks).pop())
print(f'The total priority for badges is {totalPriority}')    
