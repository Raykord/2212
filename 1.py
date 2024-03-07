import pygame
import sys
import random
pygame.init() 

WIDTH = 500 #переменная для ширины экрана
HEIGHT = 500 #переменная для высоты экрана
FPS = 60 #частота кадров
BG = (55, 61, 240) #цвет заднего фона
TOMATO = (240, 55, 55) #цвет игрока
player = pygame.Rect(100, 100, 100, 100) #игрок он квадрат
bot = pygame.Rect(300, 300, 100, 100) #игрок он квадрат

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создаём экран

clock = pygame.time.Clock() #класс для работы с фпс
playerImageOrig = pygame.image.load('oar2.jpg') #Добавили картинку 
playerImage = pygame.transform.scale(playerImageOrig, (player.width,player.height)) #Растянули по размеру хитбокса игрока
direction = 'none'
gameState = 0

while True:
    screen.fill(BG) #Меняем цвет фона
    
    if gameState == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameState = 1
    elif gameState == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    TOMATO = (0, 0, 0)
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                if event.key == pygame.K_UP:
                    direction = 'up'
                if event.key == pygame.K_RIGHT:
                    direction = 'right'
                if event.key == pygame.K_DOWN:
                    direction = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                    direction = 'none'
            if event.type == pygame.QUIT:
                sys.exit()

        if direction == 'right':
            player.x += 5
        elif direction == 'left':
            player.x -= 5
        elif direction == 'up':
            player.y -= 5
        elif direction == 'down':
            player.y += 5

        if player.colliderect(bot):
            bot.x = random.randint(0, WIDTH-bot.width)
            bot.y = random.randint(0, HEIGHT-bot.height)
            player.width += 10
            player.height += 10
            bot.width -= 10
            bot.height -= 10
            playerImage = pygame.transform.scale(playerImageOrig, (player.width, player.height))
            if player.width <= 0 or bot.width <= 0:
                gameState = 2
    
        screen.blit(playerImage, player) #отрисовываем на экране
        pygame.draw.rect(screen, TOMATO, bot) #отрисовываем на экране


    elif gameState == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.width = 100
                    player.height = 100
                    bot.width = 100
                    bot.height = 100
                    playerImage = pygame.transform.scale(playerImageOrig, (player.width, player.height))
                    gameState = 1
                    
    



    pygame.display.update() #обновляем изображение на экране
    clock.tick(FPS) #задаём FPS