import random
import math
import config

class BotController:
    def __init__(self):
        self.target_x = random.randint(0, config.WIDTH)
        self.target_y = random.randint(0, config.HEIGHT)
        self.change_timer = 0

    def update(self, player, npcs, dt):
        # ganti tujuan tiap beberapa detik supaya gerakan natural
        self.change_timer += dt
        if self.change_timer > 2:
            self.target_x = random.randint(0, config.WIDTH)
            self.target_y = random.randint(0, config.HEIGHT)
            self.change_timer = 0

        # ===============================
        # Hindari NPC terdekat (survival AI)
        # ===============================
        closest_npc = None
        closest_dist = 999999

        for npc in npcs:
            dx = npc.x - player.x
            dy = npc.y - player.y
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < closest_dist:
                closest_dist = dist
                closest_npc = npc

        move_x, move_y = 0, 0

        # jika NPC dekat → kabur
        if closest_npc and closest_dist < 120:
            move_x = player.x - closest_npc.x
            move_y = player.y - closest_npc.y

        # jika aman → jalan ke target random
        else:
            move_x = self.target_x - player.x
            move_y = self.target_y - player.y

        # normalize movement
        length = math.sqrt(move_x*move_x + move_y*move_y)
        if length > 0:
            move_x /= length
            move_y /= length

        # gerakkan player
        player.x += move_x * config.PLAYER_SPEED
        player.y += move_y * config.PLAYER_SPEED

        # batasi dalam map
        player.x = max(0, min(config.WIDTH, player.x))
        player.y = max(0, min(config.HEIGHT, player.y))