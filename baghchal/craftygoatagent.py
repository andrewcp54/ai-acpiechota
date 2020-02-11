from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List
import random

class CraftyGoatAgent(Agent):
    def __init__(self, game : Game):
        super(CraftyGoatAgent, self).__init__(game,Const.MARK_GOAT)
    def propose(self) -> Move:  
        moves = self.game.goatMoves()
        #print(moves[0])
        return moves[0]
        '''captures : List[Move]=[]
        for move in moves:
            if move.capture:
                captures.append(move)
        if len(captures) != 0:
            return random.choice(captures)
        else:
            return random.choice(moves)
        '''