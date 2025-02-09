# Battleship Game Simulator

## Overview
This project is a Battleship Game Simulator implemented in Python. It allows multiple players to battle each other using a grid-based battlefield. Each player can place ships on their battle area and take turns firing missiles at the opponent’s ships until one player emerges victorious or the game ends in a draw.

## Features
- Multi-player battleship game simulation with a graphical interface.
- Configurable battle area and ship placements.
- Circular turn-based gameplay with firing sequences.
- Comprehensive input validation and error handling.
- Real-time game visualization using Turtle graphics.
- Detailed logging for game events and results.
- Unit tests for core functionalities.

## Project Structure

📦 Battleship Game  
├── battle_area.py        # Defines the battle area and ship placement logic  
├── game_controller.py    # Manages game logic, player turns, and interactions with the UI  
├── player.py             # Defines the Player class and its operations  
├── ship.py               # Defines Ship and ShipCell classes  
├── utils.py              # Contains utility classes and functions (e.g., Position, ShipType)  
├── battleship_ui.py      # Provides the game’s graphical interface using Turtle graphics  
├── main.py               # Entry point for the game  
├── test_game.py          # Unit tests for core game components  
└── README.md             # Documentation (you are here)  


## Prerequisites
1. **Python 3.6+**
2. Install required packages using:
   bash
   pip install -r requirements.txt
   

## How to Run the Game
1. **Clone the repository:**
   git clone https://github.com/bhavna9926/BattleShipGame.git
   cd BattleShipGame
   
2. **Run the game:**
   python main.py
   
3. **Follow the prompts to provide input:**
   - Battle area dimensions
   - Ship positions for each player
   - Firing sequences for each player

### Example Input (for 2 players):

5 E           # Battle area dimensions (width = 5, height = E)
2             # Number of ships
Q 1 1 A1 B2   # Ship 1: Type = Q, Width = 1, Height = 1, Positions: A1 (Player 1), B2 (Player 2)
P 2 1 D4 C3   # Ship 2: Type = P, Width = 2, Height = 1, Positions: D4 (Player 1), C3 (Player 2)
A1 B2 B3      # Player 1 firing sequence
B1 C3 D4      # Player 2 firing sequence


## How the Game Works
1. **Ship Placement:** Players place their ships on the battle area grid according to the input.
2. **Turn-Based Firing:** Players take turns firing missiles at their opponent’s grid.
3. **Hit or Miss:** The missile either hits a ship (reducing its health) or misses.
4. **Victory or Draw:** The game continues until one player wins by destroying all opponent ships, or it ends in a draw.

## Graphical Interface
The game uses **Turtle graphics** to render the battle grids and visualize hits, misses, and ship placements in real time. Each player has their own grid.

- **Grid Colors:**
  - Black: Grid lines
  - Blue/Green: Ship types (`P` and `Q`)
  - Red: Hit
  - Gray: Miss

## Logging
The game logs all key events (e.g., hits, misses, player turns, and game results) to both the console and a `game.log` file.

## Unit Testing
Unit tests are provided for core functionalities in `test_game.py`. To run the tests:
bash
python -m unittest test_game.py
 
## Using bash file
You can use the bash file setup_and_run.sh to install all dependencies of the project
What this script does:
    Creates a virtual environment (venv).
    Activates the virtual environment.
    Installs the packages from requirements.txt.
    Runs the project using main.py.
Steps to Run - 
    chmod +x setup_and_run.sh
    ./setup_and_run.sh

## Author
Bhavna Sharma
