import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()
        #我方飞机被击毁图像
        self.destroy_image = []
        self.destroy_image.extend([\
            pygame.image.load("images/me_destroy_1.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_2.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_3.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_4.png").convert_alpha()
            ])
        #是否存活
        self.active = True
        self.invincible = False

        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        #开始时飞机的位置
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height -self.rect.height - 40
        self.speed = 10

        self.mask = pygame.mask.from_surface(self.image1)


    #定义向四个方向移动的方法
    def moveUp(self):
        if self.rect.top <= 20:
            self.rect.top = 20
            
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.bottom < self.height - 40:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 40
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right  = self.width

    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height -self.rect.height - 40
        self.active = True
        self.invincible = True

            
            
