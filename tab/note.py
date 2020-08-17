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