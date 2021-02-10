import sys, pygame

def retornaLayout (tela, corLinhas, largura, altura):
    pygame.draw.line(tela, corLinhas, [largura/2, 0], [largura/2, altura], 6)#linha do meio
    pygame.draw.line(tela, corLinhas, [0, 2], [largura, 2], 6) #linha de cima
    pygame.draw.line(tela, corLinhas, [2, 0], [2, altura], 6) #linha da esquerda
    pygame.draw.line(tela, corLinhas, [0, altura-4], [largura, altura-4], 6) #linha de baixo
    pygame.draw.line(tela, corLinhas, [largura-4, 0], [largura-4, altura], 6) #linha da direita
    pygame.draw.ellipse(tela, corLinhas, [largura/2 - altura/6, altura/2-altura/6, altura/3, altura/3] , 6) #bolota do meio
    pygame.draw.rect(tela, corLinhas, [2, altura/4, (largura/4)-50, altura/2], 6) #trave da esquerda
    pygame.draw.rect(tela, corLinhas, [(largura-4)-(largura/4 -50), altura/4, (largura/4)-50, altura/2], 6) #trave da direita

class Jogador(object):
    def __init__(self, x, y, tela, cor):
        pygame.draw.rect(tela,cor , [x, y, 40, 40])
        self.horizontal = x
        self.vertical = y
        self.tela = tela
        self.cor = cor
    def movimento(self, x, y):
        pygame.draw.rect(self.tela, self.cor, [self.horizontal + x, self.vertical + y, 40, 40])


pygame.init()
tamanho = largura, altura = 1350, 680
color = 10, 200, 5
corLinhas = 240, 240,240
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption('UTEBO')

tela.fill(color)

retornaLayout(tela,corLinhas, tamanho[0], tamanho[1])

jogador1 = Jogador(tamanho[0]/4, tamanho[1]/2 - 20, tela, "#0000FF")
jogador2 = Jogador(tamanho[0]*2/3, tamanho[1]/2 - 20, tela, "#FFFF00")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # if (event.type == pygame.KEYUP and event.key == pygame.K_a):
    
    pygame.display.flip()
    
    