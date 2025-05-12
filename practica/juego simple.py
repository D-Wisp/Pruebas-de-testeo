import pygame  

peso = input("cuanto pesas? ")

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Imagen rotando")

imagen = pygame.image.load("imagen.jpg")
imagen = pygame.transform.scale(imagen, (400, 400))
rect = imagen.get_rect(center=(300, 200))
angulo = 0
reloj = pygame.time.Clock()

pygame.mixer.music.load("meme.mp3")
pygame.mixer.music.play(-1)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    ventana.fill((255, 255, 255))
    angulo += 1
    imagen_rotada = pygame.transform.rotate(imagen, angulo)
    rect = imagen_rotada.get_rect(center=rect.center)
    ventana.blit(imagen_rotada, rect.topleft)

    pygame.display.flip()
    reloj.tick(60)
    if int(peso) > 100:
        print("Eres muy pesado")
    else:
        print("Eres ligero")
        break