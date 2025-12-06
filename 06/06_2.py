def transpose(matrix: list[list]):
    transposed = []
    for j in range(len(matrix[0])):
        line = []
        for i in range(len(matrix)):
            line.append(matrix[i][j])
        transposed.append(line)
    return transposed


def read_input():
    with open('input.txt') as f:
        matrix = []
        while line := f.readline()[:-1]:
            matrix.append(line)
        t_matrix = transpose(matrix)

        str_lines = []
        for line in t_matrix:
            str_lines.append("".join(line))

        operations = [str_line[-1] for str_line in str_lines if str_line[-1] == '+' or str_line[-1] == '*']
        operands = [[]]

        i= 0
        for str_line in str_lines:
            str_line = str_line.replace(' ', '').replace('*', '').replace('+', '')
            if len(str_line) == 0:
                i+=1
                operands.append([])
            else:
                operands[i].append(int(str_line))

        return operands, operations


def main():
    operands, operations = read_input()

    result = 0

    for index, operation in enumerate(operations):
        sub_result = 0 if operation == '+' else 1
        for i in range(len(operands[index])):
            if operation == '+':
                sub_result += operands[index][i]
            else:
                sub_result *= operands[index][i]
        result += sub_result

    return result
                
            


if __name__ == '__main__':
    result = main()
    print(result)