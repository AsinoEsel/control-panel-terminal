import pygame as pg
import os
from gui.media import load_file_stream
pg.font.init()  # TODO: Fix console clutter coming from here
pg.display.init()

RUNNING_ON_LINUX = (os.name == 'posix')

RENDER_SIZE = (960, 540)
RENDER_WIDTH, RENDER_HEIGHT = RENDER_SIZE
QUARTER_RENDER_SIZE = (RENDER_WIDTH//2, RENDER_HEIGHT//2)
TARGET_FRAME_RATE = 30

BACKGROUND_COLOR = pg.Color((5, 10, 5))
COLOR_INACTIVE = pg.Color((0, 128, 0))
COLOR_ACTIVE = pg.Color((0,255,0))
ACCENT_COLOR_INACTIVE = pg.Color((0,32,0))
ACCENT_COLOR_ACTIVE = pg.Color((0, 64, 0))
DEBUG_COLOR = pg.Color((255,20,147))
DEBUG_LONG_TEXT = "What the dog doin. " * 10
FONT_PATH = "clacon2.ttf"
DEFAULT_FONT = pg.font.Font(load_file_stream(FONT_PATH), 20)
SMALL_FONT = pg.font.Font(load_file_stream(FONT_PATH), 12)

CHAR_WIDTH = {
    DEFAULT_FONT: DEFAULT_FONT.render("|", False, (0, 0, 0)).get_width()
}

CHAR_HEIGHT = {
    DEFAULT_FONT: DEFAULT_FONT.render("Ög", False, (0, 0, 0)).get_height()
}

DEFAULT_GAP = 6
LINE_THICKNESS_THIN = 1
LINE_THICKNESS_THICK = 2
