from conways_game.env_manager import GridManager
from conways_game.cell_manager import CellManager
from conways_game.cell_manager import CellState

class GameOfLife:
    
    def __init__(self, rows, cols):
        self.grid_manager = GridManager(rows, cols)
