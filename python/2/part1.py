from typing import List

LIMITS = {
    'red': 12,
    'green': 13,
    "blue" : 14,
}

def sum_possible_games(games: List[str]) -> int:
    return sum(get_possible_games(games))

def get_possible_games(games: List[str]) -> List[int]:
    return [parse_game_num(g) for g in games if is_possible(g)]

def parse_game_num(game: str) -> int:
    return int(game.split(' ')[1].split(':')[0])

def is_possible(game: str) -> bool:
    for reveal in game.split(': ')[1].split('; '):
        for color_reveal in reveal.split(', '):
            parts = color_reveal.split(' ')
            count = int(parts[0])
            color = parts[1]
            if count > LIMITS[color]:
                return False
    return True

if __name__ == '__main__':
    with open('2/input.txt', 'r') as f:
        data = f.read()
    games = data.split('\n')
    print(sum_possible_games(games))
