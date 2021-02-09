import sys, pygame
pygame.init()
size = width, height = 1200, 680
color = 124, 252, 000
screen = pygame.display.set_mode(size)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(color)
    pygame.display.flip()