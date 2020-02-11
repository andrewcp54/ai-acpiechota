from agent import Agent
from const import Const
from game import Game
from move import Move

class OccamsGoatAgent(Agent):
    def __init__(self, game : Game):
        super(OccamsGoatAgent, self).__init__(game,Const.MARK_GOAT)
    def propose(self) -> Move:  
        moves = self.game.goatMoves()
        Game.TURN_COUNT = Game.TURN_COUNT + 1
        
        if Game.TURN_COUNT == 1:
            return moves[1]
        else:
        # returns first possible place for goat to go, starting at a1 each time. 
        # one way to make this faster, is if we know a goat has gone and been placed and NOT captured, remove that from list of moves
        # pretty sure this would only affect computation speeds, not really benefit gameplay
            return moves[0]