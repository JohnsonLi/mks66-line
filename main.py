from display import *
from draw import *

screen = new_screen()
color = [ 242, 150, 242 ]

draw_line(0, 0, 500, 500, screen, color );
draw_line(0, 500, 500, 0, screen, color );
draw_line(250, 0, 250, 500, screen, color );
draw_line(0, 250, 500, 250, screen, color );

# for i in range(500):
#     draw_line(250, 250, 250 % (i + 1) , 0, screen, color)

display(screen)
save_extension(screen, 'img.png')
