plik = open("input.txt")

sum = 0

for line in plik:
    line.strip()
    a = list(line)
    max1 = int(a[0])
    idx1 = 0
    max2 = 0
    idx2 = 0
    for i in range(len(a)-2):
        if int(a[i])>max1:
            idx1 = i
            max1 = int(a[i])
    idx2 = idx1+1
    max2 = int(a[idx2])
    for i in range(idx2,len(a)-1):
        if int(a[i])>max2:
            idx2 = i
            max2 = int(a[i])
    sum+= max1*10 + max2
        
        
print(sum)

        
    