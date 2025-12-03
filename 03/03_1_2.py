def read_input():
    with open('input.txt', 'r') as f:
        return [list(map(lambda x: int(x), list(bank[:-1]))) for bank in f.readlines()]


def find_batteries(bank: list[int], size: int):
    current_battery = (0, 0)

    if len(bank) == size:
        return int("".join([str(battery) for battery in bank]))

    for index, battery in enumerate(bank[:-size+1]):
        if battery > current_battery[0]:
            current_battery = (battery, index)

    if size == 1:
        return max(bank)

    return (10**(size-1)) * current_battery[0] + find_batteries(bank[current_battery[1]+1:], size-1)

def main():
    banks = read_input()
    part1 = sum([find_batteries(bank, 2) for bank in banks])
    part2 = sum([find_batteries(bank, 12) for bank in banks])
    return part1, part2


if __name__ == '__main__':
    result = main()
    print(result)