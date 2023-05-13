assignments = open('test_data.txt','r')
pairs = []
OVpairs = []
elfset = ['']*3
for line in assignments:
    elf = line.strip('\n')
    elf = elf.split(',')
    for i in range(len(elf)):
        elf[i] = list(map(int,elf[i].split('-')))
        elfset[i] = set(range(elf[i][0],elf[i][1]+1))
    if len(elfset[0]) >= len(elfset[1]):
        pairs.append(int(elfset[0].issuperset(elfset[1])))
    else:
        pairs.append(int(elfset[0].issubset(elfset[1])))
    OVpairs.append(int(not elfset[0].isdisjoint(elfset[1])))
print(sum(pairs))
print(sum(OVpairs))
assignments.close()
