def read_input():
    with open('input_test.txt') as f:
        operands = []
        operations = []
        while line := f.readline()[:-1]:
            strs = list(filter(lambda x: len(x) != 0, line.split(' ')))
            if strs[0].isnumeric():
                strs = list(map(lambda x: int(x), strs))
                operands.append(strs)
            else:
                operations = strs
        return operands, operations


def main():
    operands, operations = read_input()
    
    result = 0

    for index, operation in enumerate(operations):
        sub_result = 0 if operation == '+' else 1
        for i in range(len(operands)):
            if operation == '+':
                sub_result += operands[i][index]
            else:
                sub_result *= operands[i][index]
        result += sub_result
    
    return result
                
            


if __name__ == '__main__':
    result = main()
    print(result)