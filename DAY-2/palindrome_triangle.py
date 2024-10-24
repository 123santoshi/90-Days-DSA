'''
      1 

    2 1 2 

   3 2 1 2 3 

  4 3 2 1 2 3 4 

 5 4 3 2 1 2 3 4 5 

'''



n=int(input("Enter no of rows=="))
for i in range(n):
    print(" "*(n-i-1),end=' ')
  
    for j in range(i+1,0,-1):
        print(j,end=" ")
        
    for j in range(2,i+2):
        print(j,end=" ")
    
    print("\n")