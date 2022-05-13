#Basic Imports 
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty

#Graphic interface imports 
from kivy.uix.behaviors import DragBehavior
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

from kivy.graphics import Rectangle

#Server Communivation
import requests
url = 'http://localhost/adveisor/data.php'

#Chess engine 
from stockfish import Stockfish
stockfish = Stockfish(path="/usr/games/stockfish", depth=15, parameters={"Threads": 2, "Minimum Thinking Time": 5})


#Basic Settings
Window.size = (480,320)
Window.borderless = False

###### 					 ___  ___   ___  ___  					######
###### 					|_ _|| . | | . \| . | 					######
######			   		 | | | | | | | || | | 					######
######  				 |_| `___' |___/`___' 					######
#	- Add Boundary to piece draggable Position
#	- Add prevention of grid position outside boards and related crash issue
#	- Load/Output with Forsyth–Edwards Notation
#	- Implement restart game function Fix start game button will spawn new pieces above existing ones 
#	- Remake and restyle right side of GUI (Terminal and command) and Implement new functions
#	- Implement check mate check and response, including
#		> Pawn Promotion
#		> Castling 
#		> En Passant Capture
#	- Implement control / config screen
# 	- Implement more functionality 
# 	- Implement communication with server and data syncronization
#	- Implement music player and sound effects 
#	- Implement timed chess function
# 	- Implement command line input
#	- Implement bottom Status bar
#	- Make everything look better by Implementing better color scheme and better layout
#	- Create Public and Private class for better access
#Global Variable 
checker_size = [0.0,0.0]
board_size = [0.0,0.0]
bottom_margin = 0.0
GlobalLayout = None
autoPlay = False

#Position Conversion
def to_chess_notation(move_from, move_to):
	x = "abcdefgh"
	y = "12345678"
	return x[move_from[0]] + y[move_from[1]] + x[move_to[0]]+ y[move_to[1]]
def to_move_position(chess_notation):
	x = "abcdefgh"
	y = "12345678"
	movePos = [0,0,0,0]
	for i in range(2):
		for j in range(8):
			if x[j] == chess_notation[i*2]:
				movePos[i*2] = j
			if y[j] == chess_notation[i*2+1]:
				movePos[i*2+1] = j
	return movePos
def position_to_coordinate(pos): 
	piece_coordinate = (checker_size[0] * pos[0] , checker_size[1] * pos[1] + board_size[1] * 0.05 )
	return piece_coordinate
def coordinate_to_position(coordinate): 
	piece_position = (round(coordinate[0]/ checker_size[0]), round((coordinate[1] - bottom_margin ) / checker_size[1]))
	return piece_position
#Sloppy resizing method, but hey it Works 
def grid_sizeing(self, x, y):
	global checker_size, bottom_margin, board_size
	board_size = (self.ids.chess_board.size[0] , self.ids.chess_board.size[1])
	checker_size = (board_size[0] / 8.1 , board_size[1] / 8.1)
	bottom_margin = board_size[1] * 0.05
	piece_position = (checker_size[0] * x , checker_size[1] * y + board_size[1] * 0.05 )
	return piece_position

#Classes for enabling mulitple screens
class WindowManager(ScreenManager):
	pass
class ConfigLayout(Screen,Widget):
	pass

#Main GUI Menu
class GUILayout(Screen,Widget):
	#Widget layer conversion. Kivy quirky magic: set parameter? No! DELETE the widget and make a NEW one!?! :D 
	#How I wish the documentation is better then bunch of Stackoverflow posts....
	def bring_to_front(self, widget):
		for child in self.ids.chess_board.children:
			if child == widget:
				self.ids.chess_board.remove_widget(widget)
				self.ids.chess_board.add_widget(widget)
	def send_to_back(self, widget):
		for child in self.ids.chess_board.children:
			if child == widget:
				self.ids.chess_board.remove_widget(widget)
				self.ids.chess_board.add_widget(widget, -1)
	#create chess pieces on the boards 
	def start_game(self):
		#TO_DO: Fully Implement load by FEN (Replace cmd or make a FEN to cmd parser)
		stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
		cmd = [["rnbqkbnr","wwwwwwww"],['pppppppp','wwwwwwww'],['00000000','00000000'],['00000000','00000000'],
			  ['00000000','00000000'],['00000000','00000000'],['pppppppp','bbbbbbbb'],["rnbqkbnr","bbbbbbbb"]]
		for j in range(8):
			for k in range(8):
				newPiece = None
				if cmd[j][0][k] == 'r':
					newPiece = rook(cmd[j][1][k])
				elif cmd[j][0][k] == 'n':
					newPiece = knight(cmd[j][1][k])
				elif cmd[j][0][k] == 'b':
					newPiece = bishop(cmd[j][1][k])
				elif cmd[j][0][k] == 'q':
					newPiece = queen(cmd[j][1][k])
				elif cmd[j][0][k] == 'k':
					newPiece = king(cmd[j][1][k])
				elif cmd[j][0][k] == 'p':
					newPiece = pawn(cmd[j][1][k])
				else:
					continue
				newPiece.numid = j*10 + k
				newPiece.pos = grid_sizeing(self,k, j)
				newPiece.previous_position = (k, j)
				self.ids.chess_board.add_widget(newPiece)
	#Not Implemented now
	def reset_board(self):
		pieces = [i for i in GlobalLayout.ids.chess_board.children]
		for piece in pieces:
			GlobalLayout.ids.chess_board.remove_widget(piece)


	def on_touch_down(self, touch):
		#prevent movement of chess pieces when not their turn
		if self.parent.turn != self.side and self.collide_point(*touch.pos):
			return False
		if self.collide_point(*touch.pos):
			#dirty quirky solution due to lazyness and lack of kivy documentation
			#must be a better way but i dont know python :D 
			#bring chess piece to the front of UI
			GlobalLayout.bring_to_front(self)
			#print(self.previous_position)
			#print(self.numid)
			#print("Working!")
		return super(Piece, self).on_touch_down(touch)

	def on_touch_up(self, touch):
		global checker_size, bottom_margin

		if self.collide_point(*touch.pos):
			GlobalLayout.send_to_back(self)
			#print("Yeeet!" + str(touch.pos))

			#snap to fit
			snap_pos = (round(self.pos[0]/ checker_size[0]) * checker_size[0],round((self.pos[1] - bottom_margin ) / checker_size[1])  * checker_size[1] + bottom_margin )
			#print("snap Pos:" + str(coordinate_to_position(snap_pos)))

			#get current move from chess piece, and chuck it into stockfish to do the move logic wizardy y
			move = to_chess_notation(self.previous_position, coordinate_to_position(snap_pos))
			#print(self.previous_position, coordinate_to_position(snap_pos))
			#print(move)
			#print(to_move_position(move))
			if stockfish.is_move_correct(move):
				stockfish.make_moves_from_current_position([move])
				#Send Data to Server
				dataToSend = {'game_round': '1', 'game_type': 'chess', 'game_data': move, 'is_new_round': 0}
				requests.post(url, data = dataToSend)

				GlobalLayout.ids.cmd_out.text = GlobalLayout.ids.cmd_out.text + "\n" + self.side + ": " + move 
				#print(stockfish.get_board_visual())
				self.pos = snap_pos
				self.previous_position  = coordinate_to_position(snap_pos)
				
				#remove captured piece if there is any
				for piece in self.parent.children:
					if (piece.pos[0], piece.pos[1]) == snap_pos and piece.side != self.side:
						#print('removing captured piece at ' + str(snap_pos))
						self.parent.remove_widget(piece)
				#change round
				if self.parent.turn ==  'w':
					self.parent.turn =  'b'
					print('Now Blacks Turn')
				else:
					#print('hmm_[B]:' + self.parent.turn)
					self.parent.turn = 'w'
					print('Now White Turn')
				if autoPlay == True:
					bestMove = stockfish.get_best_move()
					print(bestMove)
					best_move_pos = to_move_position(bestMove)
					stockfish.make_moves_from_current_position([bestMove])
					dataToSend = {'game_round': '1', 'game_type': 'chess', 'game_data': bestMove, 'is_new_round': 0}
					requests.post(url, data = dataToSend)
					for piece in GlobalLayout.ids.chess_board.children:
						if coordinate_to_position((piece.pos[0], piece.pos[1])) == (best_move_pos[0], best_move_pos[1]):
							piece.previous_position  = (best_move_pos[0],best_move_pos[1]) 
							GlobalLayout.ids.cmd_out.text = GlobalLayout.ids.cmd_out.text + "\n" + piece.side + ": " + bestMove
							for checkpiece in self.parent.children:
								if coordinate_to_position((checkpiece.pos[0], checkpiece.pos[1])) == (best_move_pos[2], best_move_pos[3]) and checkpiece.side == self.side:
									GlobalLayout.ids.chess_board.remove_widget(checkpiece)
									break
							piece.pos = position_to_coordinate((best_move_pos[2], best_move_pos[3]))
							if GlobalLayout.ids.chess_board.turn ==  'w':
								GlobalLayout.ids.chess_board.turn =  'b'
								print('Now Blacks Turn')
							else:
								GlobalLayout.ids.chess_board.turn = 'w'
								print('Now White Turn')
							break
			else:
				print("nope")
				self.pos = position_to_coordinate(self.previous_position)
				


		return super(Piece, self).on_touch_up(touch)

		


#load .kv style sheet
Builder.load_file('gui.kv')
class MyApp(App): 
	def build(self):
		global GlobalLayout 
		GlobalLayout =  GUILayout()
		ScrManager = ScreenManager(transition=WipeTransition())
		ScrManager.add_widget(GlobalLayout)
		ScrManager.add_widget(ConfigLayout())
		return ScrManager


if __name__ == '__main__':
    MyApp().run()