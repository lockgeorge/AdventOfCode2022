from parse import *

def rotateArray(stack):
    rotStack = []
    for i in range(len(stack)):
        for j in range(len(stack[0])):
            if i == 0:
                rotStack.append([])
            if stack[i][j] != ' ':
                rotStack[j].insert(0,stack[i][j])
    return(rotStack)

plan = open('stacks.txt','r')
stack = []
stack_complete = 0
for line in plan:
    if stack_complete == 0:
        if line != '\n':
            row = line[1::4]
            stack.append([*row])
        else:
            stack_complete = 1
            stack.pop()
            stack = rotateArray(stack)
            print(stack)
    else:
        instruction = parse("move {} from {} to {}",line)
        stack[int(instruction[2])-1].extend(*[stack[int(instruction[1])-1][len(stack[int(instruction[1])-1])-int(instruction[0]):]])
        stack[int(instruction[1])-1]=stack[int(instruction[1])-1][:len(stack[int(instruction[1])-1])-int(instruction[0])]        
            
print(stack)
output = ''  
for i in stack:
    output=output+i.pop()
print(output)
plan.close()


