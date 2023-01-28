import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self,file1,file2,file3,window_size):
        pygame.sprite.Sprite.__init__(self)
        self.images=[pygame.image.load(file1),
                     pygame.image.load(file2),
                     pygame.image.load(file3)]
        self.image=self.images[0]
        self.rect=self.image.get_rect()
        self.rect.bottom=window_size[1]//2-self.image.get_height()//2
        self.rect.left=window_size[0]//2-self.image.get_width()//2
        self.imageId=0
        self.jumpSpeed=0
    def show(self,screen):
        screen.blit(self.image,self.rect)
        self.imageId+=1
        if self.imageId>2:
            self.imageId=0
    def jump(self):
        self.jumpSpeed=15
    def update(self,border_Y):
        self.rect=self.rect.move((0,-self.jumpSpeed))
        if self.rect.bottom<border_Y[0] or self.rect.bottom>border_Y[1]:
            return 0
        self.jumpSpeed-=2
        return 1
    def reset(self,window_size):
        self.rect.bottom=window_size[1]//2-self.image.get_height()//2
        self.rect.left=window_size[0]//2-self.image.get_width()//2
        self.jumpSpeed=0
        self.imageId=0

class Tube(pygame.sprite.Sprite):
    def __init__(self,length,isUp,window_size,group):
        pygame.sprite.Sprite.__init__(self)
        # left,top,width,height
        self.rect=pygame.Rect(0,0,25,length)
        self.rect.left=window_size[0]
        if isUp:
            self.rect.top=0
            print(self.rect)
        else:
            self.rect.bottom=window_size[1]
        group.add(self)
        self.goal=False
        self.window_size=window_size
    def show(self,screen,speed):
        pygame.draw.rect(screen,(0,255,0),self.rect)
        self.rect=self.rect.move((-speed,0))
        if self.rect.right<0:
            del self
            return
        if self.rect.right<self.window_size[0]//2 and self.goal==False:
            self.goal=True

        
        
