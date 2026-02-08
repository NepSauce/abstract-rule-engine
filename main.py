# Entry point for Game of Life engine
import pygame
from engine.grid import Grid

def main():
    from engine.rules import RuleConfig, Rule
    rule_config = RuleConfig()
    # ...existing code...
    def eat_dead_condition(cell, neighbors):
        # Dead cell (state 0) is absorbed if any live neighbor is present
        if cell.state == 0:
            live_neighbors = [n.state for n in neighbors if n.state > 0]
            if live_neighbors:
                return True
        return False
    def eat_dead_action(cell, neighbors):
        live_neighbors = [n.state for n in neighbors if n.state > 0]
        if live_neighbors:
            return max(set(live_neighbors), key=live_neighbors.count)
        return 0
    rule_config.add_rule(Rule(eat_dead_condition, eat_dead_action))
    # ...existing code...
    pygame.init()
    width, height = 80, 50
    num_states = 5  # Multiple entity types/colors
    import random
    grid = Grid(width, height, num_states)
    # Seed grid with mostly empty cells
    for y in range(height):
        for x in range(width):
            grid.set_state(x, y, 0)
    # Seed clusters of random states (entities)
    for _ in range(20):  # 20 clusters
        cx = random.randint(2, width - 3)
        cy = random.randint(2, height - 3)
        entity_state = random.randint(1, num_states - 1)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if random.random() < 0.7:  # 70% chance to fill
                    grid.set_state(cx + dx, cy + dy, entity_state)

    from engine.visualizer import Visualizer
    from engine.rules import RuleConfig, Rule

    visualizer = Visualizer(grid, cell_size=10)
    rule_config = RuleConfig()

    # Game of Life-like birth: only if exactly 3 neighbors of same type
    def birth_condition(cell, neighbors):
        if cell.state == 0:
            for s in range(1, num_states):
                if sum(n.state == s for n in neighbors) == 3:
                    return True
        return False
    def birth_action(cell, neighbors):
        # Born as the most common neighbor type
        neighbor_states = [n.state for n in neighbors if n.state > 0]
        if neighbor_states:
            return max(set(neighbor_states), key=neighbor_states.count)
        return 0
    rule_config.add_rule(Rule(birth_condition, birth_action))

    # Survival: only if 2 or 3 neighbors of same type (flocking)
    def survive_condition(cell, neighbors):
        if cell.state > 0:
            return sum(n.state == cell.state for n in neighbors) in [2, 3]
        return False
    def survive_action(cell, neighbors):
        return cell.state
    rule_config.add_rule(Rule(survive_condition, survive_action))

    # Removed death rule: dead cells are only absorbed through eating

    # Absorption: if a cell is surrounded by more neighbors of a different type, it gets absorbed
    def absorb_condition(cell, neighbors):
        if cell.state > 0:
            neighbor_states = [n.state for n in neighbors if n.state > 0 and n.state != cell.state]
            if neighbor_states:
                # If more neighbors are of a different type than own type, absorb
                most_common = max(set(neighbor_states), key=neighbor_states.count)
                if neighbor_states.count(most_common) > sum(n.state == cell.state for n in neighbors):
                    return True
        return False
    def absorb_action(cell, neighbors):
        neighbor_states = [n.state for n in neighbors if n.state > 0 and n.state != cell.state]
        if neighbor_states:
            # Become the most common adjacent type
            return max(set(neighbor_states), key=neighbor_states.count)
        return cell.state
    rule_config.add_rule(Rule(absorb_condition, absorb_action))
    
    pygame.init()
    width, height = 80, 50
    num_states = 5  # Multiple entity types/colors
    import random
    grid = Grid(width, height, num_states)
    # Seed grid with mostly empty cells
    for y in range(height):
        for x in range(width):
            grid.set_state(x, y, 0)
    # Seed clusters of random states (entities)
    for _ in range(20):  # 20 clusters
        cx = random.randint(2, width - 3)
        cy = random.randint(2, height - 3)
        entity_state = random.randint(1, num_states - 1)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if random.random() < 0.7:  # 70% chance to fill
                    grid.set_state(cx + dx, cy + dy, entity_state)

    from engine.visualizer import Visualizer
    from engine.rules import RuleConfig, Rule

    visualizer = Visualizer(grid, cell_size=10)
    rule_config = RuleConfig()

    # Classic Game of Life rules for continual movement
    # Game of Life-like birth: only if exactly 3 neighbors of same type
    def birth_condition(cell, neighbors):
        if cell.state == 0:
            for s in range(1, num_states):
                if sum(n.state == s for n in neighbors) == 3:
                    return True
        return False
    def birth_action(cell, neighbors):
        # Born as the most common neighbor type
        neighbor_states = [n.state for n in neighbors if n.state > 0]
        if neighbor_states:
            return max(set(neighbor_states), key=neighbor_states.count)
        return 0
    rule_config.add_rule(Rule(birth_condition, birth_action))

    # Survival: only if 2 or 3 neighbors of same type (flocking)
    def survive_condition(cell, neighbors):
        if cell.state > 0:
            return sum(n.state == cell.state for n in neighbors) in [2, 3]
        return False
    def survive_action(cell, neighbors):
        return cell.state
    rule_config.add_rule(Rule(survive_condition, survive_action))

    # Death: if not enough flocking neighbors
    def die_condition(cell, neighbors):
        if cell.state > 0:
            return sum(n.state == cell.state for n in neighbors) not in [2, 3]
        return False
    def die_action(cell, neighbors):
        return 0
    rule_config.add_rule(Rule(die_condition, die_action))

    # Removed redundant death rule; classic rules already handle cell death

    running = True
    paused = False
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    # Reset grid with new random states
                    grid = Grid(width, height, num_states)
                    for y in range(height):
                        for x in range(width):
                            grid.set_state(x, y, random.randint(0, num_states - 1))
                    visualizer = Visualizer(grid, cell_size=10)
        if not paused:
            rule_config.apply_rules(grid)
        visualizer.draw()
        clock.tick(3)  # Slower simulation for organic movement

if __name__ == "__main__":
    main()
