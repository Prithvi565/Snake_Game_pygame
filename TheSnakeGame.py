import pygame as p
from pygame import mixer
import random as r
import time
import sys
import os

def ovr(rect, circle):
    circle_distance_x = abs(circle[0] - rect[0] - rect[2] / 2)
    circle_distance_y = abs(circle[1] - rect[1] - rect[3] / 2)
    
    if circle_distance_x > (rect[2] / 2 + circle[2]) or circle_distance_y > (rect[3] / 2 + circle[2]):
        return False
    if circle_distance_x <= (rect[2] / 2) or circle_distance_y <= (rect[3] / 2):
        return True
    
    corner_distance_sq = (circle_distance_x - rect[2] / 2) ** 2 + (circle_distance_y - rect[3] / 2) ** 2
    return corner_distance_sq <= (circle[2] ** 2)

p.init()
p.font.init()
mixer.init()
m1 = mixer.Sound(os.path.join("Bite.mp3"))
m2 = mixer.Sound(os.path.join("GO.wav"))
m3 = mixer.Sound(os.path.join("Bg.mp3"))
bg = p.USEREVENT + 1
p.time.set_timer(bg, 4000)  
mixer.music.set_volume(3)
fon = p.font.Font(None, 32)
pon = p.font.Font(None, 26)
ton = p.font.Font(None, 22)
gon = p.font.Font(None, 100)
ent = p.font.Font(None, 36)
conp = p.font.Font(None, 18)
w = p.display.set_mode((500, 500), p.RESIZABLE)  
ssc = 0
color = [(0, 0, 255),(255,0,0),(0,255,0),(0,0,0),(100,100,254),(255,255,255)]

coloc = (255, 0, 0)
colod = (0,255,0)
p.display.set_caption("Snake Game")
img = p.image.load(os.path.join("Snake.png"))
p.display.set_icon(img)
clock = p.time.Clock()

con = False  
con2 = False

def TheSnakeGame():
    global con, con2, w
    
    a = 290
    b = 250
    l = 20
    b2 = 20
    le = 240
    wid = 240
    
    con = True  
    game_over = False
    gs = True
    sp = 100
    snake_speed_x = 0
    snake_speed_y = 0
    di = 'M'
    start_time = time.time()
    snakeHead = [[240,240]]
    point = 0
    con2 = True  

    screen_width, screen_height = w.get_size()  

    while con:
        p.time.delay(50)
        for event in p.event.get():
            if event.type == p.QUIT:
                con = False
            elif event.type == bg:
                m3.play()
            elif event.type == p.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                w = p.display.set_mode((screen_width, screen_height), p.RESIZABLE)

        if gs:
            k = p.key.get_pressed()
            if k[p.K_UP] and di != 'D':
                di = 'U'
            if k[p.K_DOWN] and di != 'U':
                di = 'D'
            if (k[p.K_RIGHT] and di != 'L'):
                di = 'R'
            if k[p.K_LEFT] and di != 'R':
                di = 'L'

            dt = clock.tick(60) / 1000
               
            if di=='U':
                snake_speed_x = 0
                snake_speed_y = -sp
            if di == 'D': 
                snake_speed_x = 0
                snake_speed_y = sp
            if di == 'L':  
                snake_speed_x = -sp
                snake_speed_y = 0
            if di == 'R':
                snake_speed_x = sp
                snake_speed_y = 0

            nh = [snakeHead[0][0]+snake_speed_x*dt, snakeHead[0][1]+snake_speed_y*dt]
            snakeHead = [nh]+snakeHead[:-1]

            le += snake_speed_x * dt
            wid += snake_speed_y * dt
            khs = 0

            
            if nh[0] <= 0 or nh[0] >= screen_width - l or nh[1] <= 21 or nh[1] > screen_height - b2:
                m2.play()
                con = False
                con2 = False
            if colod == (0,255,0):
                for sss in snakeHead[1:]:
                    if sss == nh:
                        m2.play()
                        con = False
                        con2 = False
                
            w.fill((0, 190, 0))

            
            for j in range(0, screen_height, 20):
                p.draw.line(w, 'black', (0, j), (screen_width, j), 1)
            for i in range(0, screen_width, 20):
                p.draw.line(w, 'black', (i, 20), (i, screen_height), 1)
            
            
            c = p.draw.circle(w, coloc, (a, b), 8, 0)

            
            for sb in snakeHead:
                re = p.draw.rect(w, color[ssc], p.Rect(sb[0], sb[1], l, b2), 0, 5)
                if di == "L" or di == "R":
                    c = p.draw.circle(w, (0,0,0), (snakeHead[0][0]+5, snakeHead[0][1]), 3.7,0)
                    c = p.draw.circle(w, (0,0,0), (snakeHead[0][0]+15, snakeHead[0][1]), 3.7,0)
                    c = p.draw.circle(w, (255,255,255), (snakeHead[0][0]+5, snakeHead[0][1]+1), 1,0)
                    c = p.draw.circle(w, (255,255,255), (snakeHead[0][0]+15, snakeHead[0][1]+1), 1,0)
                else:
                    c = p.draw.circle(w, (0,0,0), (snakeHead[0][0]+5, snakeHead[0][1]+5), 3.7,0)
                    c = p.draw.circle(w, (0,0,0), (snakeHead[0][0]+15, snakeHead[0][1]+5), 3.7,0)
                    c = p.draw.circle(w, (255,255,255), (snakeHead[0][0]+5, snakeHead[0][1]+5), 1,0)
                    c = p.draw.circle(w, (255,255,255), (snakeHead[0][0]+15, snakeHead[0][1]+5), 1,0)
                    
            
            text = fon.render("Snake Game", True, (0, 0, 0))
            w.blit(text, (10, 3))
            
            tex = pon.render(f"Points: {point}", True, (0, 0, 0))
            w.blit(tex, (screen_width // 2 - 30, 3))
            
            elapsed_time = int(time.time() - start_time)
            time_text = ton.render(f"{elapsed_time}s", True, (0, 0, 0))
            w.blit(time_text, (screen_width - 40, 5))

            if con2 == False:
                gg = gon.render("Game Over!!",True,(0,0,0))
                w.blit(gg, (screen_width // 2 - 160, screen_height // 2 - 70))
                
                ee = ent.render("*Space -- Restart*",True,(0,0,0))
                w.blit(ee,(screen_width // 2 - 85, screen_height // 2 + 20))
                
                mm = p.font.SysFont(None,26)
                mmm = mm.render("*Enter -- Main Menu*",True,(0,0,0))
                w.blit(mmm,(screen_width // 2 - 95, screen_height // 2 + 63))
            
            p.display.update()

            if ovr([nh[0], nh[1], l, b2], (a, b, 8)):
                m1.play()
                a = r.randrange(10, screen_width, 20)
                b = r.randrange(30, screen_height, 20)
                snakeHead.append(snakeHead[-1])
                point += 1
                sp += 1  # Increase difficulty
            clock.tick(60)


def optScreen():

    global colod, ssc, w
    
    w.fill((0,170,0))
    p.draw.rect(w,(0,100,0),p.Rect(225,400,50,20),0,2)
    p.draw.rect(w,(0,0,0),p.Rect(225,400,50,20),1,2)
    aon = p.font.Font(None,25)
    at = aon.render("OK",True,(255,255,255))
    w.blit(at,(235,402))
    
    p.draw.rect(w,colod,p.Rect(150,100,200,40),0,2)
    p.draw.rect(w,(0,0,0),p.Rect(150,100,200,40),2,2)
    don = p.font.Font(None,36)
    dt = don.render("Body Collision",True,(0,0,0))
    w.blit(dt,(165,107))

    def snakeColor(color):
        p.draw.rect(w,color,p.Rect(150,150,200,40),0,2)
        p.draw.rect(w,(0,0,0),p.Rect(150,150,200,40),2,2)
        don = p.font.Font(None,36)
        if color == (0,0,0):
            dt = don.render("Snake Color",True,(255,255,255))
            w.blit(dt,(165,157))
        else:
            dt = don.render("Snake Color",True,(0,0,0))
            w.blit(dt,(165,157))
        
    snakeColor(color[ssc])
    p.display.update()
    c3 = True
    while c3:
    
        mouse = p.mouse.get_pos()
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit() 
            elif event.type == p.MOUSEBUTTONUP:
                if 225<=mouse[0]<=275 and 400<=mouse[1]<=420:
                    gameMainScreen()
                    
                elif 150<=mouse[0]<=350 and 100<=mouse[1]<=140 and colod == (0,255,0):
                    colod = (255,0,0)
                    p.draw.rect(w,colod,p.Rect(150,100,200,40),0,2)
                    p.draw.rect(w,(0,0,0),p.Rect(150,100,200,40),2,2)
                    don = p.font.Font(None,36)
                    dt = don.render("Body Collision",True,"white")
                    w.blit(dt,(165,107))
                    p.display.update()
                elif 150<=mouse[0]<=350 and 100<=mouse[1]<=140 and colod == (255,0,0):
                    colod = (0,255,0)
                    p.draw.rect(w,colod,p.Rect(150,100,200,40),0,2)
                    p.draw.rect(w,(0,0,0),p.Rect(150,100,200,40),2,2)
                    don = p.font.Font(None,36)
                    dt = don.render("Body Collision",True,"white")
                    w.blit(dt,(165,107))
                    p.display.update()

                elif 150<=mouse[0]<=350 and 150<=mouse[1]<=190 and ssc < len(color):
                    ssc += 1
                    if ssc == len(color):
                        ssc = 0
                    snakeColor(color[ssc])
                    p.display.update()
                     
                    
def gameMainScreen():
    global w
    
    imp = p.image.load(os.path.join("download.jpg")).convert()
    sp = p.transform.scale(imp, w.get_size())
    w.blit(sp,(0,0))

    hon = p.font.SysFont("terasong",90)
    ht = hon.render("Snake",True,(0,100,0))
    w.blit(ht,(20,0))

    hon = p.font.SysFont("terasong",90)
    ht = hon.render("Game",True,(0,100,0))
    w.blit(ht,(240,80))
    
    re = p.draw.rect(w,"darkgreen",p.Rect(180,220,140,40),3,8)
    son = p.font.Font(None,36)
    st = son.render("Start",True,(0,0,0))
    w.blit(st,(220,228))
    
    p.draw.rect(w,"darkgreen",p.Rect(190,270,120,40),3,8)
    son = p.font.Font(None,36)
    st = son.render("Options",True,(0,0,0))
    w.blit(st,(200,278))

    p.draw.rect(w,"darkgreen",p.Rect(200,320,100,40),3,8)
    son = p.font.Font(None,36)
    st = son.render("Exit",True,(0,0,0))
    w.blit(st,(227,328))
    
    p.display.update()
    cc = True
    while cc:
        
        mouse = p.mouse.get_pos()
        if 180<=mouse[0]<=320 and 220<=mouse[1]<=260:
            re = p.draw.rect(w,(0,150,0),p.Rect(180,220,140,40),3,8)
            p.display.update()
        else:
            re = p.draw.rect(w,"darkgreen",p.Rect(180,220,140,40),3,8)
            p.display.update()
            
            
        if 190<=mouse[0]<=310 and 270<=mouse[1]<=310:
            re = p.draw.rect(w,(0,150,0),p.Rect(190,270,120,40),3,8)
            p.display.update()
        else:
            re = p.draw.rect(w,"darkgreen",p.Rect(190,270,120,40),3,8)
            p.display.update()

        if 200<=mouse[0]<=300 and 320<=mouse[1]<=360:
            re = p.draw.rect(w,(0,150,0),p.Rect(200,320,100,40),3,8)
            p.display.update()
        else:
            re = p.draw.rect(w,"darkgreen",p.Rect(200,320,100,40),3,8)
            p.display.update()
            
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            elif event.type == p.MOUSEBUTTONUP:
                if 200<=mouse[0]<=300 and 320<=mouse[1]<=360:
                    p.quit()
                    sys.exit()
                elif 180<=mouse[0]<=320 and 220<=mouse[1]<=260:
                    TheSnakeGame()
                elif 190<=mouse[0]<=310 and 270<=mouse[1]<=310:
                    optScreen()
            elif event.type==p.KEYDOWN and event.key==p.K_ESCAPE:
                p.quit()
                sys.exit()
            elif event.type==p.KEYDOWN and event.key==p.K_RETURN:
                TheSnakeGame()
                while con == False:
                    for event in p.event.get():
                        if event.type == p.QUIT:
                            p.quit()
                            sys.exit()
                        elif event.type == p.KEYDOWN:
                            if event.key == p.K_RETURN:
                                gameMainScreen()
                            elif event.key == p.K_SPACE:
                                TheSnakeGame()
                
                    
gameMainScreen()
