'''
1  
3 2  
6 5 4  
10 9 8 7  
15 14 13 12 11

 '''




n=int(input("Enter n valyue=="))
c=1
temp=c
for i in range(n):
    c=c+i
    temp=c
    for j in range(i+1):
        print(c,end=" ")
        c-=1
    c=temp+1
    print(" ")