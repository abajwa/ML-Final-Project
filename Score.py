class Score:
	def __init__(self, parts):
		self.parts = parts

	def printScore(self):
		output = '<score-partwise>\n'
		output += '\t<part-list>\n'
		for part in self.parts:
			output += part.printPartList()
		output += '\t</part-list>\n'
		for part in self.parts:
			output += part.printPart()
		output += '</score-partwise>\n'

	def getNotes(self):
		notes = []
		for part in self.parts:
			notes += part.getNotes()
		return notes
