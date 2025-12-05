def read_input():
    with open('input.txt', 'r') as f:
        ranges = []
        ingredients = []
        while line := f.readline() :
            line = line.replace("\n", "")
            if "-" in line:
                _range = line.split('-')
                ranges.append((int(_range[0]), int(_range[1])))
            elif line != "":
                ingredients.append(int(line))
        return ranges, ingredients


def main():
    ranges, ingredients = read_input()

    count = 0

    for ingredient in ingredients:
        for lower, upper in ranges:
            if lower <= ingredient <= upper:
                count += 1
                break
    return count


if __name__ == '__main__':
    result = main()
    print(result)
