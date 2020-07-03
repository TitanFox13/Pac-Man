import pygame
from scripts.settings import block_size, play_x, food_img


# sprite class of our food
class Food(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        # x and y of the food based on the grid
        self.x = x
        self.y = y
        # image of the food
        self.image = food_img
        # getting rect
        self.rect = self.image.get_rect()
        self.rect.x = self.x * block_size + play_x
        self.rect.y = self.y * block_size

    # checks if the food should be eaten
    def get_eaten(self, player):
        # if the Xs and Ys match then the food will be removed from the food group
        if player.rect.x == self.rect.x and player.rect.y == self.rect.y:
            self.kill()
