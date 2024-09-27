import pygame
pygame.init()

#importar random
from random import randrange

#tela
altura = 1270
largura = 720
tela = pygame.display.set_mode((altura,largura))




tamanho_dos_quadrados = 35

#numero aleatorio
numx = randrange(0 + tamanho_dos_quadrados, 1270 - tamanho_dos_quadrados)
numy = randrange(0 + tamanho_dos_quadrados, 720 - tamanho_dos_quadrados)
comida_pos = [numx, numy]



#delta time
dt = 0

#cria o clock
relogio = pygame.time.Clock()

#posição inicial do jogador
player_pos = pygame.Vector2(tela.get_width()/2, tela.get_height()/2)

#cobra

"""
class Cobra:
    def __init__(self):
        self.cobra =  pygame.rect.Rect([10,10, tamanho_dos_quadrados - 2, tamanho_dos_quadrados -2])
        self.segments = [self.cobra.copy()]

        self.velocity = 2
    
        #tamanho da  cobra

        self.length = 1
    



"""

cobra = pygame.rect.Rect([10,10, tamanho_dos_quadrados - 2, tamanho_dos_quadrados - 2])
segments = [cobra.copy()]

length = 1

velocityx = 0
velocityy = 0





running = True

while running:
    #definições iniciais gerais
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #fecha o jogo
            running = False

        

        


    


    #preencher a tela
        tela.fill((255,255,255))

    


    #gameplay

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # Movimento para a esquerda
                velocityx = -1
                velocityy = 0
        if keys[pygame.K_d]:  # Movimento para a direita
                velocityx = 1
                velocityy = 0
        if keys[pygame.K_w]:  # Movimento para cima
                velocityx = 0
                velocityy = -1
        if keys[pygame.K_s]:  # Movimento para baixo
                velocityx = 0
                velocityy = 1

        cobra.move_ip(velocityx * tamanho_dos_quadrados, velocityy * tamanho_dos_quadrados)
    #mostra cobra na tela
   
        if len(segments) > length:
                del segments[0] 
        for segment in segments:
                pygame.draw.rect(tela, (0,0,0), segment, tamanho_dos_quadrados - 2)
    
    

    #mostra  comida
        pygame.draw.circle(tela, "red", comida_pos, 15)

    #teclas
    
    
    

    
    #movimenta a cobra de uma forma diferenciada
    
    #atualiza a tela
        pygame.display.flip()

    #maximiza o fpss
        relogio.tick(60)

#garantir que o jogo fechou....¨¨¨¨¨¨¨¨¨¨!¨!¨!¨!¨!¨!¨!
pygame.quit()
