import pygame
from random import randrange

# Inicializa o Pygame
pygame.init()

# Configuração da tela
altura = 1270
largura = 720
tela = pygame.display.set_mode((altura, largura))

# Configuração do tamanho dos quadrados (segmentos da cobra)
tamanho_dos_quadrados = 35

# Posição inicial da comida (aleatória)
numx = randrange(0 + tamanho_dos_quadrados, 1270 - tamanho_dos_quadrados)
numy = randrange(0 + tamanho_dos_quadrados, 720 - tamanho_dos_quadrados)
comida_pos = [numx, numy]

# Cria o clock para controlar o FPS
relogio = pygame.time.Clock()

# Cria o corpo da cobra (um retângulo)
cobra = pygame.rect.Rect([10, 10, tamanho_dos_quadrados - 2, tamanho_dos_quadrados - 2])
segments = [cobra.copy()]

# Tamanho inicial da cobra
length = 1

# Inicializa a velocidade
velocityx = 0
velocityy = 0

# Variável de controle do loop
running = True

# Loop principal do jogo
while running:
    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Movimento da cobra com as teclas
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
    cobra.move_ip(velocityx * tamanho_dos_quadrados, velocityy * tamanho_dos_quadrados)

    # Preenche a tela com a cor branca
    tela.fill((255, 255, 255))

    # Atualiza a lista de segmentos da cobra
    segments.append(cobra.copy())
    if len(segments) > length:
        del segments[0]

    # Desenha a cobra na tela
    for segment in segments:
        pygame.draw.rect(tela, (0, 0, 0), segment)

    # Desenha a comida
    pygame.draw.circle(tela, "red", comida_pos, 15)

    # Atualiza a tela
    pygame.display.flip()

    # Controla o FPS (60 quadros por segundo)
    relogio.tick(60)

# Fecha o Pygame