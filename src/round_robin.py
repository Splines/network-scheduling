import math


# Round Robin:
# in turn one source can send one package at a time

def next_source_number(sources) -> int:
    next_packages_arrival_times = [(source[0][0] if source else math.inf) for source in sources]
    smallest_arrival_time = min(next_packages_arrival_times)
    source_numbers = [index for index in range(len(next_packages_arrival_times))
                      if next_packages_arrival_times[index] == smallest_arrival_time]
    if len(source_numbers) == 1:
        return source_numbers[0]
    else:  # two messages arrived at the same time
        return source_numbers[1]


def round_robin(sources) -> (list, int, list):
    print('=== Round Robin ===')
    sources_out = [[], [], []]  # (start_processing_time, package_size)
    data = []  # (package_size, waiting_time)
    # waiting_time = start_processing_time - arrival_time

    time = 0
    # while there is at least one element in any of the sources nested arrays
    while sum([len(source) for source in sources]) > 0:
        curr_source_number = next_source_number(sources)
        curr_source = sources[curr_source_number]

        # set new start time
        curr_source_arrival_time = curr_source[0][0]
        if curr_source_arrival_time > time:  # if package arrives "in the future"
            time = curr_source_arrival_time
        # else: package arrived in the past (while we were processing another package)
        # so just leave time and immediately process the old package

        # get the first package of the current source and remove it (pop),
        # since we are processing it now
        package = curr_source.pop(0)
        package_size = package[1]
        sources_out[curr_source_number].append((time, package_size))
        data.append((package[1], time - package[0]))

        time += package_size  # "process" the current package

    print('Sources: ', sources_out)
    print('Data: ', data)

    # the last state of the clock is the maximum time
    return sources_out, time, data
