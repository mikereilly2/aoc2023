from typing import List, Set


def get_total_value(cards: List[str]) -> int:
    return sum(get_card_value(card) for card in cards)


def get_card_value(card: str) -> int:
    winning_nums = get_winning_nums(card)
    nums_i_have = get_nums_i_have(card)
    nums_won = winning_nums & nums_i_have
    return 2**(len(nums_won)-1) if nums_won else 0


def get_winning_nums(card: str) -> Set[int]:
    num_string = card.split(': ')[1].split(' | ')[0]
    return {int(n) for n in num_string.split(' ') if n.isnumeric()}


def get_nums_i_have(card: str) -> Set[int]:
    num_string = card.split(': ')[1].split(' | ')[1]
    return {int(n) for n in num_string.split(' ') if n.isnumeric()}


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    cards = data.split('\n')
    print(get_total_value(cards))
