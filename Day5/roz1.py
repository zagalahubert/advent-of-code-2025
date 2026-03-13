plik = open("input.txt")

pom = []
id = []
fresh = []

for line in plik:
    line = line.strip()
    if line.find('-') != -1:
        pom.append(line)
    if line == '':
        continue
    if line.isdecimal():
        id.append(line)


def fun(i):
    return list(i.split('-'))

pom = list(map(fun,pom))

for i in id:
    i = int(i)
    for x in pom:
        beg = int(x[0])
        end = int(x[1])
        if i<=end and i>=beg:
            if fresh.count(i)==0:
                fresh.append(i)

print(fresh)     
print(len(fresh))

#print(pom)
#print(id)