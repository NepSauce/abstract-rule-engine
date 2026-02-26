<p align="center">
  <img src="game.gif" alt="Demo GIF" style="width:100%;max-width:1000px;display:block;margin:auto;" />
</p>

# Conway's Rule Engine

**Small rules. Big consequences.**

## Overview

Conway's Rule Engine is a flexible and extensible framework for simulating Conway's Game of Life and other rule-based cellular automata. Built with Python and Pygame, it provides a visual simulation environment with highly customizable rules, initial patterns, and dynamic spawning behaviors.

## Features

- **Configurable Conway's Game of Life simulation** with customizable survival and birth rules
- **Pygame-based visualization** with real-time rendering
- **Flexible initial pattern generation** from any edge (top, bottom, left, right)
- **Continuous cell spawning** for dynamic, flowing animations
- **JSON-based configuration** for easy rule and parameter modification
- **Modular architecture** for easy extension and customization

## Configuration

All simulation parameters are configured via `rules_config.json`:

### Game Rules
- `survival_min_rule`: Minimum neighbors for a live cell to survive (default: 2)
- `survival_max_rule`: Maximum neighbors for a live cell to survive (default: 3)
- `birth_rule`: Number of neighbors needed for a dead cell to become alive (default: 3)

### Grid & Performance
- `height_rule`: Grid height in cells
- `width_rule`: Grid width in cells
- `tick_rule`: Updates per second (higher = faster simulation)

### Initial Pattern
- `initial_spawn_direction`: Where to spawn initial cells ("top", "bottom", "left", "right")
- `initial_spawn_rows`: Number of rows/columns to fill with initial pattern
- `initial_alive_percentage`: Probability (0.0-1.0) that each cell in the spawn area starts alive

### Continuous Spawning
- `continuous_spawn_rate`: Probability (0.0-1.0) that new cells spawn each update
- `continuous_spawn_direction`: Edge to continuously spawn from ("top", "bottom", "left", "right", "none")

## Project Structure

- `conways_game/`: Core Conway's Game of Life implementation
  - `cell_manager.py`: Cell state logic and neighbor counting
  - `env_manager.py`: Grid management and update logic
  - `conways_game_of_life.py`: Main game loop and rendering coordination
  - `pygame_module/`: Pygame visualization components
- `utils/`: Utility modules (JSON reader, timing)
- `rules_config.json`: Configuration file for all simulation parameters
- `main.py`: Entry point for running the simulation

## Getting Started

1. Clone the repository
2. Install Python 3.x
3. Install dependencies:
   ```bash
   pip install pygame
   ```
4. Configure your simulation in `rules_config.json`
5. Run the simulation:
   ```bash
   python main.py
   ```

## Example Configurations

### Classic Conway's Game of Life
```json
    "survival_min_rule": 2,
    "survival_max_rule": 3,
    "birth_rule": 3,
    "continuous_spawn_rate": 0.0,
    "continuous_spawn_direction": "none"
}
```

### Flowing Animation (Google-style)
```json
{
    "survival_min_rule": 2,
    "survival_max_rule": 3,
    "birth_rule": 3,
    "continuous_spawn_rate": 0.3,
    "continuous_spawn_direction": "bottom",
    "initial_spawn_direction": "bottom",
    "initial_spawn_rows": 10
}
```

## Controls

- Close the window to exit the simulation

## Future Extensions

The modular architecture allows for:
- Custom rule engines beyond Conway's Game of Life
- User-defined cellular automata rules
- Interactive cell placement and editing
- Pattern saving and loading

