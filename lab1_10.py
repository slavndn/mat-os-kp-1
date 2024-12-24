import pygame
import math

# Константы
width, height = 600, 600  # Размеры окна
white = (255, 255, 255)
blue = (0, 0, 255)

# Параметры улитки Паскаля
a = 50  # Радиус, влияющий на амплитуду
b = 50  # Начальный радиус

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Улитка Паскаля")

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана белым
    screen.fill(white)

    # Координаты центра экрана
    center_x, center_y = width // 2, height // 2

    # Рисуем спираль
    theta = 0  # Угол в радианах
    step = 0.01  # Шаг изменения угла
    max_loops = 20  # Количество витков

    while theta < max_loops * 2 * math.pi:  # Вращаем до заданного количества витков
        # Вычисляем радиус и координаты
        r = b + 2 * a * math.cos(theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)

        # Преобразуем в координаты окна
        screen_x = int(center_x + x)
        screen_y = int(center_y - y)

        # Рисуем точку
        pygame.draw.circle(screen, blue, (screen_x, screen_y), 1)

        # Увеличиваем угол
        theta += step

    # Обновление экрана
    pygame.display.flip()

# Закрытие Pygame
pygame.quit()
