import pygame
from pygame import image, Rect, Surface

TILE_POSITIONS = [
    ('#', 0, 0),  # wall
    (' ', 0, 1),  # floor
    ('.', 2, 0),  # dot
    ('*', 3, 0),
]
SIZE = 32

images = 'explo.xpm'

def get_tile_rect(x, y):
    return Rect(x * SIZE, y * SIZE, SIZE, SIZE)


def load_tiles():
    '''
    # Load tiles from an image file into a dictionary
    # :return: a tuple of (image, tile_dict)
    '''
    tiles = {}
    tile_img = image.load('tiles.xpm')
    for symbol, x, y in TILE_POSITIONS:
        tiles[symbol] = get_tile_rect(x, y)
    return tile_img, tiles


if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    m = Surface((128, 32))
    m.blit(tile_img, get_tile_rect(0, 0), tiles['#'])
    m.blit(tile_img, get_tile_rect(1, 0), tiles[' '])
    m.blit(tile_img, get_tile_rect(2, 0), tiles['*'])
    m.blit(tile_img, get_tile_rect(3, 0), tiles['.'])

    image.save(m, 'tile_combo.png')

# ------------------------------
# Optional exercise


class Tile:
    def __init__(self, achar, x, y):
        self.char = achar


t = Tile('#', 0, 0)
print(t.char)
