from conways_game.env_manager import CellState

class GridManager: 
    def __init__(self, rows, cols):
        self.grid = [[CellState.DEAD for _ in range(cols)] for _ in range(rows)]
    
    def set_cell(self, row_index, col_index, state):
        self.grid[row_index][col_index] = state
