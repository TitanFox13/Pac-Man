import pygame
from scripts.settings import block_size, play_x, ghost_images
from scripts.solver import Solver


# sprite class of our enemy
class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, grid, player, order):

        pygame.sprite.Sprite.__init__(self)
        # x and y based on the grid
        self.x = x
        self.y = y
        # order of the enemy used to releasing it and choosing correct image
        self.order = order
        # getting image
        self.image = ghost_images[self.order]
        # getting rect and true x and y
        self.rect = self.image.get_rect()
        self.rect.x = self.x * block_size + play_x
        self.rect.y = self.y * block_size
        # velocity
        self.vel = 1

        # a* path finding
        self.solver = None
        # found path to Pac-Man
        self.path = []
        # grid the enemy is in
        self.grid = grid
        # player used to get its position
        self.player = player

        # basically a direction he should move in can be 1, 0, -1
        # vertical
        self.kv = 0
        # horizontal
        self.kh = 0

        # constant used to get the release time
        self.k_release = 100
        # release time of the enemy
        self.release_time = self.order * self.k_release

        # list of all enemies
        self.enemies = None

    # function that will move the enemy
    def move(self):
        # if enemy is completely on a block then he can be moved
        if self.rect.x % block_size == 0:
            self.rect.y += self.vel * self.kv
            self.y = self.rect.y // block_size
        # if enemy is completely on a block then he can be moved
        if self.rect.y % block_size == 0:
            self.rect.x += self.vel * self.kh
            self.x = (self.rect.x - play_x) // block_size

    # function which will get how should the player move
    def get_next_move(self):
        # a* solver
        self.solver = Solver(self.grid[int(self.x)][int(self.y)], self.player, self.grid, self.enemies)
        # running the solver
        self.solver.solve_run()
        # getting solvers path
        if len(self.solver.path) != 0:
            self.path = self.solver.path
        # setting the next move
        try:
            next_move = self.path[1]
            # removing the first element of the path so we can reuse it if the solver doesnt find a path
            self.path.pop(0)
        except IndexError:
            next_move = self.grid[int(self.x)][int(self.y)]
        # setting up correctly values determining the direction
        self.kh = next_move.grid_x - self.x
        self.kv = next_move.grid_y - self.y
        # resetting the costs of blocks
        self.solver.reset()

    # update function
    def update(self):
        # releasing the enemy
        if self.release_time != 0:
            self.release_time -= 1
        else:
            # can move if it is completely on a block
            if self.rect.x % block_size == 0 and self.rect.y % block_size == 0:
                self.get_next_move()
            self.move()
