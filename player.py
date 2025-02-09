from battle_area import BattleArea
from ship import Ship
from collections import deque
from logger import logging

class Player:
    def __init__(self, name):
        self.name = name
        self.battle_area = None
        self.ship_count = 0
        self.firing_sequence = []

    def set_battle_area(self, width, height):
        self.battle_area = BattleArea(int(width), height)

    def set_ship_count(self, ship_count):
        self.ship_count = ship_count

    def place_ships(self, width, height, position, ship_type):
        ship = Ship(ship_type, width, height)
        self.battle_area.place_ship(width, height, position, ship)

    def set_firing_sequence(self, sequence):
        self.firing_sequence = deque(sequence)

    def check_all_ships_destroyed(self):
        return self.ship_count == 0

    def print_input(self):
        logging.info(f"name: {self.name}")
        logging.info(f"battle_area:{self.battle_area}")
        logging.info(f"ship_count:{self.ship_count}")
        logging.info(f"firing_sequence: {self.firing_sequence}")
