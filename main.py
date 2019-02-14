from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
matrix_2 = new_matrix()

print_matrix(matrix)
print_matrix(matrix_2)
# ident(matrix)
# print_matrix(matrix)

#matrix = matrix_mult(matrix_2, matrix);

print_matrix(matrix)
#add_point(matrix, 100,200)
print_matrix(matrix)
add_edge(matrix, 100, 200, 0, 300, 400, 0)
print_matrix(matrix)


draw_lines( matrix, screen, color )
print_matrix(matrix)

display(screen)
