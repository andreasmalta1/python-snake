# Snake game

import pygame
import random

pygame.init()

# Declaring the colours in RGB
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Setting the game window size
dis_width = 600
dis_height = 400

# Displaying the game screen
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Setting the size and speed of the snake
snake_block = 10
# snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("arial", 25)


# Function to show the score
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# Function to draw the snake
def our_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], block, block])


# Function to display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


# Game function
def game_loop():
    game_over = False
    game_close = False

    # Setting the starting snake location at the centre
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1
    snake_speed = 10

    # Setting the fruit location at random
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Loop while game is not over
    while not game_over:
        # Run after loss but before quitting
        while game_close:
            # Tell the user they lost and ask whether they wish to continue or quit
            dis.fill(blue)
            message("You Lost! Press P-Play Again or Q-Quit", red)
            your_score(snake_length - 1)
            pygame.display.update()

            # Check the keyboard user entry
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # If q is pressed game is quit
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    # If the p is pressed user wants to play again and game_loop function is restarted
                    if event.key == pygame.K_p:
                        game_loop()

        # Checking every event in pygame
        for event in pygame.event.get():
            # If the quit icon is selected, game is closed down
            if event.type == pygame.QUIT:
                game_over = True
            # Ever time a key is pressed, the button pressed is checked
            if event.type == pygame.KEYDOWN:
                # If left key is pressed snake block will move to negative x axis
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                # If right key is pressed snake block will move to positive x axis
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                # If up key is pressed snake block will move to negative y axis
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                # If down is pressed snake block will move to positive y axis
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Once the snake hits the boundaries the game is over
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Setting the direction changes
        x1 += x1_change
        y1 += y1_change

        # Drawing the game
        dis.fill(blue)
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(snake_length - 1)

        pygame.display.update()

        # If snake eats food, new food is generated and snake increases in length
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_length += 1
            snake_speed += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
