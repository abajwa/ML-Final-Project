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

def makeNoteMatrix():
  return [ [0 for i in range(0,57)] for j in range(0,57) ]

def noteIndex(note, octave):
  if note == 'rest':
    return 0
  elif note == 'A':
    return 1 + (octave-1)*7
  elif note == 'B':
    return 2 + (octave-1)*7
  elif note == 'C':
    return 3 + (octave-1)*7
  elif note == 'D':
    return 4 + (octave-1)*7
  elif note == 'E':
    return 5 + (octave-1)*7
  elif note == 'F':
    return 6 + (octave-1)*7
  elif note == 'G':
    return 7 + (octave-1)*7

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
  i = 0

  # reads through the whole file
  while i < len(f):

      # while not at the end of the file and the keyword note is not found, increment the line number
      while i < len(f) and not 'note' in f[i]:
          i += 1

      # attributes for each note
      step = ""
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
          noteList.append(Note(step, octave, time, alter))
  return noteList


f = open('blah.xml').readlines()

ts = getTimeSignature(f)

print ts

notes = readFile(f)

print len(notes)

print notes[len(notes)-1].printNote()


#nl = readFile(f)


#</score-partwise>
