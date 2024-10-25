'''
1 1 1 1 1 1 1
1 2 2 2 2 2 1
1 2 3 3 3 2 1
1 2 3 4 3 2 1
1 2 3 3 3 2 1
1 2 2 2 2 2 1
1 1 1 1 1 1 1
'''
n=int(input("Enter n value=="))
total_size=2*n-1
mat=[[0 for j in range(total_size)] for i in range(total_size)]
for box in range(n):
    for i in range(box,total_size-box):
        for j in range(box,total_size-box):
            mat[i][j]=box+1
# to print matrix
for row in mat:
    print(" ".join(map(str,row)))


