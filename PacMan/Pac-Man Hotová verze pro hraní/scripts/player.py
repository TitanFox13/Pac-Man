import pygame
from scripts.settings import maze, block_size, play_x, player_images


# sprite class of our player(Pac-Man)
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        # the x and y based on the grid
        self.x = x
        self.y = y

        # list of all the images the pac-man can be
        self.images = player_images
        # the actual used image
        self.image = player_images[0]

        # time the image has been shown for
        self.animation_time = 0
        # time the image can be shown for
        self.animation_limit = 7
        # the order the images are shown at, can be either 1 or -1
        self.animation_order = 1
        # index of the used image
        self.image_index = 0
        # rotation of the image
        self.image_rotation = 0

        # player rect
        self.rect = self.image.get_rect()
        self.rect.x = self.x * block_size + play_x
        self.rect.y = self.y * block_size

        # direction our player is facing
        self.direction = "left"
        # direction we want our player to be facing
        self.stored_direction = "left"

        # velocity
        self.vel = 2

        # constant of the direction the player is moving to can be 1, 0, -1
        # vertical
        self.kv = 0
        # horizontal
        self.kh = 0

        # constant of the direction we want the player to be moving to, can be 1, 0, -1
        # vertical
        self.skv = 0
        # horizontal
        self.skh = 0

    # checking if the player can move to a certain position
    def valid_space(self, v, h):
        # checking if the player is completely on a block and the block we want to move to is not a wall
        if (self.rect.x % block_size == 0 and v == 0) or (self.rect.y % block_size == 0 and h == 0):
            if self.rect.x % block_size == 0 and self.rect.y % block_size == 0:
                if maze[int(self.y + v)][int(self.x + h)] != "0":
                    return True
                else:
                    return False
        else:
            return True

    # moving the player
    def move(self):

        # actually moving the player
        def moving_player(v, h):

            # if the player is completely on a block then it can be moved
            if self.rect.x % block_size == 0:
                self.rect.y += self.vel * v
                if self.rect.y % block_size == 0:
                    self.y = self.rect.y // block_size

            if self.rect.y % block_size == 0:
                self.rect.x += self.vel * h
                if self.rect.x % block_size == 0:
                    self.x = (self.rect.x - play_x) // block_size

        # checking for valid space of stored direction
        if self.valid_space(self.skv, self.skh):
            # moving the player in the direction of stored direction
            moving_player(self.skv, self.skh)
            # setting the direction to stored direction
            self.direction = self.stored_direction
        # if stored direction is not valid
        else:
            # checking for valid space of direction
            if self.valid_space(self.kv, self.kh):
                # moving the player in the direction
                moving_player(self.kv, self.kh)

    # setting up all constants correctly
    def get_k(self):
        # setting up constants of direction
        if self.direction == "right":
            self.kh = 1
            self.kv = 0
            self.image_rotation = 0
        elif self.direction == "left":
            self.kh = -1
            self.kv = 0
            self.image_rotation = 180
        elif self.direction == "up":
            self.kh = 0
            self.kv = -1
            self.image_rotation = 90
        elif self.direction == "down":
            self.kh = 0
            self.kv = 1
            self.image_rotation = 270

        # setting up constants of stored direction
        if self.stored_direction == "right":
            self.skh = 1
            self.skv = 0
        elif self.stored_direction == "left":
            self.skh = -1
            self.skv = 0
        elif self.stored_direction == "up":
            self.skh = 0
            self.skv = -1
        elif self.stored_direction == "down":
            self.skh = 0
            self.skv = 1

    # getting the image that should be used
    def get_img(self):
        # adding 1 to the animation time
        self.animation_time += 1
        # if the image has been animated for a certain amount of time then
        if self.animation_time == self.animation_limit:
            # reset the timer
            self.animation_time = 0
            # setting up correctly the order of animating images
            if self.image_index == len(self.images) - 1:
                # backwards
                self.animation_order = -1
            elif self.image_index == 0:
                # frontwards
                self.animation_order = 1
            # changing the image
            self.image_index += self.animation_order

        # changing the image
        self.image = self.images[self.image_index]
        # rotating the image
        self.image = pygame.transform.rotate(self.image, self.image_rotation)

    # updating the player
    def update(self):
        self.get_k()
        self.move()
        self.get_img()
