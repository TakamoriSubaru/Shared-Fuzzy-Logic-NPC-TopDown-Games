import pygame,sys,time,config,stats
from world import reset_world
from player_behavior import PlayerBehavior
from fuzzy_adaptation import update_brain
from performance import PerformanceTracker
from logger import init_csv,log_run
from bot_player import BotController

pygame.init()
screen=pygame.display.set_mode((config.WIDTH,config.HEIGHT))
clock=pygame.time.Clock()

stats.init(); init_csv()
performance=PerformanceTracker()
player_behavior=PlayerBehavior()
player,npcs=reset_world()
bot = BotController()

run_number=1
start_time=time.time()

while True:
    dt = clock.tick(config.FPS) / 1000

    # ========= EVENTS =========
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    # ========= 1. BOT GERAKKAN PLAYER =========
    bot.update(player, npcs, dt)

    # ========= 2. AI BELAJAR DARI PLAYER =========
    player_behavior.update(player, npcs, dt)

    if config.ADAPTIVE_AI:
        update_brain(player_behavior)

    # ========= 3. NPC UPDATE =========
    for npc in npcs:
        npc.update(player)

    # ========= 4. PERFORMANCE TRACKING =========
    performance.update(clock)

    # ========= 5. CEK PLAYER MATI =========
    if player.hp <= 0:
        survival = time.time() - start_time
        avg_fps, avg_cpu, avg_ram = performance.get_averages()

        log_run(run_number, survival, avg_fps, avg_cpu, avg_ram)

        run_number += 1
        performance.reset()

        pygame.time.delay(800)
        player, npcs = reset_world()
        start_time = time.time()

    # ========= 6. DRAW =========
    screen.fill(config.BG_COLOR)
    player.draw(screen)
    player.draw_hp(screen, stats.font)

    for npc in npcs:
        npc.draw(screen)

    stats.draw_stats(screen, clock, len(npcs))
    pygame.display.flip()