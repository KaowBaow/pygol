from tile import Tile


class Field:
    def __init__(self, size: int):
        self.size: int = size
        self.tiles: list = self._build()

    def _build(self) -> list:
        listOfList = []
        for y in range(self.size):
            subList = []
            for x in range(self.size):
                subList.append(Tile(x, y, 0, 0))

            listOfList.append(subList)

        return listOfList

    def get_neighbours(self, y_cord: int, x_cord: int) -> list:
        neighbours = []
        for row in range(y_cord - 1, y_cord + 2):
            # print(row)
            if 0 < row < self.size:
                # print("row in bounds")
                for neighbour in range(x_cord - 1, x_cord + 2):
                    # print(f"Neighbour {neighbour}")
                    if 0 < neighbour < self.size:
                        # print("neighbour in bounds")
                        neighbours.append(self.tiles[row][neighbour])

        return neighbours

    def count_neighbours(self, x: int, y: int) -> int:
        count = 0
        for n in self.get_neighbours(y, x):
            if isinstance(n, Tile):
                count += n.get_status()

        return count

    def advance(self) -> None:
        new_fields = []
        for row in self.tiles:
            new_rows = []
            for tile in row:
                x, y = tile.get_cords()
                num = self.count_neighbours(x, y)
                state = tile.get_status()
                if state:
                    if 3 <= num <= 4:
                        new_rows.append(Tile(x, y, 1, 0))
                    else:
                        new_rows.append(Tile(x, y, 0, 1))
                else:
                    if num == 3:
                        new_rows.append(Tile(x, y, 1, 1))
                    else:
                        new_rows.append(Tile(x, y, 0, 0))

            new_fields.append(new_rows)

        self.tiles = new_fields
