"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    total = ""
    for i in range(4):
        for row in matrix:
            total += str(row[i]) + " "
        total += "\n"
    print(total)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            matrix[i][j] = 0 if i != j else 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if(len(m1) != len(m2[0])):
        print("Cannot be multiplied")
    else:
        for r in range(4):
            
    print_matrix(m2)
               
def new_matrix(rows = 4, cols = 4):
    m = []
    counter = 0
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append(counter )
            counter+=1
    return m
