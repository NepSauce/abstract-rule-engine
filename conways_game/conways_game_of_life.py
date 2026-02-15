from conways_game.env_manager import EnvManager
from conways_game.pygame_module.pygame_grid import PygameGrid

class GameOfLife:
    def __init__(self, dimension_rule_arr, survival_rule_arr):
        self.env_manager = EnvManager(dimension_rule_arr, survival_rule_arr)
        self.pygame_grid = PygameGrid(self.env_manager.grid)
        self.dimension_rule_arr = dimension_rule_arr
        self.survival_rule_arr = survival_rule_arr
        self.isPaused = False

    def run(self, game_rule_arr):
        self.pygame_grid.run()

        while not self.isPaused:
            self.update()
            self.render()

    def update(self):
        self.env_manager.update_grid()

    def render(self):
        self.pygame_grid.draw_squares()


    def pause(self):
        self.isPaused = True
        self.pygame_grid.pause()