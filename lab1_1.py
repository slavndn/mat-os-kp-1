import numpy as np
import pygame

# Исходная матрица и точка
transformation_matrix = np.array([[1, 3],
                                  [4, 1]])
point = np.array([1, 1])

# Перемножаем матрицу и точку
transformed_point = np.dot(transformation_matrix, point)

# Вывод начальных и преобразованных координат точки
print("Начальная точка:", point)
print("Преобразованная точка:", transformed_point)

# Инициализация Pygame
pygame.init()

# Размеры экрана
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Визуализация преобразования")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана белым цветом
    screen.fill(white)

    # Рисуем оси
    pygame.draw.line(screen, (0, 0, 0), (width // 2, 0), (width // 2, height), 2)  # вертикальная ось
    pygame.draw.line(screen, (0, 0, 0), (0, height // 2), (width, height // 2), 2)  # горизонтальная ось

    # Масштабирование для визуализации
    scale = 25  # Масштаб точек

    # Отображаем исходную точку (1, 2)
    pygame.draw.circle(screen, red, (int(point[0] * scale + width / 2), int(-point[1] * scale + height / 2)), 5)

    # Отображаем преобразованную точку
    pygame.draw.circle(screen, blue, (int(transformed_point[0] * scale + width / 2), int(-transformed_point[1] * scale + height / 2)), 5)

    # Обновление экрана
    pygame.display.flip()

# Закрытие Pygame
pygame.quit()
