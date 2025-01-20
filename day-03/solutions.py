import re


def solve_part_1(data: str) -> int:
    result = 0
    instructions = re.findall(r'mul\(\d+,\d+\)', data)
    for i in instructions:
        numbers = re.findall(r'\d+', i)
        numbers = [int(n) for n in numbers]
        result_i = numbers[0] * numbers[1]
        result += result_i
    return result


def solve_part_2(data: str) -> int:
    result = 0
    instructions = re.split(r'do\(\)', data)
    for i in instructions:
        do = re.split(r"don't\(\)", i)[0]
        result += solve_part_1(do)
    return result


if __name__ == '__main__':
    with open('day-03/input.txt') as file:
        data = file.read()

    print(f'Part 1: {solve_part_1(data)}')

    print(f'Part 2: {solve_part_2(data)}')
