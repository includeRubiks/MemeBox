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
for i,j in enumerate(mp3s):
    if i <= 4:
        row1txt.append(font.render(j,False,'black'))
    if i >= 5 and i <= 9:
        row2txt.append(font.render(j,False,'black'))
    if i >= 10 and i <= 15:
        row3txt.append(font.render(j,False,'black'))
    if i >= 16 and i <= 20:
        row4txt.append(font.render(j,False,'black'))
    if i >= 21 and i <= 25:
        row5txt.append(font.render(j,False,'black'))
def memebox(x,y):
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,200,100))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
    
    screen.fill("white")
    
    for i,j in enumerate(row1txt):
        memebox(i*240+20,20)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),i*240+50+(j.get_rect().height/2)))
    for i,j in enumerate(row2txt):
        memebox(i*240+20,140)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),i*240+170+(j.get_rect().height/2)))
    for i,j in enumerate(row3txt):
        memebox(i*240+20,260)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),i*240+290+(j.get_rect().height/2)))
    for i,j in enumerate(row4txt):
        memebox(i*240+20,380)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),i*240+410-(j.get_rect().height/2)))
    for i,j in enumerate(row5txt):
        memebox(i*240+20,500)
        screen.blit(j,((i*240+20+100)-(j.get_rect().width/2),i*240+530-(j.get_rect().height/2)))

    pygame.display.flip()
            
pygame.quit()
