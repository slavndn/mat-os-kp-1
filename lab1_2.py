import pygame
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Графические примитивы")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
black = (0, 0, 0)
orange = (255, 165, 0)

# Настройка шрифта
font = pygame.font.Font(None, 36)

# Основной цикл
running = True
while running:
    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана белым цветом
    screen.fill(white)

    # Рисование окружности
    pygame.draw.circle(screen, yellow, (width // 4, height // 3), 70, 4)

    # Рисование линии
    pygame.draw.line(screen, blue, (100, height // 2), (width - 100, height // 2), 5)

    # Рисование прямоугольника
    pygame.draw.rect(screen, green, (width // 2 - 100, height - 150, 200, 100), 0)  # Заполненный

    # Рисование многоугольника
    pygame.draw.polygon(screen, red, [(width // 2 + 50, height // 3 - 20),
                                      (width // 2 + 150, height // 3 - 100),
                                      (width // 2 + 250, height // 3 - 20),
                                      (width // 2 + 200, height // 3 + 50),
                                      (width // 2 + 100, height // 3 + 50)], 3)  # С контуром

    # Рисование маленькой пурпурной окружности в центре
    pygame.draw.circle(screen, purple, (width // 2, height // 2), 20, 0)  # Заполненный

    # Рисование маленькой оранжевой окружности
    pygame.draw.circle(screen, orange, (width - 100, 100), 30, 0)

    # Добавление текста
    text = font.render("text", True, purple)
    screen.blit(text, (width // 4 - text.get_width() // 2, height - 100))

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
sys.exit()
