from conways_game.env_manager import EnvManager
from conways_game.pygame_module.pygame_grid import PygameGrid

class GameOfLife:
    
    def __init__(self, rows, cols):
        self.env_manager = EnvManager(rows, cols)
        self.pygame_grid = PygameGrid(self.env_manager.grid)

    def run(self):
        self.pygame_grid.run()

    def update(self):
        # Placeholder for the logic to update the grid based on the rules of the game
        pass

    def render(self):
        # Placeholder for the logic to render the grid using Pygame
        pass

    def pause(self):
        # Placeholder for the logic to pause the game
        pass
