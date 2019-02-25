# maze clipping version

import pyxel
import maze as mz
import random as rd
import wall as wl

# 大きな数字をmazeクラスに渡すと再帰の回数が多すぎて
# エラーになってしまう
ROW_MAX = 30
COL_MAX = 30

WIDTH = 255
HEIGHT = 255

SCALE = 2

WALL_RATIO = 0.3

class MazeClip:
	def __init__(self, width, height):
	
		self.window_width = width
		self.window_height = height
		self.color = 1
		self.blockSize = 5

		pyxel.init(self.window_width, self.window_height, scale = SCALE)
		
		# self.GenerateMaze(ROW_MAX, COL_MAX)

		self.wall = wl.Wall(self.width, self.height, self.color)
		
		# self.map = [[0 for i in range(5)] for j in range(5)]
		
#		for tempW in range(len(self.map)):
#			for tempH in range(len(self.map[tempW])):
#				self.map[tempW][tempH] = rd.randrange(2)
				
	def GenerateMaze(self, rowMax, colMax):
		self.maze = mz.Maze(rowMax, colMax)
		
		self.maze.Run()
		# self.maze.Display()
