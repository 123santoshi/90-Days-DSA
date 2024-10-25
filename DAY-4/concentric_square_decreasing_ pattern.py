'''
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''

n=int(input("Enter n value=="))
total_size = 2*n-1
mat=[[0 for j in range(total_size)] for i in range(total_size)]
for box in range(n):
    for i in range(box,total_size-box):
        for j in range(box,total_size-box):
            mat[i][j]=n-box
#to print the matrix
for row in mat:
    print(" ".join(map(str,row)))
