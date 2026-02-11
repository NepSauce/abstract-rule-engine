class GridManager: 
    def __init__(self, rows, cols):
        self.grid = [[CellState.DEAD for _ in range(cols)] for _ in range(rows)]
    
    def set_cell(self, row_index, col_index, state):
        self.grid[row_index][col_index] = state

class CellManager:
    def __init__(self):
        pass

    # Moore-neighborhood counting algorithm
    def count_live_neighbors(self, grid, row_index, col_index):
        live_neightbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0):
                    continue
                
                neighbor_row = row_index + i
                neighbor_col = col_index + j

                if (0 <= neighbor_row < len(grid) and
                    0 <= neighbor_col < len(grid[0]) and
                    grid[neighbor_row][neighbor_col]):
                    live_neightbors += 1

        return live_neightbors
    
    def determine_next_state(self, cell_coords, survival_min, survival_max, birth_neighbors):
        row_index, col_index = cell_coords
        current_state = self.grid[row_index][col_index]
        live_neighbors = self.count_live_neighbors(self.grid, row_index, col_index)

        if current_state == CellState.ALIVE:
            if live_neighbors < survival_min or live_neighbors > survival_max:
                return CellState.DEAD
            else:
                return CellState.ALIVE
        else:
            if live_neighbors in birth_neighbors:
                return CellState.ALIVE
            else:
                return CellState.DEAD

    
class CellState:
    ALIVE = True
    DEAD = False