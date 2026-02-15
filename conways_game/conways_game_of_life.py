from conways_game.env_manager import EnvManager
from conways_game.cell_manager import CellManager
from conways_game.pygame_module.pygame_grid import PygameGrid

class GameOfLife:
    def __init__(self, dimension_rule_arr, survival_rule_arr):
        self.env_manager = EnvManager(dimension_rule_arr[0], dimension_rule_arr[1])
        self.pygame_grid = PygameGrid(self.env_manager.grid)
        self.height_rule = dimension_rule_arr[0]
        self.width_rule = dimension_rule_arr[1]
        self.survival_rule_arr = survival_rule_arr
        self.isPaused = False

    def run(self):
        self.pygame_grid.run()

        while not self.isPaused:
            self.update(self.survival_rule_arr)
            self.render()

    def update(self, survival_rule_arr):
        self.env_manager.update_grid(self.height_rule, self.width_rule)

    def render(self):
        self.pygame_grid.draw_squares()


    def pause(self):
        self.isPaused = True
        self.pygame_grid.pause()