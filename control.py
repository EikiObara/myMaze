import pyxel

class PlayerController:
	def __init__(self, row, col, map):
		self.row = row
		self.col = col
		self.map = map
		
	# coordinate control
	def RowPlus(self):
		self.row = self.row + 1
	def RowMinus(self):
		self.row = self.row - 1
	def ColPlus(self):
		self.col = self.col + 1
	def ColMinus(self):
		self.col = self.col - 1
		
	def Run(self):
		
		self.SetBeforeCoord()

		if pyxel.btnp(pyxel.KEY_LEFT,4,4):
			self.RowMinus()
		elif pyxel.btnp(pyxel.KEY_RIGHT,4,4):
			self.RowPlus()
		elif pyxel.btnp(pyxel.KEY_UP,4,4):
			self.ColMinus()
		elif pyxel.btnp(pyxel.KEY_DOWN,4,4):
			self.ColPlus()
			
		self.WallJudgment()
		
		return self.row, self.col
	
	def SetBeforeCoord(self):
		self.beforeRow = self.row
		self.beforeCol = self.col

	def WallJudgment(self):
		if self.map[self.row][self.col] == 0:
			self.row = self.beforeRow
			self.col = self.beforeCol


