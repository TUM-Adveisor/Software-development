

#main chess piece class
class Piece(DragBehavior, Label, Widget):
	def __init__(self, **args):
		super(Piece, self).__init__(**args)
		self.numid = 0
		self.size_hint = (0.125, 0.125)
		self.is_active = True
		self.previous_position = (0, 0)
		with self.canvas:
			self.rect = Rectangle(pos=self.pos, size=self.size)
		self.bind(pos=self.update_rect)
		self.bind(size=self.update_rect)
		print('piece now at ' + str(self.pos))
	#Canvas related positioning 
	def update_rect(self, *args):
		self.rect.pos = self.pos
		self.rect.size = self.size
        
#Define different Chess Pieces 
class pawn(Piece):
	def __init__(self, side):
		super(pawn, self).__init__()
		self.side = side
		self.rect.source = './img/' + side +  'P' + '.png'
class rook(Piece):
	def __init__(self, side):
		super(rook, self).__init__()
		self.side = side
		self.rect.source = './img/' + side +  'R' + '.png'		
class knight(Piece):
	def __init__(self, side):
		super(knight, self).__init__()
		self.side = side
		self.rect.source = './img/' + side +  'N' + '.png'
class bishop(Piece):
	def __init__(self, side):
		super(bishop, self).__init__()
		self.side = side
		self.rect.source = './img/' + side +  'B' + '.png'
class king(Piece):
	def __init__(self, side):
		super(king, self).__init__()
		self.side = side
		self.rect.source = './img/' + side +  'K' + '.png'
class queen(Piece):
	def __init__(self, side):
		super(queen, self).__init__()
		self.side = side
		self.rect.source = './img/' + side +  'Q' + '.png'