"""Dessiner le sapin en remplaçant les pixels 1 par des étoiles."""
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]


def display_picture(picture):
    for row in picture:
        for pixel in row:
            print("*" if pixel == 1 else " ", end="")
        print()


if __name__ == "__main__":
    display_picture(picture)
