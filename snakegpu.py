import pygame , random
from pygame.locals import*

UP = 0
direia = 1
down = 2
esquerda = 3 

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("snakegpu")

caio = [(200,200), (210,200),(220,200)]
caio_skin = pygame.Surface((10,10))
caio_skin.fill((80, 200, 120))

coca_pos = (random.randint(0,590), random.randint(0,590))
coca = pygame.Surface((10,10))
coca.fill((255,0,0))





minha_direçao = esquerda

clock = pygame.time.Clock()

while True:
    clock.tick(25)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYDOWN:
              if evento.key == K_UP:
                    minha_direçao = UP
              if evento.key == K_DOWN:
                      minha_direçao = down
              if evento.key == K_RIGHT:
                      minha_direçao = esquerda
              if evento.key == K_LEFT:
                    minha_direçao = direia          

    if minha_direçao == UP:
        caio[0] = (caio[0][0], caio[0][1] - 10 )
    if minha_direçao == down:
            caio[0] = (caio[0][0], caio[0][1] + 10 )
    if minha_direçao == esquerda:
            caio[0] = (caio[0][0] +10, caio[0][1]  )
    if minha_direçao == direia:
            caio[0] = (caio[0][0] - 10 , caio[0][1]  )

    for i in range(len(caio) - 1,0 , -1):
          caio[i] = (caio[i-1][0], caio[i-1][1])

    screen.fill((0,0,0))
    screen.blit(coca, coca_pos)
    for pos in caio :
        screen.blit(caio_skin,pos )       
    pygame.display.update()
