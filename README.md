# Практическая работа 1  
Цель работы. Работа направлена на прорешивание простых базовых задач с помощью библиотек pygame и numpy.  
Только последняя 11-я задача является более объемной и предполагает элементы ООП.  

1. Напишите программу, которая позволяет ввести координаты точки и применить к ним матричное преобразование с матрицей:  
```
T =  ⎡ 1  3 ⎤  
     ⎣ 4  1 ⎦  
```
Выведите на экран начальные и полученные координаты. Прорисуйте исходную и новую точки в окне с использованием pygame.  

![image](https://github.com/user-attachments/assets/95d6d5d6-f49d-47b9-9559-8fcb51d113c2)

![image](https://github.com/user-attachments/assets/d1164ff8-d630-4e4b-87ff-a8d01b1a8f0f)


2. Нарисуйте графические примитивы (pygame) — окружность, линии, текст — различными цветами в окне программы.

![image](https://github.com/user-attachments/assets/06566ea6-69e6-44cd-9e4f-57c96a8673fe)


3. Напишите программу, которая преобразует отрезок, заданный двумя точками. Запишите координаты в матрицу
отрезка и примените к ней матричное преобразование:
```
T =  ⎡ 1  3 ⎤  
     ⎣ 4  1 ⎦  
```
Отобразите исходный и преобразованный отрезок разными цветами.  
 
![image](https://github.com/user-attachments/assets/f6c87294-d63e-41fb-aa5e-76a124a37ecd)
![image](https://github.com/user-attachments/assets/02653d06-0bff-46b2-999d-36779a65fc6e)


4. Напишите программу для преобразования координат конца отрезка

```
𝐿 =  ⎡  0  100 ⎤  
     ⎣ 200 300 ⎦  
```
по матрице:
```
T =  ⎡ 1  2 ⎤  
     ⎣ 3  1 ⎦  
```

Найдите середину исходного и преобразованного отрезка и визуализируйте оба отрезка с помощью pygame. Обозначьте середины отрезков небольшими кругами и соедините их ещё одним отрезком.

![image](https://github.com/user-attachments/assets/3031dd25-8295-411e-98ec-036840575a79)
![image](https://github.com/user-attachments/assets/4ea55224-6174-443b-bbb7-b8d8063f91cd)
 

5. Преобразуйте два параллельных отрезка, заданных матрицей
```
𝐿 =  ⎡ 50  100 ⎤
     ⎜250 200 ⎜
     ⎜ 50 200 ⎜
     ⎣ 250 300 ⎦  ,
```
с помощью той же матрицы 𝑇, что и в предыдущей задаче. Рассчитайте и отобразите их начальный и конечный наклоны.

![image](https://github.com/user-attachments/assets/3e505a28-6629-44d4-9c40-689d65756aa2)  
![image](https://github.com/user-attachments/assets/7c768055-857e-41a6-bc02-7220ff7422cf)  


6. Напишите программу для преобразования пересекающихся отрезков
```
𝐿 =  ⎡ −1/2  3/2 ⎤
     ⎜  3   −2  ⎜
     ⎜ −1   −1  ⎜
     ⎣  3   5/3  ⎦
```
по матрице:
```
T =  ⎡ 1  2 ⎤  
     ⎣ 1 -3 ⎦  
```

Искусственно сместите все получившиеся отрезки в видимую область игрового окна для наглядности (сохраняйте оригинальную матрицу координат в изначальной матрице 𝐿 !). Перед преобразованиями умножьте искусственно
матрицу отрезка 𝐿 на 100, чтобы он и его преобразованная версия имели видимую длину в пикселях.

![image](https://github.com/user-attachments/assets/85993f34-a52a-48c9-821d-ca033a85658e)

![image](https://github.com/user-attachments/assets/e3c24b3b-603d-48fa-a7dc-5b93e6617657)


7. Вращайте треугольник
```
𝐿 =  ⎡  3   -1 ⎤
     ⎜ 4   1   ⎜
     ⎣  2   1  ⎦
```

на 90 градусов (𝜋/2) против часовой стрелки с помощью матрицы:
```
T =  ⎡  0  1 ⎤  
     ⎣ -1  0 ⎦  
```

Перед преобразованиями умножьте искусственно матрицу отрезка 𝐿 на 100, чтобы он и его преобразованная версия
имели видимую длину в пикселях. Как и в предыдущей задаче, смещайте оригинальный треугольник, чтобы он был
виден на экране (сохраняйте оригинальную матрицу координат в изначальной матрице 𝐿 !), после преобразования
матрицы 𝐿 сместите на такое же количество пикселей в видимую область окна новый треугольник 𝐿.

![image](https://github.com/user-attachments/assets/c94c4e4a-98bc-4751-ac54-08e389b7677e)  


8. Отразите треугольник

```
𝐿 =  ⎡  8   1  ⎤
     ⎜ 7   3  ⎜
     ⎣  6   2  ⎦
```
относительно линии 𝑦 = 𝑥 с помощью матрицы:
```
T =  ⎡  0  1 ⎤  
     ⎣  1  0 ⎦  
```
Также прибегайте к смещениям в пикселях, к умножению на 100 и тому подобным приёмам, как и в предыдущей
задаче, чтобы треугольники были видны.

![image](https://github.com/user-attachments/assets/8c5dafe1-da67-47b1-8b20-0f73115d6b22)  


9. Масштабируйте (с надлежащим изменением координат в пикселях, чтобы всё было видно) треугольник

```
𝐿 =  ⎡  5   1  ⎤
     ⎜ 5   2  ⎜
     ⎣  3   2  ⎦
```
с помощью матрицы:
```
T =  ⎡  2  0 ⎤  
     ⎣  0  2 ⎦  
```

![image](https://github.com/user-attachments/assets/6dc989ab-f89f-4d09-86f6-bbf3c739517c) 


10. Нарисуйте на экране спираль в виде улитки Паскаля, используя полярные координаты:  
𝑟 = 𝑏 + 2 ⋅ 𝑎 ⋅ cos(𝜃)  
𝑥 = 𝑟 ⋅ cos(𝜃), 𝑦 = 𝑟 ⋅ sin(𝜃)

![image](https://github.com/user-attachments/assets/17cd27a9-e10d-4172-8ca7-0ac76375b711)


11. Постройте квадрат, масштабируйте его с коэффициентом 𝑚 = 0.9 и поворачивайте на угол 𝛼 = 𝜋/32. Начальные координаты квадрата:

```
X =  ⎡  2  -2 ⎤
     ⎜ -2 -2  ⎜
     ⎜ -2  2  ⎜   × 100
     ⎣  2   2 ⎦  
```

Используйте комбинированное преобразование и выполните 20 таких операций с отрисовкой в pygame.  


Программа реализована с помощью модулей graphics.py и transform.py. Основной файл - main.py.
Модуль graphics.py содержит:  
- class Unit - Класс, представляющий единичную величину в пикселях для оси координат.  
- class Origin - Класс, представляющий точку начала координат.  
- class ReferenceFrame - Класс для хранения информации о системе координат, включающей начало координат и единичные величины для осей X и Y.  
- class Drawer - Класс для рисования объектов на экране с использованием библиотеки Pygame. Отвечает за отображение графики, работу с цветами и координатами.  

Класс Drawer содержит следующие функции
```
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
        self.__color = (255, 255, 255)  # Цвет по умолчанию (белый)

    def initialize(self, caption: str):
        """
        Инициализация Pygame, создание окна и заполнение экрана фоном.

        Параметры:
            caption (str): Заголовок окна.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.res_x, self.res_y))
        pygame.display.set_caption(caption)
        self.screen.fill((255, 255, 255))

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

```
Модуль transform.py содержит следующие функции
```
def translate(dx: float, dy: float):
    return np.array([
        [1, 0, 0],
        [0, 1, 0],
        [dx, dy, 1]
    ])

def scale(sx: float, sy: float):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def rotate(angle: float):
    cs = m.cos(angle)
    sn = m.sin(angle)
    return np.array([
        [cs, sn, 0],
        [-sn, cs, 0],
        [0, 0, 1]
    ])

```

Основной файл для запуска выглядит следующим образом
```
import pygame
import numpy as np
import sys
from graphics import Unit, Origin, ReferenceFrame, Drawer
from transform import translate, scale, rotate

# Константы
RES_X, RES_Y = 800, 600
SCALE = 0.9  # Коэффициент масштабирования
ANGLE = np.pi / 32  # Угол поворота (π/32)
ITERATIONS = 20  # Количество итераций трансформаций

# Начальные координаты квадрата
square = np.array([
    [2, -2, 1],
    [-2, -2, 1],
    [-2, 2, 1],
    [2, 2, 1]
])

# Единичный размер и начало координат
unit = Unit(100)  # Каждая единица равна 100 пикселям
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
    drawer.screen.fill((0, 0, 0))

    # Нарисовать оси
    # drawer.color = (255, 255, 255)
    # drawer.draw_axes(-5, 5, -5, 5)

    # Рисовать все итерации
    current_square = square.copy()
    for i in range(ITERATIONS + 1):
        # Преобразование: масштабирование и поворот относительно центра
        transform = (
            translate(-origin.x0 / unit.pixels, -origin.y0 / unit.pixels) @  # Сдвиг к центру
            scale(SCALE, SCALE) @  # Масштабирование
            rotate(ANGLE) @  # Поворот
            translate(origin.x0 / unit.pixels, origin.y0 / unit.pixels)  # Возврат к центру
        )

        # Цвет квадрата зависит от итерации
        drawer.color = (255 - i * 10, 0, i * 12)

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

```
Вывод программы    
![image](https://github.com/user-attachments/assets/e3d22a71-8774-41a7-95c2-515cb412b8f8)

