def read_input():
    with open('input.txt', 'r') as f:
        grid = []
        while line := f.readline():
            grid.append(list(line.replace('\n', '')))
        return grid


def main():
    grid = read_input()
    count = 0
    to_remove = []
    
    while True:
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                cell = grid[y][x]
                if cell == '@':
                    adjacent = [(y-1, x-1), (y-1, x), (y-1, x+1),
                                (y, x-1), (y, x+1),
                                (y+1, x-1), (y+1, x), (y+1, x+1)]
                    accessible = [adj for adj in adjacent
                                  if 0 <= adj[0] < len(grid)
                                  and 0 <= adj[1] < len(grid[y])]
                    n_neighbors = 0
                    for neighbor in accessible:
                        if grid[neighbor[0]][neighbor[1]] == '@':
                            n_neighbors += 1
                    if n_neighbors < 4:
                        count += 1
                        to_remove.append((y, x))
        if len(to_remove) == 0:
            return count

        for removable in to_remove:
            grid[removable[0]][removable[1]] = '.'
        to_remove = []


if __name__ == '__main__':
    result = main()
    print(result)