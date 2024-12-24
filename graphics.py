import pygame
import numpy as np


class Unit:
    """
    Класс, представляющий единичную величину в пикселях для оси координат.

    Атрибуты:
        pixels (int): Количество пикселей, соответствующее одной единице измерения на оси.
    """

    def __init__(self, pixels):
        self.pixels = pixels


class Origin:
    """
    Класс, представляющий точку начала координат.

    Атрибуты:
        x0 (float): Начальная координата по оси X.
        y0 (float): Начальная координата по оси Y.
    """

    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0


class ReferenceFrame:
    """
    Класс для хранения информации о системе координат, включающей начало координат и единичные величины для осей X и Y.

    Атрибуты:
        origin (Origin): Объект, представляющий точку начала координат.
        unit_x (Unit): Объект, представляющий единичную величину для оси X.
        unit_y (Unit): Объект, представляющий единичную величину для оси Y.
    """

    def __init__(self, origin, unit_x, unit_y):
        self.origin = origin
        self.unit_x = unit_x
        self.unit_y = unit_y


class Drawer:
    """
    Класс для рисования объектов на экране с использованием библиотеки Pygame.
    Отвечает за отображение графики, работу с цветами и координатами.

    Атрибуты:
        res_x (int): Ширина окна.
        res_y (int): Высота окна.
        rf (ReferenceFrame): Объект, представляющий систему координат.
        screen (pygame.Surface): Объект экрана Pygame, на котором происходит рисование.
        __color (tuple): Цвет, используемый для рисования объектов.
    """

    def __init__(self, res_x, res_y, rf: ReferenceFrame):
        """
        Инициализация объекта Drawer.

        Параметры:
            res_x (int): Ширина экрана.
            res_y (int): Высота экрана.
            rf (ReferenceFrame): Система координат для рисования.
        """
        self.res_x = res_x
        self.res_y = res_y
        self.rf = rf
        self.screen = None
        self.__color = (0,0,0)

    def initialize(self, caption: str):
        """
        Инициализация Pygame, создание окна и заполнение экрана фоном.

        Параметры:
            caption (str): Заголовок окна.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.res_x, self.res_y))
        pygame.display.set_caption(caption)
        self.screen.fill((0, 0, 0))

    @property
    def color(self):
        """
        Геттер для текущего цвета.

        Возвращает:
            tuple: Цвет в формате (r, g, b).
        """
        return self.__color

    @color.setter
    def color(self, color: tuple):
        """
        Сеттер для изменения цвета.

        Параметры:
            color (tuple): Новый цвет в формате (r, g, b).
        """
        self.__color = color

    def get_x(self, x: float):
        """
        Преобразование координаты X из системы координат в пиксели экрана.

        Параметры:
            x (float): Координата по оси X в системе координат.

        Возвращает:
            int: Пиксельная координата X на экране.
        """
        return int(self.rf.origin.x0 + x * self.rf.unit_x.pixels)

    def get_y(self, y: float):
        """
        Преобразование координаты Y из системы координат в пиксели экрана.
        Начало координат (0, 0) будет находиться в левом нижнем углу экрана.

        Параметры:
            y (float): Координата по оси Y в системе координат.

        Возвращает:
            int: Пиксельная координата Y на экране.
        """
        return int(self.res_y - (self.rf.origin.y0 + y * self.rf.unit_y.pixels))

    def draw_text(self, x: float, y: float, text: str):
        """
        Рисование текста на экране в заданной точке.

        Параметры:
            x (float): Координата X для текста.
            y (float): Координата Y для текста.
            text (str): Текст для отображения.
        """
        font = pygame.font.Font(None, 24)  # Шрифт
        text_surface = font.render(text, True, self.color)  # Создание текстового изображения
        self.screen.blit(text_surface, (self.get_x(x), self.get_y(y)))  # Отображение текста на экране

    def draw_line(self, x1: float, y1: float, x2: float, y2: float, width: int = 1):
        """
        Рисование линии на экране от одной точки до другой.

        Параметры:
            x1 (float): Начальная координата X.
            y1 (float): Начальная координата Y.
            x2 (float): Конечная координата X.
            y2 (float): Конечная координата Y.
            width (int): Ширина линии (по умолчанию 1).
        """
        pygame.draw.line(
            self.screen,
            self.color,
            (self.get_x(x1), self.get_y(y1)),
            (self.get_x(x2), self.get_y(y2)),
            width
        )

    def draw_polygon(self, points: np.ndarray, width: int = 1):
        """
        Рисование многоугольника по заданным вершинам.

        Параметры:
            points (np.ndarray): Массив точек многоугольника в системе координат.
            width (int): Ширина линий многоугольника (по умолчанию 1).
        """
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.get_x(pt[0]), self.get_y(pt[1])) for pt in points],
            width
        )

    def draw_axes(self, x_min, x_max, y_min, y_max):
        """
        Рисование осей координат на экране.
        Ось X рисуется на уровне y = 0, а ось Y — на уровне x = 0.

        Параметры:
            x_min (float): Минимальное значение для оси X.
            x_max (float): Максимальное значение для оси X.
            y_min (float): Минимальное значение для оси Y.
            y_max (float): Максимальное значение для оси Y.
        """
        self.draw_line(x_min, 0, x_max, 0, 2)  # Рисование X-оси
        self.draw_line(0, y_min, 0, y_max, 2)  # Рисование Y-оси
