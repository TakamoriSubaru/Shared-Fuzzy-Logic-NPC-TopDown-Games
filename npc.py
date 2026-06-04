import pygame,math,config
from fuzzy_adaptation import shared_brain

class NPC:
    def __init__(self,x,y):
        self.x=x; self.y=y; self.base_speed=1.5

    def update(self,player):
        speed=self.base_speed*shared_brain["speed"]
        attack_range=shared_brain["attack_range"]
        aggression=shared_brain["aggression"]

        dx=player.x-self.x
        dy=player.y-self.y
        dist=math.sqrt(dx*dx+dy*dy)

        if dist>0:
            self.x+=(dx/dist)*speed
            self.y+=(dy/dist)*speed

        if dist<attack_range:
            player.hp-=0.3*aggression

    def draw(self,screen):
        pygame.draw.circle(screen,config.NPC_COLOR,(int(self.x),int(self.y)),6)