import pygame

pygame.init()
screen = pygame.display.set_mode((535, 330))
clock = pygame.time.Clock()
running = True
dt = 0
x = (screen.get_width()/2)-8
y = (screen.get_height()/2)-5
a = 10
b = 10

def background():
    screen.fill((0, 0, 0))
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(10, 10), (525, 10), (10, 10), (10, 320), (525, 320),
                       (525, 10)], 5)
    pygame.draw.line(screen, (255, 255, 255), (263, 10), (263, 320), 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background()

    pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10))

    x += a
    y += b/4
    if x >= 510 or x <=10:
        a *= -1

    if y >= 315 or y <= 10:
        b *= -1


    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()