from typing import List


def sum_gear_ratios(rows: List[str]) -> int:
    sum = 0
    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            if char == '*':
                adj_nums = get_adjacent_nums(rows, r, c)
                if len(adj_nums) == 2:
                    sum += adj_nums[0] * adj_nums[1]
    return sum


def get_adjacent_nums(rows: List[str], row_num: int, col_num: int) -> List[int]:
    directions = (-1, 0, 1)
    options = {(row_num + a, col_num + b) for a in directions for b in directions}
    options.remove((row_num, col_num))
    options = {(r, c) for r, c in options if r >= 0 and r < len(rows) and c >= 0 and c < len(rows[row_num])}

    adjacent_nums = []

    positions_seen = set()
    for a, b in options:
        if (a, b) in positions_seen:
            continue
        if rows[a][b].isdigit():
            num_start, num_end = get_num_start_end(rows[a], b)
            positions_seen.update((a, y) for y in range(num_start, num_end+1))
            adjacent_nums.append(int(rows[a][num_start:num_end+1]))

    return adjacent_nums



def get_num_start_end(row: str, num_start: int) -> int:
    num_end = num_start
    while num_end + 1 < len(row) and row[num_end+1].isdigit():
        num_end += 1
    
    real_start = num_start
    while real_start > 0 and row[real_start-1].isdigit():
        real_start -= 1

    return real_start, num_end
    

if __name__ == '__main__':
    with open('3/input.txt', 'r') as f:
        data = f.read()
    rows = data.split('\n')
    print(sum_gear_ratios(rows))
