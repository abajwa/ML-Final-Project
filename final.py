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


  
def readFile(f):
  noteList = []
  i = 114

  part = []
  # reads through the whole file
  while i < len(f):
      # while not at the end of the file and the keyword note is not found, increment the line number
      while i < len(f) and not 'note' in f[i]:
          i += 1
          # if the part id changes then append the previous to the list
          if i < len(f) and 'part id' in f[i]:
            noteList.append(part)
            part = []
        
      # attributes for each note
      step = "R"
      alter = 0
      octave = 0
      time = ''
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

print ts

notes = readFile(f)

print len(notes[0])
print len(notes[1])
print len(notes[2])
print len(notes[3])
print len(notes[4])

makeNoteMatrix(notes)

#nl = readFile(f)


#</score-partwise>
