from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

edges = new_matrix(4, 4);
add_edge(edges, 50, 450, 0, 100, 450, 0);
add_edge(edges, 50, 450, 0, 50, 400, 0);
add_edge(edges, 100, 450, 0, 100, 400, 0);
add_edge(edges, 100, 400, 0, 50, 400, 0);

add_edge(edges, 200, 450, 0, 250, 450, 0);
add_edge(edges, 200, 450, 0, 200, 400, 0);
add_edge(edges, 250, 450, 0, 250, 400, 0);
add_edge(edges, 250, 400, 0, 200, 400, 0);

add_edge(edges, 150, 400, 0, 130, 360, 0);
add_edge(edges, 150, 400, 0, 170, 360, 0);
add_edge(edges, 130, 360, 0, 170, 360, 0);

add_edge(edges, 100, 340, 0, 200, 340, 0);
add_edge(edges, 100, 320, 0, 200, 320, 0);
add_edge(edges, 100, 340, 0, 100, 320, 0);
add_edge(edges, 200, 340, 0, 200, 320, 0);

draw_lines( edges, screen, color);

# matrix = new_matrix()
# matrix_2 = new_matrix()

# print_matrix(matrix)
# print_matrix(matrix_2)
# # ident(matrix)
# # print_matrix(matrix)

# #matrix = matrix_mult(matrix_2, matrix);

# print_matrix(matrix)
# #add_point(matrix, 100,200)
# print_matrix(matrix)
# add_edge(matrix, 100, 200, 0, 300, 400, 0)
# print_matrix(matrix)


# draw_lines( matrix, screen, color )
# print_matrix(matrix)

display(screen)
