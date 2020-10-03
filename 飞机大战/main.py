#main.py
import pygame
import sys
import traceback
import myplane
import enemy
import bullet
import supply
from pygame.locals import *
from random import *



#初始化
pygame.init()
pygame.mixer.init()

bg_size = width, height = 480, 700          #背景尺寸
screen = pygame.display.set_mode(bg_size)   #设置屏幕尺寸
pygame.display.set_caption("飞机大战 - - LPH_Z")

background = pygame.image.load("images/background.png").convert()

#游戏结束画面
gameover_font = pygame.font.Font("font/font.ttf", 48)
again_image = pygame.image.load("images/again.png").convert_alpha()
again_rect = again_image.get_rect()
gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
gameover_rect = gameover_image.get_rect()


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#载入音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.1)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.1)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.1)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)



def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)                       #e1为小型飞机的实例化对象，逐个生成num个
        group1.add(e1)                                      #将生成的小型飞机逐个添加到group1和group2中
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)                       
        group1.add(e2)                                      
        group2.add(e2)


def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)                      
        group1.add(e3)                                      
        group2.add(e3)



def inc_speed(target, inc):
    for each in target:
        each.speed += inc


def main():
    pygame.mixer.music.play(-1)
    #-1 表示循环播放

    #生成我方飞机
    me = myplane.MyPlane(bg_size)

    #生成敌方飞机
    enemies = pygame.sprite.Group()
    #生成敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    #生成敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)
    #生成敌方大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 4)


    #生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 10
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))


    #生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 20
    for i in range(BULLET2_NUM // 2):
        bullet2.append(bullet.Bullet2((me.rect.centerx - 33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx + 30, me.rect.centery)))
    

    
    clock = pygame.time.Clock()

    #中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0


    #统计得分
    score = 0
    #设置得分字体
    score_font = pygame.font.Font("font/font.ttf", 36)

    #标志是否暂停游戏
    paused = False
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image

    #设置初始难度级别
    level = 1

    #全屏炸弹
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf", 48)
    bomb_num = 3

    #每30s发放一次补给包
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 10 * 1000)

    #超级子弹定时器
    DOUBLE_BULLET_TIME = USEREVENT + 1

    #标志是否使用超级子弹
    is_double_bullet = False

        
    #用于切换我方飞机图片
    switch_image = True

    #用于延时
    delay = 10
    
    running = True

    #生命数量
    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3

    #解除我方无敌状态计时器
    INVINCIBLE_TIME = USEREVENT + 2

    #用于阻止重复打开记录文件
    recorded = False
    

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()#背景音乐暂停
                        pygame.mixer.pause()#音效暂停
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 10 * 1000)
                        pygame.mixer.music.unpause()#背景音乐继续
                        pygame.mixer.unpause()#音效继续
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = pause_nor_image
            #检测是否按下空格(使用全屏炸弹)
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False



            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)
            elif event.type == INVINCIBLE_TIME:
                me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)
        


        #根据玩家得分增加难度
        if level == 1 and score > 50000:
            level = 2
            upgrade_sound.play()
            #增加3架小型敌机、2架中型敌机和1架大型敌机
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            #提升敌机的速度
            inc_speed(small_enemies, 1)
        elif level == 2 and score > 300000:
            level = 3
            upgrade_sound.play()
            #增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #提升敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 3 and score > 600000:
            level = 4
            upgrade_sound.play()
            #增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #提升敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 4 and score > 100000:
            level = 5
            upgrade_sound.play()
            #增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #提升敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        

        screen.blit(background, (0, 0))         #blit位块传送    


        if life_num and not paused:
            #检测用户的键盘操作
            key_pressed = pygame.key.get_pressed()

            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            
            #绘制全屏炸弹补给并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            #绘制超级子弹补给并检测是否获得超级子弹
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):
                    get_bullet_sound.play()
                    #发射超级子弹
                    bullet_supply.active = False
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 18 * 1000)

            
           

            #发射子弹
            if not (delay % 10):
                bullet_sound.play
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-33, me.rect.centery))
                    bullets[bullet2_index + 1].reset((me.rect.centerx+30, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM
                    
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM

            #检测是否击中敌机
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
                    

            #绘制大型敌机
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        #每次被击中是，绘制被击中的图片,
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False

                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)

                    #绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                    (each.rect.left, each.rect.top - 5), \
                                    (each.rect.right, each.rect.top - 5),\
                                    2)
                    #当生命大于20%时显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5), \
                                     2)

                    #即将出现在画面中，播放音效
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)
                else:
                    #敌机被摧毁,播放一次音效
                    if e3_destroy_index == 0:
                        enemy3_down_sound.play()
                        score += 10000
                    #间隔显示被击毁图片
                    if not(delay % 3):
                        screen.blit(each.destroy_image[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1)%6                       #此语句第一次执行完 e3_destroy_index为2
                        if e3_destroy_index == 0:                                         #下次e3_destroy_index为0时，图片播放完毕，重置敌机
                            enemy3_fly_sound.stop()
                            each.reset()
                        
            
                    

            #绘制中型敌机与摧毁显示
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)
                    #绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                    (each.rect.left, each.rect.top - 5), \
                                    (each.rect.right, each.rect.top - 5),\
                                    2)
                    #当生命大于20%时显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5), \
                                     2)
                    
                else:
                    #敌机被摧毁
                    if e2_destroy_index == 0:
                        enemy2_down_sound.play()
                        score += 6000
                    #间隔显示被击毁图片
                    if not(delay % 3):
                        screen.blit(each.destroy_image[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1)%4
                        if e2_destroy_index == 0:
                            each.reset()

            #绘制小型敌机与摧毁显示
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    #敌机被摧毁
                    if e1_destroy_index == 0:
                        enemy1_down_sound.play()
                        score += 1000
                    #间隔显示被击毁图片
                    if not(delay % 3):
                        screen.blit(each.destroy_image[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1)%4
                        if e1_destroy_index == 0:
                            each.reset()
                


            #检测我方飞机是否被撞
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            #以sprite.collide_mask的方式检测碰撞
            if enemies_down and not me.invincible:
                me.active = False
                for e in enemies_down:
                    e.active = False
            
            #绘制我方飞机与剩余生命检测
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                me_down_sound.play()
                #间隔显示被击毁图片
                if not(delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    screen.blit(me.destroy_image[me_destroy_index], each.rect)
                    me_destroy_index = (me_destroy_index + 1)%4
                    if me_destroy_index == 0:
                        life_num -= 1
                        me.reset()
                        #开启无敌定时器3秒
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)
            #绘制得分。将font字体渲染成surface对象，传给score_text
            score_text = score_font.render("Score: %s" % str(score), True, WHITE)
            #True 表示无锯齿， WHITE是设置字体颜色
            screen.blit(score_text, (10, 5))
            
        elif life_num == 0:
            #绘制结束画面
            
            #背景音乐停止
            pygame.mixer.music.stop()
            #停止所有音效
            pygame.mixer.stop()
            #停止发放补给
            pygame.time.set_timer(SUPPLY_TIME, 0)

            if not recorded:
                recorded = True
                #读取历史最高得分
                with open("record.txt","r") as f:
                    record_score=int(f.read())
                #如果此次得分高于历史记录，则保存得分
                if score > record_score:
                     with open('record.txt','w')as f:
                        f.write(str(score))
                        
            #绘制结束界面
            record_score_text = score_font.render("Best : %d" % record_score, True, (255, 255, 255))
            screen.blit(record_score_text, (50, 50))

            gameover_text1 = gameover_font.render("Your Score:", True, WHITE)
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                                     (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)
            
            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                                 (width - gameover_text2_rect.width) // 2, \
                                 gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                             (width - again_rect.width) // 2, \
                             gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                                (width - again_rect.width) // 2, \
                                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)    
            


        #绘制炸弹图片
        bomb_text = bomb_font.render("x %d" % bomb_num, True, WHITE)
        text_rect = bomb_text.get_rect()
        screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
        screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))

        #绘制剩余生命数量
        if life_num:
            for i in range(life_num):
                screen.blit(life_image, \
                            (width-10-(i+1)*life_rect.width,\
                            height - 10 - life_rect.height))

        
        
        

        #绘制暂停按钮
        screen.blit(paused_image, paused_rect)


        #延时，计时作用
        delay -=1
        if not delay:
            switch_image = not switch_image
            delay = 10
        
        pygame.display.flip()                   #刷新界面

        clock.tick(60)                          #设置刷新间隔，单位ms


if __name__ == "__main__":
    try:
        main()
    except SystemExit:                          #正常退出
        pass
    except:
        traceback.print_exc()                   #打印出异常后退出
        pygame.quit()
        input()
        
