import pygame

pygame.init()

# color library
white = (255, 255, 255)
black = (0, 0, 0)
purple = (255, 0, 255)
orange = (255, 165, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((300, 450))
pygame.display.set_caption("My first Pygame game")
background = black
framerate = 60
font = pygame.font.SysFont("Arial", 16)
timer = pygame.time.Clock()

# game variables
green_value = 1
red_value = 2
orange_value = 3
white_value = 4
purple_value = 5

draw_green = False
draw_red = False
draw_orange = False
draw_white = False
draw_purple = False

green_length = 0
red_length = 0
orange_length = 0
white_length = 0
purple_length = 0

green_speed = 5
red_speed = 4
orange_speed = 3
white_speed = 2
purple_speed = 1

score = 90

green_cost = 1
green_owned = False
green_manager_cost = 100
red_cost = 2
red_owned = False
red_manager_cost = 500
orange_cost = 3
orange_owned = False
orange_manager_cost = 1000
white_cost = 4
white_owned = False
white_manager_cost = 2000
purple_cost = 5
purple_owned = False
purple_manager_cost = 5000



def draw_task(color, y_coord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
    task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])
    value_text = font.render(str(round(value,2)), True, color)
    screen.blit(value_text, (16, y_coord - 10))
    return task, length, draw

def draw_buttons(color, x_coord, cost, manager_cost, owned):
    color_button = pygame.draw.rect(screen, color, [x_coord, 340, 50, 30])
    color_cost = font.render(str(round(cost, 2)), True, black)
    screen.blit(color_cost, (x_coord + 6, 350))
    if not owned:
        manager_button = pygame.draw.rect(screen, color, [x_coord, 405, 50, 30])
        manager_text = font.render(str(round(manager_cost, 2)), True, black)
        screen.blit(manager_text, (x_coord + 6, 410))
    else:
        manager_button = pygame.draw.rect(screen, black, [x_coord, 405, 50, 30], 5)
    return color_button, manager_button

running = True
while running:
    timer.tick(framerate)
    
    if green_owned and not draw_green:
        draw_green = True
    if red_owned and not draw_red:
        draw_red = True
    if orange_owned and not draw_orange:
        draw_orange = True
    if white_owned and not draw_white:
        draw_white = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_green = True
            if task2.collidepoint(event.pos):
                draw_red = True
            if task3.collidepoint(event.pos):
                draw_orange = True
            if task4.collidepoint(event.pos):
                draw_white = True
            if task5.collidepoint(event.pos):
                draw_purple = True
            if green_manager_buy.collidepoint(event.pos):
                if score >= green_manager_cost and not green_owned:
                    score -= green_manager_cost
                    green_owned = True
            if red_manager_buy.collidepoint(event.pos):
                if score >= red_cost and not red_owned:
                    score -= red_manager_cost
                    red_owned = True
            if orange_manager_buy.collidepoint(event.pos):
                if score >= orange_cost and not orange_owned:
                    score -= orange_manager_cost
                    orange_owned = True
            if white_manager_buy.collidepoint(event.pos):
                if score >= white_cost and not white_owned:
                    score -= white_manager_cost
                    white_owned = True
            if purple_manager_buy.collidepoint(event.pos):
                if score >= purple_cost and not purple_owned:
                    score -= purple_manager_cost
                    purple_owned = True
            if green_buy.collidepoint(event.pos) and score >= green_cost:
                green_value += .15
                green_cost += .1 
                score -= green_cost
            if red_buy.collidepoint(event.pos) and score >= red_cost:
                red_value += .15
                red_cost += .1 
                score -= red_cost
            if orange_buy.collidepoint(event.pos) and score >= orange_cost:
                orange_value += .15
                orange_cost += .1 
                score -= orange_cost
            if white_buy.collidepoint(event.pos) and score >= white_cost:
                white_value += .15
                white_cost += .1 
                score -= white_cost
            if purple_buy.collidepoint(event.pos) and score >= purple_cost:
                purple_value += .15
                purple_cost += .1 
                score -= purple_cost

    screen.fill(background)
    task1, green_length, draw_green = draw_task(green, 50, green_value, draw_green, green_length, green_speed)
    task2, red_length, draw_red = draw_task(red, 110, red_value, draw_red, red_length, red_speed)
    task3, orange_length, draw_orange = draw_task(orange, 170, orange_value, draw_orange, orange_length, orange_speed)
    task4, white_length, draw_white = draw_task(white, 230, white_value, draw_white, white_length, white_speed)
    task5, purple_length, draw_purple = draw_task(purple, 290, purple_value, draw_purple, purple_length, purple_speed)

    green_buy, green_manager_buy = draw_buttons(green, 10, green_cost, green_manager_cost, green_owned)
    red_buy, red_manager_buy = draw_buttons(red, 70, red_cost, red_manager_cost, red_owned)
    orange_buy, orange_manager_buy = draw_buttons(orange, 130, orange_cost, orange_manager_cost, orange_owned)
    white_buy, white_manager_buy = draw_buttons(white, 190, white_cost, white_manager_cost, white_owned)
    purple_buy, purple_manager_buy = draw_buttons(purple, 250, purple_cost, purple_manager_cost, purple_owned)

    score_text = font.render("Score: $" + str(round(score, 2)), True, white, black)
    screen.blit(score_text, (10, 5))
    buy_more = font.render('Buy more', True, white, black)
    screen.blit(buy_more, (10, 315))
    buy_managers = font.render('Buy managers', True, white, black)
    screen.blit(buy_managers, (10, 380))
    pygame.display.flip()

pygame.quit()