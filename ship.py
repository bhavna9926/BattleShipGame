class Ship:
    def __init__(self, ship_type, width, height):
        self.ship_type = ship_type
        self.size = width * height

    def reduce_health(self, grid, position):
        """Removes a cell from the grid and reduces the ship size."""
        self.size -= 1
        grid[position.x][position.y] = None
    
    def is_destroyed(self):
        return self.size == 0

class ShipCell:
    def __init__(self, ship, health, position) -> None:
        self.ship = ship
        self.health = health
        self.position = position

    def record_hit(self, grid):
        """Records a hit on this cell and removes it from the grid if the health reaches zero."""
        self.health -= 1
        if self.health == 0:
            self.ship.reduce_health(grid, self.position)
