class Note:
  def __init__(self, note, octave, time='quarter', duration=4, alter=0):
    self.note = note
    self.octave = octave
    self.time = time
    self.alter = alter
    self.duration = duration

  # prints out the xml encoding for the note
  def printNote(self):
    output = "\t\t\t<note>\n"

    if 'R' in str(self.note):
      output += "\t\t\t\t<rest/>\n"
    else:
      output += "\t\t\t\t<pitch>\n" + \
                 "\t\t\t\t\t<step>" + str(self.note) + "</step>\n"
      if self.alter != 0:
        output += "\t\t\t\t\t<alter>" + str(self.alter) + "</alter>\n"

      output +=   "\t\t\t\t\t<octave>" + str(self.octave) + "</octave>\n" + \
                "\t\t\t\t</pitch>\n"
    output += "\t\t\t\t<duration>"+str(self.duration)+"</duration>\n"
    output +="\t\t\t\t<voice>1</voice>\n" + \
              "\t\t\t\t<type>" + str(self.time) + "</type>\n" + \
              "\t\t\t</note>\n"
                                
    return output
