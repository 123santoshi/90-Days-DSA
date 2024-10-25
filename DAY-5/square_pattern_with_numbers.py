
'''
1 2 3 4 5  
2 2 3 4 5  
3 3 3 4 5  
4 4 4 4 5  
5 5 5 5 5 

 '''

n=int(input("Enter n valyue=="))
for i in range(n):
    for j in range(n):
        if(i>=j):
            print(i+1,end=" ")
        else:
            print(j+1,end=' ')
    print(' ')