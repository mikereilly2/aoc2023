from typing import List, Set
from collections import deque


def get_total_card_count(cards: List[str]) -> int:
    cards.insert(0, '')  # make indexes match card nums

    queue = deque(range(1, len(cards)))
    num_processed = 0
    while queue:
        num_processed += 1
        card_num = queue.popleft()
        card = cards[card_num]
        num_wins = get_num_wins(card)
        queue.extend(i for i in range(card_num+1, card_num+1+num_wins) if i < len(cards))

    return num_processed


def get_num_wins(card: str) -> int:
    winning_nums = get_winning_nums(card)
    nums_i_have = get_nums_i_have(card)
    nums_won = winning_nums & nums_i_have
    return len(nums_won)


def get_winning_nums(card: str) -> Set[int]:
    num_string = card.split(': ')[1].split(' | ')[0]
    return {int(n) for n in num_string.split(' ') if n.isnumeric()}


def get_nums_i_have(card: str) -> Set[int]:
    num_string = card.split(': ')[1].split(' | ')[1]
    return {int(n) for n in num_string.split(' ') if n.isnumeric()}


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    rows = data.split('\n')
    print(get_total_card_count(rows))
