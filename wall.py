
class Wall:
	def __init__(self, width, height, color):
		self.width = width
		self.height = height
		self.color = color

	def Generate(self):
		for wallW in range(len(self.map)):
			tempW	= self.width / len(self.map)
			tempH	= self.height / len(self.map[wallW])

			for wallH in range(len(self.map[wallW])):
				if(self.map[wallW][wallH] == 1):
					pyxel.rect(int(wallW * tempW), int(wallH * tempH), \
					int(wallW * tempW + tempW), int(wallH * tempH + tempH), \
					self.color)