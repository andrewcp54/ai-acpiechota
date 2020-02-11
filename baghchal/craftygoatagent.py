from agent import Agent
from const import Const
from game import Game
from move import Move

class CraftyGoatAgent(Agent):
    def __init__(self, game : Game):
        super(CraftyGoatAgent, self).__init__(game,Const.MARK_GOAT)
    def propose(self) -> Move:  
        moves = self.game.goatMoves()
        # returns first possible place for goat to go, starting at a1 each time. 
        # one way to make this faster, is if we know a goat has gone and been placed and NOT captured, remove that from list of moves
        # pretty sure this would only affect computation speeds, not really benefit gameplay
        return moves[0]
