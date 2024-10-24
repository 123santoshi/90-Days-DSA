''' 
*  *  *  *  *  

  *       *

   *     *

    *   *

     *  

    *   *

   *     *

  *       *

 *  *  *  *  *  
'''
n=int(input("Enter No of rows=="))
for i in range(n):
    print(" "*(i),end=" ")
    if(i==0):
        for j in range(n):
            print('* ',end=" ")
    elif i==n-1:
        print("* ",end=" ")
    else:
        print("*",end="")
        print(" "*(2*(n-i)-1),end="")
        print("*",end="")
    print("\n")
for i in range(1,n):
    print(" "*(n-i-1),end=" ")
    if(i==n-1):
        for j in range(n):
            print('* ',end=" ")
    else:
        print("*",end="")
        print(" "*(2*i+1),end="")
        print("*",end="")
    print("\n")
