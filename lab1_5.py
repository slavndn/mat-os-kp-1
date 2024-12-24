import numpy as np
import pygame

# Матрица преобразования
transformation_matrix = np.array([[1, 2],
                                  [3, 1]])

# Исходный отрезок
start_point_L = np.array([50, 100])
end_point_L = np.array([250, 200])

start_point_M = np.array([50, 200])
end_point_M = np.array([250, 300])


# Применение матрицы преобразования к началу и концу отрезка
transformed_start_L = np.dot(start_point_L, transformation_matrix)
transformed_end_L = np.dot(end_point_L, transformation_matrix)

transformed_start_M = np.dot(start_point_M, transformation_matrix)
transformed_end_M = np.dot(end_point_M, transformation_matrix)


# Функция для расчёта наклона
def calculate_slope(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    return dy / dx if dx != 0 else float('inf')  # Возвращаем "бесконечность" для вертикальных линий

# Расчёт наклонов
initial_slope_L = calculate_slope(start_point_L, end_point_L)
transformed_slope_L = calculate_slope(transformed_start_L, transformed_end_L)

initial_slope_M = calculate_slope(start_point_M, end_point_M)
transformed_slope_M = calculate_slope(transformed_start_M, transformed_end_M)


# Вывод координат и наклонов
print("Исходный отрезок L: начало", start_point_L, ", конец", end_point_L)
print("Преобразованный отрезок L: начало", transformed_start_L, ", конец", transformed_end_L)
print("Наклон исходного отрезка L:", initial_slope_L)
print("Наклон преобразованного отрезка L:", transformed_slope_L)

print("Исходный отрезок M: начало", start_point_M, ", конец", end_point_M)
print("Преобразованный отрезок M: начало", transformed_start_M, ", конец", transformed_end_M)
print("Наклон исходного отрезка M:", initial_slope_M)
print("Наклон преобразованного отрезка M:", transformed_slope_M)


# Инициализация Pygame
pygame.init()

# Размеры экрана
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Преобразование отрезков")

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
                     (int(start_point_L[0] * scale + width / 2), int(-start_point_L[1] * scale + height / 2)),
                     (int(end_point_L[0] * scale + width / 2), int(-end_point_L[1] * scale + height / 2)), 3)

    pygame.draw.line(screen, green,
                     (int(start_point_M[0] * scale + width / 2), int(-start_point_M[1] * scale + height / 2)),
                     (int(end_point_M[0] * scale + width / 2), int(-end_point_M[1] * scale + height / 2)), 3)

    # Отображаем преобразованный отрезок синим цветом
    pygame.draw.line(screen, blue,
                     (int(transformed_start_L[0] * scale + width / 2), int(-transformed_start_L[1] * scale + height / 2)),
                     (int(transformed_end_L[0] * scale + width / 2), int(-transformed_end_L[1] * scale + height / 2)), 3)

    pygame.draw.line(screen, green,
                     (int(transformed_start_M[0] * scale + width / 2), int(-transformed_start_M[1] * scale + height / 2)),
                     (int(transformed_end_M[0] * scale + width / 2), int(-transformed_end_M[1] * scale + height / 2)), 3)



    # Обновление экрана
    pygame.display.flip()

# Закрытие Pygame
pygame.quit()
