import random,config
from npc import NPC
from player import Player

def spawn_npcs():
    return [NPC(random.randint(0,config.WIDTH),random.randint(0,config.HEIGHT)) for _ in range(config.NPC_COUNT)]

def reset_world():
    return Player(),spawn_npcs()