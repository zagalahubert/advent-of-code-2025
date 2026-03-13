plik = open("input2.txt")

pom = []
temp = []

for line in plik:
    line = line.strip()
    if line.find('-') != -1:
        pom.append(line)

def fun(i):
    return list(i.split('-'))

pom = list(map(fun,pom))

for x in pom:
    x[0] = int(x[0])
    x[1] = int(x[1])
    

pom.sort()

def fun(pom):
    idx = 0
    i = 0
    fresh = []
    fresh.append(pom[0])
        

    for i in range(len(pom)):
        if fresh[idx][1]==pom[i][1] and fresh[idx][0]==pom[i][0]:
            continue
        if fresh[idx][1]>=pom[i][1] and fresh[idx][0]<=pom[i][0]:
            continue
        if fresh[idx][1]>=pom[i][0] and fresh[idx][1]<=pom[i][1]:
            fresh[idx][1] = pom[i][1]
        else:
            idx+=1
            fresh.append(pom[i])
    if fresh == pom:
        return False
    return fresh



tab = fun(pom)
print(tab)

sum = 0

for x in tab:
    sum+=x[1]-x[0]+1

print(sum)