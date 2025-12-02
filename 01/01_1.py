def read_input():
    with open('input.txt', 'r') as f:
        return f.readlines()

def main():
    dial_inputs = read_input()

    rotations = [(dial_input[0], int(dial_input[1:])) for dial_input in dial_inputs]

    dial_value = 50
    stops_at_zero = 0

    for direction, steps in rotations:
        if direction == 'L':
            dial_value = (dial_value - steps) % 100
        else:
            dial_value = (dial_value + steps) % 100
        if dial_value == 0:
            stops_at_zero += 1

    return stops_at_zero


if __name__ == '__main__':
    result = main()
    print(result)


