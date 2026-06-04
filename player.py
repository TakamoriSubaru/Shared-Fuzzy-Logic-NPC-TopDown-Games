import pygame, config

class Player:
    def __init__(self):
        self.x = config.WIDTH//2
        self.y = config.HEIGHT//2
        self.hp = config.PLAYER_MAX_HP

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.y -= config.PLAYER_SPEED
        if keys[pygame.K_s]: self.y += config.PLAYER_SPEED
        if keys[pygame.K_a]: self.x -= config.PLAYER_SPEED
        if keys[pygame.K_d]: self.x += config.PLAYER_SPEED

        self.x = max(0, min(config.WIDTH, self.x))
        self.y = max(0, min(config.HEIGHT, self.y))

    def draw(self, screen):
        pygame.draw.circle(screen, config.PLAYER_COLOR,(int(self.x),int(self.y)),config.PLAYER_RADIUS)

    def draw_hp(self, screen, font):
        screen.blit(font.render(f"HP:{int(self.hp)}",True,(255,255,255)),(10,100))