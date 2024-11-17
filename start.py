import pygame

pygame.init()
screen = pygame.display.set_mode((535, 330))
pygame.display.set_caption('Pong')
icon = pygame.image.load('pongicon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True
dt = 0
x = (screen.get_width()/2)-8
y = (screen.get_height()/2)-5
a = 10
b = 10
player1 = 0 #score player 1
player1x = 30
player1y = 155

player2 = 0 #score player 2
player2x = 495
player2y = 155
myfont = pygame.font.SysFont("monospace", 30, bold=pygame.font.Font.bold)
score = 0


def background():
    screen.fill((0, 0, 0))
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(10, 10), (525, 10), (10, 10), (10, 320), (525, 320),
                       (525, 10)], 5)
    pygame.draw.line(screen, (255, 255, 255), (263, 20), (263, 310), 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background()

    scoretext1 = myfont.render("{0}".format(player1), 0, (255,255,255))
    screen.blit(scoretext1, (210, 15))

    scoretext2 = myfont.render("{0}".format(player2), 0, (255, 255, 255))
    screen.blit(scoretext2, (285, 15))


    pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10))

    #raquete do player 1
    pygame.draw.rect(screen, (255, 255, 255), (player1x, player1y, 10, 40))

    #raquete do player 2
    pygame.draw.rect(screen, (255, 255, 255), (player2x, player2y, 10, 40))

    x += a
    y += b/4
    if x >= 510 or x <= 10:
        a *= -1
        if x >= 510:
            player1 += 1
        else:
            player2 += 1

    if y >= 315 or y <= 10:
        b *= -1


    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()