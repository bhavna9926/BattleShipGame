import turtle
from typing import Dict, List, Optional
from utils import Position
from ship import Ship

class BattleshipUI:
    def __init__(self, players: List[str], grid_size: tuple):
        """Initialize the UI with player count and grid dimensions."""
        self.width, self.height = grid_size
        self.cell_size = 40  # Size of each grid cell in pixels
        self.players = players
        self.player_count = len(players)
        
        # Calculate total width needed for all grids with padding
        total_width = self.player_count * (self.width * self.cell_size + 50)
        
        # Setup main window
        self.screen = turtle.Screen()
        self.screen.title("Battleship Game")
        self.screen.setup(total_width + 100, 600)
        self.screen.tracer(0)  # Turn off animation for faster drawing
        
        # Create drawing turtle
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        
        # Create message turtle
        self.message_pen = turtle.Turtle()
        self.message_pen.hideturtle()
        self.message_pen.speed(0)
        
        # Colors for different elements
        self.colors = {
            'grid': 'black',
            'P': 'blue',
            'Q': 'green',
            'hit': 'red',
            'miss': 'gray',
            'text': 'black',
            'win': 'green',
            'draw': 'orange',
            'turn': 'blue'
        }
        
        # Store grid positions for each player
        self.grid_origins = self._calculate_grid_origins()
        
        # Draw initial grids
        self._draw_initial_grids()
        self.screen.update()

    def _calculate_grid_origins(self) -> List[tuple]:
        """Calculate the starting position for each player's grid."""
        origins = []
        total_width = self.player_count * (self.width * self.cell_size + 50)
        start_x = -(total_width / 2) + (self.width * self.cell_size / 2)
        
        for i in range(self.player_count):
            x = start_x + i * (self.width * self.cell_size + 50)
            origins.append((x, 100))
        
        return origins

    def _draw_grid(self, origin_x: float, origin_y: float):
        """Draw a single grid with coordinates."""
        self.pen.penup()
        self.pen.color(self.colors['grid'])

        # Draw horizontal lines
        for i in range(self.height + 1):
            self.pen.goto(origin_x - (self.width * self.cell_size / 2),
                          origin_y - (i * self.cell_size))
            self.pen.pendown()
            self.pen.forward(self.width * self.cell_size)
            self.pen.penup()

        # Draw vertical lines
        for i in range(self.width + 1):
            self.pen.goto(origin_x - (self.width * self.cell_size / 2) + (i * self.cell_size),
                          origin_y)
            self.pen.setheading(-90)
            self.pen.pendown()
            self.pen.forward(self.height * self.cell_size)
            self.pen.penup()
        
        self.pen.setheading(0)  # Reset direction

        # Draw column numbers
        for i in range(self.width):
            self.pen.goto(origin_x - (self.width * self.cell_size / 2) + (i * self.cell_size) + self.cell_size / 2,
                          origin_y - (self.height * self.cell_size) - 25)
            self.pen.write(str(i + 1), align="center", font=("Arial", 8, "normal"))

        # Draw row letters
        for i in range(self.height):
            self.pen.goto(origin_x - (self.width * self.cell_size / 2) - 20,
                          origin_y - (i * self.cell_size) - self.cell_size / 2)
            self.pen.write(chr(65 + i), align="center", font=("Arial", 8, "normal"))

    def _draw_initial_grids(self):
        """Draw all player grids with their names."""
        for i, (origin_x, origin_y) in enumerate(self.grid_origins):
            self._draw_grid(origin_x, origin_y)
            
            # Draw player name
            self.pen.goto(origin_x, origin_y - (self.height * self.cell_size) - 50)
            self.pen.color(self.colors['text'])
            self.pen.write(self.players[i], align="center", font=("Arial", 12, "bold"))

    # def draw_ship(self, player_index: int, position: Position, width: int, height: int, ship_type: str):
    def draw_ship(self, player_index: int, ship:Ship):
        """Place a ship on the grid with the appropriate color."""
        origin_x, origin_y = self.grid_origins[player_index]
        color = self.colors[f'{ship.ship_type}']
        
        self.pen.color(color)
        self.pen.fillcolor(color)
        
        # Calculate actual position
        start_x = origin_x - (self.width * self.cell_size / 2) + ((ship.position.y - 1) * self.cell_size)
        start_y = origin_y - ((ord(ship.position.x) - ord('A')) * self.cell_size)
        
        # Draw ship
        self.pen.penup()
        self.pen.goto(start_x, start_y)
        self.pen.pendown()
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(ship.width * self.cell_size)
            self.pen.right(90)
            self.pen.forward(ship.height * self.cell_size)
            self.pen.right(90)
        self.pen.end_fill()
        self.screen.update()

    def mark_hit(self, player_index: int, position: Position):
        """Mark a hit on the grid with a red X."""
        origin_x, origin_y = self.grid_origins[player_index]
        x = origin_x - (self.width * self.cell_size / 2) + ((position.y - 1) * self.cell_size) + self.cell_size/2
        y = origin_y - ((ord(position.x) - ord('A')) * self.cell_size) - self.cell_size/2
        
        self.pen.color(self.colors['hit'])
        self.pen.penup()
        self.pen.goto(x - 10, y + 10)
        self.pen.pendown()
        self.pen.goto(x + 10, y - 10)
        self.pen.penup()
        self.pen.goto(x - 10, y - 10)
        self.pen.pendown()
        self.pen.goto(x + 10, y + 10)
        self.screen.update()

    def mark_miss(self, player_index: int, position: Position):
        """Mark a miss on the grid with a gray dot."""
        origin_x, origin_y = self.grid_origins[player_index]
        x = origin_x - (self.width * self.cell_size / 2) + ((position.y - 1) * self.cell_size) + self.cell_size/2
        y = origin_y - ((ord(position.x) - ord('A')) * self.cell_size) - self.cell_size/2
        
        self.pen.color(self.colors['miss'])
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.dot(10)
        self.screen.update()

    def close(self):
        """Close the turtle window."""
        self.screen.bye()

    def display_message(self, message: str, message_type: str = 'text'):
        """Display a message at the top of the screen."""
        self.message_pen.clear()
        self.message_pen.penup()
        self.message_pen.color(self.colors[message_type])
        self.message_pen.goto(0, 250)  # Position above the grids
        self.message_pen.write(message, align="center", font=("Arial", 24, "bold"))
        self.screen.update()

    def announce_winner(self, player_name: str):
        """Display the winner announcement."""
        self.display_message(f"{player_name} Wins!", 'win')

    def announce_draw(self):
        """Display the draw announcement."""
        self.display_message("Game Ends in a Draw!", 'draw')

    def announce_turn(self, player_name: str):
        """Display whose turn it is."""
        self.display_message(f"{player_name} Turn", 'turn')
