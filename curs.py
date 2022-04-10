from curses import textpad, wrapper, curs_set
import time
import os
from field import Field


def main(window):
    curs_set(0)
    cols, rows = os.get_terminal_size()
    rec_rows = min(round(cols / 2) - 2, rows) - 1
    rec_cols = (rec_rows * 2) + 3
    board_size = rec_rows - 1
    textpad.rectangle(window, 0, 0, rec_rows, rec_cols)
    window.refresh()
    board = Field(board_size)

    template = open("templates/glider", "r").readlines()

    for row in template:
        y, x = row.split(',')
        board.tiles[int(y)][int(x)].set_status(1)

    changed = 1
    while changed:
        changed = 0
        for row in board.tiles:
            for tile in row:
                if tile.changed:
                    changed = 1
                    window.addstr(
                        tile.y_cord + 1,
                        tile.x_cord * 2 + 1,
                        tile.show()
                    )
        window.refresh()
        board.advance()
        time.sleep(0.2)


if __name__ == "__main__":
    wrapper(main)
