# repeat what I say but in a different language

# use a phrase database, so that 'translation' is at least grammatically correct (?)
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr


def main(keyword):
    keyseconds = 3  # Duration of recording
    phraseseconds = 10
    keyname = "key"
    phrasename = "phrase"
    startRecording(keyseconds, fs, keyname)
    text = analyzeSpeech(name)
    # if text contains keyword start recording
    playBeep();
    startRecording(phraseseconds, phrasename)
    
def startRecording(seconds, name):
    # if existing file exists with same name, delete
    fs = 44100
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(name + '.wav', fs, myrecording)

def analyzeSpeech(name):
    r = sr.Recognizer()
    recording = sr.AudioFile(name + '.wav')
    with recording as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text



def getMostSimilar(text):


def playBeep():


main()
