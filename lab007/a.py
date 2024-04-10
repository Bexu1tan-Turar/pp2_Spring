import pygame
from datetime import datetime

pygame.init()

# размеры экрана
width, height = 800, 800
x = width // 2
y = height // 2
white = (255, 255, 255)
sc = pygame.display.set_mode((width, height))

mickey = pygame.image.load("mickeyclock.png")
leftHand = pygame.image.load("left-hand.png")
rightHand = pygame.image.load("right-hand.png")
mickeyRect = mickey.get_rect()

# Функция для вращения и вывода изображения на экран
def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
    surf.blit(rotated_image, new_rect)

current_datetime = datetime.now()
#Вычисление начальных углов для стрелок часов на основе текущего времени
second = 78 - current_datetime.second * 6  # 6 degrees per second
minute = 78 - current_datetime.minute * 6  # 6 degrees per minute

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Обновление углов для стрелок часов
    second -= 0.099  
    minute -= 0.00165  

    # заливка экрана(белый)
    sc.fill(white)

    #Вывод изображения часов с изображением Микки Мауса
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)  

    # Вращение и вывод стрелок часов
    blitRotateCenter(sc, leftHand, (x, y), second)
    blitRotateCenter(sc, rightHand, (x, y), minute)
    #изменения в изображений(fps)
    pygame.display.update()
