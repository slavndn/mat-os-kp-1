import numpy as np
import pygame

# Матрица преобразования
transformation_matrix = np.array([[1, 2],
                                  [3, 1]])

# Исходный отрезок
start_point = np.array([0, 100])
end_point = np.array([200, 300])

# Применение матрицы преобразования к началу и концу отрезка
transformed_start = np.dot(start_point, transformation_matrix)
transformed_end = np.dot(end_point, transformation_matrix)

# Вычисление середины исходного и преобразованного отрезков
mid_original = (start_point + end_point) / 2
mid_transformed = (transformed_start + transformed_end) / 2
mid_original = mid_original.astype(int)
mid_transformed = mid_transformed.astype(int)

# Вывод координат
print("Исходный отрезок: начало", start_point, ", конец", end_point)
print("Преобразованный отрезок: начало", transformed_start, ", конец", transformed_end)
print("Середина исходного отрезка:", mid_original)
print("Середина преобразованного отрезка:", mid_transformed)

# Инициализация Pygame
pygame.init()

# Размеры экрана
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Преобразование отрезка и середины")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
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
    scale = 0.2  # Масштаб для отрезков

    # Отображаем исходный отрезок красным цветом
    pygame.draw.line(screen, red,
                     (int(start_point[0] * scale + width / 2), int(-start_point[1] * scale + height / 2)),
                     (int(end_point[0] * scale + width / 2), int(-end_point[1] * scale + height / 2)), 3)

    # Отображаем преобразованный отрезок синим цветом
    pygame.draw.line(screen, blue,
                     (int(transformed_start[0] * scale + width / 2), int(-transformed_start[1] * scale + height / 2)),
                     (int(transformed_end[0] * scale + width / 2), int(-transformed_end[1] * scale + height / 2)), 3)

    # Отображаем середины отрезков
    pygame.draw.circle(screen, green, (int(mid_original[0] * scale + width / 2), int(-mid_original[1] * scale + height / 2)), 5)
    pygame.draw.circle(screen, green, (int(mid_transformed[0] * scale + width / 2), int(-mid_transformed[1] * scale + height / 2)), 5)

    # Соединяем середины отрезков линией
    pygame.draw.line(screen, green,
                     (int(mid_original[0] * scale + width / 2), int(-mid_original[1] * scale + height / 2)),
                     (int(mid_transformed[0] * scale + width / 2), int(-mid_transformed[1] * scale + height / 2)), 2)

    # Обновление экрана
    pygame.display.flip()

# Закрытие Pygame
pygame.quit()
