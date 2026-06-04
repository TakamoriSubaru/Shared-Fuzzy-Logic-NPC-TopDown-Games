import pygame,psutil
font=None

def init():
    global font
    font=pygame.font.SysFont("consolas",18)

def draw_stats(screen,clock,npc_count):
    texts=[f"FPS:{int(clock.get_fps())}",f"CPU:{psutil.cpu_percent()}%",f"NPC:{npc_count}"]
    y=10
    for t in texts:
        screen.blit(font.render(t,True,(255,255,255)),(10,y)); y+=22