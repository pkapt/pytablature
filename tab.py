import const
from math import log2, pow

class Converter:
    A4 = 440
    C0 = self.A4*pow(2, -4.75)
    NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    def pitch(freq):
        h = round(12*log2(freq/self.C0))
        octave = h // 12
        n = h % 12
        return self.NOTES[n] + str(octave)

    def freq(name):
        if name[1] == '#':
            octave = int(name[2:])
            steps = self.NOTES.index(name[0:2].upper())
        else:
            octave = int(name[1])
            steps = self.NOTES.index(name[0].upper())
        print(octave, steps)
        return (self.C0*(2**octave))*(2**(steps/12))

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

    def __init__(self, _string_num=None, _fret_num=None):
        self._string_num = _string_num
        self._fret_num = _fret_num
    
    def string_num(self):
        return self._string_num

    def fret_num(self):
        return self._fret_num
    
    def __str__(self):
        return f'Tab note with string {self._string_num} and duration {self._fret_num}'


class Tab:
    """ Supplies a class to generate guitar tabs from a list of note """

    def __init__(self, notes=None):
        self.notes = notes

    def generate(self):
        pass

    def _convert_pitch_to_tab(self, pitch):
        freq = Converter.freq(pitch)
        matches = []
        for string_num, string_note,  in enumerate(const.GUITAR_TUNING):
            for step in const.GUITAR_FRETS:
                guitar_freq = string_note * (2**(step/12))
                if guitar_freq == freq:
                    matches.append(TabNote(string_num, step))
        
        
        

if __name__ == '__main__':
    print(freq("A#14"))