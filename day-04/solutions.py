import re


def count_xmas(sequence: str, pattern: str) -> int:
    pattern_reversed = pattern[::-1]
    xmas_count = len(re.findall(pattern, sequence))
    samx_count = len(re.findall(pattern_reversed, sequence))
    return xmas_count + samx_count


def transpose(data: list) -> list:
    data_transposed = []
    rows = len(data)
    columns = len(data[0])
    for c in range(columns):
        result_c = ''
        for r in range(rows):
            result_c += data[r][c]
        data_transposed.append(result_c)
    return data_transposed


def get_diagonals_down_right(grid):
    # Created by ChatGPT
    rows = len(grid)
    cols = len(grid[0])

    diagonals = []

    # 1. Diagonals starting from first column, row by row
    for row_start in range(rows):
        diagonal = []
        r, c = row_start, 0
        while r < rows and c < cols:
            diagonal.append(grid[r][c])
            r += 1
            c += 1
        diagonals.append(''.join(diagonal))

    # 2. Diagonals starting from top row, col by col (excluding the [0,0] corner we already did)
    for col_start in range(1, cols):
        diagonal = []
        r, c = 0, col_start
        while r < rows and c < cols:
            diagonal.append(grid[r][c])
            r += 1
            c += 1
        diagonals.append(''.join(diagonal))

    return diagonals


def get_diagonals_down_left(grid):
    # Created by ChatGPT
    rows = len(grid)
    cols = len(grid[0])

    diagonals = []

    # 1. Diagonals starting from first row, rightmost column downwards
    for col_start in range(cols):
        diagonal = []
        r, c = 0, col_start
        while r < rows and c >= 0:
            diagonal.append(grid[r][c])
            r += 1
            c -= 1
        diagonals.append(''.join(diagonal))

    # 2. Diagonals starting from leftmost column, row by row (excluding the top corner we did)
    for row_start in range(1, rows):
        diagonal = []
        r, c = row_start, cols - 1
        while r < rows and c >= 0:
            diagonal.append(grid[r][c])
            r += 1
            c -= 1
        diagonals.append(''.join(diagonal))

    return diagonals


def solve_part_1(data: list) -> int:
    result = 0

    for line in data:
        result += count_xmas(line, 'XMAS')

    data_transposed = transpose(data)
    for line in data_transposed:
        result += count_xmas(line, 'XMAS')

    # data_diagonal = get_diagonal(data)
    data_diagonal = get_diagonals_down_right(data)
    for line in data_diagonal:
        result += count_xmas(line, 'XMAS')

    # data_transposed_diagonal = get_diagonal(data_transposed)
    data_transposed_diagonal = get_diagonals_down_left(data)
    for line in data_transposed_diagonal:
        result += count_xmas(line, 'XMAS')

    return result


def solve_part_2(data: list) -> int:
    result = 0
    rows = len(data)
    cols = len(data[0])
    for r in range(rows - 2):
        for c in range(cols - 2):
            zoom = data[r:r + 3]
            zoom = [row[c:c + 3] for row in zoom]
            diag_down_right = zoom[0][0] + zoom[1][1] + zoom[2][2]
            diag_down_left = zoom[0][2] + zoom[1][1] + zoom[2][0]
            if (
                count_xmas(diag_down_right, 'MAS') == 1 and 
                count_xmas(diag_down_left, 'MAS') == 1
            ):
                result += 1
    return result


if __name__ == '__main__':
    with open('day-04/input.txt') as file:
        data = file.read().splitlines()

    print(f'Part 1: {solve_part_1(data)}')

    print(f'Part 2: {solve_part_2(data)}')
