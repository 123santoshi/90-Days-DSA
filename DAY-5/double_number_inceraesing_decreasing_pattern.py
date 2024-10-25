
#Enter n value==5
'''
1  
1 2 1  
1 2 4 2 1  
1 2 4 8 4 2 1  
1 2 4 8 16 8 4 2 1 
'''


n=int(input("Enter n value=="))
for i in range(n):
    temp=i
    for j in range(2*i+1):
        if(i>=j):
            print(2**(j),end=" ")
        else:
            print(2**(temp-1),end=" ")
            temp-=1
    print(" ")