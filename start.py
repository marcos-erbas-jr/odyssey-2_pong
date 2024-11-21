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
zone = 450


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
    #pygame.draw.rect(screen, "green", (x, y, 1, 1))

    #raquete do player 1
    pygame.draw.rect(screen, (255, 255, 255), (player1x, player1y, 10, 40))

    #pygame.draw.rect(screen, "red", (player1x, player1y, 1, 40))

    #raquete do player 2
    pygame.draw.rect(screen, (255, 255, 255), (player2x, player2y, 10, 40))

    #movimentação da bolinha
    x += a/4
    y += b/3

    if (x >= 510 or x <= 10 or (x >= player1x and x < (player1x + 10) and
                                y >= (player1y) and y < (player1y + 40)) or
                                (x >=player2x and x < (player2x + 10) and
                                 y >=(player2y) and y < (player2y + 40))):
        if a > 60:
            a = 60
            a *= -1
        else:
            a *= -1.09
        if x >= 510 and zone < x:
            x = 510
            player1 += 1
            zone = 450
        elif x <= 10 and zone > x:
            x = 10
            zone = 70
            player2 += 1


    if y >= 315 or y <= 10:
        b *= -1

    # MOVIMENTAÇÃO DO PLAYER 2
    if player2y > y:
        if player2y <= 17:
            player2y = 17
        else:
            player2y -= 4
    elif player2y < y:
        if player2y >= 275:
            player2y = 275
        else:
            player2y += 4
    #CAPTURA DE TECLA
    keys = pygame.key.get_pressed()

    #MOVIMENTAÇÃO DA RAQUETE
    if keys[pygame.K_UP]:
        if player1y <= 17:
            player1y = 17
        else:
            player1y -= 3
    if keys[pygame.K_DOWN]:
        if player1y >= 275:
            player1y = 275
        else:
            player1y += 3



    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()