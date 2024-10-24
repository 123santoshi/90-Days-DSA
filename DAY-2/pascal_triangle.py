'''     
      1 

     1 1 

    1 2 1 

   1 3 3 1 

  1 4 6 4 1 
'''

n=int(input("Enter No of rows=="))

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def com(n,r):
    num=fact(n)
    den=fact(n-r)*fact(r)
    ans=num//den
    return ans

for i in range(n):
    print(" "*(n-i),end=" ")
    for j in range(i+1):
        c=com(i,j)
        print(c,end=" ")
    print("\n")
        

