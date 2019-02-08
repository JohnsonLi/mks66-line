from display import *
from draw import *

screen = new_screen()
color = [ 242, 150, 242 ]

draw_line(250, 250, 350, 500, screen, color );

display(screen)
save_extension(screen, 'img.png')
