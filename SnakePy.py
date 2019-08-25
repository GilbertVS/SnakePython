#_*_ coding: utf-8-*_
#@date : 23 d'agost del 2019
#@file : SnakePy.py
#@description : joc de la serp, menjar el màxim nombres possibles però no la teva cua o l'altre serp o les pareds
#@author : Gilbert Viader
#importarem la llibreria pygame per poder usar els seus mètodes
import pygame, time, random
from snakepy1 import snakePython1
from snakepy2 import snakePython2
def snake_menu() :
    #començament de la finestre pygame
    pygame.init()
    sortir = False
    blau, marro, blanc = (21, 21, 154), (121, 54, 54), (254, 254, 254)
    blau2, marro2, blanc2 = (21, 21, 154), (121, 54, 54), (254, 254, 254)
    amplada = 950
    alsada = 690
    finestre = pygame.display.set_mode((amplada, alsada))
    #nom del joc
    pygame.display.set_caption("snake python")
    serp = "cobra.gif"
    po_serp = pygame.image.load(serp)
    po_serp = pygame.transform.scale(po_serp, (amplada, alsada))
    clock = pygame.time.Clock()
    while not sortir:
        clock.tick(10)
        for moment in pygame.event.get():
            if moment.type == pygame.QUIT :
                sortir = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] :
            sortir = True
        finestre.fill((184, 254, 114))
        finestre.blit(po_serp, (0, 0))
        tipograf = pygame.font.SysFont("serif", int(amplada/6))
        retol = tipograf.render("Snake  python",1, (21, 21, 154))
        finestre.blit(retol, (amplada/30, alsada/5))
        tipograf2 = pygame.font.SysFont("serif", int(amplada/16))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if amplada*0.15<mouse[0]<amplada/4+amplada*0.15 and alsada*0.45<mouse[1]<alsada*0.45+alsada/5 :
            blau, marro, blanc = (0, 0, 254), (204, 138, 138), (0, 0, 0)
            if click[0] == 1 or keys[pygame.K_RETURN] :
                snakePython1()
        elif amplada*0.15+amplada/2<mouse[0]<amplada*0.15+amplada*3/4 and alsada*0.45<mouse[1]<alsada*0.45+alsada/5 :
            blau2, marro2, blanc2 = (0, 0, 254), (204, 138, 138), (0, 0, 0)
            if click[0] == 1 or keys[pygame.K_RETURN] :
                snakePython2()
        else :
            blau, marro, blanc = (21, 21, 154), (121, 54, 54), (254, 254, 254)
            blau2, marro2, blanc2 = (21, 21, 154), (121, 54, 54), (254, 254, 254)
        pygame.draw.rect(finestre, blau, (amplada*0.15, alsada*0.45, amplada/4, alsada/10))
        pygame.draw.rect(finestre, marro, (amplada*0.15, alsada*0.45+alsada/10, amplada/4, alsada/10))
        boto1 = tipograf2.render("1 Player", 1, blanc)
        finestre.blit(boto1, (amplada*0.15+ alsada/69, alsada*0.45+alsada/28+ alsada/69))
        pygame.draw.rect(finestre, blau2, (amplada*0.15+ amplada/2, alsada*0.45, amplada/4, alsada/10))
        pygame.draw.rect(finestre, marro2, (amplada*0.15 + amplada/2, alsada*0.45+alsada/10, amplada/4, alsada/10)) 
        boto2 = tipograf2.render("2 Players", 1, blanc2)
        finestre.blit(boto2, (amplada*0.15+amplada/2+alsada/69, alsada*0.45+alsada/28+ alsada/69))    
        pygame.display.flip()
    # sortida de la finestre pygame i de python
    pygame.quit()
    quit()
#---------------- comença el programa
snake_menu()

