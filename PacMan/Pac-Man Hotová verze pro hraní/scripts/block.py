import pygame
import math
from scripts.settings import colors, play_width, block_size


class Block:

    def __init__(self, color, x, y):
        # grid positions
        self.grid_x = x
        self.grid_y = y
        # calculating x and y to adjust it to the grid
        self.x = self.grid_x * block_size + 100
        self.y = self.grid_y * block_size
        # setting up position for drawing rectangles
        self.pos = (self.x, self.y, block_size, block_size)
        # choosing color
        self.color = color

        # costs helping the enemies to find their path
        # distance from the end
        self.h_cost = 0
        # distance from the start
        self.g_cost = 0
        # f cost + h cost
        self.f_cost = 0
        # parent block of this one
        self.parent = None
        # positions where the neighbour could be
        self.possible_neighbour_pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # list of neighbours
        self.neighbours = []

        # group of enemies used to know if this block is occupied
        self.enemies = None

    # getting the h cost by using pythagorean theorem
    def get_h_cost(self, end):
        self.h_cost = math.sqrt((self.x - end.x)**2 + (self.y - end.y)**2)

    # adding up the g cost and the h cost to create f cost
    def get_f_cost(self):
        self.f_cost = self.g_cost + self.h_cost

    # getting the g cost by adding the g cost of our parent and the distance between the parent and this block
    def get_g_cost(self):
        self.g_cost = self.parent.g_cost + 1

    # getting all costs at once
    def get_all_costs(self, end):
        self.get_h_cost(end)
        self.get_g_cost()
        self.get_f_cost()

    # checking if an enemy is on this block
    def if_occupied(self, enemies):
        if enemies is not None:
            for enemy in enemies:
                if enemy.x == self.grid_x and enemy.y == self.grid_y:
                    return True

    # getting neighbours of this block
    def get_neighbours(self, grid, enemies):
        # list of possible neighbours
        neighbours = []
        # checking for blocks in possible positions
        for new_position in self.possible_neighbour_pos:
            if 0 < self.grid_x + new_position[0] < play_width/block_size and\
                    0 < self.grid_y + new_position[1] < play_width/block_size:
                # adding each block on the possible neighbour positions to list of possible neighbours
                neighbours.append(grid[self.grid_x + new_position[0]][self.grid_y + new_position[1]])

        for neighbour in neighbours:
            # if the possible neighbour is not a wall and is not occupied
            if neighbour.color != colors["BLUE"] and not neighbour.if_occupied(enemies):
                # adding the neighbour the list of real neighbours
                self.neighbours.append(neighbour)

    # function used to reset all the costs and neighbours of a block
    def reset(self):
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
        self.neighbours = []
        self.parent = None

    # drawing function
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.pos)
