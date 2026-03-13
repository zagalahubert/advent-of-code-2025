f = open("input.txt")
tab = []

a = f.readline()

a = list(a.split(','))

def fun(i):
    return list(i.split('-'))

a = list(map(fun,a))


counter = 0

for i in a:
    begin = int(i[0])
    end = int(i[1])
    for j in range(begin,end+1):
        j = str(j)
        leng = len(j)

        if leng % 2 == 1:
            continue 
        
        leng1 = int(leng/2)
        leng2 = int(leng/2)

        first = j[:leng1]
        second = j[leng2:]
        
        if first == second:
            counter+=int(j)
        
print(counter)
