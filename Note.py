class Note:
  def __init__(self,note, octave, time='quarter', alter=0):
    self.note = note
    self.octave = octave
    self.time = time
    self.alter = alter

  def printNote(self):
                #<note>
      #<pitch>
        #<step>A|B|C|D|E|F|G</step>
        #<alter>-1|1</alter>
        #<octave>1-8</octave>
      #<duration>1,2,4,8,16
      #<voice>1</
      #<type>quarter|eighth|16th
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
