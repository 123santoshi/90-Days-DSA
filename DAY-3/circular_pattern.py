'''
1 2 3 4 5 6
2 3 4 5 6 1
3 4 5 6 1 2
4 5 6 1 2 3
5 6 1 2 3 4
6 1 2 3 4 5

'''


n=int(input("Enter n valyue=="))
v=[ i  for i in range(1,n+1)]
for i in range(n):
    val=v[i:n+1]+v[:i]
    val= " ".join(map(str,val))
    print(val)