from pygame import image, Surface
from homework_1 import load_tiles, get_tile_rect, SIZE
from homework_2 import create_maze

def parase_grid(data):
    """
    Parse the string representation into a nested list
    """
    return data.strip().split('\n')

def draw_grid(data, tile_img, tiles):
    """
    :return: an image of a tile-based grid
    """
    xs = len(data[0]) * SIZE
    ys = len(data) * SIZE
    img = Surface((xs, ys))
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            rect = get_tile_rect(x, y)
            img.blit(tile_img, rect, tiles[char])
    return img

if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    level = create_maze(12, 7)
    level = parase_grid(level)
    maze = draw_grid(level, tile_img, tiles)
    image.save(maze, 'maze.png')