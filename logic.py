from field import Field


def main():
    f = Field(10)
    f.show()
    f.tiles[1][1].set_status(1)
    f.show()

    print(f.count_neighbours(f.tiles[0][0]))
    print(f.count_neighbours(f.tiles[0][1]))
    print(f.count_neighbours(f.tiles[0][2]))
    print(f.count_neighbours(f.tiles[1][0]))
    print(f.count_neighbours(f.tiles[1][2]))
    print(f.count_neighbours(f.tiles[2][0]))
    print(f.count_neighbours(f.tiles[2][1]))
    print(f.count_neighbours(f.tiles[2][2]))
    print(f.count_neighbours(f.tiles[1][1]))
