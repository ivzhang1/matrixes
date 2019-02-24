from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [255, 0, 0]

matrix = new_matrix(0, 0);

print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6)\nmatrix =")
add_edge(matrix, 1, 2, 3, 4, 5, 6);

print_matrix(matrix)

print("Testing ident. \nidentity_matrix =")
identity_matrix = new_matrix()
ident(identity_matrix)
print_matrix(identity_matrix)

print("Testing Matrix mult.\nidentity_matrix * matrix =")
print_matrix(matrix_mult(identity_matrix, matrix))

print("Testing Matrix mult. \nm1 =")
m1 = [[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1]]
print_matrix(m1)

print("Testing Matrix mult. \nm1 * matrix =")
print_matrix(matrix_mult(m1, matrix))


# add_edge(edges, 250, 150, 0, 350, 250, 0);
# add_edge(edges, 150, 250, 0, 200, 320, 0);
# add_edge(edges, 200, 320, 0, 250, 300, 0);
#
# add_edge(edges, 250, 300, 0, 300, 320, 0);
# add_edge(edges, 300, 320, 0, 350, 250, 0);
# add_edge(edges, 250, 450, 0, 250, 400, 0);
# add_edge(edges, 250, 400, 0, 200, 400, 0);
#
# add_edge(edges, 150, 400, 0, 130, 360, 0);
# add_edge(edges, 150, 400, 0, 170, 360, 0);
# add_edge(edges, 130, 360, 0, 170, 360, 0);
#
# add_edge(edges, 100, 340, 0, 200, 340, 0);
# add_edge(edges, 100, 320, 0, 200, 320, 0);
# add_edge(edges, 100, 340, 0, 100, 320, 0);
# add_edge(edges, 200, 340, 0, 200, 320, 0);

# draw_lines( edges, screen, color);
#
# matrix = new_matrix()
# matrix_2 = new_matrix()
#
# print_matrix(matrix)
# print_matrix(matrix_2)
# ident(matrix)
# print_matrix(matrix)


# matrix = [[5,0,3,1],[2,6,8,8],[6,2,1,5],[1,0,4,6]]#new_matrix()
# matrix_2 = [[7,1,9,5],[5,8,4,3],[8,2,3,7],[0,6,8,9]]#new_matrix()
#
# print_matrix(matrix_2)
#
# print("MULTIPLIED BY\n")
# print_matrix(matrix)
#
# matrix = matrix_mult(matrix_2, matrix);
#
# print_matrix(matrix)
# #add_point(matrix, 100,200)
# print_matrix(matrix)
# add_edge(matrix, 100, 200, 0, 300, 400, 0)
# print_matrix(matrix)


# draw_lines( matrix, screen, color )
# print_matrix(matrix)

display(screen)
