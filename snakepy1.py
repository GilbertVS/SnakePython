import pygame, time, random
from datetime import datetime

def snakePython1() :
    # posició nova aleatòria
    random.seed(datetime.now().second*43)
    pygame.mixer.music.load("scooter.mp3")
    pygame.mixer.music.play(-1)
    crash_sound = pygame.mixer.Sound("crash.wav")
    # valors d'amplada i alçada de la nostre finestre
    amplada = 950
    alsada = 690
    finestre = pygame.display.set_mode((amplada, alsada))
    # nom del joc
    pygame.display.set_caption("snake python")
    # variable de repetició del bucle pygame
    moment = pygame.time.Clock()
    # inicialització de variables
    ample = int(amplada/55)
    alt = int(alsada/30)
    vel = int(amplada/190)
    s_cap = pygame.image.load("serpCap0.jpg")
    s_cap = pygame.transform.scale(s_cap, (int(ample*1.8), int(alt*1.8)))
    s_cape = pygame.image.load("serpCap0e.jpg")
    s_cape= pygame.transform.scale(s_cape, (int(ample*1.8), int(alt*1.8)))
    s_capd = pygame.image.load("serpCap0d.jpg")
    s_capd = pygame.transform.scale(s_capd, (int(ample*1.8), int(alt*1.8)))
    s_capu = pygame.image.load("serpCap0u.jpg")
    s_capu = pygame.transform.scale(s_capu, (int(ample*1.8), int(alt*1.8)))
    cap_serp = s_cap
    sortir, run, ordenada, abcisa, pause, aleatori, crash = False, True, True, True, False, True, False 
    x_canvi, y_canvi, am, al = 0, 0, 0, 0
    cont_Ale = 1
    x_Ale = ample + vel
    y_Ale = alt + vel
    x_canvi += vel
    x, y = [], []
    y = []
    level, score1 = 1, 0
    for i in range(0, 121) :
        x.append(amplada/2)
        y.append(alsada/2)
    # bucle de tornar a començar
    while not(sortir) :
        run = True
        # bucle de redibuixar la nostra finestre pygame
        while run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sortir = True
                elif event.type == pygame.KEYDOWN  :
                    if event.key == pygame.K_ESCAPE :
                        run = False
                        sortir = True
                    if event.key == pygame.K_RIGHT and ordenada == True :
                        am, al = 0, -alt/2
                        cap_serp = s_cap
                        y_canvi = 0
                        x_canvi += vel
                        abcisa, ordenada = True, False
                    if event.key == pygame.K_LEFT and ordenada  == True :
                        am, al = -ample/2, -alt/2
                        cap_serp = s_cape
                        y_canvi = 0
                        x_canvi -= vel
                        abcisa, ordenada = True, False
                    if event.key == pygame.K_UP and abcisa == True :
                        am, al = -ample/2, -alt
                        cap_serp = s_capu
                        x_canvi = 0
                        y_canvi -= vel
                        abcisa, ordenada = False, True
                    if event.key == pygame.K_DOWN and abcisa == True :
                        am, al = -ample/2, 0
                        cap_serp = s_capd
                        abcisa, ordenada = False, True
                        x_canvi = 0
                        y_canvi += vel
                    if event.key == 112 :
                        pygame.mixer.music.pause()
                        pause = True
            while pause :
                for event2 in pygame.event.get() :
                    if event2.type  == pygame.QUIT :
                        pause = False
                    elif event2.type == pygame.KEYDOWN :
                        if event2.key == pygame.K_RIGHT or event2.key == pygame.K_LEFT or event2.key == pygame.K_UP :
                            pygame.mixer.music.unpause()
                            pause = False
                        if event2.key == pygame.K_DOWN or event2.key == pygame.K_ESCAPE or event2.key == 112 :
                            pygame.mixer.music.unpause()
                            pause = False
                tipografia = pygame.font.SysFont("serif", int(amplada/15))
                texte = tipografia.render("PAUSED", 1, (121, 121, 121))
                finestre.blit(texte, (amplada/5, alsada/3))            
                pygame.display.update()
                moment.tick(30)
            finestre.fill((184, 254, 114))
            if x[0] >= amplada*0.7 :
                crash = True
            if x[0] <= ample :
                crash = True
            if y[0] >= alsada*0.9 :
                crash = True
            if y[0] <= alt :
                crash = True
            index = 120
            while index > 0 :
                x[index] = x[index-1]
                y[index] = y[index-1]
                index -= 1
            x[0] += x_canvi
            y[0] += y_canvi    
            if x[0] <= x_Ale + ample/2 <= x[0]+ample :
                if y[0] <= y_Ale + alt/2 <= y[0]+alt :
                    aleatori = True
                    score1 += cont_Ale
                    cont_Ale += 1
                    
            if aleatori == True :
                while aleatori:
                    x_Ale = random.randrange(ample + vel, amplada*0.7 - vel)
                    y_Ale = random.randrange(alt + vel, alsada*0.9 - vel)
                    aleatori = False
                    if amplada*0.35<=x_Ale<=amplada*0.35+ample and alt<=y_Ale<=alt+alsada*0.8 :
                        aleatori = True
                    if amplada*0.175<=x_Ale<=amplada*0.175+ample and alsada*0.1<y_Ale<=alsada*0.9+alt :
                        aleatori = True
                    if amplada*0.525<=x_Ale<=amplada*0.525+ample and alsada*0.1<y_Ale<=alsada*0.9+alt :
                        aleatori = True
            tipografia2 = pygame.font.SysFont("serif", int(amplada/15))
            nivell = tipografia2.render("LEVEL :", 1, (21, 21, 154))
            finestre.blit(nivell, (amplada*0.7+vel*9, alt))
            tipografia3 = pygame.font.SysFont("serif", int(amplada/10))
            n = tipografia3. render("{}".format(level), 1, (21, 21, 154))
            finestre.blit(n, (amplada*0.7+20*vel, alt*3))
            score = tipografia2.render("SCORE :", 1, (71, 124, 71))
            finestre.blit(score, (amplada*0.7+vel*5, alt*7))
            s_nom = tipografia2.render("{}".format(score1), 1, (71, 124, 71))
            finestre.blit(s_nom, (amplada*0.7+vel*20, alt*9+vel))
            pygame.draw.rect(finestre, (254, 254, 124), (ample, alt, amplada*0.7, alsada*0.9), vel*2)
            if level > 2 :
                pygame.draw.rect(finestre, (254, 254, 124), (amplada*0.35, alt, ample, alsada*0.8))
                if amplada*0.35<=x[0]<=amplada*0.35+ample and alt<=y[0]<alt+alsada*0.8 :
                    crash = True
            if level > 3 :
                pygame.draw.rect(finestre, (254, 254, 124), (amplada*0.175, alsada*0.1, ample, alsada*0.8+alt))
                if amplada*0.175<=x[0]<=amplada*0.175+ample and alsada*0.1<y[0]<=alsada*0.9+alt :
                    crash = True
                pygame.draw.rect(finestre, (254, 254, 124), (amplada*0.525, alsada*0.1, ample, alsada*0.8+alt))
                if amplada*0.525<=x[0]<=amplada*0.525+ample and alsada*0.1<y[0]<=alsada*0.9+alt :
                    crash = True
            tipografia1 = pygame.font.SysFont("serif", int(alt))
            aleatori = tipografia1.render("{}".format(cont_Ale), 1, (21, 21, 21))
            if cont_Ale < 10 :
                finestre.blit(aleatori, (x_Ale, y_Ale))
            if cont_Ale > 1 :
                for i in range(1, 16) :
                    pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                    for i in range(1,16) :
                        if x[i]==x[0] and y[i]==y[0]:
                            crash = True                         
            if cont_Ale > 2 :
                for i in range(17, 31) :
                    pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                    for i in range(17,31) :
                        if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                            crash = True
            if cont_Ale > 3 :
                for i in range(32, 46) :
                    pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                    for i in range(32, 46) :
                        if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                            crash = True
            if cont_Ale > 4 :
                for i in range(47, 61) :
                    pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                    for i in range(47, 61) :
                        if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                            crash = True
            if cont_Ale > 5 :
                for i in range(62, 76) :
                    pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                    for i in range(62, 76) :
                        if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                            crash = True
            if cont_Ale > 6 :
                for i in range(77, 91) :
                    pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                    for i in range(77, 91) :
                        if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                            crash = True
            if cont_Ale > 7 :
                for i in range(92, 106) :
                    pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                    for i in range(92, 106) :
                        if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                            crash = True               
            if cont_Ale > 8 :
                for i in range(107, 120) :
                    pygame.draw.rect(finestre, (54, 154, 54), (x[i], y[i], ample, alt))
                    for i in range(107, 120) :
                        if x[i]<x[0]+ample/2<x[i]+ample and y[i]<y[0]+alt/2<y[i]+alt :
                            crash = True
            if cont_Ale > 9 :
                run = False
                level += 1
                sortir, ordenada, abcisa, aleatori = False, True, True, True 
                cont_Ale = 1
                texte = tipografia2.render("LEVEL {}".format(level), 1, (121, 121, 121))
                finestre.blit(texte, (amplada/5, alsada/3))
            pygame.draw.rect(finestre, (54, 154, 54), (x[0],  y[0], ample, alt))
            finestre.blit(cap_serp, (x[0]+am, y[0]+al))
            if crash == True :
                pygame.mixer.Sound.play(crash_sound)
                pygame.mixer.music.stop()
                run = False
                sortir = True
                xoc = tipografia3.render("CRASH !!", 1, (144, 64, 64))
                finestre.blit(xoc, (amplada/7, alsada/3))
            pygame.display.flip()
            if crash == True:
                time.sleep(2)
                from SnakePy import snake_menu
                snake_menu()
            if run == False:
                time.sleep(2)
            pygame.display.update()
            moment.tick(30)
