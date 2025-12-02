def read_input():
    with open('input.txt', 'r') as f:
        return f.readlines()

def main():
    dial_inputs = read_input()

    rotations = [(dial_input[0], int(dial_input[1:])) for dial_input in dial_inputs]

    dial_value = 50
    ticks_at_zero = 0

    for direction, steps in rotations:
        if direction == 'L':
            dist = dial_value if dial_value != 0 else 100
            ticks_at_zero += 1 + (steps - dist) // 100 if steps >= dist else 0
            dial_value = (dial_value - steps) % 100
        else:
            dist = 100 - dial_value
            if dist == 0:
                dist = 100
            ticks_at_zero += 1 + (steps - dist) // 100 if steps >= dist else 0
            dial_value = (dial_value + steps) % 100

    return ticks_at_zero


if __name__ == '__main__':
    result = main()
    print(result)


