import numpy as np
import pygame

# Матрица преобразования
transformation_matrix = np.array([[1, 3],
                                  [4, 1]])

# Координаты начального отрезка
start_point = np.array([1, 2])
end_point = np.array([3, 1])

# Применение матрицы преобразования к начальной и конечной точкам отрезка
transformed_start = np.dot(start_point, transformation_matrix)
transformed_end = np.dot(end_point, transformation_matrix)

# Вывод начальных и преобразованных координат
print("Исходный отрезок: начало", start_point, ", конец", end_point)
print("Преобразованный отрезок: начало", transformed_start, ", конец", transformed_end)

# Инициализация Pygame
pygame.init()

# Размеры экрана
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Преобразование отрезка")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

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
    scale = 10  # Масштаб точек

    # Отображаем исходный отрезок красным цветом
    pygame.draw.line(screen, red,
                     (int(start_point[0] * scale + width / 2), int(-start_point[1] * scale + height / 2)),
                     (int(end_point[0] * scale + width / 2), int(-end_point[1] * scale + height / 2)), 3)

    # Отображаем преобразованный отрезок синим цветом
    pygame.draw.line(screen, blue,
                     (int(transformed_start[0] * scale + width / 2), int(-transformed_start[1] * scale + height / 2)),
                     (int(transformed_end[0] * scale + width / 2), int(-transformed_end[1] * scale + height / 2)), 3)

    # Обновление экрана
    pygame.display.flip()

# Закрытие Pygame
pygame.quit()
