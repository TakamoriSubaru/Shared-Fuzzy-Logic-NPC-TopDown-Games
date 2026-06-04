import math

class PlayerBehavior:
    def __init__(self):
        self.prev_pos=None
        self.movement_intensity=0
        self.avg_distance_to_npcs=200

    def update(self,player,npcs,dt):
        if self.prev_pos:
            dx=player.x-self.prev_pos[0]
            dy=player.y-self.prev_pos[1]
            speed=math.sqrt(dx*dx+dy*dy)
            self.movement_intensity=self.movement_intensity*0.9+speed*10*0.1
        self.prev_pos=(player.x,player.y)

        if len(npcs)>0:
            total=0
            for npc in npcs:
                dx=npc.x-player.x
                dy=npc.y-player.y
                total+=math.sqrt(dx*dx+dy*dy)
            self.avg_distance_to_npcs=total/len(npcs)