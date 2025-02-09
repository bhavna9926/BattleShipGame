from utils import ShipType, Position, InputValidationError
from ship import ShipCell


class BattleArea:
    def __init__(self, width, height):
        self.width:int = width
        self.height:str = height
        self.grid = {}  # Grid represented as a dictionary

    def _is_out_of_bounds(self, x: str, y: int) -> bool:
        return ord(x) > ord(self.height) or (y > self.width)

    def place_ship(self, width, height, position, ship):
        """Places the ship in the grid with specified width, height, and position."""
        ship_cell_health = ShipType.Q.value if ship.ship_type == 'Q' else ShipType.P.value

        for i in range(height):
            for j in range(width):
                new_x = chr(ord(position.x.upper()) + i)
                new_y = int(position.y + j)

                if self._is_out_of_bounds(new_x, new_y):
                    raise InputValidationError(f"Ship placement out of bounds at {new_x}{new_y}.")

                if self.grid.get(new_x, {}).get(new_y):
                    raise InputValidationError(f"Ship overlap detected at {new_x}{new_y}.")

                new_position = Position(new_x, new_y)
                ship_cell = ShipCell(ship, ship_cell_health, new_position)

                if new_position.x not in self.grid:
                    self.grid[new_position.x] = {}

                self.grid[new_position.x][new_position.y] = ship_cell
