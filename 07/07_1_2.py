def read_input():
    with open("input.txt") as f:
        return [list(line.strip()) for line in f]


def transform_line(signal_positions: list[int], line: list[str], timelines: list[int]):
    splits = 0

    for signal_position in signal_positions:
        if line[signal_position] == '.':
            line[signal_position] = '|'

        if line[signal_position] == '^':
            line[signal_position - 1] = '|'
            line[signal_position + 1] = '|'
            splits += 1

            timelines[signal_position - 1] = timelines[signal_position - 1] + timelines[signal_position]
            timelines[signal_position + 1] = timelines[signal_position] + timelines[signal_position + 1]
            timelines[signal_position] = 0

    return splits, timelines


def main():
    lines = read_input()

    timelines = [0] * len(lines[0])
    timelines[lines[0].index('S')] = 1
    total_splits = 0

    for i in range(1, len(lines)):
        signal_positions = [idx for idx, char in enumerate(lines[i-1]) if char in ['S', '|']]
        splits, timelines = transform_line(signal_positions, lines[i], timelines)
        total_splits += splits

    for l in lines:
        print("".join(l))

    return total_splits, timelines


if __name__ == '__main__':
    total_splits, timelines = main()

    print(total_splits, sum(timelines))
