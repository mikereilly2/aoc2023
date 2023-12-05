from typing import List, Tuple, Optional


def solution(data: str) -> int:
    seeds_str = data.split('seeds: ')[1].split('\n')[0]
    seeds = [int(s) for s in seeds_str.split(' ')]

    seed_to_soil_tuples = parse_map_tuples('seed-to-soil map:', 'soil-to-fertilizer map:')
    soil_to_fert_tuples = parse_map_tuples('soil-to-fertilizer map:', 'fertilizer-to-water map:')
    fert_to_water_tuples = parse_map_tuples('fertilizer-to-water map:', 'water-to-light map:')
    water_to_light_tuples = parse_map_tuples('water-to-light map:', 'light-to-temperature map:')
    light_to_temp_tuples = parse_map_tuples('light-to-temperature map:', 'temperature-to-humidity map:')
    temp_to_humid_tuples = parse_map_tuples('temperature-to-humidity map:', 'humidity-to-location map:')
    humid_to_location_tuples = parse_map_tuples('humidity-to-location map:', None)

    locations = []
    for seed in seeds:
        soil = get_mapped(seed, seed_to_soil_tuples)
        fert = get_mapped(soil, soil_to_fert_tuples)
        water = get_mapped(fert, fert_to_water_tuples)
        light = get_mapped(water, water_to_light_tuples)
        temp = get_mapped(light, light_to_temp_tuples)
        humid = get_mapped(temp, temp_to_humid_tuples)
        location = get_mapped(humid, humid_to_location_tuples)
        locations.append(location)
    return min(locations)


def parse_map_tuples(start_marker: str, end_marker: Optional[str]) -> List[Tuple[int, int, int]]:
    tuples = []
    lines = data.split(start_marker)[1]
    if end_marker:
        lines = lines.split(end_marker)[0]
    lines = lines.strip().split('\n')

    for l in lines:
        dest, source, length = l.split(' ')
        tuples.append((int(dest), int(source), int(length)))
    return tuples


def get_mapped(num: int, map_tuples: List[Tuple[int, int, int]]) -> int:
    for dest_range_start, source_range_start, range_length in map_tuples:
        if source_range_start <= num < source_range_start + range_length:
            return num - source_range_start + dest_range_start
    return num


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
#     data = """seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4"""
    print(solution(data))
