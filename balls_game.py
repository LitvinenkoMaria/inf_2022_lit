import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 25) #выбрали шрифт

FPS = 10
screen = pygame.display.set_mode((500, 500))

balls = [[]] #параметры шариков
k = 0 #количество шариков за все время
k_n = 0 #количество шариков сейчас

point = 0 #очки
sign_x = 1 #знак движения по x
sign_y = 1 #знак движения по y

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
screen.fill(BLACK)

def new_ball(): #рисует шарик с рандомными параметрами x, y, r
    global x, y, r, color, p
    x = randint(50, 450)
    y = randint(50, 450)
    r = randint(10, 50)
    p = 51 - r #очки за шарик: чем шарик меньше, тем сложнее по нему попасть, значит, за маленькие шарики даем много очков
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)



def dr_ball(x, y, r, color): #рисует шарик (вместо обычного circle)
    circle(screen, color, (x, y), r)


def delete(l): #удаление шарика
    balls[l][0] = 0
    balls[l][1] = 0
    balls[l][2] = 0

def check_ball(a, b, c, d1, e, del_b):
	return ((((a - b) ** 2 + (c - d1) ** 2) < e ** 2) and del_b == 0)

    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for click in pygame.event.get():
        if click.type == pygame.QUIT:
            finished = True
        if click.type == pygame.MOUSEBUTTONDOWN: 
            if click.button == 1: #если нажал ЛКМ
                d = 0
                for i in range(k - 1, 0, -1): #проверка, смогли ли попасть по шарику мышкой
                    if check_ball(balls[i][0], click.pos[0], balls[i][1], click.pos[1], balls[i][2], d):
                        delete(i)
                        k_n = k_n - 1 #общее количество шариков уменьшилось
                        point += balls[i][4] #прибавление очков
                        d += 1 #сколько удалили

                pygame.display.update()
            if click.button == 3: #выключение при нажатии ПКМ
                    finished = True
    for i in range(randint(0,1)): #с вероятностью 0,5 появится шарик
        if(k_n < 30): 
            new_ball() 
            balls.append([x, y, r, color, p, sign_x, sign_y]) #параметры шарика
            k = k + 1 #количество шариков в массиве
            k_n = k_n + 1 #количество шариков в данный момент
   
    rect(screen, BLACK, (0, 0, 500, 500))
    for j in range(1, k, 1):
        if(balls[j][1] - balls[j][2] < 15): #проверяем приближение к границам экрана
            balls[j][6] = balls[j][6] * (-1)
        if(balls[j][1] + balls[j][2] > 485):
            balls[j][6] = balls[j][6] * (-1)
        if(balls[j][0] + balls[j][2] > 485):
            balls[j][5] = balls[j][5] * (-1)
        if(balls[j][0] - balls[j][2] < 15):
            balls[j][5] = balls[j][5] * (-1)
        balls[j][0] -= balls[j][5] * 10 #меняем координаты
        balls[j][1] -= balls[j][6] * 10
        dr_ball(balls[j][0], balls[j][1], balls[j][2], balls[j][3]) #рисуем шарик с новыми параметрами
 
    text = myfont.render('ОЧКИ:', False, (255, 255, 255)) #пишем очки на экране
    level = str(point) 
    text1 = myfont.render(level, False, (255, 255, 255))
    screen.blit(text,(0,0)) 
    screen.blit(text1,(100,0))
    pygame.display.update()
pygame.quit()

print('Write down your name') #имя игрока
a = input()
f = open('winners.txt', 'a') #открыть файл
f.write(a + ' ' + level + '\n') #в файл пишем имя + баллы
f.close() #закрыть файл
