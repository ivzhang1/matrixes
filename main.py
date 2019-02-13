from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = [[5,0,3,1],[2,6,8,8],[6,2,1,5],[1,0,4,6]]#new_matrix()
matrix_2 = [[7,1,9,5],[5,8,4,3],[8,2,3,7],[0,6,8,9]]#new_matrix()

print_matrix(matrix)
print_matrix(matrix_2)
#ident(matrix)
#print_matrix(matrix)
matrix_mult(matrix_2, matrix);
print_matrix(matrix_2)

draw_lines( matrix, screen, color )
display(screen)
