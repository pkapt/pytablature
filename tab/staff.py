from .const import *

class Staff:
    """ Supplies a class to create a staff object """

    NOTE_SPACING = 3
    STAFF_LENGTH = 100

    def __init__(self):
        self.staff = [["-" for _ in range(self.STAFF_LENGTH)] for _ in range(NUM_STRINGS)]
        self.pos = self.NOTE_SPACING
        self.beat_within_measure = 0
    
    def add_note(self, tab_note, note):
        self.staff[tab_note.string_num() - 1][self.pos] = str(tab_note.fret_num())
        self.pos += self.NOTE_SPACING
        self.beat_within_measure += float(4/int(note.duration()))

        if self.beat_within_measure == 4:
            for i in range(NUM_STRINGS):
                self.staff[i][self.pos] = '|'
            self.beat_within_measure = 0
            self.pos += self.NOTE_SPACING
    
    def __str__(self):
        for line in self.staff:
            for note in line:
                print(note, end="")
            print("")
        return ""