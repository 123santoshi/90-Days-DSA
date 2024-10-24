''' 
      * 

     * *

    *   *

   *     *

  *       *

   *     *

    *   *

     * *

      * 
'''

n=int(input("Enter No of rows=="))
for i in range(n):
    print(" "*(n-i),end=" ")
    if(i==0):
       print("*",end=" ")
    else:
        print("*",end="")
        print(" "*(2*i-1),end="")
        print("*",end="")
    print("\n")
for i in range(2,n+1):
    print(" "*(i),end=" ")
    if(i==n):
       print("*",end=" ")
    else:
        print("*",end="")
        print(" "*(2*(n-i)-1),end="")
        print("*",end="")
    print("\n")