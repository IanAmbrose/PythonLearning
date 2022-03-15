import pygame

pygame.init()
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
background = GRAY


screen = pygame.display.set_mode((640, 240))

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN
        if event.type == pygame.QUIT:
            print(event)

    screen.fill(background)
    pygame.display.update()

pygame.quit()