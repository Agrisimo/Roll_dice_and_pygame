import random
import time
import pygame

pygame.init()
pygame.font.init()


# Main arena dimensions and program name
arena_x = 700
arena_y = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

arena = pygame.display.set_mode((arena_x, arena_y))
pygame.display.set_caption("Agrisimo Dice game")

# Object and arena colors

background_color = (0,0,0)
dice_color = WHITE
digit_color = (111, 142, 20)

# Sizes of objects:
width_dice = 200
height_dice = 200

digit_font_size = 20

# Coordinates of objects:
x_dice1 = arena_x / 2 - width_dice
y_dice1 = arena_y / 2 - height_dice / 2
x_dice2 = arena_x / 2 + 50
y_dice2 = arena_y / 2 - height_dice / 2
x_digit1 = 200
y_digit1 = 55
x_digit2 = 445
y_digit2 = 55



game_running = True
exit_time = 3

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)


myfont = pygame.font.SysFont('Comic Sans MS', 200)
mainfont = pygame.font.SysFont('Comic Sans MS', 35)
bottomfont = pygame.font.SysFont('Comic Sans MS', 35)

def draw_dice_digit(text, color):
    screen_text = myfont.render(text, True, color)
    arena.blit(screen_text, [x_digit1, y_digit1])

def draw_dice_digitTwo(text, color):
    screen_text = myfont.render(text, True, color)
    arena.blit(screen_text, [x_digit2, y_digit2])

def draw_summ(text, color):
    screen_text = mainfont.render(text, True, color)
    arena.blit(screen_text, [520, 350])

def main_text(text, color):
    screen_text = mainfont.render(text, True, color)
    arena.blit(screen_text, [100, 0])

def bottom_text(text, color):
    screen_text = mainfont.render(text, True, color)
    arena.blit(screen_text, [230, 350])



doubles = True

while game_running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    main_text(""""To roll dices press and hold "r"!""", WHITE)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:
        doubles = True
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        arena.fill((background_color))
        pygame.draw.rect(arena, dice_color, (x_dice1, y_dice1, width_dice, height_dice))
        pygame.draw.rect(arena, dice_color, (x_dice2, y_dice2, width_dice, height_dice))
        draw_summ(f"Summ = {dice1+dice2}",WHITE)
        draw_dice_digit(f"{dice1}", digit_color)
        draw_dice_digitTwo(f"{dice2}", digit_color)
        time.sleep(0.01)
        pygame.display.update()

        print(f"""1. dice = {dice1}        
2. dice = {dice2}
""")
    if dice1 == dice2 and keys[pygame.K_r] == False and doubles == True:
        bottom_text("Double trouble!", WHITE)
        pygame.display.update()
        print("Double trouble!")
        doubles = False



    if keys[pygame.K_ESCAPE]:
        print("Sorry to hear you`re leaving!")
        print(f"The program will terminate in {exit_time} seconds!")
        time.sleep(exit_time)
        quit()


# Character. Shape, on which surface, color, coordinates, width and height)

pygame.quit()