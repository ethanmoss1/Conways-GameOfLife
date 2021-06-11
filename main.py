import pygame

from random import randint
from cell import Cell


class Life():
    def __init__(self, screen, size):
        self.grid = []
        self.screen = pygame.display.set_mode(screen)
        self.size = size

        self.tiles_to_check = set()
        self.new_tiles = []
        self.alive = set()
        self.dead = []

        self.build_grid(self.screen.get_width() // self.size)

        self.grid_size = len(self.grid)
        self.nearest_neighbour_list = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0), (-1, 1),
            (0, 1), (1, 1)
        ]
        self.nearest_neighbour_list00 = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (0, 0), (1, 0), (-1, 1),
            (0, 1), (1, 1)
        ]

    def build_grid(self, tile_size):
        for y in range(tile_size):
            self.grid.append([])
            for x in range(tile_size):
                pos = (x, y)
                cell = Cell(pos, self.size)
                self.grid[y].append(cell)

    def update_tilev2(self):
        self.get_tiles_to_check()
        self.find_neighbours()

        self.screen.fill((0, 0, 0))
        for tile in self.alive:
            tile.state = True
            tile.draw(self.screen)

        for tile in self.dead:
            tile.state = False

        self.tiles_to_check.clear()
        self.dead.clear()

    def get_tiles_to_check(self):
        for tile in self.alive:
            for dx, dy in self.nearest_neighbour_list00:
                pos_x = tile.pos_x + dx
                pos_y = tile.pos_y + dy
                if self.inside_grid(pos_y, pos_x):
                    current_tile = self.grid[pos_y][pos_x]
                else:
                    continue
                if current_tile not in self.tiles_to_check:
                    self.tiles_to_check.add(current_tile)
        self.alive.clear()

    def check_tiles(self, tile, neighbours):
        if tile.state and (neighbours < 2 or neighbours > 3) and (tile not in self.alive):
            self.dead.append(tile)
        elif tile.state == False and neighbours == 3 and (tile not in self.dead):
            self.alive.add(tile)
        elif tile.state and (neighbours == 2 or neighbours == 3):
            self.alive.add(tile)

    def find_neighbours(self):
        for tile in self.tiles_to_check:
            neighbours = 0
            for dx, dy in self.nearest_neighbour_list:
                # if self.inside_grid(tile.pos_y + dy, tile.pos_x + dx):
                try:
                    if self.grid[tile.pos_y + dy][tile.pos_x + dx].state:
                        neighbours += 1
                except IndexError:
                    continue
            self.check_tiles(tile, neighbours)

    def build_obj(self, pos, obj=None):
        if obj == None:
            obj = [
                [0, 0, 1],
                [1, 0, 1],
                [0, 1, 1]
            ]
        dx = pos[0]
        dy = pos[1]
        for y in range(len(obj)):
            for x in range(len(obj[y])):
                if bool(obj[y][x]):
                    try:
                        tile = self.grid[dy + y][dx + x]
                    except IndexError:
                        continue
                    tile.state = True
                    self.alive.add(tile)

    def inside_grid(self, y, x):
        if (0 < x < (self.grid_size - 1)) and \
                (0 < y < (self.grid_size - 1)):
            return True
        return False

    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                grid_pos_of_mouse = list(
                    pygame.mouse.get_pos())  # // game.tile_size
                grid_pos_of_mouse[0] = grid_pos_of_mouse[0] // game.size
                grid_pos_of_mouse[1] = grid_pos_of_mouse[1] // game.size
                self.build_obj(grid_pos_of_mouse, cannon)
        return True


if __name__ == '__main__':

    game = Life((800, 800), 10)
    print(game.grid_size)
    cannon = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
            0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0,
            0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    clock = pygame.time.Clock()

    FPS = 120
    run = True
    game.build_obj([1, 1], cannon)
    while run:
        # clock.tick(FPS)
        run = game.update_events()
        game.update_tilev2()
        pygame.display.update()
    pygame.quit()
