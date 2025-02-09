from typing import List, Optional
from ship import Ship
from player import Player
from logger import logging
from utils import Position

class GameController:
    def __init__(self):
        self.state = None

    def check_hit(self, target, player) -> Optional[Ship]:
        """Check if a missile hits a ship at the given position in the player's battle area."""
        battle_area = player.battle_area.grid

        ship_cell = battle_area.get(target.x, {}).get(target.y)
        if ship_cell:
            ship_cell.record_hit(battle_area)
            return ship_cell.ship
        return None

    def get_next_player(self, active_players:List[Player], current_index:int) -> Optional[Player]:
        """
        Find the next player with remaining ships in a circular list of active players.
        If no such player is found, the function returns `None`.
        """

        if not active_players:
            return None

        start = (current_index+1) % len(active_players)
        while start != current_index:
            if active_players[start].ship_count > 0:
                return active_players[start]
            start = (start+1) % len(active_players)

        return None

    def get_active_players(self, players: List['Player']) -> List['Player']:
        """Returns a list of players who still have ships left."""
        return [player for player in players if player.ship_count > 0]

    def fire_missile(self, current_player: Player, target: Position, next_player: Player) -> bool:
        """Handles the missile firing logic and returns True if it was a hit, False otherwise."""
        ship = self.check_hit(target, next_player)
        if ship:
            logging.info(f"{current_player.name} fires a missile at {target} which is a hit.")
            if ship.is_destroyed():
                next_player.ship_count -= 1
                logging.info(f"{current_player.name} destroyed a ship!")
            return True
        else:
            logging.info(f"{current_player.name} fires a missile at {target} which missed.")
            return False

    def process_player_turn(self, current_player: Player, active_players: List[Player], index: int):
        """Processes the turn for the current player."""
        while current_player.firing_sequence:
            target = current_player.firing_sequence.popleft()
            next_player = self.get_next_player(active_players, index)

            if not next_player:
                # logging.info(f"{current_player.name} wins the game!")
                return

            if not self.fire_missile(current_player, target, next_player):
                break

    def is_firing_sequence_available(self, players:List[Player]):
        """
        Check if any player in the list has a non-empty firing sequence.
        """
        for player in players:
            if len(player.firing_sequence)>0:
                return True
        return False

    def game_is_on(self, active_players:List[Player]):
        """
        Determine if the game is still ongoing.
        The game is considered "on" if there are at least two active players and at least one player 
        has a non-empty firing sequence.
        """
        if not active_players:
            return False
        return len(active_players)>1 and self.is_firing_sequence_available(active_players)

    def start_game(self, players:List[Player]):
        """Starts the battleship game between multiple players."""
        active_players = self.get_active_players(players)

        while self.game_is_on(active_players):

            for i, player in enumerate(active_players):
                current_player = player
                if not current_player.firing_sequence:
                    logging.info(f"{current_player.name} has no more missiles left to launch")
                    continue
                
                self.process_player_turn(current_player, active_players, i)

            #refreshing active palyers
            active_players = self.get_active_players(players)

        if len(active_players) == 1:
            logging.info(f"{active_players[0].name} wins the game!")
        else:
            logging.info("Game ends in a draw.")
            