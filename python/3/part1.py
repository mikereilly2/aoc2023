from typing import List


def sum_part_numbers(rows: List[str]) -> int:
    sum = 0
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            if row[c].isdigit():
                num_end = get_num_end(row, c)
                if is_symbol_adjacent(rows, r, c, num_end):
                    sum += int(row[c:num_end+1])
                c = num_end + 2  # already know +1 is not a digit, so skip it
            else:
                c += 1
    return sum


def get_num_end(row: str, num_start: int) -> int:
    num_end = num_start
    while num_end + 1 < len(row) and row[num_end+1].isdigit():
        num_end += 1
    return num_end


def is_symbol_adjacent(rows: List[str], row_num: int, num_start: int, num_end: int) -> bool:
    options = [(row_num, num_start-1), (row_num, num_end+1)]
    for col in range(num_start-1, num_end+2):
        options.append((row_num-1, col))
        options.append((row_num+1, col))
    options = [(r, c) for r, c in options if r >= 0 and r < len(rows) and c >= 0 and c < len(rows[row_num])]

    return any(is_symbol(rows[r][c]) for r, c in options)


def is_symbol(char: str):
    return not char.isdigit() and not char == '.'
    

if __name__ == '__main__':
    with open('3/input.txt', 'r') as f:
        data = f.read()
    rows = data.split('\n')
    print(sum_part_numbers(rows))
