f = open("input.txt")
tab = []

a = f.readline()

a = list(a.split(','))

def fun(i):
    return list(i.split('-'))

a = list(map(fun,a))


counter = 0

def checkStr(str1, str2, leng1, leng2):
    for i in range(0,leng2,leng1):
        if str2[i:i+leng1]!=str1:
            return 0
    return 1

for i in a:
    begin = int(i[0])
    end = int(i[1])
    for j in range(begin,end+1):
        j = str(j)
        leng = len(j)

        for k in range(1,int(leng)):
            if leng % k != 0:
                continue
            temp1 = j[0:k]
            temp2 = j[k:]

            if checkStr(temp1,temp2,k,leng-k):
                counter+=int(j)
                break

            

        
print(counter)