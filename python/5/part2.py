from typing import Optional, List, Tuple


def solution(data):
    seeds_str = data.split('seeds: ')[1].split('\n')[0]
    seeds = [int(s) for s in seeds_str.split(' ')]
    seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

    seed_to_soil_tuples = parse_map_tuples('seed-to-soil map:', 'soil-to-fertilizer map:')
    soil_to_fert_tuples = parse_map_tuples('soil-to-fertilizer map:', 'fertilizer-to-water map:')
    fert_to_water_tuples = parse_map_tuples('fertilizer-to-water map:', 'water-to-light map:')
    water_to_light_tuples = parse_map_tuples('water-to-light map:', 'light-to-temperature map:')
    light_to_temp_tuples = parse_map_tuples('light-to-temperature map:', 'temperature-to-humidity map:')
    temp_to_humid_tuples = parse_map_tuples('temperature-to-humidity map:', 'humidity-to-location map:')
    humid_to_location_tuples = parse_map_tuples('humidity-to-location map:', None)

    soil_ranges = get_mapped_ranges(seed_ranges, seed_to_soil_tuples)
    fert_ranges = get_mapped_ranges(soil_ranges, soil_to_fert_tuples)
    water_ranges = get_mapped_ranges(fert_ranges, fert_to_water_tuples)
    light_ranges = get_mapped_ranges(water_ranges, water_to_light_tuples)
    temp_ranges = get_mapped_ranges(light_ranges, light_to_temp_tuples)
    humid_ranges = get_mapped_ranges(temp_ranges, temp_to_humid_tuples)
    location_ranges = get_mapped_ranges(humid_ranges, humid_to_location_tuples)
    return min(t[0] for t in location_ranges)


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


def get_mapped_ranges(ranges, map_tuples):
    result_ranges = []
    for start, length in ranges:
        if length == 0:
            continue
        match_found = False
        for dest_start, source_start, map_length in map_tuples:
            if not match_found and source_start <= start < source_start + map_length:
                match_found = True
                if start + length < source_start + map_length:
                    # map fully covers this interval
                    result_ranges.append((start - source_start + dest_start, length))
                else:
                    # add what we can to result ranges, add rest to end of ranges
                    result_ranges.append((start - source_start + dest_start, (source_start + map_length) - start))
                    ranges.extend([(start, source_start - start), (source_start + map_length, start + length - (source_start + map_length))])
        if not match_found:
            result_ranges.append((start, length))
    return result_ranges


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    print(solution(data))
