import pygame
import os


# Pac-man image
player_images = [pygame.image.load(os.path.join("images", "pacman1.png")),
                 pygame.image.load(os.path.join("images", "pacman2.png")),
                 pygame.image.load(os.path.join("images", "pacman3.png")),
                 pygame.image.load(os.path.join("images", "pacman4.png"))]

# Ghost images
ghost_images = [pygame.image.load(os.path.join("images", "Enemy1.png")),
                pygame.image.load(os.path.join("images", "Enemy2.png")),
                pygame.image.load(os.path.join("images", "Enemy3.png")),
                pygame.image.load(os.path.join("images", "Enemy4.png"))]

# Food img
food_img = pygame.image.load(os.path.join("images", "food.png"))

# used font
pygame.font.init()
font = pygame.font.Font(os.path.join("fonts", "straighttext.ttf"), 84)

# screen parameters
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)

# game parameters
play_width = 600
play_height = 600

# game X and Y
play_x = (screen_width - play_width) / 2
play_y = screen_height - play_height

# dictionary containing all used colors
colors = {"BLACK": (0, 0, 0),
          "BLUE": (0, 0, 255),
          "WHITE": (255, 255, 255)}

# 0 represents a wall
# 1 represents the player
# 2 represents an empty space
# 3 represents an enemy
# . represents food
maze = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "0", "0", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "0"],
        ["0", ".", "0", "0", "0", "0", ".", "0", "0", "0", "0", ".", "0", ".", "0", "0", ".", "0", ".", "0", "0", "0", "0", ".", "0", "0", "0", "0", ".", "0"],
        ["0", ".", "0", "2", "2", "0", ".", "0", "2", "2", "0", ".", "0", ".", "0", "0", ".", "0", ".", "0", "2", "2", "0", ".", "0", "2", "2", "0", ".", "0"],
        ["0", ".", "0", "2", "2", "0", ".", "0", "2", "2", "0", ".", ".", ".", ".", ".", ".", ".", ".", "0", "2", "2", "0", ".", "0", "2", "2", "0", ".", "0"],
        ["0", ".", "0", "0", "0", "0", ".", "0", "0", "0", "0", ".", "0", "0", "0", "0", "0", "0", ".", "0", "0", "0", "0", ".", "0", "0", "0", "0", ".", "0"],
        ["0", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "0"],
        ["0", "0", "0", ".", "0", ".", "0", "0", "0", ".", "0", ".", "0", ".", "0", "0", ".", "0", ".", "0", ".", "0", "0", "0", ".", "0", ".", "0", "0", "0"],
        ["0", "2", "0", ".", "0", ".", ".", ".", ".", ".", "0", ".", "0", ".", "0", "0", ".", "0", ".", "0", ".", ".", ".", ".", ".", "0", ".", "0", "2", "0"],
        ["0", "2", "0", ".", "0", "0", "0", "0", "0", ".", "0", ".", "0", ".", ".", ".", ".", "0", ".", "0", ".", "0", "0", "0", "0", "0", ".", "0", "2", "0"],
        ["0", "2", "0", ".", "0", ".", ".", ".", ".", ".", "0", ".", "0", ".", "0", "0", ".", "0", ".", "0", ".", ".", ".", ".", ".", "0", ".", "0", "2", "0"],
        ["0", "0", "0", ".", "0", ".", "0", "0", "0", ".", "0", ".", "0", ".", "0", "0", ".", "0", ".", "0", ".", "0", "0", "0", ".", "0", ".", "0", "0", "0"],
        ["0", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "0"],
        ["0", "0", "0", "0", "0", ".", "0", ".", "0", ".", "0", "0", "0", "0", "2", "2", "0", "0", "0", "0", ".", "0", ".", "0", ".", "0", "0", "0", "0", "0"],
        ["0", "2", "2", "2", "0", ".", "0", ".", "0", ".", "0", "2", "2", "2", "2", "2", "2", "2", "2", "0", ".", "0", ".", "0", ".", "0", "2", "2", "2", "0"],
        ["0", "2", "2", "2", "0", ".", "0", ".", "0", ".", "0", "2", "3", "2", "2", "2", "2", "3", "2", "0", ".", "0", ".", "0", ".", "0", "2", "2", "2", "0"],
        ["0", "2", "2", "2", "0", ".", ".", ".", ".", ".", "0", "2", "2", "2", "2", "2", "2", "2", "2", "0", ".", ".", ".", ".", ".", "0", "2", "2", "2", "0"],
        ["0", "2", "2", "2", "0", ".", "0", ".", "0", ".", "0", "2", "3", "2", "2", "2", "2", "3", "2", "0", ".", "0", ".", "0", ".", "0", "2", "2", "2", "0"],
        ["0", "2", "2", "2", "0", ".", "0", ".", "0", ".", "0", "2", "2", "2", "2", "2", "2", "2", "2", "0", ".", "0", ".", "0", ".", "0", "2", "2", "2", "0"],
        ["0", "0", "0", "0", "0", ".", "0", ".", "0", ".", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", ".", "0", ".", "0", ".", "0", "0", "0", "0", "0"],
        ["0", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "0"],
        ["0", ".", "0", "0", "0", ".", "0", "0", "0", ".", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", ".", "0", "0", "0", ".", "0", "0", "0", ".", "0"],
        ["0", ".", ".", ".", "0", ".", ".", ".", ".", ".", ".", ".", ".", ".", "0", "0", ".", ".", ".", ".", ".", ".", ".", ".", ".", "0", ".", ".", ".", "0"],
        ["0", "0", "0", ".", "0", ".", "0", ".", "0", "0", ".", "0", "0", ".", "0", "0", ".", "0", "0", ".", "0", "0", ".", "0", ".", "0", ".", "0", "0", "0"],
        ["0", "0", "0", ".", "0", ".", "0", ".", "0", "0", ".", "0", "0", ".", ".", "1", ".", "0", "0", ".", "0", "0", ".", "0", ".", "0", ".", "0", "0", "0"],
        ["0", "0", "0", ".", "0", ".", "0", ".", "0", "0", ".", "0", "0", ".", "0", "0", ".", "0", "0", ".", "0", "0", ".", "0", ".", "0", ".", "0", "0", "0"],
        ["0", ".", ".", ".", ".", ".", "0", ".", "0", "0", ".", ".", ".", ".", "0", "0", ".", ".", ".", ".", "0", "0", ".", "0", ".", ".", ".", ".", ".", "0"],
        ["0", ".", "0", "0", "0", "0", "0", ".", "0", "0", ".", "0", "0", "0", "0", "0", "0", "0", "0", ".", "0", "0", ".", "0", "0", "0", "0", "0", ".", "0"],
        ["0", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

# size of one block in our grid
block_size = screen_height / len(maze)
