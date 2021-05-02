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
        self.horizontal += x
        self.vertical += y
        pygame.draw.rect(self.tela, self.cor, [self.horizontal, self.vertical, 40, 40])

class Bola(object):
    
    def __init__(self, tela, cor, x, y):
        self.tamanho = 24
        self.horizontal = x-(self.tamanho/2)
        self.vertical = y-(self.tamanho/2)
        pygame.draw.ellipse(tela, cor, [self.horizontal, self.vertical, self.tamanho, self.tamanho])
        
        # self.largura = largura
        # self.tamanho = altura
        self.tela = tela
        self.cor = cor
    def movimento(self, x, y):
        self.horizontal += x
        self.vertical += y
        pygame.draw.ellipse(self.tela, self.cor, [self.horizontal, self.vertical, self.tamanho, self.tamanho])

def testeVelocidade (velocidade):
    if(velocidade ==0):
        return 1
    else:
        return 0
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
bola = Bola(tela, "#4B3621", tamanho[0]/2, tamanho[1]/2)

movimentoHorizonal1 = 0
movimentoHorizonal2 = 0
movimentoVertical1 = 0
movimentoVertical2 = 0
# sp = True
while 1:
    tela.fill(color)
    retornaLayout(tela,corLinhas, tamanho[0], tamanho[1])
    bola.movimento(0, 0)
    
    # if((jogador2.horizontal > bola.horizontal-60 and jogador2.horizontal < bola.horizontal+60) and (jogador2.vertical > bola.vertical -60  and jogador2.vertical < bola.vertical+60)):
    #     if((jogador2.horizontal > bola.horizontal-50 and jogador2.horizontal < bola.horizontal+50) and (jogador2.vertical > bola.vertical -50  and jogador2.vertical < bola.vertical+50) and sp == False):
    #         bola.movimento(movimentoHorizonal2, movimentoVertical2)
    jogador1.movimento(movimentoHorizonal1,movimentoVertical1)
    jogador2.movimento(movimentoHorizonal2,movimentoVertical2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
        #     sp = False
        # if(event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
        #     sp = True
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
            movimentoHorizonal1 = -testeVelocidade(movimentoHorizonal1)

        if (event.type == pygame.KEYUP and event.key == pygame.K_a):
            movimentoHorizonal1 = testeVelocidade(movimentoHorizonal1)

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
            movimentoVertical1 = -testeVelocidade(movimentoVertical1)

        if (event.type == pygame.KEYUP and event.key == pygame.K_w):
            movimentoVertical1 = testeVelocidade(movimentoVertical1)

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
            movimentoVertical1 = testeVelocidade(movimentoVertical1)

        if (event.type == pygame.KEYUP and event.key == pygame.K_s):
            movimentoVertical1 = -testeVelocidade(movimentoVertical1)

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_d):
            movimentoHorizonal1 = testeVelocidade(movimentoHorizonal1)

        if (event.type == pygame.KEYUP and event.key == pygame.K_d):
            movimentoHorizonal1 = -testeVelocidade(movimentoHorizonal1)

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            movimentoHorizonal2 = -testeVelocidade(movimentoHorizonal2)

        if (event.type == pygame.KEYUP and event.key == pygame.K_LEFT):
            movimentoHorizonal2 = testeVelocidade(movimentoHorizonal2)

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            movimentoVertical2 = -testeVelocidade(movimentoVertical2)

        if (event.type == pygame.KEYUP and event.key == pygame.K_UP):
            movimentoVertical2 = testeVelocidade(movimentoVertical2)

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            movimentoVertical2 = testeVelocidade(movimentoVertical2)

        if (event.type == pygame.KEYUP and event.key == pygame.K_DOWN):
            movimentoVertical2 = -testeVelocidade(movimentoVertical2)

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            movimentoHorizonal2 = testeVelocidade(movimentoHorizonal2)

        if (event.type == pygame.KEYUP and event.key == pygame.K_RIGHT):
            movimentoHorizonal2 = -testeVelocidade(movimentoHorizonal2)

    pygame.display.flip()
    
    