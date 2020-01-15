import pygame
import os
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

pygame.init()

BLACK =  (  0,   0,   0)
GREY  =  (100, 100, 100)
WHITE =  (255, 255, 255)

GROUND_HEIGHT = 160
WIDTH, HEIGHT = (1000, 300)

FPS = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Dino")

done = False
clock = pygame.time.Clock()

sprites = load_image("sprites.png")
dino_left = sprites.subsurface((1514, 0, 88, 100))
dino_right = sprites.subsurface((1602, 0, 88, 100))
cactus1 = sprites.subsurface((652, 0, 50, 100))
ground = sprites.subsurface((2, 104, 2402, 26))

font = pygame.font.Font(None, 40)

HIGH_SCORE = 0

x = 0
y = GROUND_HEIGHT
speed_x = 7
speed_y = 0
anim = 0
cactuses = [WIDTH + 100]

while not done:
 
    clock.tick(FPS)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]:
        if y == GROUND_HEIGHT:
            speed_y = -14
    
    for i in range(len(cactuses)):
        if cactuses[i] < x - 100:
            del cactuses[i]
            break
    
    if len(cactuses) < 5:
        cactuses.append(max(cactuses) + random.randint(250, 700))

    screen.fill(WHITE)

    screen.blit(ground, ((-x) % 2402, GROUND_HEIGHT + 70))
    screen.blit(ground, ((-x) % 2402 - 2402, GROUND_HEIGHT + 70))

    for c in cactuses:
        screen.blit(cactus1, (c - x, GROUND_HEIGHT))
    
    x += speed_x
    y = min(y + speed_y, GROUND_HEIGHT)
    if y < GROUND_HEIGHT:
        speed_y += 0.65
    else:
        speed_y = 0

    anim = (anim + 1) % (FPS // 4)
    if anim < (FPS // 4) // 2:
        screen.blit(dino_left, (50, y))
    else:
        screen.blit(dino_right, (50, y))
    
    current_score = str(x // 20)
    current_score = font.render("0" * (5 - len(current_score)) + current_score, False, BLACK)
    screen.blit(current_score, (WIDTH - 100, 20))
    if x // 20 > HIGH_SCORE:
        HIGH_SCORE = x // 20
    high_score = font.render("HI    " + "0" * (5 - len(str(HIGH_SCORE))) + str(HIGH_SCORE), False, GREY)
    screen.blit(high_score, (WIDTH - 300, 20))

    pygame.display.flip()
    
    for c in cactuses:
        if abs(x - c + 45) + abs(y - GROUND_HEIGHT) < 80:
            x = 0
            y = GROUND_HEIGHT
            speed_x = 7
            speed_y = 0
            anim = 0
            cactuses = [WIDTH + 100]
            #restarted = False
            #while not restarted:
            #   clock.tick(FPS)
            #   кнопка
            #   if pygame.key.get_pressed()[pygame.K_SPACE]:
            #       restarted = True
            #   pygame.display.flip()


pygame.quit()
