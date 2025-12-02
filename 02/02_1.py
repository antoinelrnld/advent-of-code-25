def read_input():
    with open('input.txt') as f:
        file_content = f.readline()
        id_ranges = file_content.split(',')
        return [id_range.split('-') for id_range in id_ranges]


def main():
    id_ranges = read_input()

    total = 0

    for lower, upper in id_ranges:
        for i in range(int(lower), int(upper)+1):
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                total += i
    return total


if __name__ == '__main__':
    result = main()
    print(result)