from conways_game.conways_game_of_life import GameOfLife
from utils.json_reader import JsonReader

if __name__ == "__main__":
    rule_reader = JsonReader.read_json_file('rules_config.json')

    grid_height = rule_reader['height_rule']
    grid_width = rule_reader['width_rule']

    print(f'grid_height: {grid_height}, grid_width: {grid_width}')

    game = GameOfLife(grid_height, grid_width)