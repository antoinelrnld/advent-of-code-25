def read_input():
    with open('input.txt', 'r') as f:
        ranges = []
        while line := f.readline() :
            line = line.replace("\n", "")
            if "-" in line:
                _range = line.split('-')
                ranges.append((int(_range[0]), int(_range[1])))
        return ranges


def main():
    ranges = read_input()
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    ranges_no_overlap = [sorted_ranges[0]]
    
    count = 0

    for i in range(1, len(sorted_ranges)):
        low1, up1 = ranges_no_overlap[-1]
        low2, up2 = sorted_ranges[i]

        if low2 <= up1 and up1 <= up2:
            ranges_no_overlap[-1] = (low1, up2)
        elif low2 <= up1 and up1 >= up1:
            ranges_no_overlap[-1] = (low1, up1)
        else:
            ranges_no_overlap.append((low2, up2))

    for _range in ranges_no_overlap:
        count += _range[1] - _range[0] + 1

    return count


if __name__ == '__main__':
    result = main()
    print(result)
