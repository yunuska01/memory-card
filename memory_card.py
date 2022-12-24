class Wall(sprite.Sprite):
    def init(self,color_1,color_2,color_3,x,y,width,height):
        super().init()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height=height
        self.image=Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect= self.image.get_rect()
        self.rect.x= x
        self.rect.y = y
    def drawall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
wall_1 = Wall(41,23,25,200,250,40,400)
wall_2 = Wall(41,23,25,320,20,20,350)
wall_3 = Wall(41,23,25,450,200,10,450)

winText = font.render('йу вин', True, (0,0,0))
loseText = font.render('йу лусер', True, (0,0,0))
hero = Player("hero.png",5,400,5)
cyborg = Enemy('cyborg.png',600,300,3)
treasure = GameSprite('treasure.png',600,400,0)
mixer.music.load('jungles.ogg')
mixer.music.play()
win_music = mixer.Sound('kick.ogg')
lose_music = mixer.Sound('money.ogg')
finish = False
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        if sprite.collide_rect(hero,treasure):
            finish = True
            lose_music.play()
        if sprite.collide_rect(hero,cyborg) or sprite.collide_rect(hero,wall_1) or sprite.collide_rect(hero,wall_2) or sprite.collide_rect(hero,wall_3):
            finish = True
            window.blit(winText,(200,200))
            win_music.play()
        window.blit(background,(0,0))
        hero.update()
        hero.reset()
        cyborg.auto()
        cyborg.reset()
        wall_1.drawall()
        wall_2.drawall()
        wall_3.drawall()
        treasure.reset()
        display.update()
        clock.tick(60)
        class GameSprite(sprite.Sprite):
    def init(self, player_img,player_x,player_y,player_speed):
        super().init()
        self.image = transform.scale(image.load(player_img),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.autos = 'right'
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y+= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
