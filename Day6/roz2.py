plik = open('input.txt')

tab = []
opstr = []
sum = 0

for line in plik:
    line = line.rstrip('\n')
    if  not (line.startswith('+') or line.startswith('*')):
        tab.append(line)
        continue
    opstr = list(line)




idxfst = 0
idxsnd = 0
strlicz = []
readytab = []

while True:
    if idxsnd+2 >= len(opstr):
        strlicz = []
        temp = []
        for line in tab:
            temp = list(line[idxfst:idxsnd+2])
            strlicz.append(temp)
        readytab.append(strlicz)
        break

    if opstr[idxsnd+2] in "+*":
        strlicz = []
        temp = []
        for line in tab:
            temp = list(line[idxfst:idxsnd+1])
            strlicz.append(temp)
        readytab.append(strlicz)
        idxfst = idxsnd+2

    idxsnd+=1




#Transposition

def fun(tab):
    temp = ""
    liczby = []
    idxstr = 0
    for i in range(len(tab[0])):
        for j in range(len(tab)):
            temp+=tab[j][i]
        liczby.append(int(temp))
        temp = ""
    return liczby

liczby = list(map(fun, readytab))



def fun1(x):
    return 0 if x == " " else 1
opstr = list(filter(fun1,opstr))



for op in range(len(opstr)):
    if opstr[op] == "+":
        for i in range(len(liczby[op])):
            sum+=liczby[op][i]
    else:
        temp = 1
        for i in range(len(liczby[op])):
            temp*=liczby[op][i]
        sum+=temp

print(sum)