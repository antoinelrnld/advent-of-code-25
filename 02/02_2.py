def read_input():
    with open('input.txt') as f:
        file_content = f.readline()
        id_ranges = file_content.split(',')
        return [id_range.split('-') for id_range in id_ranges]


def is_invalid(number: int):
    for n in range(len(str(number))//2, 0, -1):
        parts = [str(number)[j:j+n] for j in range(0, len(str(number)), n)]
        if all([part == parts[0] for part in parts]):
            return True
    return False


def main():
    id_ranges = read_input()

    total = 0

    for lower, upper in id_ranges:
        for i in range(int(lower), int(upper)+1):
            if is_invalid(i):
                total += i
                    
    return total

if __name__ == '__main__':
    result = main()
    print(result)