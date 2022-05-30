from stockfish import Stockfish

stockfish = Stockfish(path="/usr/games/stockfish",depth=5,parameters={"Threads": 2, "Minimum Thinking Time": 5})
print(stockfish.is_move_correct('a2a3'))
print(stockfish.get_best_move())

