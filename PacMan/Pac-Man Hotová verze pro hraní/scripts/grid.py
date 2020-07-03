from scripts.settings import maze, colors
from scripts.food import Food
from scripts.player import Player
from scripts.block import Block
from scripts.enemy import Enemy


# class representing our grid(playing space)
class Grid:

    def __init__(self):
        # our maze
        self.maze = maze
        # creating a grid using list comprehension
        self.grid = [[Block(colors["BLACK"], i, j)
                      for j in range(len(self.maze))] for i in range(len(self.maze))]
        # get location of walls in our grid
        self.get_walls()

    # function used to get the position of the walls
    def get_walls(self):
        # determines where the walls are and coloring them to blue
        for i, row in enumerate(self.maze):
            for j, col in enumerate(row):
                if col == "0":
                    self.grid[j][i].color = colors["BLUE"]

    # function used to get the position of the food
    def get_foods(self, foods):
        # determines where is the food and adding it to its sprite group
        for i, row in enumerate(self.maze):
            for j, col in enumerate(row):
                if col == ".":
                    foods.add(Food(j, i))

    # function used to get the position of the player
    def get_player(self):
        # determines where is the player and returning it
        player = None
        for i, row in enumerate(self.maze):
            for j, col in enumerate(row):
                if col == "1":
                    player = Player(j, i)

        return player

    #  function used to get the position of the enemies
    def get_enemies(self, enemies, player):
        # determines where are the enemies and adding them to their sprite group
        for i, row in enumerate(self.maze):
            for j, col in enumerate(row):
                if col == "3":
                    enemies.add(Enemy(j, i, self.grid, player, len(enemies)))

    # function used to draw our grid
    def draw_grid(self, surface):

        for row in self.grid:
            for block in row:
                block.draw(surface)
