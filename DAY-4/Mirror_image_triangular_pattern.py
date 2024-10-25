'''
 1 2 3 4 

  2 3 4 

   3 4 

    4 

   3 4 

  2 3 4 

 1 2 3 4 
'''


n=int(input("Enter no of rows=="))
for i in range(n):
    print(" "*(i),end=" ")
    k=i
    for j in range(n-i):
        print(k+1,end=" ")
        k+=1
    
    print("\n")
for i in range(1,n):
    print(" "*(n-i-1),end=" ")
    k=n-i
    for j in range(i+1):
        print(k,end=" ")
        k+=1
        
    print("\n")
        

