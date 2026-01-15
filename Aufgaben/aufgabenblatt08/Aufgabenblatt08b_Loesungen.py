import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

#%%
def dfs(maze, x, y, end_x, end_y, path):
    if (x, y) == (end_x, end_y):
        path.append((x, y))
        maze[x][y] = '.'
        return True

    #Mauer oder schon probiert
    if maze[x][y] != ' ':
        return False

    # Schon da gewesen
    maze[x][y] = '.'
    path.append((x, y))


    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # Grenzen prüfen
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if dfs(maze, nx, ny, end_x, end_y, path):
                return True

    # Dead-End markieren
    maze[x][y] = 'X'
    path.pop()
    return False


def print_maze(maze, start, end):
    color_map = {'#': 0, ' ': 1, '.': 2, 'S': 3, 'E': 4, 'X': 5}
    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'
    maze_color = np.array([[color_map[cell] for cell in row] for row in maze])
    cmap = ListedColormap(['black', 'white', 'lime', 'blue', 'red', 'gray'])

    plt.figure(figsize=(10, 5))
    plt.imshow(maze_color, cmap=cmap, interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()

# Gegebenes Labyrinth
maze = [
    "######################",
    "#       #           ##",
    "# #### # ##### ##### #",
    "#    # #     #     # #",
    "# # ## # ### ##### # #",
    "# # ## #     #     # #",
    "# # ## ##### ####### #",
    "# #           #      #",
    "####### ########## ###",
    "#                   ##",
    "######################"
]

# Definiert den Start- und Endpunkt
maze = [list(row) for row in maze]
starts_ends = [((1, 15), (9, 17)), ((1, 2), (9, 17))]

# Prüft, ob ein Weg gefunden worden ist.
for start, end in starts_ends:
    path = []
    if dfs(maze, *start, *end, path):
        print("Weg gefunden von", start, "nach", end)
        print_maze(maze, start, end)
    else:
        print("Kein Weg gefunden von", start, "nach", end)

    # Labyrinth zurücksetzen
    maze = [list(row) for row in [
        "######################",
        "#       #           ##",
        "# #### # ##### ##### #",
        "#    # #     #     # #",
        "# # ## # ### ##### # #",
        "# # ## #     #     # #",
        "# # ## ##### ####### #",
        "# #           #      #",
        "####### ########## ###",
        "#                   ##",
        "######################"
    ]]

def test_mazes(mazes, starts_ends_list):
    results = []
    for maze, starts_ends in zip(mazes, starts_ends_list):
        original_maze = [list(row) for row in maze]
        for start, end in starts_ends:
            path = []
            maze = [row[:] for row in original_maze]
            if dfs(maze, *start, *end, path):
                results.append((start, end, True))
            else:
                results.append((start, end, False))
    return results


mazes = [
    [
        "###############",
        "#             #",
        "# ##### #######",
        "# #   #       #",
        "# # # ####### #",
        "# # #       # #",
        "# # ####### # #",
        "# #       # # #",
        "# ######### # #",
        "#           # #",
        "# ########### #",
        "#             #",
        "# #############",
        "#             #",
        "###############"
    ],
    [
        "###############",
        "#             #",
        "# ##### ##### #",
        "# #   #     # #",
        "# # ### ### # #",
        "# # #       # #",
        "# # # ##### # #",
        "# # # #   # # #",
        "# # # # # ### #",
        "# # # # #     #",
        "# # # # #######",
        "# #     #     #",
        "# ########### #",
        "#             #",
        "###############"
    ]
]

starts_ends_list = [
    [((1, 1), (13, 13)), ((1, 13), (13, 1))],
    [((1, 1), (13, 13)), ((1, 13), (13, 1))]
]

test_results = test_mazes(mazes, starts_ends_list)

for result in test_results:
    print(f"Path from {result[0]} to {result[1]} found: {result[2]}")
