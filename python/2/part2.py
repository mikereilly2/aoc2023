from typing import List


def sum_powers(games: List[str]) -> int:
    return sum(get_game_power(g) for g in games)


def get_game_power(game: str) -> bool:
    maxes = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for reveal in game.split(': ')[1].split('; '):
        for color_reveal in reveal.split(', '):
            parts = color_reveal.split(' ')
            count = int(parts[0])
            color = parts[1]
            if count > maxes[color]:
                maxes[color] = count
    
    return maxes['red'] * maxes['green'] * maxes['blue']


if __name__ == '__main__':
    with open('2/input.txt', 'r') as f:
        data = f.read()
    games = data.split('\n')
    print(sum_powers(games))
