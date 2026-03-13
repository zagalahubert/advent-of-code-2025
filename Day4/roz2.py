f = open("input.txt")
i=0
ans = 0
tab = []
for line in f:
    line = line.strip()
    line = list(line)

    tab.append(line)
    i+=1

def fun(tab):
    ans = 0
    memory = []
    for row in range(len(tab)):
        for col in range(len(tab[0])):
            if tab[row][col] == '@':
                counter = 0

                up = -1
                down = 2
                left = -1
                right = 2

                if row==0:
                    up = 0
                if row==len(tab)-1:
                    down = 1
                if col==0:
                    left = 0
                if col == len(tab[0]) -1:
                    right = 1 

                for i in range(left,right):
                    for j in range(up,down):
                        if tab[row+j][col+i]=='@':
                            if i==0 and j==0:
                                continue
                            counter+=1
                if counter<4:
                    memory.append((row,col))
                    ans+=1
    if ans == 0:
        return False
    for k in range(len(memory)):
        tab[memory[k][0]][memory[k][1]] = '.'
    return tab, ans

odp = fun(tab) 
finnal_ans = 0
finnal_ans += odp[1]

while True :
    odp = fun(odp[0])
    if not odp:
        break
    finnal_ans += odp[1]


print(finnal_ans)
