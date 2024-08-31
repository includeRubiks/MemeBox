import pygame,os

pygame.init()
pygame.mixer.init()
pygame.font.init()
x = 0
y = 0
screen = pygame.display.set_mode((1200, 720))
running = True
font = pygame.font.SysFont("Comic Sans MS", 15)
pygame.display.set_caption("MemeBox")
mp3s = os.listdir("mp3s")
row1txt = [] 
row2txt = []
row3txt = []
row4txt = []
row5txt = []
row1mp3 = [] 
row2mp3 = []
row3mp3 = []
row4mp3 = []
row5mp3 = []
for i,j in enumerate(mp3s):
    if i <= 4:
        row1txt.append(font.render(j,False,'black'))
        row1mp3.append(j)
    if i >= 5 and i <= 9:
        row2txt.append(font.render(j,False,'black'))
        row2mp3.append(j)
    if i >= 10 and i <= 15:
        row3txt.append(font.render(j,False,'black'))
        row3mp3.append(j)
    if i >= 16 and i <= 20:
        row4txt.append(font.render(j,False,'black'))
        row4mp3.append(j)
    if i >= 21 and i <= 25:
        row5txt.append(font.render(j,False,'black'))
        row5mp3.append(j)
def memebox(x,y):
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,200,100))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

            if y >= 20 and y <= 120:
                for i in range(len(row1txt)):
                    if x >= i*240+20 and x <= i*240+20+200:
                        mp3 = pygame.mixer.Sound(f'mp3s/{row1mp3[i]}')
                        pygame.mixer.Sound.play(mp3)
                        pygame.mixer.music.stop()
    
    screen.fill("white")
    
    for i,j in enumerate(row1txt):
        memebox(i*240+20,20)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),50+7.5))
    for i,j in enumerate(row2txt):
        memebox(i*240+20,140)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),170+7.5))
    for i,j in enumerate(row3txt):
        memebox(i*240+20,260)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),290+7.5))
    for i,j in enumerate(row4txt):
        memebox(i*240+20,380)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),410-7.5))
    for i,j in enumerate(row5txt):
        memebox(i*240+20,500)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),530-7.5))

    pygame.display.flip()
            
pygame.quit()
