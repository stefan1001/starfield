import pygame
import random

WIDTH = 800
HEIGHT = 600

class Star:
    def __init__(self):
        self.x = int(random.random() * WIDTH)
        self.y = int(random.random() * HEIGHT)
        self.depth = int(random.random() * 5)

    def update(self):
        if self.finished():
            self.x = int(random.random() * WIDTH)
            self.y = 0
        speed = 5 - self.depth
        self.y = self.y + speed

    def finished(self):
        if self.y > HEIGHT:
            return True
        else:
            return False

    def draw(self):
        color = (255-self.depth*30,255-self.depth*30,255-self.depth*30)
        pygame.draw.circle(screen, color, (self.x,self.y),1)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

stars = []
for i in range(1,100):
    star = Star()
    stars.append(star)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill((0, 0, 0))

    for star in stars:
        star.update()
        star.draw()
    pygame.display.flip()