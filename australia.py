# Игрок упрвляет стиками с обеих сторон, однако иногда верх и низ меняются местами
import pygame as pg
pg.init()

# Подготовка
wind = pg.display.set_mode((500, 350))
pg.display.set_caption('Australian')
clock = pg.time.Clock()
FPS = 60

# Тригеры
play, australia = True, False
introd, over = True, False

# Задаем параметры стиков
x, y, speed = 1, 130, 5
second_x, second_y = 480, 130
stick_lenth = 60
shots = 0                       # Число отбитых мячей
balls = 0                       # Очки

# Функция завершения игры
def end():
    wind.fill((100, 100, 100))                          # Фон
    pg.draw.polygon(wind, (245, 245, 220), [(0, 0), (50, 175), (0, 350)])
    font1 = pg.font.SysFont('arial', 27)
    text1 = font1.render('Результат: ' + str(int(balls)), 1, (255, 255, 255))
    place1 = text1.get_rect(center = (250, 150))

    font2 = pg.font.SysFont('arial', 14)
    text2 = font2.render('tab - новая игра', 1, (255, 255, 255))        # Создаем нужные надписи
    place2 = text2.get_rect(center = (420, 335))

    wind.blit(text1, place1)
    wind.blit(text2, place2)                                  # Отрисовываем и добавляем их
    pg.display.update()

# Класс мячика
class Ball:
    def __init__(self, x, y, is_right, is_down):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.r = 10
        self.is_right = is_right
        self.is_down = is_down
        self.is_begin = False
        self.ball_speed = 3

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), self.r)                # Прорисовка

    def move(self):                                                                 # Логика движения
        global y, shots, over
        if self.is_begin:
            if self.x < 470 and self.x > 30:
                if self.is_right:
                    self.x += self.ball_speed                 # Обычное движение по Ox
                else:
                    self.x -= self.ball_speed
            else:
                if shots % 5 == 0:          # На каждом 10-м ударе увеличиваем скорость мяча
                    self.ball_speed += 1

                if self.x < 250 and (self.y >= y and self.y <= y + stick_lenth):        # Отскок от первого стика
                    self.is_right = True
                    shots += 0.5
                    self.x += self.ball_speed

                elif self.x > 250 and (self.y >= second_y and self.y <= second_y + stick_lenth):          # Отскок от второго стика
                    shots += 0.5
                    self.is_right = False
                    self.x -= self.ball_speed

                else:                                            # Проигрыш
                    over = True
                    self.x = 250                                # Мяч уходит в центр
                    self.y = 150
                    self.is_begin = False                       # Скидываем показатели
                    self.ball_speed = 3

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
ball = Ball(250, 150, True, False)

# Функция отрисовки окна
def draw():
    global balls
    wind.fill((100, 100, 100))
    pg.draw.lines(wind, (152, 255, 152), True, [(0, 300), (499, 300), (499, 0), (0, 0)])
    pg.draw.line(wind, (152, 255, 152), [0, 150], [500, 150], 2)
    pg.draw.line(wind, (152, 255, 152), [250, 0], [250, 300], 2)                    # Отрисовываем разметку
    pg.draw.circle(wind, (152, 255, 152), [250, 150], 10)

    font = pg.font.SysFont('arial', 25)
    font2 = pg.font.SysFont('arial', 20)
    if not australia:
        text = font.render('Все хорошо', 1, (152, 255, 152))
    else:
        text = font.render('Австралия!', 1, (255, 255, 0))

    place = text.get_rect(center = (250, 330))

    balls = 20*shots
    count = font2.render('Счёт: ' + str(int(balls)), 1, (152, 255, 152))            # Обновляем и отрисовываем фигуры
    count_place = count.get_rect(center = (50, 330))

    ball.draw(wind)
    pg.draw.rect(wind, (255, 52, 179), [x, y, 19, stick_lenth])
    pg.draw.rect(wind, (219, 112, 147), [second_x, second_y, 19, stick_lenth])
    wind.blit(text, place)
    wind.blit(count, count_place)
    pg.display.update()

# Функция приветствия игрока
def introdution():
    wind.fill((100, 100, 100))               # Фон
    pg.draw.polygon(wind, (245, 245, 220), [(0, 0), (125, 0), (0, 75)])
    pg.draw.polygon(wind, (245, 245, 220), [(500, 350), (375, 350), (500, 275)])

    font1 = pg.font.SysFont('arial', 25)
    font2 = pg.font.SysFont('arial', 14)

    text1 = font1.render('Австралийский режим!', 1, (152, 255, 152))
    text2 = font2.render('Игра идет до ошибки!', 1, (255, 255, 255))            # Создаем нужные надписи
    text3 = font2.render('backspace - начать', 1, (255, 255, 255))
    
    place1 = text1.get_rect(center = (250, 150))
    place2 = text2.get_rect(center = (90, 320))
    place3 = text3.get_rect(center = (90, 340))

    wind.blit(text1, place1)
    wind.blit(text2, place2)                                    # Отрисовываем и обновляем
    wind.blit(text3, place3)
    pg.display.update()

# Скелет игры
while play:
    clock.tick(FPS)
    for event in pg.event.get():                        # Проверяем на выход
        if event.type == pg.QUIT:
            play = False
            pg.quit()
    if 2 * shots % 4 == 0 or 2 * shots % 4 == 1:
        australia = False
    else:
        australia = True

    keys = pg.key.get_pressed()
    if keys[pg.K_DOWN]:
        if y < 300 - stick_lenth:
            y += speed
        if not australia:
            if second_y < 300 - stick_lenth:
                second_y += speed
        else:
            if second_y > 0:
                second_y -= speed
                                                    # Передвижение стиков
    if keys[pg.K_UP]:
        if y > 0:
            y -= speed
        if not australia:
            if second_y > 0:
                second_y -= speed
        else:
            if second_y < 300 - stick_lenth:
                second_y += speed

    if ball.is_begin:
        ball.move()                                     # Если нужно, двигается и мяч
    else:
        if keys[pg.K_SPACE]:                                # Возобновление движения мяча
            ball.is_begin = True

    if introd:
        introdution()                   # Привествуем игрока
        keys = pg.key.get_pressed()
        if keys[pg.K_BACKSPACE]:        # Если он нажимает backspace, завершаем приветствие
            introd = False

    if over:                        # Если игра завершилась
        end()
        if keys[pg.K_TAB]:          # Если пользователь нажимает tab, начинаем новую игру
            shots = 0
            ball.is_begin = False
            over = False

    else:
        if not introd:              # Если игра не завершена и мы не приветствуем пользователя
            draw()                  # Отрисовываем