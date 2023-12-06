from typing import List, Tuple, Optional


def solution(data: str) -> int:
    lines = data.split('\n')
    times = [int(t) for t in lines[0][5:].split(' ') if t != '']
    dists = [int(t) for t in lines[1][9:].split(' ') if t != '']

    result = 1
    for time, record_dist in zip(times, dists):
        num_ways = 0
        for time_charged in range(time + 1):
            time_moving = time - time_charged
            dist = time_moving * time_charged
            if dist > record_dist:
                num_ways += 1
        result *= num_ways
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    print(solution(data))
