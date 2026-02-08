# Visualization and GUI setup for Game of Life engine
import pygame
from engine.grid import Grid
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Visualizer:
    def __init__(self, grid, cell_size=10):
        self.grid = grid
        self.cell_size = cell_size
        self.width = grid.width * cell_size
        self.height = grid.height * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                state = self.grid.get_state(x, y)
                color = self.get_color(state)
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color, rect)
        pygame.display.flip()

    def get_color(self, state):
        # Organic color gradient for states
        base_colors = [
            (30, 30, 30),   # Empty
            (0, 120, 255),  # Entity 1: Blue
            (0, 255, 120),  # Entity 2: Green
            (255, 200, 0),  # Entity 3: Yellow
            (255, 50, 50)   # Entity 4: Red
        ]
        if state < len(base_colors):
            return base_colors[state]
        # Interpolate for extra states
        return tuple(min(255, int(30 + state * 40)) for _ in range(3))
