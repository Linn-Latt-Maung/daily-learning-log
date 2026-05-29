import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]
    def make_move(self):
        # Pick a random move from the available moves list
        selected_move = random.choice(self.moves)
        
        # Calculate new position coordinates: (current_x + move_x, current_y + move_y)
        new_x = self.position[0] + selected_move[0]
        new_y = self.position[1] + selected_move[1]
        
        # Update current position, append to tracking path, and return it
        self.position = (new_x, new_y)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1), (0,-1), (-1,0), (1,0)]

    def level_up(self):
        diagonal_moves = [(1,1), (1,-1), (-1,-1), (-1,1)]
        self.moves.extend(diagonal_moves)





