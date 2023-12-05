from typing import List, Optional


spelled_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def sum_calibration_values(lines: List[str]) -> int:
    return sum(calc_calibration_value(line) for line in lines)


def calc_calibration_value(line: str) -> int:
    return int(first_digit(line) + last_digit(line))


def first_digit(line: str) -> str:
    for i in range(len(line)):
        if d := parse_digit(line, i):
            return d


def last_digit(line: str) -> str:
    for i in range(len(line) - 1, -1, -1):
        if d := parse_digit(line, i):
            return d


def parse_digit(line: str, start_index: int) -> Optional[str]:
    if line[start_index].isdigit():
        return line[start_index]
    for digit, value in spelled_digits.items():
        if line[start_index : start_index + len(digit)] == digit:
            return value
    return None


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()
    lines = data.split("\n")
    print(sum_calibration_values(lines))
