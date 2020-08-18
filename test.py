from tab import Tab
from tab import Note
from tab import const

if __name__ == '__main__':
    notes = [Note("C3", const.QUARTER), 
             Note("D3", const.QUARTER),
             Note("E3", const.QUARTER),
             Note("F3", const.QUARTER),
             Note("G3", const.QUARTER),
             Note("A3", const.QUARTER),
             Note("B3", const.QUARTER),
             Note("C4", const.QUARTER),
             Note("C3", const.QUARTER), 
             Note("D3", const.QUARTER),
             Note("E3", const.QUARTER),
             Note("F3", const.QUARTER),
             Note("G3", const.QUARTER),
             Note("A3", const.QUARTER),
             Note("B3", const.QUARTER),
             Note("C4", const.QUARTER)]

    tab = Tab(notes)
    tab.generate()
