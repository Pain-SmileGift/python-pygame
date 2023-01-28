import pygame as pg
import sys
import random
from dino import Dragon,Map,Block

WINDOW_WIDTH=400
WINDOW_HEIGHT=256

game=True
spawnTime=0
score=0

def restart():
    global spawnTime,score
    score=0
    spawnTime=pg.time.get_ticks()
    dragon.reset()
    background.reset((0,WINDOW_HEIGHT))
    for b in blocks:
        blocks.remove(b)

def lose():
    global game
    while not game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                game=True
                restart()
        screen.blit(gameOver,gameOverRect)
        font_surface = font.render('score:'+str(score), True, 'black')
        screen.blit(font_surface,(WINDOW_WIDTH-100,20))
        pg.display.flip()

'''
控制障碍物随机生成
'''
def spawn():
    global spawnTime
    time = pg.time.get_ticks()
    if time-spawnTime > 1000:
        if random.randint(0,10)>9:
            if random.randint(0,1)>0:
                block=Block("./trap1.png",[400,215],blocks)
            else:
                block=Block("./trap2.png",[400,215],blocks)
            spawnTime=time

if __name__=="__main__":
    pg.init()
    screen = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pg.display.set_caption("dino")

    clock = pg.time.Clock()
    blocks=pg.sprite.Group()
    bgcolor = [255,255,255]
    screen.fill(bgcolor)
    # 创建小恐龙和背景
    dragon = Dragon("./dragon1.png","./dragon2.png",(50,215),215)
    background = Map("./background1.png","./background2.png",(0,WINDOW_HEIGHT))
    # 加载游戏结束UI
    gameOver=pg.image.load("./gameover.png")
    gameOverRect=gameOver.get_rect()
    gameOverRect=gameOverRect.move((WINDOW_WIDTH//2-gameOver.get_width()//2,WINDOW_HEIGHT//2-gameOver.get_height()//2))
    # 字体设置
    font = pg.font.Font(None, 20)
    # 主循环
    while game:
        # 按键监测
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP or event.key==pg.K_SPACE:
                    dragon.jump()
        # FPS设置20帧
        clock.tick(20)
        # 游戏对象控制
        dragon.update()
        background.show(screen, -10)
        spawn()
        for b in blocks:
            b.update(screen,-10)   
        dragon.show(screen)
        # 碰撞检测
        if pg.sprite.spritecollide(dragon,blocks,False):
            game=False
            lose()
        # 显示得分
        score+=1
        font_surface = font.render('score:'+str(score), True, 'black')
        screen.blit(font_surface,(WINDOW_WIDTH-100,20))
        
        pg.display.flip()

