a=int(input("Enter number of rows: "))
b=int(input("Enter number of columns: "))
mat=[[0 for col in range(b)] for row in range(a)]
for row in range(a):
    for col in range(b):
        mat[row][col]= row*col

print(mat)
