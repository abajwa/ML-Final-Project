#from music21 import *
from Note import *

#<score-partwise>
#<movement-title></movement-title>
#Need <part-list>
  #Need <score-part>s
    #<part-name>
    #<part-abbreviation>
    #<score-instrument id=P#-I#>
      #<instrument-name>
    #<midi-instrument id=P#-I#>
      #<midi-channel>#
      #<midi-program>#
#<part id="P#">
  #<measure number="#">
    #<attrivutes>
    #<time>
      #<beats>
      #<beat-type>
    #<note>
      #<pitch>
        #<step>A|B|C|D|E|F|G</step>
        #<alter>-1|1</alter>
        #<octave>1-8</octave>
      #<duration>1,2,4,8,16
      #<voice>1</
      #<type>quarter|eighth|16th

def makeNoteMatrix(parts):
  nm = [ [0 for i in range(0,57)] for j in range(0,57) ]
  noteCount = [0 for i in range(0,57)]
  for part in parts:
  	nm[0][noteIndex(part[0].note,part[0].octave)] = nm[0][noteIndex(part[0].note,part[0].octave)] + 1
  	noteCount[0] = noteCount[0] + 1
  	for i in range(1,len(part)):
  		nm[noteIndex(part[i-1].note,part[i-1].octave)][noteIndex(part[i].note,part[i].octave)] = nm[noteIndex(part[i-1].note,part[i-1].octave)][noteIndex(part[i].note,part[i].octave)] + 1
  		noteCount[noteIndex(part[i].note,part[i].octave)] = noteCount[noteIndex(part[i].note,part[i].octave)] + 1
  numNotes = sum(noteCount)
  for i in range(0,57):
  	for j in range(0,57):
  		if noteCount[i] != 0:
	  		nm[i][j] = float(nm[i][j])/noteCount[i]
  		if j != 0:
  			nm[i][j] = nm[i][j-1] + nm[i][j]
  return nm

def noteIndex(note, octave):
  if note == 'R':
    return 0
  elif note == 'A':
    return 1 + (int(octave)-1)*7
  elif note == 'B':
    return 2 + (int(octave)-1)*7
  elif note == 'C':
    return 3 + (int(octave)-1)*7
  elif note == 'D':
    return 4 + (int(octave)-1)*7
  elif note == 'E':
    return 5 + (int(octave)-1)*7
  elif note == 'F':
    return 6 + (int(octave)-1)*7
  elif note == 'G':
    return 7 + (int(octave)-1)*7

def getTimeSignature(f):
  i=0
  while not 'time' in f[i]:
      i = i+1
  i = i+1
  beats = f[i].split('>')[1].split('<')[0]
  i += 1
  beatType = f[i].split('>')[1].split('<')[0]
    
  return [beats, beatType]

def writeTop(f):
  # list of the labels of each part in the midi file
  parts = ["Soprano", "Alto", "Tenor", "Bass"]

  # prints out the data for each part
  f.write('<score-partwise>\n' + \
            '\t<part-list>\n');

  i = 1
  for part in parts:
    f.write('\t\t<score-part id="P' + str(i) + '">\n' \
              '\t\t\t<part-name>' + part + '</part-name>\n' + \
              '\t\t\t<part-abbreviation>' + part[0] + '</part-abbreviation>\n' + \
              '\t\t\t<score-instrument id="P' + str(i) + '-I' + str(i) + '">\n' + \
                '\t\t\t\t<instrument-name>Instrument ' + str(i) + '</instrument-name>\n' + \
              '\t\t\t</score-instrument>\n' + \
              '\t\t\t<midi-instrument id="P' + str(i) + '-I' + str(i) + '">\n' + \
                '\t\t\t\t<midi-channel>' + str(i) + '</midi-channel>\n' + \
                '\t\t\t\t<midi-program>1</midi-program>\n' + \
              '\t\t\t</midi-instrument>\n' + \
            '\t\t</score-part>\n')
    i += 1
    
  f.write('\t</part-list>\n')


# writes a whole song to an xml file given the file and a list of notes
def writeSong(f, notes):
  writeTop(f)

  measureNumber = 1
  measureCompletion = 0
  partNumber = 1
  newMeasure = 1
  # for each part
  for part in notes:
    f.write('\t<part id ="P' + str(partNumber) + '">\n')
    measureNumber = 1
    f.write( '\t\t<measure number="0">\n' + \
                '\t\t\t<attributes>\n' + \
                  '\t\t\t\t<divisions>4</divisions>\n' + \
                  '\t\t\t\t<key>\n' + \
                    '\t\t\t\t\t<fifths>-1</fifths>\n' + \
                    '\t\t\t\t\t<mode>major</mode>\n' + \
                  '\t\t\t\t</key>\n' + \
                  '\t\t\t\t<time symbol="common">\n' + \
                    '\t\t\t\t\t<beats>4</beats>\n' + \
                    '\t\t\t\t\t<beat-type>4</beat-type>\n' + \
                  '\t\t\t\t</time>\n' + \
             '\t\t\t</attributes>\n' + \
             '\t\t\t<sound tempo="76"/>\n' + \
           '\t\t</measure>\n')

    measureNumber = 1
    measureCompletion = 0
    newMeasure = 1
  
    for note in part:
      if newMeasure == 1:
        f.write('\t\t<!--=======================================================-->\n')
        f.write('\t\t<measure number="' + str(measureNumber) + '">\n')
        newMeasure = 0

      f.write(note.printNote() + '\n')

      # adds to the measure completion depending on the note type
      if 'quarter' in note.time:
        measureCompletion += 0.25
      elif 'eighth' in note.time:
        measureCompletion += 0.125
      elif '16th' in note.time:
        measureCompletion += 0.0625
      # a measure is complete when the note count = 1
      if measureCompletion == 1.0:
        f.write('\t\t</measure>\n')
        measureCompletion = 0
        measureNumber += 1
        newMeasure = 1
    f.write('\t\t</measure>\n\t\t</part>\n')
    partNumber += 1
  f.write('</score-partwise>')
  
def readFile(f):
  noteList = []
  i = 0

  # finds where the first part starts - skips all the other part id stuff at the beginning of the xml file
  while i < len(f) and not '<part id=' in f[i]:
    i += 1

  part = []
  # reads through the whole file
  while i < len(f):
      
      # while not at the end of the file and the keyword note is not found, increment the line number
      while i < len(f) and not 'note' in f[i]:
          i += 1
          # if the part id changes then append the previous to the list
          if i < len(f) and '<part id=\"' in f[i]:
            noteList.append(part)
            part = []

      # attributes for each note
      step = "R"
      alter = 0
      octave = 0
      time = 'quarter'
      duration = 0
      
      # get the above attributes for each note while /note is not yet encountered
      while i < len(f) -1 and not '/note' in f[i]:
          i += 1
          if 'step' in f[i]:
              step = f[i].split('>')[1].split('<')[0]
          elif 'alter' in f[i]:
              alter = f[i].split('>')[1].split('<')[0]
          elif 'octave' in f[i]:
              octave = f[i].split('>')[1].split('<')[0]
          elif 'type' in f[i]:
              time = f[i].split('>')[1].split('<')[0]
          elif 'duration' in f[i]:
              duration = f[i].split('>')[1].split('<')[0]
      # increment the row number one more time to skip the /note line since it is the current
      # line at this point
      i = i+1
      # add the note to the list of notes
      if i < len(f):
          part.append(Note(step, octave, time, alter))
  noteList.append(part)
  return noteList


f = open('blah.xml').readlines()

ts = getTimeSignature(f)

#print ts

notes = readFile(f)

# prints the number of notes in each part
#print len(notes[0])
#print len(notes[1])
#print len(notes[2])
#print len(notes[3])
#print len(notes[4])

probMat = makeNoteMatrix(notes)

fi = open('test.xml', 'w')
writeSong(fi, notes)

fi.close()
