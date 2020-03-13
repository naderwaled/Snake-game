import pygame
import sys
import random
import time

class Snake():
    def __init__(self):
        self.position=[100,50]
        self.body=[[90,50],[80,50]]
        self.direction="RIGHT"
        self.changeDirectionTo=self.direction

    def changeDirctionTo(self,dirction):
        if dirction=="RIGHT" and not self.direction=="LEFT":
            self.direction="RIGHT"
        elif dirction=="LEFT" and not self.direction=="RIGHT":
            self.direction="LEFT"
        elif dirction=="UP" and not self.direction=="DOWN":
            self.direction="UP"
        elif dirction=="DOWN" and not self.direction=="UP":
            self.direction="DOWN"

    def move(self,foodposition):
        if self.direction =="RIGHT":
            self.position[0]+=10
        elif self.direction =="LEFT":
            self.position[0]-=10
        elif self.direction =="UP":
            self.position[1]-=10
        elif self.direction =="DOWN":
            self.position[1]+=10
        self.body.insert(0,list(self.position))
        if self.position==foodposition:
            return 1
        else:
            self.body.pop()
            return 0
    def checkCollision(self):
        if self.position[0]>490 or self.position[0]<0:
            return 1
        elif self.position[1]>490 or self.position[1]<0:
            return 1
        for bodypoart in self.body[1:]:
            if self.position==bodypoart:
                return 1
        return 0
    def getHeadPos(self):
        return self.position
    def getBody(self):
        return self.body


class FoodSwaper():
    def __init__(self):
        self.position=[random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.isFoodOnScreen=True

    def spawnFood(self):
        if self.isFoodOnScreen== False:
            self.position=[random.randrange(1,50)*10,random.randrange(1,50)*10]
            self.isFoodOnScreen=True
        return self.position
    def setFoodOnScreen(self,b):
        self.isFoodOnScreen=b
window=pygame.display.set_mode((500,500))
pygame.display.set_caption("WoW Snake")
fps=pygame.time.Clock()

score=0
snake=Snake()
foodSpawner=FoodSwaper()

def gameover():
    pygame.quit()
    sys.exit()


while True:
    time.sleep(0.07)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover();
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snake.changeDirctionTo("RIGHT")
            if event.key==pygame.K_LEFT:
                snake.changeDirctionTo("LEFT")
            if event.key==pygame.K_UP:
                snake.changeDirctionTo("UP")
            if event.key==pygame.K_DOWN:
                snake.changeDirctionTo("DOWN")
    foodpos=foodSpawner.spawnFood()
    snake.position[0]%=500
    snake.position[1] %= 500
    if (snake.move(foodpos)==1):
        score+=1
        foodSpawner.setFoodOnScreen(False)

    window.fill(pygame.Color(225,225,225))
    for pos in snake.getBody():
        pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0]%500,pos[1]%500,10,10))
    pygame.draw.rect(window, pygame.Color(225, 0, 0), pygame.Rect(foodpos[0], foodpos[1], 10, 10))
    #if(snake.eated()==1):
       #gameover()
    head=snake.getHeadPos()
    body=snake.getBody()
    if head in body:
        gameover()

    pygame.display.set_caption("WoW Snake | Score : "+str(score))
    pygame.display.flip()
    fps.tick(24)
