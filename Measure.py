class Measure:
        def __init__(self, number, notes):
                self.number = number
                self.notes = notes
               
        # adds a note to a measure 
        def addNote(self, note):
                self.notes.append(note)
        
        # prints out the MusicXML for a measure, including all the notes
        # the definition for measure 0 is special and prints out extra settings
        def printMeasure(self):
                if self.number != 0:
                        output = "\t\t<measure number=\"" + str(self.number) + "\">\n"
                else:
                        output = "\t\t<measure implicit=\"yes\" number=\"0\">\n"
                        output +='\t\t\t<attributes>\n'
                        output +='\t\t\t\t<divisions>4</divisions>\n'
                        output +='\t\t\t\t<key>\n'
                        output +='\t\t\t\t\t<fifths>-1</fifths>\n'
                        output +='\t\t\t\t\t<mode>major</mode>\n'
                        output +='\t\t\t\t</key>\n'
                        output +='\t\t\t\t<time symbol="common">\n'
                        output +='\t\t\t\t\t<beats>4</beats>\n'
                        output +='\t\t\t\t\t<beat-type>4</beat-type>\n'
                        output +='\t\t\t\t</time>\n'
                        output +='\t\t\t</attributes>\n'
                        output +='\t\t\t<sound tempo="76"/>\n'
                for note in self.notes:
                        output += note.printNote()
                output += "\t\t</measure>\n"
                output += "\t\t<!--=======================================================-->\n"
                return output
