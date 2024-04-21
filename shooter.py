#Создай собственный Шутер!

from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('pygame window')
galaxy = transform.scale(image.load("iStock-1159238834-1628x1080.jpg"), (700, 500))
app = True
finish = False
clock = time.Clock()
FPS = 60
from time import time as timer  

#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_w, player_h):
        super().__init__()
        self.direction = 'left'
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and se
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 36)
font3 = font.Font(None, 36)
font4 = font.Font(None, 36)

asteroids = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()
for i in range(5):
    monster = Enemy('ufo.png', randint(6, 7),randint(0, 600), -50, 65,65)
    monsters.add(monster)
player = Player('shooter.png', 8,0,415,65,65)
for i in range(3):
    asteroid = Enemy('meteor.png', randint(4, 5), randint(0, 600),-50,65,65)
    asteroids.add(asteroid)
    
counts = 0
y1 = 0
y2 = -500
rel_time = 0
num_fire = 0
while app:
    window.blit(galaxy, (0, y1))
    window.blit(galaxy, (0, y2))
    collides = sprite.groupcollide(bullets,monsters,True,True)
    for i in collides:
counts += 1
        monster = Enemy('ufo.png', randint(6, 10),randint(0, 600), -50, 65,65)
        monsters.add(monster)
    text_win = font3.render('YOU WIN!' + str(counts), 1, (255, 255, 255))
    text_lost = font4.render('YOU LOSE!', True, (255, 0, 0))
    text_lose = font1.render('Пропущено' + str(lost), 1, (255, 255, 255))
    text_lose2 = font2.render('Счёт' + str(counts), 1, (255, 255, 255))
    window.blit(text_lose, (10, 10))
    window.blit(text_lose2, (10, 50))
    
    y1 += 5
    y2 += 5
    if y1 >= 500:
        y1 = -500
    if y2 == 500:
        y2 = -500
    for e in event.get():
        if e.type == QUIT:
            app = False
        if e.type == KEYDOWN:
            if num_fire <= 5 and rel_time == False:
                if e.key == K_SPACE:
                    player.fire()
                    num_fire += 1
            if num_fire >= 5 and rel_time == False:
                rel_time = True
                start = timer()
if counts >= 10:
        finish = True
        window.blit(text_win, (10, 100))    
    elif lost >= 10:
        window.blit(text_lost, (250, 300))
        finish = True
    if finish != True:
        
        if rel_time == True:
            end = timer()  
            if end - start >= 2:
                num_fire = 0
                rel_time = False
            else:
                reload = font2.render('Wait! reloading...', True, (50, 100, 25))
                window.blit(reload, (250, 450))
        player.reset()
        player.update()
        monsters.update()
        monsters.draw(window)
        asteroids.update()
        asteroids.draw(window)
        bullets.update()
        bullets.draw(window)
    clock.tick(FPS)
    display.update()
