import pygame
import sys
import random
pygame.init() 

class Sprite:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.orig_img, (self.rect.width,self.rect.height))
        self.direction = 'none'
    def move(self):#метод движения
        if self.direction == 'right':
            self.rect.x += 5
        elif self.direction == 'left':
            self.rect.x -= 5
        elif self.direction == 'up':
            self.rect.y -= 5
        elif self.direction == 'down':
            self.rect.y += 5

    
    def draw(self):#метод отрисовки
        screen.blit(self.img, self.rect)


FPS = 60 #частота кадров
BG = (55, 61, 240) #цвет заднего фона
TOMATO = (240, 55, 55) #цвет игрока
player = Sprite(100, 100, 100, 100, 'oar2.jpg')
bot = pygame.Rect(300, 300, 100, 100) #игрок он квадрат
closeButton = pygame.Rect(0, 0, 50, 50)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #создаём экран

clock = pygame.time.Clock() #класс для работы с фпс


gameState = 0

font = pygame.font.SysFont('Arial', 30)

startText1 = font.render('Добро пожаловать', True, (0, 255, 0))
startText2 = font.render('Нажмите пробел', True, (0, 255, 0))

while True:
    screen.fill(BG) #Меняем цвет фона
    
    if gameState == 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameState = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if closeButton.x < x < closeButton.right and closeButton.y < y < closeButton.bottom:
                    sys.exit()
        screen.blit(startText1, (20, 225))
        screen.blit(startText2, (20, 255))
        pygame.draw.rect(screen, TOMATO, closeButton)
    elif gameState == 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if player.rect.x < x < player.rect.right and player.rect.y < y < player.rect.bottom:
                    player.rect.width += 10
                    player.rect.height += 10
                    player.img= pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    TOMATO = (0, 0, 0)
                if event.key == pygame.K_LEFT:
                    player.direction = 'left'
                if event.key == pygame.K_UP:
                    player.direction = 'up'
                if event.key == pygame.K_RIGHT:
                    player.direction = 'right'
                if event.key == pygame.K_DOWN:
                    player.direction = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                    player.direction = 'none'
            if event.type == pygame.MOUSEBUTTONDOWN: #проверяем нажатие мыши
                x, y = event.pos #записываем координаты мыши
                #проверяем что мышь в момент клика была на кнопке
                if closeButton.x < x < closeButton.right and closeButton.y < y < closeButton.bottom:
                    sys.exit()

        player.move()
    
    

        if player.rect.colliderect(bot):
            bot.x = random.randint(0, 1600)
            bot.y = random.randint(0, 1600)
            player.rect.width += 10
            player.rect.height += 10
            bot.width -= 10
            bot.height -= 10
            player.img= pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
            if player.rect.width <= 0 or bot.width <= 0:
                gameState = 2
    
        player.draw() #отрисовываем на экране
        pygame.draw.rect(screen, TOMATO, bot) #отрисовываем на экране
        pygame.draw.rect(screen, TOMATO, closeButton)

    elif gameState == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.rect.width = 100
                    player.rect.height = 100
                    bot.width = 100
                    bot.height = 100
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    gameState = 1
         
                    
    



    pygame.display.update() #обновляем изображение на экране
    clock.tick(FPS) #задаём FPS

