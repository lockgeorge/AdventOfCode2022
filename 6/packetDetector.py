import sys

string = sys.argv[1]
packetSize = 14
test = []
idx = 0
for i in string:
    idx += 1
    if len(test)>packetSize-1:
        test = test[1:]
    if i in test:
        test = test[test.index(i)+1:]
    elif len(test) == packetSize-1:
        print(idx)
        break
    test.append(i)
