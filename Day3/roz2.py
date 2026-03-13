import math
plik = open("input.txt")

sum = 0

for line in plik:
    line=line.strip()
    a = list(line)
    
    alen = len(a)
    max = int(a[0])
    idx = 0
    idx1 = 0

    for i in range(alen-11):
        if int(a[i])>max:
            idx1 = i
            max = int(a[i])
    sum +=max*(10**11)

    idx1+=1
    max = int(a[idx1]) 

    for i in range(1,12):
        max = int(a[idx1]) 
        for j in range(idx1,alen-11+i):
            if int(a[j])>max:
                idx1 = j
                max = int(a[j])
        sum += max*(10**(11-i)) 
        idx1 += 1
        
print(sum)
