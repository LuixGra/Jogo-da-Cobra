import sys


import pygame
pygame.init()

#importar random
from random import randrange

musica = pygame.mixer.music.load("musicaprincipal.mp3")
pygame.mixer.music.play()

#tela
altura = 1270
largura = 720
tela = pygame.display.set_mode((altura,largura))




tamanho_dos_quadrados = 35

#numero aleatorio
def gerarComida():
    numx = randrange(start=0, stop=1270, step=tamanho_dos_quadrados)
    numy = randrange(start=0, stop=720, step=tamanho_dos_quadrados)

    return numx, numy
numx, numy = gerarComida()
comida_pos = [numx, numy]   




#delta time
dt = 0

#cria o clock
relogio = pygame.time.Clock()


#cria a cobra
cobra = pygame.rect.Rect([10,10, tamanho_dos_quadrados, tamanho_dos_quadrados])
segments = [cobra.copy()]

length = 1

velocityx = 0
velocityy = 0


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #pega a entrada das teclas
    keys = pygame.key.get_pressed()

    #movimenta a cobra
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

    # Atualiza a posição da cobra
    cobra.x += velocityx * dt * 500   
    cobra.y += velocityy * dt * 500

    #preenche a tela
    tela.fill((255,255,255))

    #atualiza os segmentos da cobra
    segments.append(cobra.copy())

    if len(segments) > length:
        del segments[0]

    #mostra a cobra na tela
    for segment in segments:
        pygame.draw.rect(tela, (0,0,0), segment)
        if cobra.x  > altura +  tamanho_dos_quadrados or cobra.x < 0 - tamanho_dos_quadrados or cobra.y < 0 - tamanho_dos_quadrados or cobra.y > largura + tamanho_dos_quadrados:
            pygame.quit()
            print("Game Over")
            sys.exit()

        

    #mostra a  comida
    comida = pygame.rect.Rect([numx, numy, tamanho_dos_quadrados, tamanho_dos_quadrados])

    pygame.draw.rect(tela, "red", comida)

    
    if cobra.colliderect(comida):
        length += 1
        segments.append(pygame.rect.Rect([cobra.x, cobra.y, tamanho_dos_quadrados, tamanho_dos_quadrados]))
        numx, numy =  gerarComida()
        comida.centerx, comida.centery = numx, numy

    #comendo
    
   

    


    #gameover bateu na parede
    
        

    #atualiza a tela
    pygame.display.update()

    #relogio
    dt = relogio.tick(60)/1000

pygame.quit()
sys.exit()