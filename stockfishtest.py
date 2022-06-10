from stockfish import Stockfish

stockfish = Stockfish()
print(stockfish.is_move_correct('a2a3'))
print(stockfish.get_best_move())
