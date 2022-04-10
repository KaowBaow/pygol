class Tile:
    def __init__(self, x_cord: int, y_cord: int, status: int, changed: int):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.status = status
        self.changed = changed

    def get_status(self) -> int:
        return self.status

    def set_status(self, state: int) -> None:
        self.status = state
        self.changed = 1

    def get_cords(self) -> tuple:
        return (self.x_cord, self.y_cord)

    def get_index(self) -> int:
        return self.index

    def show(self) -> str:
        if self.get_status():
            return "X"
        else:
            return " "

    def switch_status(self) -> None:
        if self.status:
            self.set_status(0)
        else:
            self.set_status(1)
