
import pygame

class PygameGrid:
    def __init__(self, grid, resolution=(800, 800), line_width=3):
        self.grid = grid
        self.resolution = resolution
        self.line_width = line_width
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()

    def evaluate_dimensions(self):
        square_width = (self.resolution[0] / self.rows) - self.line_width * ((self.rows + 1) / self.rows)
        square_height = (self.resolution[1] / self.cols) - self.line_width * ((self.cols + 1) / self.cols)
        return (square_width, square_height)

    def convert_column_to_x(self, column, square_width):
        x = self.line_width * (column + 1) + square_width * column
        return x

    def convert_row_to_y(self, row, square_height):
        y = self.line_width * (row + 1) + square_height * row
        return y

    def draw_squares(self):
        square_width, square_height = self.evaluate_dimensions()
        for row in range(self.rows):
            for column in range(self.cols):
                color = (100, 100, 100)  # Default color, will update for alive/dead
                x = self.convert_column_to_x(column, square_width)
                y = self.convert_row_to_y(row, square_height)
                geometry = (x, y, square_width, square_height)
                pygame.draw.rect(self.screen, color, geometry)

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            self.draw_squares()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
