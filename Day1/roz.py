# Advent of code - Day 1 - 
# remade task 1 instead of creating 2nd file  
# too much unnecessary code when starts with L, but I chose to leave it as it is 

f = open("teskt.txt")

start = 50
zm = 0
count = 1
for line in f:
    temp = 0
    
    line = line.strip()
    temp = int(line[1:])

    if line.startswith('R'):
        start += temp 
        while (start > 99):
            start-= 100
            zm+=1
        
    if line.startswith('L'):
        if (start == 0) and ((temp % 100) !=0):
            start-=temp
            while (start<-100):
                start+=100
                zm+=1
            start+=100

        elif (start == 0):
            start-=temp
            while (start<0):
                start+=100
                zm+=1
        else:   
            start -= temp

            while (start<0):
                start+=100
                zm+=1

            if start == 0:
                zm+=1

print(zm)


#7682 too high
#4592 too low