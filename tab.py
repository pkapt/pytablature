import const
from math import log2, pow

class Converter:
    A4 = 440
    C0 = A4*pow(2, -4.75)
    NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
    def __init__(self):
        pass

    def pitch(self, freq):
        h = round(12*log2(freq/self.C0))
        octave = h // 12
        n = h % 12
        return self.NOTES[n] + str(octave)

    def freq(self, name):
        if name[1] == '#':
            octave = int(name[2:])
            steps = self.NOTES.index(name[0:2].upper())
        else:
            octave = int(name[1])
            steps = self.NOTES.index(name[0].upper())
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

    def __init__(self, string_num=None, fret_num=None):
        self._string_num = string_num
        self._fret_num = fret_num
    
    def string_num(self):
        return self._string_num

    def fret_num(self):
        return self._fret_num
    
    def __str__(self):
        return f'Tab note with string {self._string_num} and fret {self._fret_num}'

class Staff:
    """ Supplies a class to create a staff object """

    NOTE_SPACING = 3

    def __init__(self):
        self.staff = [["-" for _ in range(100)] for _ in range(6)]
        self.pos = self.NOTE_SPACING
    
    def add_note(self, note):
        self.staff[note.string_num() - 1][self.pos] = str(note.fret_num())
        self.pos += self.NOTE_SPACING
    
    def __str__(self):
        for line in self.staff:
            for note in line:
                print(note, end="")
            print("")
        return ""


class Tab:
    """ Supplies a class to generate guitar tabs from a list of note """

    def __init__(self, notes=None):
        self.notes = notes

    def generate(self):
        self.tab_notes = [self.convert_pitch_to_tab(note) for note in notes]
        self.staff = Staff()

        for note in self.tab_notes:
            self.staff.add_note(note)

        print(self.staff)

    def convert_pitch_to_tab(self, pitch):
        c = Converter()
        freq = c.freq(pitch.pitch())
        matches = []
        for string_num, string_note,  in enumerate(const.GUITAR_TUNING):
            for step in range(const.GUITAR_FRETS):
                guitar_freq = c.freq(string_note) * (2**(step/12))
                if round(guitar_freq, 1) == round(freq, 1):
                    matches.append(TabNote(string_num + 1, step))
        if matches:
            lowest = TabNote(0, 24)
            for match in matches:
                fret_num = match.fret_num()
                if fret_num < lowest.fret_num():
                    lowest = match
            return lowest
        
    def _print_note(self, note):
        for i in range(1,7):
            if i == note.string_num():
                pass
        

if __name__ == '__main__':
    notes = [Note("C3", const.QUARTER), 
             Note("D3", const.QUARTER),
             Note("E3", const.QUARTER),
             Note("F3", const.QUARTER),
             Note("G3", const.QUARTER),
             Note("A3", const.QUARTER),
             Note("B3", const.QUARTER),
             Note("C4", const.QUARTER)]

    tab = Tab(notes)
    tab.generate()
