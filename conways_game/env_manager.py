from conways_game.cell_manager import CellState 
from conways_game.cell_manager import CellManager

class EnvManager: 
    def __init__(self, dimension_rule_arr, survival_rule_arr):
        self.cell_manager = CellManager(dimension_rule_arr, survival_rule_arr)
        self.dimension_rule_arr = dimension_rule_arr
        self.survival_rule_arr = survival_rule_arr
        self.grid = [[CellState.DEAD for _ in range(dimension_rule_arr[1])] 
                     for _ in range(dimension_rule_arr[0])]

    def update_grid(self):
        # Placeholder for the logic to update the grid based on the rules
        pass

