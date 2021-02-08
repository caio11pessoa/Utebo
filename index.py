import sys, pygame
pygame.init()

width, height = 640, 480
screen=pygame.display.set_mode((width, height))

while 1:
    screen.fill("#FFF555")
    pygame.display.flip()
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0) 