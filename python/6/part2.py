from typing import List, Tuple, Optional


def solution(data: str) -> int:
    lines = data.split('\n')
    time = int(lines[0].replace(' ', '')[5:])
    record_dist = int(lines[1].replace(' ', '')[9:])

    num_ways = 0
    for time_charged in range(time + 1):
        time_moving = time - time_charged
        dist = time_moving * time_charged
        if dist > record_dist:
            num_ways += 1
    return num_ways


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    print(solution(data))
