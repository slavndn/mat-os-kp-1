import pygame
import numpy as np
import sys
from graphics import Unit, Origin, ReferenceFrame, Drawer
from transform import translate, scale, rotate

# Константы
RES_X, RES_Y = 800, 600
SCALE = 0.9
ANGLE = np.pi / 32
ITERATIONS = 20

# Начальные координаты квадрата
square = np.array([
    [2, -2, 1],
    [-2, -2, 1],
    [-2, 2, 1],
    [2, 2, 1]
])

# Единичный размер и начало координат
unit = Unit(100)
origin = Origin(RES_X / 2, RES_Y / 2)
rf = ReferenceFrame(origin, unit, unit)

# Drawer для рисования
drawer = Drawer(RES_X, RES_Y, rf)
drawer.initialize("Square Transformation")

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    drawer.screen.fill((255, 255, 255))


    # Рисовать все итерации
    current_square = square.copy()
    for i in range(ITERATIONS + 1):
        # Преобразование: масштабирование и поворот относительно центра
        transform = (
            scale(SCALE, SCALE) @  # Масштабирование
            rotate(ANGLE) @  # Поворот
            translate(origin.x0 / unit.pixels, origin.y0 / unit.pixels)  # Возврат к центру
        )

        # Цвет квадрата зависит от итерации
        drawer.color = (255, 0, 0)

        # Нарисовать квадрат
        drawer.draw_polygon(current_square)

        # Применить трансформацию для следующей итерации
        current_square = current_square @ transform.T

    # Обновление экрана
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Завершение Pygame
pygame.quit()
sys.exit()
