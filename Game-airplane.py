import pygame
import random
import math
#初始化界面
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Airplane")
icon = pygame.image.load('bg.jpg')
pygame.display.set_icon(icon)
bgimg = pygame.image.load('bg.jpg')
class player():
    def __init__(self):
        self.image = pygame.image.load('2.png')
        self.playerX = 350
        self.playerY = 480
        self.playerstep = 0
playerimg = pygame.image.load('2.png')
playerX = 350
playerY = 480
playerstep = 0 #玩家移动速度
#子弹
pygame.mixer.music.load('1.mp3')
pygame.mixer.music.play(-1)
score = 0
is_over = False
font = pygame.font.SysFont('simsunnsimsun', 30)
def show(score):
    text = f"分数:{score}"
    score_render = font.render(text, True, (0, 255, 0))
    screen.blit(score_render, (20, 20))
def show_over():
    if is_over == True:
        text = "Game over"
        score_render = font.render(text, True, (0, 255, 0))
        screen.blit(score_render, (400, 300))

class bullet():
    def __init__(self):
        self.img = pygame.image.load('456.png')
        self.x = playerX
        self.y = playerY - 10
        self.step = 3
    def hit(self):
        global score
        for e in enemies:
            if (distance(self.x, self.y, e.x, e.y) < 50):
                pygame.mixer.music.load('1.mp3')
                pygame.mixer.music.play()
                score += 1
                bullets.remove(self)
                e.reset()

bullets = []
#添加敌人
number_enemies = 6
class enemy():
    def __init__(self):
        self.img = pygame.image.load('2.png')
        self.x = random.randint(200, 400)
        self.y = random.randint(100, 300)
        self.step = random.randint(1, 3)
    def reset(self):
        self.x = random.randint(50, 200)
        self.y = random.randint(50, 200)
enemies = []
for i in range(number_enemies):
    enemies.append(enemy())


def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a + b*b)

#显示并移动子弹
def showbullet():
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)
def showenemy():
    global is_over
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 680 or e.x < 20:
            e.step *= -1
            e.y += 30
            if e.y > 400:
                is_over = True
                enemies.clear()
def moveplayer():
    global playerX
    if playerX > 680:
        playerX = 680
    if playerX < 20:
        playerX = 20
def process():
    global running
    global playerstep
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerstep = 3
            if event.key == pygame.K_LEFT:
                playerstep = -3
            if event.key == pygame.K_SPACE:
                bullets.append(bullet())

        if event.type == pygame.KEYUP:
            playerstep = 0
#游戏主循环
running = True
while running:
    screen.blit(bgimg, (0, 0))
    show(score)
    process()
    screen.blit(playerimg, (playerX, playerY))
    playerX += playerstep
    #防止飞机出界
    moveplayer()
    showbullet()
    showenemy()
    show_over()
    pygame.display.update()