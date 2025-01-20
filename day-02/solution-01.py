def is_safe(report: list) -> bool:

    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    if all(-3 <= diff <= -1 for diff in differences):
        return True
    elif all(1 <= diff <= 3 for diff in differences):
        return True
    else:
        return False


def solve_part_1(reports: list) -> int:
    return sum(is_safe(report) for report in reports)


def solve_part_2(reports: list) -> int:
    result = 0
    for report in reports:
        if is_safe(report):
            result += 1
        else:
            for i in range(len(report)):
                report_dampened = [report[j] for j in range(len(report)) if j != i]
                if is_safe(report_dampened):
                    result += 1
                    break

    return result


if __name__ == '__main__':
    # Read and clean input data
    with open('day-02/input.txt') as file:
        reports = [
            [int(x) for x in line.strip().split()]
            for line in file.readlines()
        ]

    result_part_1 = solve_part_1(reports)
    print(f'Result (Part 1): {result_part_1}')

    result_part_2 = solve_part_2(reports)
    print(f'Result (Part 2): {result_part_2}')
