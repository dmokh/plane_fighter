import pygame, time, random

pygame.init()
width = 1000
height = 700
screen = pygame.display.set_mode((width, height))
image_fon = pygame.image.load("images/cosmos.png")
image_plane = pygame.image.load("images/plane.png")
image_bullet = pygame.image.load("images/bullet.png")
image_plane_for_bads = pygame.image.load("images/plane_for_bads.png")
image_boom = pygame.image.load("images/booom!!!.png")
plane_x = 350
plane_y = 500
bullet_coord = [(plane_x+100, plane_y)]
go = "stop"
S = 200
S_q = 0
random_coord_plane_for_bads = random.randint(0, width-200)
u = 0
plane_for_bads = pygame.Rect(random_coord_plane_for_bads, 0+130 + u, 139, 139)
speed = 0.08
scoor = 0
boom = False
font_of_scoor = pygame.font.SysFont("Calibri", 52)
cords_of_boom = random_coord_plane_for_bads
boom_number = 0
boom_u = 0
speed_of_plane_bads = 1


while True:
    screen.blit(image_fon, (0, 0))
    screen.blit(image_fon, (0, 350))
    screen.blit(image_plane_for_bads, (random_coord_plane_for_bads, 0+u))
    if boom and boom_number <= 10:
        screen.blit(image_boom, (cords_of_boom, boom_u))
        boom_number += 1
    u += speed_of_plane_bads
    plane_for_bads = pygame.Rect(random_coord_plane_for_bads, 0+130+u, 139, 139)
    scoor_print = font_of_scoor.render(str(scoor), False, (255, 255, 0))
    screen.blit(scoor_print, (950, 10))
    for j in pygame.event.get():
        if j.type == pygame.QUIT:
            exit(42)
        elif j.type == pygame.KEYDOWN:
            if j.key == pygame.K_RIGHT:
                go = "right"
            elif j.key == pygame.K_LEFT:
                go = "left"
        elif j.type == pygame.KEYUP:
            if j.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                go = "stop"
    if plane_x < 0 - 55:
        plane_x = 0 - 55
    elif plane_x > width - 230:
        plane_x = width - 230
    screen.blit(image_plane, (plane_x, plane_y))
    for c in range(len(bullet_coord)):
        screen.blit(image_bullet, bullet_coord[c])
        bullet_coord[c] = (bullet_coord[c][0], bullet_coord[c][1]-10)
        bullet = pygame.Rect(bullet_coord[c][0], bullet_coord[c][1]+100, 50, 10)
        if plane_for_bads.colliderect(bullet):
            screen.blit(image_boom, (random_coord_plane_for_bads + 100, 0+u+100))
            cords_of_boom = random_coord_plane_for_bads + 100
            random_coord_plane_for_bads = random.randint(0, width - 200)
            boom_u = u + 100
            u = 0
            boom = True
            scoor += 1
            boom_number = 0
            if speed_of_plane_bads <= 20:
                speed_of_plane_bads += 1
            bullet_coord[c] = (bullet_coord[c][0], -100)
            if speed == 0.03:
                continue
            else:
                speed -= 0.01
    if u >= height-139:
        x = False
        while not x:
            font = pygame.font.SysFont("Calibri", 52)
            font_2 = font.render("GAME OVER", False, (255, 0, 100))
            scoor_print = font.render("Score: %s" % str(scoor), False, (255, 255, 0))
            image_again = pygame.image.load("images/again.png")
            for y in pygame.event.get():
                if y.type == pygame.QUIT:
                    exit(43)
                elif y.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                    if pygame.mouse.get_pos() > (430, 200):
                        if pygame.mouse.get_pos() < (530, 300):
                            speed = 0.08
                            scoor = 0
                            u = 0
                            S = 200
                            S_q = 0
                            plane_x = 350
                            plane_y = 500
                            bullet_coord = [(plane_x + 100, plane_y)]
                            go = "stop"
                            x = True
                            speed_of_plane_bads = 1
            screen.blit(font_2, (370, 300))
            screen.blit(scoor_print, (390, 400))
            screen.blit(image_again, (430, 200))
            pygame.display.flip()
    S_q += 10
    if S_q == S:
        S_q = 0
        bullet_coord.append((plane_x+100, plane_y))
    if go == "right":
        plane_x += 10
    elif go == "left":
        plane_x -= 10
    pygame.display.flip()
    time.sleep(speed)

