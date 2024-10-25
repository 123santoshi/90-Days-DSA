'''
*         *

**       **

***     ***

****   ****

***** *****

***** *****

****   ****

***     ***

**       **

*         *

'''



n=int(input("Enter No of rows=="))
for i in range(n):
    print("*"*(i+1),end="")
    print(" "*(2*(n-i)-1),end="")
    print("*"*(i+1),end="")
    print("\n")
for i in range(n):
    print("*"*(n-i),end="")
    print(" "*(2*(i+1)-1),end="")
    print("*"*(n-i),end="")
    print("\n")
        