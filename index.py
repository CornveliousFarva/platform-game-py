# Initial imports
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platform Game")

# Color, screen width, and player setup
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))
