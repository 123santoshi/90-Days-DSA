'''
  1   2   3   4   

   2   3   4   

    3   4   

     4   
'''



n=int(input("Enter no of rows=="))
for i in range(n):
    print(" "*(i+1),end=" ")
    k=i+1
    for j in range(n-i):
        print(k, " ",end=" ")
        k+=1    
    
    print("\n")

