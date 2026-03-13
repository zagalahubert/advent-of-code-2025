plik = open('input.txt')

tab = []
op = ""
sum = 0

for line in plik:
    line = line.strip()
    if  not (line.startswith('+') or line.startswith('*')):
        tab.append(line)
        continue
    op = line


def fun(tab):
    temp = []
    s = ""
    for i in range(len(tab)):
        if tab[i] == " " and tab[i+1] == " ":
            continue
        elif tab[i] == " ":
            temp.append(int(s))
            s = ""
        else:
            s+=tab[i]
    temp.append(int(s))
    return temp

tab = list(map(fun,tab))


idx = 0
temp = 0

for j in range(len(op)):
    if op[j] == " ":
        continue
    elif op[j] == '*':
        temp = 1
        for i in range(len(tab)):
            temp*=tab[i][idx]
        sum+=temp
        idx+=1
    elif op[j] == '+':
        temp = 0
        for i in range(len(tab)):
            temp+=tab[i][idx]
        sum+=temp
        idx+=1

print(sum)