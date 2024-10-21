'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''



n=int(input("Enter no of rows=="))
for i in range(n):
    if(i%2==0):
        s=1
    else:
        s=0
    for j in range(i+1):
        print(int(s),end=" ")
        s=not(s)
    print("\n")
        