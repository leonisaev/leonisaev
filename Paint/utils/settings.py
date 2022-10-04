import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)
CAYAN = (0, 255, 255)
PURPLE = (255, 0, 255)

FPS = 2000000

WIDTH, HEIGHT = 610, 710

ROWS = COLS = 10

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = False


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
