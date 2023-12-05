from typing import List


def sum_calibration_values(lines: List[str]) -> int:
    return sum(calc_calibration_value(line) for line in lines)


def calc_calibration_value(line: str) -> int:
    return int(first_digit(line) + last_digit(line))


def first_digit(line: str) -> str:
    for c in line:
        if c.isdigit():
            return c


def last_digit(line: str) -> str:
    return first_digit(reversed(line))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    lines = data.split('\n')
    print(sum_calibration_values(lines))
