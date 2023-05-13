assignments = open('test_data.txt','r')
pairs = []
OVpairs = []
for line in assignments:
    elf = line.strip('\n')
    elf = elf.split(',')
    for i in range(len(elf)):
        elf[i] = list(map(int,elf[i].split('-')))
    elfset1 = set(range(elf[0][0],elf[0][1]+1))
    if not elfset1:
        elfset1 = set([elf[0][0]])
    elfset2 = set(range(elf[1][0],elf[1][1]+1))
    if not elfset2:
        elfset2 = set([elf[1][0]])
    #print(elfset1)
    #print(elfset2)
    
    if len(elfset1) >= len(elfset2):
        pairs.append(int(elfset1.issuperset(elfset2)))
    else:
        pairs.append(int(elfset1.issubset(elfset2)))
    OVpairs.append(int(not elfset1.isdisjoint(elfset2)))
print(sum(pairs))
print(sum(OVpairs))
assignments.close()
