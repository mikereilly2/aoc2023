use std::cmp::Ordering;
use std::collections::HashMap;
use std::fs;
use std::time::Instant;

enum HandRank {
    HighCard,
    OnePair,
    TwoPair,
    Three,
    FullHouse,
    Four,
    Five,
}

struct Hand {
    cards: String,
    bid: u32,
}

impl Hand {
    fn from_lines(lines: &str, part: u8) -> Vec<Hand> {
        lines.lines().map(|l| Hand::from_line(l, part)).collect()
    }

    fn from_line(line: &str, part: u8) -> Hand {
        let parts: Vec<&str> = line.split(" ").collect();
        Hand {
            cards: Hand::lexicographicize(parts[0], part),
            bid: parts[1].parse().expect("error parsing bid"),
        }
    }

    fn lexicographicize(s: &str, part: u8) -> String {
        // make card ranks match how they should be sorted lexicographically
        let j_replacement = if part == 1 { "W" } else { "1" };
        s.replace('A', "Z")
            .replace('K', "Y")
            .replace('Q', "X")
            .replace('J', j_replacement)
    }

    fn rank(&self) -> HandRank {
        let card_counts = self.cards.chars().fold(HashMap::new(), |mut acc, c| {
            *acc.entry(c).or_insert(0) += 1;
            acc
        });
        let pt2_j_count = *card_counts.get(&'1').unwrap_or_else(|| &0usize);
        let mut count_counts = card_counts.into_values().fold([0; 6], |mut acc, count| {
            acc[count] += 1;
            acc
        });

        if pt2_j_count > 0 && pt2_j_count != 5 {
            // ignore J count and upgrade the most common card by number of Js we have
            count_counts[pt2_j_count] -= 1;
            for i in (1..=5).rev() {
                if count_counts[i] != 0 {
                    count_counts[i + pt2_j_count] += 1;
                    count_counts[i] -= 1;
                    break;
                }
            }
        }

        if count_counts[5] == 1 {
            HandRank::Five
        } else if count_counts[4] == 1 {
            HandRank::Four
        } else if count_counts[3] == 1 && count_counts[2] == 1 {
            HandRank::FullHouse
        } else if count_counts[3] == 1 {
            HandRank::Three
        } else if count_counts[2] == 2 {
            HandRank::TwoPair
        } else if count_counts[2] == 1 {
            HandRank::OnePair
        } else {
            HandRank::HighCard
        }
    }
}

impl Eq for Hand {}

impl PartialEq<Self> for Hand {
    fn eq(&self, other: &Self) -> bool {
        self.cmp(other) == Ordering::Equal
    }
}

impl PartialOrd<Self> for Hand {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Hand {
    fn cmp(&self, other: &Self) -> Ordering {
        let self_rank = self.rank() as u8;
        let other_rank = other.rank() as u8;
        if self_rank != other_rank {
            self_rank.cmp(&other_rank)
        } else {
            self.cards.cmp(&other.cards)
        }
    }
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("file read fail");

    let start = Instant::now();
    println!("part 1: {}", solution(&input, 1));
    let part1_done_time = Instant::now();
    println!("Time for part 1: {:?}\n", part1_done_time - start);

    println!("part 2: {}", solution(&input, 2));
    println!("Time for part 2: {:?}", Instant::now() - part1_done_time);
}

fn solution(input: &str, part: u8) -> u32 {
    let mut hands = Hand::from_lines(input, part);
    hands.sort();
    hands
        .iter()
        .enumerate()
        .map(|(i, h)| ((i + 1) as u32) * h.bid)
        .sum()
}
