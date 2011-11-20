class Part:
	def __init__(self, number, part, measures):
		self.number = number
		self.part = part
		self.measures = measures

	def writePartList(self):
		output = '\t\t<score-part id="P' + str(self.number) + '">\n'
		output +='\t\t\t<part-name>' + self.part + '</part-name>\n' + \
		output +='\t\t\t<part-abbreviation>' + self.part[0] + '</part-abbreviation>\n'
		output +='\t\t\t<score-instrument id="P' + str(self.number) + '-I' + str(self.number) + '">\n'
		output +='\t\t\t\t<instrument-name>Instrument ' + str(self.number) + '</instrument-name>\n'
		output +='\t\t\t</score-instrument>\n'
		output +='\t\t\t<midi-instrument id="P' + str(self.number) + '-I' + str(self.number) + '">\n'
		output +='\t\t\t\t<midi-channel>' + str(self.number) + '</midi-channel>\n'
		output +='\t\t\t\t<midi-program>1</midi-program>\n'
		output +='\t\t\t</midi-instrument>\n'
		output +='\t\t</score-part>\n'
		return output

	def writePart(self):
		output = '\t<part id="P' + str(self.number) +'">\n"
		for measure in measures:
			output += measure.printMeasure()
		output +='\t</part>\n"
		return output
