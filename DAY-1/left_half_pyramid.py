'''
     *

    **

   ***

  ****

 *****

'''





n=int(input("Enter No of rows="))
for i in range(n):
    print(" "*(n-i),end="")
    for j in range(i+1):
        print("*",end="")
    print("\n")