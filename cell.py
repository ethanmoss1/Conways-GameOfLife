import pygame


class Cell():
    def __init__(self, pos, size):
        self.pos = self.pos_x, self.pos_y = pos
        self.size = size

        self.rect = pygame.Rect(0, 0, size, size)
        self.rect.x = self.pos_x * size
        self.rect.y = self.pos_y * size

        self.state = False

        self.nearest_neighbour_list = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0), (-1, 1),
            (0, 1), (1, 1)
        ]

    def __str__(self):
        return f'Cell Object - pos:{self.pos}'

    def draw(self, screen):
        if self.state:
            pygame.draw.rect(screen, (255,255,255), self.rect)
        # print(self.rect)

   
