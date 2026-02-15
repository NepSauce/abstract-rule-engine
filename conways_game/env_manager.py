from conways_game.cell_manager import CellState 

class EnvManager: 
    def __init__(self, dimension_rule_arr, survival_rule_arr):
        self.dimension_rule_arr = dimension_rule_arr
        self.survival_rule_arr = survival_rule_arr
        self.grid = [[CellState.DEAD for _ in range(dimension_rule_arr[1])] for _ in range(dimension_rule_arr[0])]
    
    def set_cell(self, row_index, col_index, state):
        self.grid[row_index][col_index] = state

    def update_grid(self, dimension_rule_arr, survival_rule_arr):
        # Placeholder for the logic to update the grid based on the rules
        pass

