from conways_game.cell_manager import CellState 

class EnvManager: 
    def __init__(self, rows, cols):
        self.grid = [[CellState.DEAD for _ in range(cols)] for _ in range(rows)]
    
    def set_cell(self, row_index, col_index, state):
        self.grid[row_index][col_index] = state

    def update_grid(self, height_rule, width_rule):
        # Placeholder for the logic to update the grid based on the rules
        pass

