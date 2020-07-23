import const
from math import log2, pow

A4 = 440
C0 = A4*pow(2, -4.75)
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
def pitch(freq):
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    return notes[n] + str(octave)

def freq(name):
    if name[1] == '#':
        octave = int(name[2:])
        steps = notes.index(name[0:2].upper())
    else:
        octave = int(name[1])
        steps = notes.index(name[0].upper())
    print(octave, steps)
    return (C0*(2**octave))*(2**(steps/12))

class Note:
    """ Supplies a class to define a note object """

    def __init__(self, pitch=None, duration=None):
        self._pitch = pitch
        self._duration = duration
    
    def pitch(self):
        return str(self._pitch)
    
    def duration(self):
        return str(self._duration)
    
    def __str__(self):
        return f'Note with pitch {self.pitch()} and duration {self.duration()}'


class TabNote:
    """ Supplies a class to define a tab note object """

    def __init__(self, string=None, number=None):
        self._string = string
        self._number = number
    
    def __str__(self):
        return f'Tab note with string {self._string} and duration {self._number}'


class Tab:
    """ Supplies a class to generate guitar tabs from a list of note """

    def __init__(self, notes=None):
        self.notes = notes

    def generate(self):
        pass

    def _get_tab_note(self, pitch):
        pass
        

if __name__ == '__main__':
    print(freq("A#14"))