import pygame
from game import Game #import Game class from game file

pygame.init()

game = Game()
game.run_game_loop()

pygame.quit()
quit()