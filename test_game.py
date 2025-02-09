import unittest
from unittest.mock import MagicMock, patch
from game_controller import GameController
from player import Player
from battle_area import BattleArea
from utils import Position, InputValidationError
from ship import Ship, ShipCell
from input_validator import ValidateInput


class TestGameController(unittest.TestCase):

    def setUp(self):
        """Setup a GameController instance before each test."""
        self.game_controller = GameController()

    def test_check_hit_hit(self):
        """Test check_hit when the missile hits a ship."""
        player = Player("Player 1")
        player.battle_area = MagicMock()
        mock_ship = MagicMock()
        player.battle_area.grid = {
            'A': {1: ShipCell(mock_ship, 1, Position('A', 1))}
        }

        result = self.game_controller.check_hit(Position('A', 1), player)
        self.assertEqual(result, mock_ship)

    def test_check_hit_miss(self):
        """Test check_hit when the missile misses."""
        player = Player("Player 1")
        player.battle_area = MagicMock()
        player.battle_area.grid = {}

        result = self.game_controller.check_hit(Position('A', 1), player)
        self.assertIsNone(result)

    def test_get_next_player(self):
        """Test get_next_player returns the next active player."""
        players = [Player("Player 1"), Player("Player 2"), Player("Player 3")]
        players[0].ship_count = 0
        players[1].ship_count = 1
        players[2].ship_count = 0

        result = self.game_controller.get_next_player(players, 0)
        self.assertEqual(result, players[1])

    def test_fire_missile_hit(self):
        """Test fire_missile when it hits a ship."""
        current_player = Player("Player 1")
        next_player = Player("Player 2")
        mock_ship = MagicMock()
        self.game_controller.check_hit = MagicMock(return_value=mock_ship)
        mock_ship.is_destroyed = MagicMock(return_value=True)

        with self.assertLogs(level='INFO') as log:
            self.game_controller.fire_missile(current_player, Position('A', 1), next_player)
        self.assertIn("fires a missile at A1 which is a hit.", log.output[0])

    def test_fire_missile_miss(self):
        """Test fire_missile when it misses."""
        current_player = Player("Player 1")
        next_player = Player("Player 2")
        self.game_controller.check_hit = MagicMock(return_value=None)

        with self.assertLogs(level='INFO') as log:
            self.game_controller.fire_missile(current_player, Position('A', 1), next_player)
        self.assertIn("fires a missile at A1 which missed.", log.output[0])


class TestPlayer(unittest.TestCase):

    def test_set_battle_area(self):
        """Test set_battle_area creates a BattleArea instance."""
        player = Player("Player 1")
        player.set_battle_area(5, 'E')
        self.assertIsInstance(player.battle_area, BattleArea)
        self.assertEqual(player.battle_area.width, 5)
        self.assertEqual(player.battle_area.height, 'E')

    def test_set_firing_sequence(self):
        """Test set_firing_sequence converts a list to deque."""
        player = Player("Player 1")
        sequence = [Position('A', 1), Position('B', 2)]
        player.set_firing_sequence(sequence)
        self.assertEqual(len(player.firing_sequence), 2)


class TestBattleArea(unittest.TestCase):

    def test_place_ship_success(self):
        """Test place_ship places the ship correctly in the grid."""
        battle_area = BattleArea(5, 'E')
        ship = Ship('P', 1, 1)
        battle_area.place_ship(1, 1, Position('A', 1), ship)
        self.assertIn('A', battle_area.grid)
        self.assertIn(1, battle_area.grid['A'])

    def test_place_ship_out_of_bounds(self):
        """Test place_ship raises an error when the ship is out of bounds."""
        battle_area = BattleArea(5, 'E')
        ship = Ship('P', 1, 1)
        with self.assertRaises(InputValidationError):
            battle_area.place_ship(1, 1, Position('F', 1), ship)


class TestValidateInput(unittest.TestCase):

    def setUp(self):
        self.validator = ValidateInput()

    def test_get_coordinates_pos_valid(self):
        """Test get_coordinates_pos returns a valid Position."""
        position = self.validator.get_coordinates_pos('A1')
        self.assertEqual(position.x, 'A')
        self.assertEqual(position.y, 1)

    def test_get_coordinates_pos_invalid(self):
        """Test get_coordinates_pos raises an error for invalid input."""
        with self.assertRaises(InputValidationError):
            self.validator.get_coordinates_pos('1A')

    def test_set_players(self):
        """Test set_players creates Player instances."""
        self.validator.set_players(['Player 1', 'Player 2'])
        self.assertEqual(len(self.validator.players), 2)
        self.assertEqual(self.validator.players[0].name, 'Player 1')

