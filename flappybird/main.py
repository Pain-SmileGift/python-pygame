import pygame
import sys
from obj import Bird,Tube
import random

WINDOW_W=288
WINDOW_H=512
game=True
spawnTime=0
score=0

def spawn():
    global spawnTime
    time=pygame.time.get_ticks()
    if time-spawnTime>1000:
        lengths=[100,150,200,250]
        Tube(lengths[random.randint(0,len(lengths)-1)],random.randint(0,1),(WINDOW_W,WINDOW_H),tubes)
        spawnTime=time
        
def restart():
    global spawnTime,score
    score=0
    spawnTime=pygame.time.get_ticks()
    player.reset((WINDOW_W,WINDOW_H))
    for t in tubes:
        tubes.remove(t)
        
def lose():
    global game
    game=False
    while not game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game=True
                restart()
        font_surface = font.render('score:'+str(score), True, 'black')
        font_gameover = font.render('GAME OVER', True, 'black')
        screen.blit(background,backgroundRect)
        screen.blit(font_surface,(WINDOW_W-100,20))
        screen.blit(font_gameover,(WINDOW_W//2-40,WINDOW_H//2))
        pygame.display.flip()
    
pygame.init()
screen=pygame.display.set_mode((WINDOW_W,WINDOW_H))
clock=pygame.time.Clock()

player=Bird("./pic/0.png","./pic/1.png","./pic/2.png",(WINDOW_W,WINDOW_H))
background=pygame.image.load("./pic/bg.png")
backgroundRect=background.get_rect()

tubes=pygame.sprite.Group()

font = pygame.font.Font(None, 20)

while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            player.jump()
    spawn()
    clock.tick(20)
    screen.blit(background,backgroundRect)
    player.show(screen)
    f=player.update((0,WINDOW_H))
    if not f:
        lose()
    score=0
    for t in tubes:
        t.show(screen,10)
        score+=t.goal
    if pygame.sprite.spritecollide(player,tubes,False):
        lose()
    font_surface = font.render('score:'+str(score), True, 'black')
    screen.blit(font_surface,(WINDOW_W-100,20))
    pygame.display.flip()
