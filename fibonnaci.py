import pygame
bg = (128, 223, 255)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (247,247,48)
colors = [WHITE,RED,YELLOW,GREEN,BLUE]

pygame.init()
pygame.display.set_caption('Fibonacci')
width = 1600
height = int(1600/1.618)
center = (width/2,height/2)

screen = pygame.display.set_mode((width, height))
background = pygame.Surface(screen.get_size())
unit = 1
background.fill(bg)

# pygame.draw.rect(background, BLACK, (center[0],center[1]                    ,unit,unit))
# pygame.draw.rect(background, WHITE, (center[0],center[1]-unit                 ,unit,unit))

# pygame.draw.rect(background, RED, (center[0]+unit,center[1]-unit                ,unit*2,unit*2))
# pygame.draw.rect(background, GREEN, (center[0],center[1]+unit                 ,unit*3,unit*3))
# pygame.draw.rect(background, BLUE, (center[0]-5*unit,center[1]-unit             ,unit*5,unit*5))
# pygame.draw.rect(background, YELLOW, (center[0]-5*unit,center[1]-unit-8*unit      ,unit*8,unit*8))

# pygame.draw.rect(background, RED, (center[0]+3*unit,center[1]-unit-8*unit       ,unit*13,unit*13))
# pygame.draw.rect(background, GREEN, (center[0]-5*unit,center[1]+unit+3*unit       ,unit*21,unit*21))
# pygame.draw.rect(background, BLUE, (center[0]-5*unit-34*unit,center[1]-unit-8*unit   ,unit*34,unit*34))
# pygame.draw.rect(background, YELLOW, (center[0]-5*unit-34*unit,center[1]-unit-8*unit-55*unit   ,unit*55,unit*55))
#pygame.draw.rect(background, RED, (center[0]+3*unit+13*unit,center[1]-unit-8*unit-55*unit       ,unit*89,unit*89))
#pygame.draw.rect(background, BLACK, (center[0]-5*unit,center[1]+unit+3*unit       ,unit*21,unit*21))
#pygame.draw.rect(background, WHITE, (center[0]-5*unit-34*unit,center[1]-unit-8*unit   ,unit*34,unit*34))
#pygame.draw.rect(background, RED, (center[0]-5*unit-34*unit,center[1]-unit-8*unit-55*unit   ,unit*55,unit*55))

def w():
    screen.blit(background, (0,0))
    pygame.display.update()
    input()
w()
a = 1
b = 1
corner = center
pygame.draw.rect(background, BLACK, (corner[0],corner[1]                    ,unit,unit))
corner = (corner[0], corner[1]-unit)

w()
fib = [a, b]
while b < 1500:
    fib += [a+b]
    b = a + b
    a = b - a
print(fib)
i =1
w()
while i < 100:
    color = colors[(i-1)%5]
    pygame.draw.rect(background, color, (corner[0],corner[1]                     ,unit*fib[i],unit*fib[i]))
    corner = (corner[0]+unit*fib[i], corner[1])
    color = colors[(i)%5]
    pygame.draw.rect(background, color, (corner[0],corner[1]                   ,unit*fib[i+1],unit*fib[i+1]))
    corner = (corner[0]-unit*fib[i], corner[1]+unit*fib[i+1])
    color = colors[(i+1)%5]
    pygame.draw.rect(background, color, (corner[0],corner[1]                    ,unit*fib[i+2],unit*fib[i+2]))
    corner = (corner[0]-unit*fib[i+3], corner[1]-unit*fib[i+1])
    color = colors[(i+2)%5]
    pygame.draw.rect(background, color, (corner[0],corner[1]                  ,unit*fib[i+3],unit*fib[i+3]))
    corner = (corner[0], corner[1]-unit*fib[i+4])

    i+=4
    w()


while True:pass
