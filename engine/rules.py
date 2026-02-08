# Placeholder for rule configuration and GUI
# Will be implemented with Pygame for user interaction

class RuleConfig:
    def __init__(self):
        self.rules = []  # List of Rule objects

    def add_rule(self, rule):
        self.rules.append(rule)

    def edit_rule(self, index, new_rule):
        if 0 <= index < len(self.rules):
            self.rules[index] = new_rule

    def delete_rule(self, index):
        if 0 <= index < len(self.rules):
            del self.rules[index]

    def load_from_file(self, path):
        import json
        with open(path, 'r') as f:
            data = json.load(f)
            self.rules = [Rule.from_dict(rd) for rd in data]

    def save_to_file(self, path):
        import json
        with open(path, 'w') as f:
            json.dump([rule.to_dict() for rule in self.rules], f, indent=2)

    def apply_rules(self, grid):
        # Apply all rules to the grid for one simulation step
        new_states = [[cell.state for cell in row] for row in grid.cells]
        for y in range(grid.height):
            for x in range(grid.width):
                cell = grid.cells[y][x]
                neighbors = grid.get_neighbors(x, y)
                for rule in self.rules:
                    if rule.matches(cell, neighbors):
                        new_states[y][x] = rule.action(cell, neighbors)
                        break
        for y in range(grid.height):
            for x in range(grid.width):
                grid.set_state(x, y, new_states[y][x])

# Rule abstraction
class Rule:
    def __init__(self, condition, action):
        self.condition = condition  # Function or dict describing when rule applies
        self.action = action        # Function or dict describing state change

    def matches(self, cell, neighbors):
        # Example: condition is a function
        if callable(self.condition):
            return self.condition(cell, neighbors)
        # Extend for dict-based conditions
        return False

    def action(self, cell, neighbors):
        # Example: action is a function
        if callable(self.action):
            return self.action(cell, neighbors)
        # Extend for dict-based actions
        return cell.state

    def to_dict(self):
        # Serialize rule for saving
        return {
            'condition': 'function',  # Placeholder
            'action': 'function'      # Placeholder
        }

    @staticmethod
    def from_dict(data):
        # Deserialize rule from dict
        return Rule(lambda c, n: False, lambda c, n: c.state)  # Placeholder
