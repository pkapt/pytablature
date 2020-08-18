from .const import *
from .note import Note
from .tabnote import TabNote
from .staff import Staff
from pitches import Converter


class Tab:
    """ Supplies a class to generate guitar tabs from a list of note """

    def __init__(self, notes=None):
        self.notes = notes

    def generate(self):
        self.tab_notes = [self.convert_pitch_to_tab(note) for note in self.notes]
        self.staff = Staff()

        for i, note in enumerate(self.tab_notes):
            self.staff.add_note(note, self.notes[i])

        print(self.staff)

    def convert_pitch_to_tab(self, pitch):
        c = Converter()
        freq = c.freq(pitch.pitch())
        matches = []
        for string_num, string_note,  in enumerate(GUITAR_TUNING, 1):
            for step in range(  GUITAR_FRETS):
                guitar_freq = c.freq(string_note) * (2**(step/12))
                if round(guitar_freq, 1) == round(freq, 1):
                    matches.append(TabNote(string_num, step))
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
