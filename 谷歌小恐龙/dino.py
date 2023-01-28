import pygame as pg

class Dragon(pg.sprite.Sprite):
    def __init__(self,img_file1,img_file2,location,y):
        pg.sprite.Sprite.__init__(self)
        self.images=[pg.image.load(img_file1),pg.image.load(img_file2)]
        self.image=self.images[0]
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.bottom=location
        self.animator=False
        self.Y=y
        self.jumpSpeed=0
        self.canJump=True
    def show(self,screen):
        if self.animator:
            self.image=self.images[0]
        else:
            self.image=self.images[1]
        self.animator=not self.animator
        screen.blit(self.image,self.rect)
    def jump(self):
        if self.canJump:
            self.jumpSpeed=16
            self.canJump=False
    def update(self):
        self.rect=self.rect.move((0,-self.jumpSpeed))
        self.jumpSpeed-=2
        if self.rect.bottom>self.Y:
            self.jumpSpeed=0
            self.canJump=True
            self.rect.bottom=self.Y
    def reset(self):
        self.jumpSpeed=0
        self.canJump=True
        self.rect.bottom=self.Y
        
class Map():
    def __init__(self,img_file1,img_file2,location):
        self.images=[pg.image.load(img_file1),pg.image.load(img_file2)]
        self.rect1=self.images[0].get_rect()
        self.rect2=self.images[1].get_rect()
        self.rect1.left,self.rect1.bottom=location
        self.rect2.left,self.rect2.bottom=self.rect1.right,self.rect1.bottom
    def show(self,screen,speed):
        self.rect1=self.rect1.move((speed,0))
        self.rect2=self.rect2.move((speed,0))
        if self.rect1.right < 0:
            self.rect1.left = self.rect2.right
        if self.rect2.right < 0:
            self.rect2.left = self.rect1.right
        screen.blit(self.images[0],self.rect1)
        screen.blit(self.images[1],self.rect2)
    def reset(self,location):
        self.rect1.left,self.rect1.bottom=location
        self.rect2.left,self.rect2.bottom=self.rect1.right,self.rect1.bottom

class Block(pg.sprite.Sprite):
    def __init__(self,img_file,location,group):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(img_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.bottom=location
        group.add(self)
        print("create:",self)
    def update(self,screen,speed):
        self.rect=self.rect.move((speed,0))
        if self.rect.right<0:
            del self
            return
        screen.blit(self.image,self.rect)
    def __del__(self):
        print("destory:",self)
