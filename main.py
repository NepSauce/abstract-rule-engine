from conways_game.conways_game_of_life import GameOfLife
from utils.json_reader import JsonReader

if __name__ == "__main__":
    rule_reader = JsonReader.read_json_file('rules_config.json')

    grid_height = rule_reader['height_rule']
    grid_width = rule_reader['width_rule']
    survival_min_rule = rule_reader['survival_min_rule']
    survival_max_rule = rule_reader['survival_max_rule']
    birth_rule = rule_reader['birth_rule']
    tick_rule = rule_reader['tick_rule']

    dimension_rule_arr = [grid_height, grid_width]
    survival_rule_arr = [survival_min_rule, survival_max_rule, birth_rule]
    game_rule_arr = [tick_rule]


    print(f'grid_height: {grid_height}, grid_width: {grid_width}')

    game = GameOfLife(dimension_rule_arr, survival_rule_arr)
    game.run(game_rule_arr);