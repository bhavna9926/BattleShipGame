from dataclasses import dataclass
from enum import Enum
from logger import logging

# Enums and Config
class ShipType(Enum):
    Q = 2    
    P = 1

class InputValidationError(Exception):
    pass

def throw_error(msg:str) -> None:
    logging.error(msg)  # Log the error
    raise InputValidationError(msg)

@dataclass
class Position:
    x:str
    y:int

    def __str__(self):
        return f'{self.x}{self.y}'