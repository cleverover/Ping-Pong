# Обычная игра с компьютером
import pygame as pg
pg.init()

# Подготовка
wind = pg.display.set_mode((500, 350))
pg.display.set_caption('Classic')
clock = pg.time.Clock()
FPS = 60

# Задаем параметры управляемого стика
x, y, speed = 1, 0, 5
stick_lenth = 60
shots = 0       # Число отбитых мячей

# Начальные счета
count1, count2 = 0, 0

class Stick:                                                                # Второй стик
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (219, 112, 147)
        self.is_down = True
        self.lenth = 100

    def draw(self, window):
        pg.draw.rect(window, self.color, [self.x, self.y, 19, self.lenth])         # Прорисовка

    def move(self):                                                         # Движение
        if ball.is_right and ball.is_begin:
            if ball.is_down:
                if self.y > 0:
                    self.y -= speed                                             # Вверх
            if not ball.is_down:                                               # Вниз
                if self.y < 300 - self.lenth:
                    self.y += speed

second_stick = Stick(480, 0)                                          # Создаем соперника

class Ball:
    def __init__(self, x, y, is_right, is_down):                  # Класс мячика
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.r = 10
        self.is_right = is_right
        self.is_down = is_down
        self.is_begin = False
        self.ball_speed = 5

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), self.r)                # Прорисовка

    def move(self):                                                                 # Логика движения
        global y, count1, count2, shots
        if self.is_begin:
            if self.x < 470 and self.x > 30:
                if self.is_right:
                    self.x += self.ball_speed                 # Обычное движение по Ox
                else:
                    self.x -= self.ball_speed
            else:
                if self.x < 250 and (self.y >= y and self.y <= y + stick_lenth):     # Отскок от первого стика
                    self.is_right = True
                    shots += 1                  # Увеличиваем число отскоков
                    if shots % 3 == 0:          # На каждом 3-м ударе увеличиваем скорость мяча
                        self.ball_speed += 1
                    self.x += self.ball_speed

                elif self.x > 250 and (self.y >= second_stick.y and self.y <= second_stick.y+ second_stick.lenth):          # Отскок от второго стика
                    self.is_right = False
                    self.x -= self.ball_speed
                else:                                    # Забитый гол
                    if self.x > 250:
                        count1 += 1
                    elif self.x < 250:
                        count2 += 1
                    self.x = 250                                # Мяч уходит в центр
                    self.y = 150
                    self.is_begin = False
                    shots = 0                                   # Обнуляем показатели
                    self.ball_speed = 5

            if self.y < 290 and self.y > 10:            # Обычное движение по Oy
                if self.is_down:
                    self.y -= self.ball_speed
                else:
                    self.y += self.ball_speed
            else:
                if self.y < 150:                            # Отскоки от стенок
                    self.is_down = False
                    self.y += self.ball_speed
                if self.y > 150:
                    self.is_down = True
                    self.y -= self.ball_speed

# Создаем мячик
ball = Ball(250, 150, False, False)

def draw():                                                   # Функция отрисовки окна
    font = pg.font.SysFont('arial', 30)
    font2 = pg.font.SysFont('arial', 25)

    text1 = font.render(str(count1), 1, (255, 255, 255))
    place1 = text1.get_rect(center=(40, 325))
    text2 = font.render(str(count2), 1, (255, 255, 255))                            # Отрисовываем счет
    place2 = text2.get_rect(center=(460, 325))
    text3 = font2.render('Счёт', 1, (255, 255, 255))
    place3 = text3.get_rect(center=(250, 325))

    wind.fill((100, 100, 100))
    wind.blit(text1, place1)
    wind.blit(text2, place2)
    wind.blit(text3, place3)

    pg.draw.lines(wind, (152, 255, 152), True, [(0, 300), (499, 300), (499, 0), (0, 0)])
    pg.draw.line(wind, (152, 255, 152), [0, 150], [500, 150], 2)
    pg.draw.line(wind, (152, 255, 152), [250, 0], [250, 300], 2)                    # Отрисовываем разметку
    pg.draw.circle(wind, (152, 255, 152), [250, 150], 10)

    second_stick.move()
    second_stick.draw(wind)
    ball.draw(wind)                                             # Обновляем и отрисовываем фигуры
    pg.draw.rect(wind, (255, 52, 179), [x, y, 19, stick_lenth])

    if count1 == count2 == 0 and not ball.is_begin:
        extra_font = pg.font.SysFont('arial', 20)
        extra = extra_font.render('space - начало', 1, (255, 255, 0))      # Объясняем, как начать игру
        extra_place = extra.get_rect(center = (370, 230))
        wind.blit(extra, extra_place)

    pg.display.update()

def introdution():                # Функция приветствия игрока
    wind.fill((100, 100, 100))                                  # Фон
    pg.draw.rect(wind, (245, 245, 220), [0, 0, 40, 40])
    pg.draw.rect(wind, (245, 245, 220), [460, 0, 40, 40])
    pg.draw.rect(wind, (245, 245, 220), [460, 310, 40, 40])

    font1 = pg.font.SysFont('arial', 27)
    font2 = pg.font.SysFont('arial', 14)

    text1 = font1.render('Классический режим!', 1, (152, 255, 152))
    text2 = font2.render('Игра идет до 5 забитых голов', 1, (255, 255, 255))            # Создаем нужные надписи
    text3 = font2.render('backspace - начало', 1, (255, 255, 255))

    place1 = text1.get_rect(center = (250, 150))
    place2 = text2.get_rect(center = (100, 327))
    place3 = text3.get_rect(center = (100, 340))

    wind.blit(text1, place1)
    wind.blit(text2, place2)                                    # Отрисовываем и обновляем
    wind.blit(text3, place3)
    pg.display.update()


def end(is_win):                                        # Функция завершения игры
    wind.fill((100, 100, 100))                  # Фон
    pg.draw.polygon(wind, (245, 245, 220), [(0, 0), (50, 175), (0, 350)])
    font1 = pg.font.SysFont('arial', 27)
    if is_win:
        text1 = font1.render('Ты сделал его!', 1, (152, 255, 152))           # Победа
    else:
        text1 = font1.render('Тест Тьюринга не пройден', 1, (152, 255, 152))          # Поражение
    place1 = text1.get_rect(center = (250, 150))

    font2 = pg.font.SysFont('arial', 14)
    text2 = font2.render('backspace - новая игра', 1, (255, 255, 255))        # Создаем нужные надписи
    place2 = text2.get_rect(center = (420, 335))

    font2 = pg.font.SysFont('arial', 20)
    text3 = font2.render(f'{count1}:{count2}', 1, (255, 255, 255))
    place3 = text3.get_rect(center = (250, 125))

    wind.blit(text1, place1)
    wind.blit(text2, place2)                                                    # Отрисовываем и добавляем их
    wind.blit(text3, place3)
    pg.display.update()

# Скелет игры
play = True                                             # Тригер выхода
over = False                                            # Тригер для функции завершения игры
introd = True                                           # Тригер для функции приветствия

while play:
    clock.tick(FPS)
    for event in pg.event.get():                        # Проверяем на выход
        if event.type == pg.QUIT:
            play = False
            pg.quit()


    keys = pg.key.get_pressed()
    if keys[pg.K_DOWN] and y < 300 - stick_lenth:                     # Передвижение левого стикера
        y += speed
    if keys[pg.K_UP] and y > 0:
        y -= speed

    if ball.is_begin:
        ball.move()                                     # Если нужно, двигается и мяч
    if keys[pg.K_SPACE]:                                # Возобновление движения мяча
        ball.is_begin = True

    if count1 == 5:
        end(True)               # Победа
        over = True             # Игра завршена
    if count2 == 5:
        end(False)              # Поражение
        over = True             # Игра завершена

    if introd:
        introdution()                           # Привествуем игрока
        keys = pg.key.get_pressed()
        if keys[pg.K_BACKSPACE]:                    # Если он нажимает backspace, завершаем приветствие
            introd = False

    if over:                                    # Если игра завершилась
        if keys[pg.K_BACKSPACE]:                    # Если поьзователь нажимает backspace, начинаем новую игру
            count1, count2 = 0, 0
            ball.is_begin = False
            over = False

    else:
        if not introd:                          # Если игра не завершена и мы не приветствуем пользователя
            draw()                              # Отрисовываем