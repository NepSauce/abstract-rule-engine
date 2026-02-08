# Grid and Cell classes for Game of Life engine
class Cell:
    def __init__(self, state=0):
        self.state = state

class Grid:
    def __init__(self, width, height, num_states=2):
        self.width = width
        self.height = height
        self.num_states = num_states
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]

    def get_neighbors(self, x, y):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    neighbors.append(self.cells[ny][nx])
        return neighbors

    def set_state(self, x, y, state):
        self.cells[y][x].state = state

    def get_state(self, x, y):
        return self.cells[y][x].state
