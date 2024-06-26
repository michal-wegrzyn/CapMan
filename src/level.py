import pygame
from win import Win
from colors import Colors

# 24x25
block_space = pygame.transform.scale(pygame.image.load("../assets/ingame_textures/map/block.png"), [Win.GRID_SIZE, Win.GRID_SIZE])
block_beach = pygame.transform.scale(pygame.image.load("../assets/ingame_textures/map/block_beach.png"), [Win.GRID_SIZE, Win.GRID_SIZE])
block_ice = pygame.transform.scale(pygame.image.load("../assets/ingame_textures/map/block_ice.png"), [Win.GRID_SIZE, Win.GRID_SIZE])

class Level:
    def __init__(self):
        self.lvl = 0
        self.maps = [
            # clean map:
            # [
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,1,1,2,1,1,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            # ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0],
                [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,0,0,1,1,2,1,1,0,0,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,2,0,0,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0],
                [1,0,0,0,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0],
                [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,1,0,1,0,1,1,2,1,1,0,1,0,1,1,1,0,1,0,1,0],
                [1,0,1,0,1,3,1,0,1,0,1,2,2,2,1,0,1,0,1,3,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,2,2,2,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,2,0,0,0,1,0,1,0,1,0,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0],
                [1,0,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0],
                [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0],
                [1,0,1,0,3,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,3,0,1,0],
                [1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0],
                [1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0],
                [1,0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,2,1,1,0,0,1,0,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,1,0,1,0,1,2,2,2,1,0,0,1,0,0,1,0,1,0,1,0],
                [1,0,1,1,1,0,1,0,1,0,1,2,2,2,1,0,0,1,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,2,0,0,0,0,1,0,1,0,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0,0],
                [0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,3,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0],
                [1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,3,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,3,0,0,1,0,0,1,0,0,1,3,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,2,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,2,2,2,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,2,2,2,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,1,1,3,1,0,0,1,0,3,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0],
                [1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,0,0,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0],
                [1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,1,1,1,1,0,0,0,1,1,2,1,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,1,1,0,1,1,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,1,1,0,1,1,0,0,0,1,0],
                [1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,0,1,0,0,1,0,0,0,2,0,0,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,1,0,0,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0],
                [1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0],
                [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,3,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,3,0,0,1,0],
                [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],
                [1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,2,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,0,0,0,0,0,2,0,0,0,0,0,1,0,1,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0],
                [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],
                [1,3,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,3,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0],
                [1,0,1,3,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,3,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0],
                [1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0],
                [2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,0],
                [1,1,1,1,1,0,1,1,0,0,1,1,2,1,1,0,0,1,1,0,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0],
                [2,2,2,2,1,0,1,1,0,0,0,0,2,0,0,0,0,1,1,0,1,2,2,2,2,0],
                [1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0],
                [1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0],
                [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            [
                [1,0,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,0,0,0,0,0,1,3,0,0,1,2,2,2,1,0,0,3,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,1,1,1,0,1,0],
                [1,0,0,0,1,0,1,1,1,0,1,2,2,2,1,0,1,1,1,0,1,0,0,0,1,0],
                [1,0,1,0,1,0,0,0,1,0,1,1,2,1,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,0],
                [1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,1,0],
                [1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,1,0,1,0,1,1,2,1,1,0,1,0,1,1,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,2,2,2,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,0,0,0,1,2,2,2,1,0,0,0,1,0,1,0,0,0,1,0],
                [1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0],
                [1,0,0,0,0,0,1,0,1,0,0,0,2,0,0,0,1,0,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0],
                [1,0,1,3,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,3,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0],
                [1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],

            # [
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,1,1,2,1,1,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,1,2,2,2,1,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,1,2,2,2,1,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,0,0,2,0,0,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            # ],
            ]
        self.start_maps = self.maps

        self.mapsCfg = [
            # [[ghosts collaboration skills],[chase speed, scary speed], [scary mode length, scatter mode time], [open ghost1, g2, g3], [player speed, player scary speed]]
            # lvl 1
            [
                [[2], [3, 2], [12, 20], [15, 30, 45], [4, 6]],
                [[3], [3, 2], [10, 25], [15, 30, 45], [4, 6]],
                [[10], [3, 2], [10, 35], [12, 24, 34], [4, 6]],
                ['space']
            ],
            # lvl 2
            [
                [[3], [3, 2], [12, 25], [15, 30, 45], [4, 6]],
                [[5], [3, 2], [10, 30], [12, 24, 36], [4, 6]],
                [[10], [3, 2], [10, 35], [12, 24, 34], [4, 6]],
                ['winter']
            ],
            # lvl 3
            [
                [[4], [3, 2], [10, 30], [12, 24, 36], [4, 6]],
                [[8], [3, 2], [10, 30], [12, 24, 36], [4, 6]],
                [[15], [3, 2], [8, 40], [12, 24, 36], [4, 4]],
                ['space']
            ],
            # lvl 4
            [
                [[5], [3, 2], [10, 35], [12, 24, 34], [4, 6]],
                [[10], [3, 2], [8, 35], [12, 24, 34], [4, 4]],
                [[20], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                ['beach']
            ],
            # lvl 5
            [
                [[5], [4, 3], [7, 30], [8, 16, 24], [6, 6]],
                [[12], [6, 4], [5, 30], [6, 12, 18], [8, 8]],
                [[25], [6, 6], [5, 35], [3, 8, 12], [8, 8]],
                ['space']
            ],
            # lvl 6
            [
                [[8], [3, 2], [8, 40], [15, 23, 30], [4, 4]],
                [[15], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[40], [3, 2], [8, 40], [5, 15, 25], [4, 4]],
                ['winter']
            ],
            # lvl 7
            [
                [[10], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[20], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[1000], [3, 2], [8, 45], [4, 12, 20], [4, 4]],
                ['space']
            ],
            # lvl 8
            [
                [[10], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[20], [3, 2], [7, 45], [6, 15, 24], [4, 4]],
                [[1000], [3, 2], [7, 45], [4, 12, 20], [4, 4]],
                ['beach']
            ]
        ]

        self.themes = {
            # name : board color, block
            'space': [Colors.DARK_GRAY, block_space],
            'winter': [Colors.ICE, block_ice],
            'beach': [Colors.SAND, block_beach]
        }

    def reset(self):
        self.lvl = 0
        self.maps = self.start_maps

    def is_blocked(self, x, y):
        if(self.maps[self.lvl][y][x] == 3):
            return 0
        return self.maps[self.lvl][y][x]

    def show_board(self):
        return self.maps[self.lvl].copy()

    def to_board(self):
        theme = self.mapsCfg[self.lvl][3][0]
        pygame.draw.rect(Win.screen, self.themes[theme][0],(Win.MARGIN_LEFT, Win.MARGIN_TOP, Win.GRID_SIZE*25, Win.GRID_SIZE*24))
        for i in range(25):
            for j in range(24):
                if(self.maps[self.lvl][j][i] == 1):
                    Win.screen.blit(self.themes[theme][1], (Win.MARGIN_LEFT + Win.GRID_SIZE * i, Win.MARGIN_TOP + Win.GRID_SIZE * j))
