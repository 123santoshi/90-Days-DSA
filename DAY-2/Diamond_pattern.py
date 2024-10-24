'''
      *

     *  *

    *  *  *

   *  *  *  *

  *  *  *  *  *

   *  *  *  *

    *  *  *

     *  *

      *
'''



n=int(input("Enter no of rows=="))
for i in range(n):
    print(" "*(n-i),end=" ")
    for j in range(i+1):
        print("* ",end=" ")
    print("\n")

for i in range(n-1,-1,-1):
    print(" "*(n-i+1),end=" ")
    for j in range(i):
        print("* ",end=" ")
    print("\n")

