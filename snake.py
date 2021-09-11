import pygame
import random
import os

pygame.mixer.init()




pygame.init()
# colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

screen_width = 800
screen_height = 500
# creating windows
gameWindow = pygame.display.set_mode((screen_width, screen_height)).convert_alpha()

#bacground image
bgimg=pygame.image.load('dragon.jpg')
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height))

pygame.display.set_caption("SNAKE WITH AKASH VERMA")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome To World Hardest Game ", black, 100, 250)
        text_screen("Press Spacebar To Play ", black, 140, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('play.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(30)


# game loop
def gameloop():
    snk_list = []
    snk_lenght = 1
    exit_game = False
    game_over = False
    snake_x = 100
    snake_y = 250
    snake_size = 20
    fps = 30
    velocity_x = 4
    velocity_y = 4
    score = 0
    init_velocity = 5
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt") as f:
        highscore = f.read()
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            text_screen("game over! press enter to coninue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y

            if abs(snake_x-food_x) < 20 and abs(snake_y-food_y) < 20:
                score += 10

                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_lenght += 5
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("score: " + str(score) + " highscore:" +
                        str(highscore), blue, 5, 5)
            pygame.draw.rect(gameWindow, red, [
                             food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('play.mp3')
                pygame.mixer.music.play()
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('play.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
