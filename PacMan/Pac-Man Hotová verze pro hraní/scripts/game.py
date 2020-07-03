import pygame
import sys
from scripts.grid import Grid
from scripts.settings import screen_size, font, colors


# class of our whole game
class Game:

    def __init__(self):

        # setting up the screen
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        # fake screen is used for the game over screen
        self.fake_screen = None
        # clock and its defined frame rate
        self.clock = pygame.time.Clock()
        self.fps = 80

        # Grid
        self.grid = Grid()
        # Pac-Man
        self.player = self.grid.get_player()
        # list of all enemies
        self.enemies = pygame.sprite.Group()
        self.grid.get_enemies(self.enemies, self.player)
        # list of food for our player
        self.foods = pygame.sprite.Group()
        self.grid.get_foods(self.foods)
        # list of all our sprites
        self.all_sprites = pygame.sprite.Group(self.foods, self.enemies, self.player)

        # if the game is running
        self.running = True
        # if the game has ended
        self.ended = False

        # used font
        self.font = font

    # function which will handle all of the events
    def event_handler(self):

        # allowing our user to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # movement controls
            if event.type == pygame.KEYDOWN:

                # says we want the Pac-Man to move right
                if event.key == pygame.K_RIGHT:
                    self.player.stored_direction = "right"

                # says we want the Pac-Man to move left
                if event.key == pygame.K_LEFT:
                    self.player.stored_direction = "left"

                # says we want the Pac-Man to move up
                if event.key == pygame.K_UP:
                    self.player.stored_direction = "up"

                # says we want the Pac-Man to move down
                if event.key == pygame.K_DOWN:
                    self.player.stored_direction = "down"

    # checking if the game has ended
    def check_for_end(self):
        # setting up the game over screen
        def game_over():
            # while the games has ended
            while self.ended:
                # handling events
                self.event_handler()
                # freezing the screen
                self.fake_screen.blit(self.screen, self.screen_size)
                # putting the label on the screen
                self.fake_screen.blit(label, (self.screen_size[0] / 2 - label.get_width() / 2,
                                              self.screen_size[1] / 2 - label.get_height() / 2))
                # updating the screen
                pygame.display.update()

        # checking if the game is lost
        for enemy in self.enemies:
            # checking if an enemy has collided with the player
            if pygame.sprite.collide_mask(enemy, self.player):

                self.ended = True
                self.running = False

                self.fake_screen = self.screen
                # the label used when you lose
                label = self.font.render("Oh no, You lost!", 0, colors["WHITE"])

                game_over()

        # checking if the game is won
        if len(self.foods) == 0:

            self.ended = True
            self.running = False

            self.fake_screen = self.screen
            # the label used when you win
            label = self.font.render("Congrats, you won!", 1, colors["WHITE"])

            game_over()

    # function drawing everything
    def draw_window(self):

        self.grid.draw_grid(self.screen)
        self.all_sprites.draw(self.screen)

        pygame.display.update()

    # function that is the actual game
    def run(self):

        # our game loop
        while self.running:

            # running the clock
            self.clock.tick(self.fps)

            # handling events
            self.event_handler()

            # updating sprites
            self.all_sprites.update()

            # updating the list of enemies for each enemy
            for enemy in self.enemies:
                enemy.enemies = self.enemies

            # checking if a food has been eaten
            for food in self.foods:
                food.get_eaten(self.player)

            # drawing everything
            self.draw_window()

            # checking for the end of the game
            self.check_for_end()
