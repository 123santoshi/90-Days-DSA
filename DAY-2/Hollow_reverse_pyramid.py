'''
 * * * * * 

  *     *

   *   *

    * *

     * 
'''





n=int(input("Enter No of rows=="))
for i in range(n):
    print(" "*(i),end=" ")
    if(i==0 or i==n-1):
        for j in range(n-i):
            print("*",end=" ")
    else:
        print("*",end="")
        print(" " * (2 * (n - i - 1) - 1), end="")
        print("*",end="")
    print('\n')
 