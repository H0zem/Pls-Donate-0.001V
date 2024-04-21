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
