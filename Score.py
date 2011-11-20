class Score:
	def __init__(self, parts):
		self.parts = parts

	def printScore(self):
		output = '<score-partwise>\n'
		output += '\t<part-list>\n'
		for part in self.parts:
			output += part.writePartList()
		output += '\t</part-list>\n'
		for part in self.parts:
			output += part.writePart()
		output += '</score-partwise>\n'
		return output

	def getNotes(self):
		notes = []
		for part in self.parts:
			notes += part.getNotes()
		return notes
