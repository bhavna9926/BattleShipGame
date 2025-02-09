from typing import List, Optional
from player import Player
from utils import Position, throw_error
import sys

class ValidateInput:
    def __init__(self) -> None:
        self.expected_input_lines:int = 6
        self.ship_count: int = 0
        self.input: List[str] = []
        self.players: List[Player] = []

    def set_players(self, player_names: List[str]):
        for name in player_names:
            self.players.append(Player(name))

    def get_coordinates_pos(self, char: str) -> Position:
        if not char[0].isalpha() or not char[1:].isdigit():
            throw_error(f"Invalid input '{char}'. Expected format: A1, B10, etc.")
        xPos = char[0]
        yPos = int(char[1:])
        return Position(xPos, yPos)

    def get_valid_input(self) -> List[str]:
        input_text = sys.stdin.read().strip()
        input_lines = input_text.splitlines()
        
        if not input_lines:
            throw_error("No input provided. Please enter valid input.")
        if len(input_lines) != self.expected_input_lines:
            throw_error(f"Expected {self.expected_input_lines} lines of input. Got {len(input_lines)}.")
        
        self.input = input_lines
        return True

    def set_battle_area(self):
        battle_area = self.input[0].split()

        # Validate battle area dimensions
        if len(battle_area) != 2 or not battle_area[0].isdigit() or not battle_area[1].isalpha():
            throw_error(f"{battle_area} is not a valid battle area dimension. Please enter valid dimensions (e.g., '5 E')!")

        width, height = battle_area

        # Set battle area dimensions for both players
        for player in self.players:
            player.set_battle_area(width, height)


    def set_ship_count(self):
        ship_count = self.input[1].strip()

        # Validate ship count
        if not ship_count.isdigit():
            throw_error("Please enter a valid integer for ship count; it cannot be empty or non-numeric!")

        ship_count = int(ship_count)
        
        # Set ship count for both players
        for player in self.players:
            player.set_ship_count(ship_count)
        
        self.ship_count = ship_count


    def set_ship_positions(self):
        start_index = 2

        while self.ship_count > 0:
            ship_positions = self.input[start_index].split()

            # Validate ship positions
            if len(ship_positions) != (3 + len(self.players)):
                throw_error("Invalid ship position input for all players.")

            try:
                ship_type, ship_width, ship_height = ship_positions[:3]
                ship_width, ship_height = int(ship_width), int(ship_height)
                # Place ships for both players
                for i, player in enumerate(self.players):
                    position = self.get_coordinates_pos(ship_positions[3+i])
                    player.place_ships(ship_width, ship_height,position, ship_type)
            except ValueError as e:
                throw_error(f"Invalid ship dimensions or positions: {e}")
            except Exception as e:
                throw_error(f"An unexpected error occurred: {e}")

            self.ship_count -= 1
            start_index += 1


    def set_firing_sequence(self):
        def validate_and_get_coordinates(sequence):
            positions = sequence.split()
            
            # Validate each position (format: letter followed by a number, e.g., A1, B2)
            for pos in positions:
                if not (len(pos) >= 2 and pos[0].isalpha() and pos[1:].isdigit()):
                    throw_error(f"Invalid position '{pos}'. Expected format: A1 B2 B3 ...")
            
            # Convert positions to coordinates
            return [self.get_coordinates_pos(pos) for pos in positions]

        # Validate and set firing sequences for both players
        for i, player in enumerate(self.players):
            sequence = validate_and_get_coordinates(self.input[-len(self.players)+i])
            player.set_firing_sequence(sequence)

    def configure_game(self) -> None:
        self.set_battle_area()
        self.set_ship_count()
        self.set_ship_positions()
        self.set_firing_sequence()
