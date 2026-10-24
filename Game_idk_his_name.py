import pygame 

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True 
dt = 0


class Player:
    def __init__(self,x,y):
        self.pos_x = x
        self.pos_y = y

        self.velocity = 100
    
    def movement(self,key):
        if key[pygame.K_z] or key[pygame.K_UP] :
            self.pos_y -= self.velocity 
            print('A')
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.pos_y += self.velocity 
            print('B')
        if key[pygame.K_q] or key[pygame.K_RIGHT] :
            self.pos_x -= self.velocity 
            print('C')
        if key == pygame.K_d or pygame.K_LEFT:
            self.pos_x += self.velocity 
            print('D')

The_Player = Player(screen.get_width() /2, screen.get_height() /2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_mods()
    The_Player.movement(key)


    screen.fill("blue")

    pygame.draw.circle(screen,"red",(The_Player.pos_x,The_Player.pos_y),40)


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()