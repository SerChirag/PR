X = [[12,7,3],
    [4,5,6]]

# 3x4 matrix
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
print result
for r in result:
   print(r)