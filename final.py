#from music21 import *
from Score import *
from Part import *
from Measure import *
from Note import *
from random import *
import os, sys

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
########################################################################################################
def makeNoteMatrix(parts):
  nm = [ [0 for i in range(0,57)] ]
  for i in range(0,56):
    tm = [0]
    for j in range(0,8):
      if i/7 == j:
        tm += [2 for x in range(0,7)]
      elif abs(i/7-j) == 1:
        tm += [1 for x in range(0,7)]
      else:
        tm += [0 for x in range(0,7)]
    nm.append(tm)
  for part in parts:
    notes = part.getNotes()
    nm[0][noteIndex(notes[0].note,notes[0].octave)] += 10
    for i in range(1,len(notes)):
      	nm[noteIndex(notes[i-1].note,notes[i-1].octave)][noteIndex(notes[i].note,notes[i].octave)] += 10
  for i in range(0,57):
    count = sum(nm[i])
    for j in range(0,57):
      if count != 0:
        nm[i][j] = float(nm[i][j])/count
      if j != 0:
        nm[i][j] += nm[i][j-1]
  return nm

########################################################################################################
def makeTimeMatrix(parts):
  tm = [ [1 for i in range(0,5)] for j in range(0,5)]
  for part in parts:
    notes = part.getNotes()
    for i in range(1,len(notes)):
      tm[timeIndex(notes[i-1].time)][timeIndex(notes[i].time)] += 10
    for i in range(0,5):
      count = sum(tm[i])
      for j in range(0,5):
        if count != 0:
          tm[i][j] = float(tm[i][j])/count
        if j != 0:
          tm[i][j] += tm[i][j-1]
  return tm

########################################################################################################
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

########################################################################################################
def indexToNote(index):
  if index == 0:
    return Note('R', 0)
  elif index%7 == 1:
    n = 'A'
  elif index%7 == 2:
    n = 'B'
  elif index%7 == 3:
    n = 'C'
  elif index%7 == 4:
    n = 'D'
  elif index%7 == 5:
    n = 'E'
  elif index%7 == 6:
    n = 'F'
  elif index%7 == 0:
    n = 'G'
  o = (index-1)/7 + 1
  return Note(n,o)

########################################################################################################
def timeIndex(time):
  if time == '16th':
    return 0
  if time == 'eighth':
    return 1
  if time == 'quarter':
    return 2
  if time == 'half':
    return 3
  if time == 'whole':
    return 4

########################################################################################################
def indexToTime(index):
  if index == 0:
    return '16th'
  if index == 1:
    return 'eighth'
  if index == 2:
    return 'quarter'
  if index == 3:
    return 'half'
  if index == 4:
    return 'whole'

########################################################################################################
def timeToDecimal(time):
  if time == '16th':
    return 1.0/16.0
  if time == 'eighth':
    return 1.0/8.0
  if time == 'quarter':
    return .25
  if time == 'half':
    return .5
  if time == 'whole':
    return 1.0

########################################################################################################
def timeToDuration(time):
  if time == '16th':
    return 1
  if time == 'eighth':
    return 2
  if time == 'quarter':
    return 4
  if time == 'half':
    return 8
  if time == 'whole':
    return 16

########################################################################################################
def getTimeSignature(f):
  i=0
  while not 'time' in f[i]:
      i = i+1
  i = i+1
  beats = f[i].split('>')[1].split('<')[0]
  i += 1
  beatType = f[i].split('>')[1].split('<')[0]
    
  return [beats, beatType]

########################################################################################################
def readFile(f):
  partsList = []
  i = 0
  partNum = 1
  
  while i < len(f) and '<part id=\"' not in f[i]:
    # finds the parts
    if '<score-part id=' in f[i]:
      # finds the name of the part
      while i < len(f) and '<part-name>' not in f[i]:
        i += 1
      partName = f[i].split('>')[1].split('<')[0]
      # create a part at this point
      partsList.append(Part(partNum, partName , []))
      partNum += 1
      
    i += 1


  # at this point i contains the line number of the first part id
  partNum = 1
  i += 1
  measureNumber = 0
  while i < len(f):
    if '<part id=\"' in f[i]:
      partNum += 1
      measureNumber = 0

    if '<measure' in f[i]:
      # create a new measure
      partsList[partNum-1].addMeasure(Measure(measureNumber, []))

      # while it is still in the same measure
      while i < len(f) and not '/measure' in f[i]:
        if '<note' in f[i]:
          # create a new note
          step = "R"
          alter = 0
          octave = 0
          time = 'quarter'
          duration = 0

          while i < len(f) -1 and not '/note' in f[i]:
            i += 1
            if '<step' in f[i]:
              step = f[i].split('>')[1].split('<')[0]
            elif '<alter' in f[i]:
              alter = f[i].split('>')[1].split('<')[0]
            elif '<octave' in f[i]:
              octave = f[i].split('>')[1].split('<')[0]
            elif '<type' in f[i]:
              time = f[i].split('>')[1].split('<')[0]
            elif '<duration' in f[i]:
              duration = f[i].split('>')[1].split('<')[0]
          # /note has been found at this point
          # create the note and add it to the measure
          partsList[partNum-1].measures[measureNumber].addNote(Note(step, octave, time, duration, alter))
        i += 1
      measureNumber += 1
      
    i += 1

#  print i
#  print "PART NUM: " + str(partNum)

#  print "Measures in part 1: " + str(len(partsList[0].measures))
#  print "Notes in part 2 measure 1: " + str(len(partsList[4].measures[20].notes))
  #print partsList[0].measures[0].notes[0].printNote()

  return Score(partsList)

########################################################################################################
def getRandomNote(pMatNote,pMatTime, prevNote):
  r = random()
  pi = noteIndex(prevNote.note, prevNote.octave)
  nextIndex = 0
  i=0
  while r > pMatNote[pi][i] and i < 56:
    i += 1
  nextNote = indexToNote(i)
  r = random()
  pi = timeIndex(prevNote.time)
  i=0
  while r > pMatTime[pi][i] and i < 4:
    i += 1
  nextNote.time = indexToTime(i)
  nextNote.duration = timeToDuration(nextNote.time)
  return nextNote

########################################################################################################
def startingNote(part,numParts):
  return randint(int(56.0/numParts*part), int(56.0/numParts*(part+1)))

########################################################################################################
def makeScore(pMatNote,pMatTime,numParts=4,numMeasures=30):
  parts = []
  for i in range(0,numParts):
    nn = indexToNote( startingNote(i,numParts) )
    #print nn.note,nn.octave
    measures = []
    for j in range(0,numMeasures):
      measure = Measure(j, [])
      noteTime = 0.0
      while noteTime < 1.0:
        nn = getRandomNote(pMatNote,pMatTime,nn)

        # if the part is not the first, generate an acceptable note
        if i > 0:
          while not acceptableNote(parts[0][,nn):
            nn = getRandomNote(pMatNote,pMatTime,nn)
        if timeToDecimal(nn.time)+noteTime <= 1.0:
          measure.addNote(nn)
          noteTime += timeToDecimal(nn.time)
      measures.append(measure)
    parts.append(Part(i,'Instrument '+str(i),measures))
  return Score(parts)

########################################################################################################
def acceptableNote(note1, note2):
    n1Index = noteIndex(note1, note1.octave) % 7 
    n2Index = noteIndex(note2, note2.octave) % 7
  # The notes are an acceptable combination if:
    # 1. it is not within 1 note from the other. ex. A and G are not acceptable neither are A and B
    if (n1Index - n2Index) == 1 or (n2Index - n1Index) == 1:
      return 0

f = open('blah.xml').readlines()

ts = getTimeSignature(f)

#print ts

song = readFile(f)

parts = song.parts

#path = 'music/'
#files = os.listdir(path)
#for file in files:
#  song = readFile(file)
#  parts += song.parts

probMat = makeNoteMatrix(parts)
timeMat = makeTimeMatrix(parts)

#print probMat
#print timeMat

song = makeScore(probMat, timeMat, 4)

ofile = sys.argv[1]

fi = open(ofile, 'w')
fi.write(song.printScore())

fi.close()

#from music21 import converter
#converter.parse(ofile).show()
