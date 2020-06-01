import mingus.core.notes as notes
from midiutil.MidiFile import MIDIFile
MyMIDI = MIDIFile(1)
track = 0
time = 0

channel = 0
pitch = 60
duration = 10
volume = 100
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time,120)

binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
