Battleship Game Simulator

Overview
    This project is a Battleship Game Simulator implemented in Python. It allows multiple players to battle each other using a grid-based battlefield. Each player can place ships on their battle area and take turns firing missiles at the opponent’s ships until one player emerges victorious or the game ends in a draw.

Features
    Multi-player battleship game simulation.
    Configurable battle area and ship placements.
    Circular turn-based gameplay with firing sequences.
    Comprehensive input validation and error handling.
    Detailed logging for game events and results.

📦 Battleship Game  
├── battle_area.py        # Defines the battle area and ship placement logic  
├── game_controller.py    # Handles the game logic and turn-based operations  
├── input_validator.py    # Validates and processes user input  
├── logger.py             # Configures logging for the game  
├── main.py               # Entry point for the game  
├── player.py             # Defines the Player class and its operations  
├── ship.py               # Defines Ship and ShipCell classes  
├── utils.py              # Contains utility classes and functions (e.g., Position, ShipType)  
├── game.log              # Log file for game events  
└── test_game.py          # Test file you can run usign "python -m unittest test_game.py"
└── README.md             # Documentation file (you are here)  

Prerequisites
    Python 3.6+

How to Run the Game
    1. Clone the repository:
        git clone <repository-url>
        cd battleship-game
    2. Run the game:
        python main.py
    3. Follow the prompts to provide input for:
        a) Battle area dimensions
        b) Ship positions
        c) Firing sequences for each player

Example Input (for 2 players) - 
    5 E           # Battle area dimensions (width = 5, height = E)  
    2             # Number of ships  
    Q 1 1 A1 B2   # Ship 1: Type = Q, Width = 1, Height = 1, Positions: A1 (Player 1), B2 (Player 2)  
    P 2 1 D4 C3   # Ship 2: Type = P, Width = 2, Height = 1, Positions: D4 (Player 1), C3 (Player 2)  
    A1 B2 B3      # Player 1 firing sequence  
    B1 C3 D4      # Player 2 firing sequence  

How the Game Works
    1) Ship Placement: Players place their ships on the battle area grid according to the input.
    2) Turn-Based Firing: Players take turns firing missiles at their opponent’s grid.
    3) Hit or Miss: The missile either hits a ship (reducing its health) or misses.
    4) Victory or Draw: The game continues until one player wins by destroying all opponent ships, or it ends in a draw.

Logging
    The game logs all key events (e.g., hits, misses, player turns, and game results) to both the console and the game.log file.

Testing
    Unit tests are provided for core functionalities. To run the tests:
        python -m unittest test_game.py

Author
    Bhavna Sharma







