#Enter n value==5

'''
1  
2 1  
4 2 1  
8 4 2 1  
16 8 4 2 1

'''


n=int(input("Enter n value=="))
for i in range(n):
    for j in range(i+1,0,-1):
        print(2**(j-1),end=" ")
    print(" ")