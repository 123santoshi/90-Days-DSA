''' 
     1 

    1 2 

   1 2 3 

  1 2 3 4 

 1 2 3 4 5 


'''
n=int(input("Enter No of Rows=="))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(i+1):
        print(j+1 ,end=" ")
    print("\n")