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