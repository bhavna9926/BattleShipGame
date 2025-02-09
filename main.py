from logger import logging
from input_validator import ValidateInput
from game_controller import GameController

def main():
    try:
        # Take input
        logging.info("Please enter all lines of your input (Press Ctrl+D to end):")
        input_class = ValidateInput()

        if input_class.get_valid_input():
            # Initialize players
            player_names = ['player-1', 'player-2']
            input_class.set_players(player_names)
            
            # Configure the game setup
            input_class.configure_game()
            
            # Print player inputs
            for player in input_class.players:
                player.print_input()
            
            # Start the game
            GameController().start_game(input_class.players)
    except Exception as e:
        logging.info(f"An error occurred: {e}")

if __name__ == '__main__':
    main()