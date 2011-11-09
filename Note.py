class Note:
  def __init__(self,note, octave, time='quarter', alter=0):
    self.note = note
    self.octave = octave
    self.time = time
    self.alter = alter

  # prints out the xml encoding for the note
  def printNote(self):
    output = "<note>\n" + \
               "\t<pitch>\n" + \
                 "\t\t<step>" + str(self.note) + "</step>\n"
    if self.alter != 0:
      output += "\t\t<alter>" + str(self.alter) + "</alter>\n"

    output +=   "\t\t<octave>" + str(self.octave) + "</octave>\n" + \
              "\t</pitch>\n" + \
              "\t<voice>1</voice>\n" + \
              "\t<type>" + str(self.time) + "</type>\n" + \
              "</note>"
                                
    return output
