# third person view maze

# imports
import pyxel
import random as rm
import sys

import control as ctrl
import maze as mz

# constant

BASE_COLOR = 0
PLAYER_COLOR = 3
DEST_COLOR = 8
WALL_COLOR = 4
GROUND_COLOR = 7

SCALE = 2
FPS = 30
BORDER = 3

LEVEL_SPAN = 4
DIFFICULTY = 4

OFFSET = 1

class maze_TPV:
	def __init__(self, blockSize):
		sys.setrecursionlimit(10000)

		gain = int(255 / blockSize)

		width = blockSize * gain
		height = blockSize * gain

		pyxel.init(width, height, caption="maze runner", scale=SCALE, fps=FPS, border_width=BORDER, border_color=WALL_COLOR)

		self.width = width
		self.height = height
		self.blockSize = blockSize
		self.initBlockSize = blockSize
		
		self.SetConstValue()
		self.SetMaze()
		
		pyxel.run(self.Update, self.Draw)

##################################################################
		
	def Update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

		if pyxel.btnp(pyxel.KEY_R):
			self.blockSize = self.blockSize - LEVEL_SPAN
			if self.blockSize <= 0:
				self.blockSize = self.initBlockSize
			self.SetConstValue()
			self.SetMaze()

		if self.isGoal == False:
			self.row, self.col = self.cl.Run()
		
	def Draw(self):
		pyxel.cls(WALL_COLOR)
		self.MazeDraw()
		
		# destination
		self.DrawCircle(self.rowDest, self.colDest, self.destColor)
		# player
		self.DrawCircle(self.row, self.col, self.playerColor)
		
		self.GoalDetect()
		
	def DrawCircle(self, row, col, color):
		pyxel.circ(row * self.blockSize + self.blockSize / 2, \
		col * self.blockSize + self.blockSize / 2, \
		(self.blockSize - OFFSET) / 2, color)
		
	def MazeDraw(self):
		for rowtemp in range(len(self.maze.map)):
			for coltemp in range(len(self.maze.map[rowtemp])):
				if self.maze.map[rowtemp][coltemp] == 0:
					pyxel.rect(rowtemp * self.blockSize, \
					coltemp * self.blockSize, \
					rowtemp * self.blockSize + self.blockSize - OFFSET, \
					coltemp * self.blockSize + self.blockSize - OFFSET, \
					self.stageColor)
				else:
					pyxel.rect(rowtemp * self.blockSize, \
					coltemp * self.blockSize, \
					rowtemp * self.blockSize + self.blockSize - OFFSET, \
					coltemp * self.blockSize + self.blockSize - OFFSET, \
					self.groundColor)
					
					
	def GenerateNode(self):
		tempRow = rm.randint(0, self.rowMax - 1)
		tempCol = rm.randint(0, self.colMax - 1)
		
		if (self.rowMax - 1) == tempRow or (self.colMax - 1) == tempCol:
			return self.GenerateNode()

		if self.maze.map[tempRow][tempCol] == 1:
			return tempRow, tempCol
		elif self.maze.map[tempRow][tempCol] == 0:
			return self.GenerateNode()
			
	def GoalDetect(self):
		if self.row == self.rowDest and self.col == self.colDest:
			pyxel.text(self.width / 2.5, self.blockSize / 3, "Congraturation", rm.randint(1,14))
			self.isGoal = True
	
	def SetConstValue(self):
		self.rowMax = int(self.width / self.blockSize)
		self.colMax = int(self.height / self.blockSize)
		
		# self.playerColor = rm.randint(1, 4)
		# self.destColor = rm.randint(5, 8)
		# self.stageColor = rm.randint(9, 12)
		self.playerColor = PLAYER_COLOR
		self.destColor = DEST_COLOR
		self.stageColor = WALL_COLOR
		self.groundColor = GROUND_COLOR

		self.isGoal = False
	
	def SetMaze(self):
		self.maze = mz.Maze(self.rowMax, self.colMax)
		
		self.maze.Run()
		# self.maze.Display()
		
		while True:
			self.row, self.col = self.GenerateNode()
			self.rowDest, self.colDest = self.GenerateNode()

			if self.row != self.rowDest or self.col != self.colDest:
				break
		
		self.cl = ctrl.PlayerController(self.row, self.col, self.maze.map)
		self.isGoal = False
		

