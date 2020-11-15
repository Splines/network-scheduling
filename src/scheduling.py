import math
from typing import Tuple, List


def schedule(sources, next_source_number_fun) -> Tuple[list, list, int, list]:
    sources_out = [[], [], []]  # (start_processing_time, package_size)
    diff_out = [[], [], []]  # (arrival_time, waiting_time)
    data = []  # (package_size, waiting_time)
    # waiting_time = start_processing_time - arrival_time

    time = 0
    curr_source_number = -1
    # while there is at least one element in any of the sources nested arrays
    while sum([len(source) for source in sources]) > 0:
        curr_source_number = next_source_number_fun(sources, curr_source_number)
        curr_source = sources[curr_source_number]

        # Set time to represent the start of the processing time
        curr_source_arrival_time = curr_source[0][0]
        if curr_source_arrival_time > time:  # if package will arrive "in the future"
            time = curr_source_arrival_time
        # else: package arrived in the past (while we were processing another package)
        # so don't alter the time and immediately process the old package

        # get the first package of the current source and remove it (pop),
        # since we are processing it now
        package = curr_source.pop(0)
        package_size = package[1]
        sources_out[curr_source_number].append((time, package_size))
        diff_out[curr_source_number].append((curr_source_arrival_time, (time - curr_source_arrival_time)))
        data.append((package[1], time - package[0]))

        time += package_size  # "process" the current package

    print('Sources: ', sources_out)
    print('Data: ', data)

    # the last state of the clock is the maximum time
    return sources_out, diff_out, time, data


def next_source_numbers_with_min_arrival_time(sources: list) -> List[int]:
    next_packages_arrival_times = [(source[0][0] if source else math.inf) for source in sources]

    # Get all source numbers that have the minimum time for the next package arrival
    next_source_numbers = []  # e.g. source 1 and source 3 send packages at the same time
    minimum = math.inf
    for i in range(len(next_packages_arrival_times)):
        arrival_time = next_packages_arrival_times[i]
        if arrival_time < minimum:
            minimum = arrival_time
            next_source_numbers = [i]
        elif arrival_time == minimum:
            minimum = arrival_time
            next_source_numbers.append(i)

    return next_source_numbers


def next_source_number_round_robin(sources: list, last_source_number: int) -> int:
    next_source_numbers = next_source_numbers_with_min_arrival_time(sources)
    if len(next_source_numbers) == 1:
        return next_source_numbers[0]  # first come, first served
    else:  # at least two sources sent at the same time
        # Find out the smallest distance from the last_source_number to the new_source_number.
        # This distance is measured in distance only going in one direction.
        # (we start at the beginning of the list if we surpass its boundaries, which is why we use modulo)
        # Example (# represents a package)
        # sources  | ------> time
        # source 0 |       #
        # source 1 |  #            => next_source_numbers = [0,2]
        # source 2 |       #
        # => in this case: distance to source2 is 1, while distance to source0 is 2
        # => source2 gets the next turn, since min(1,2)=1 => (1 + 1) % 3 = 2
        min_distance = min([((3 - last_source_number + x) % 3) for x in next_source_numbers])
        return (last_source_number + min_distance) % 3


def next_source_number_fair_queuing(sources: list, *args) -> int:
    next_source_numbers = next_source_numbers_with_min_arrival_time(sources)
    if len(next_source_numbers) == 1:
        return next_source_numbers[0]  # first come, first served
    else:  # at least two sources sent at the same time
        # take the source whose package would be finished first
        # if processed immediately after its arrival time
        min_end_time = math.inf
        next_source_number = -1
        for i in next_source_numbers:
            end_time = sources[i][0][0] + sources[i][0][1]
            if end_time <= min_end_time:  # (no special case for end_time == min_end_time)
                min_end_time = end_time
                next_source_number = i
        return next_source_number


########################
# Convenience Wrappers #
########################
def round_robin(sources) -> Tuple[list, list, int, list]:
    print('=== Round Robin ===')
    return schedule(sources, next_source_number_round_robin)


def fair_queuing(sources) -> Tuple[list, list, int, list]:
    print('=== Fair Queuing ===')
    return schedule(sources, next_source_number_fair_queuing)
