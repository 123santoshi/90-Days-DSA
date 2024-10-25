#Enter n valyue==7
'''
1  
2 4  
3 6 9  
4 8 12 16  
5 10 15 20 25  
6 12 18 24 30 36  
7 14 21 28 35 42 49  
'''



n=int(input("Enter n valyue=="))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print(" ")
        