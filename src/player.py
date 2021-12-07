import pygame
from win import Win

SPRITE_WIDTH = 50
SPRITE_HEIGHT = 50

img_u = pygame.transform.scale(pygame.image.load("../lib/Player_up.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_r = pygame.transform.scale(pygame.image.load("../lib/Player_right.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_d = pygame.transform.scale(pygame.image.load("../lib/Player_down.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_l = pygame.transform.scale(pygame.image.load("../lib/Player_left.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_r
        self.rect = self.image.get_rect()
        self.rect.center = (Win.WIDTH / 2 + Win.MARGIN_LEFT + ((Win.WIDTH / 2 + Win.MARGIN_LEFT + (Win.GRID_SIZE/2)) % Win.GRID_SIZE), Win.HEIGHT / 2 + Win.MARGIN_TOP + ((Win.HEIGHT / 2 + Win.MARGIN_TOP + (Win.GRID_SIZE/2)) % Win.GRID_SIZE))
        self.direction = 0 # 0 - none, 1 - up, 2 - right, 3 - down, 4 - left
        self.trn = 0 # 0 - none, 1 - up, 2 - right, 3 - down, 4 - left
        self.frame = 0 # count frames
        self.step = 10
    
    def turn(self, dir):
        self.trn = dir

    def update(self, map):
        if(self.trn == 1 or self.trn == 3):
            x = int(self.rect.center[0] / Win.GRID_SIZE) * Win.GRID_SIZE + int(Win.GRID_SIZE / 2)
            y = self.rect.center[1]
            if(self.direction == 1 or self.direction == 3):
                self.direction = self.trn
                self.trn = 0
            if(self.direction == 2 or self.direction == 0):
                if((self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    if(self.trn == 1):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((y - Win.MARGIN_TOP) / Win.GRID_SIZE - 1)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
                    if(self.trn == 3):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((y - Win.MARGIN_TOP) / Win.GRID_SIZE + 1)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0

            if(self.direction == 4 or self.direction == 0):
                if((self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    if(self.trn == 1):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((y - Win.MARGIN_TOP) / Win.GRID_SIZE) - 1) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
                    if(self.trn == 3):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((y - Win.MARGIN_TOP) / Win.GRID_SIZE + 1)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
            
        if(self.trn == 2 or self.trn == 4):
            x = self.rect.center[0]
            y = int(self.rect.center[1] / Win.GRID_SIZE) * Win.GRID_SIZE + int(Win.GRID_SIZE / 2)
            if(self.direction == 4 or self.direction == 2):
                self.direction = self.trn
                self.trn = 0
            if(self.direction == 1 or self.direction == 0):
                if((self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    if(self.trn == 2):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE) + 1, int((y - Win.MARGIN_TOP) / Win.GRID_SIZE)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
                    if(self.trn == 4):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE) - 1, int((y - Win.MARGIN_TOP) / Win.GRID_SIZE)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
            if(self.direction == 3 or self.direction == 0):
                if((self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    if(self.trn == 2):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE) + 1, int((y - Win.MARGIN_TOP) / Win.GRID_SIZE)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
                    if(self.trn == 4):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE) - 1, int((y - Win.MARGIN_TOP) / Win.GRID_SIZE)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
            

        if(self.direction == 1):
            if(self.rect.y - self.step >= Win.MARGIN_TOP and not map.is_blocked(int((self.rect.x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y - self.step - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.y -= self.step
            self.image = img_u

        if(self.direction == 2):
            if(self.rect.x + self.step + SPRITE_WIDTH <= Win.WIDTH + Win.MARGIN_LEFT and not map.is_blocked(int((self.rect.x + self.step + SPRITE_WIDTH - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.x += self.step
            self.image = img_r

        if(self.direction == 3):
            if(self.rect.y + self.step + SPRITE_HEIGHT <= Win.HEIGHT + Win.MARGIN_TOP and not map.is_blocked(int((self.rect.x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y + self.step + SPRITE_HEIGHT - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.y += self.step
            self.image = img_d
            
        if(self.direction == 4):
            if(self.rect.x - self.step >= Win.MARGIN_LEFT and not map.is_blocked(int((self.rect.x - self.step - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.x -= self.step
            self.image = img_l
        