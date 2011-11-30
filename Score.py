class Score:
	def __init__(self, parts):
		self.parts = parts

	def printScore(self):
		output = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
		output += "<!DOCTYPE score-partwise PUBLIC \"-//Recordare//DTD MusicXML 1.1 Partwise//EN\""
		output += " \"http://www.musicxml.org/dtds/partwise.dtd\">"
		output += '<score-partwise version="1.1">\n'
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
