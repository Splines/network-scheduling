import numpy as np

rg = np.random.default_rng()


# Example
# Source  | Arrival Time | Package size |
# ------------------------------------- |
# S1      |      0       |     5        |
# S2      |      3       |     7        |
# S3      |      3       |     1        |
# S1      |      1       |     6        |
# ...
# => We can process 1 package / 1 time unit

def calc_max_end_time(sources):
    last_package_end_times = []
    for source in sources:
        last_package_end_times += [source[-1][0] + source[-1][1]]
    return max(last_package_end_times)


def simulate_packages(number_of_total_processes, max_arrival_time, max_package_size):
    # Simulate packages (arrival_time, package_size)
    arrival_times = rg.integers(0, max_arrival_time, number_of_total_processes)
    arrival_times = np.sort(arrival_times)
    package_sizes = rg.integers(1, max_package_size, number_of_total_processes)
    packages = np.array((arrival_times, package_sizes)).transpose()
    print('=== Packages ===')
    print(packages)

    # Distribute total packages to sources [(arrival_time, package_size), (...) ,(...)]
    # [(1), (2), (3), (4), (5)]
    sources = [[], [], []]
    i = 0
    distributed = 0
    failed = 0
    while distributed < len(packages):  # we need to distribute ALL packages to the sources
        curr_source = sources[i % 3]
        # print('cur_source: ', curr_source)

        # if we can't find any source where there is no overlap with the new package
        # just add one with a custom start time
        if failed == 3:
            i += np.random.randint(0, 3)  # increase i randomly to figure out new source
            last_package = sources[i % 3][-1]
            last_end_time = last_package[0] + last_package[1]
            curr_source += [(last_end_time, packages[distributed][1])]
            distributed += 1
            failed = 0
            continue

        new_arrival_time = packages[distributed][0]
        should_add = True
        # if we have elements in the current source already, we need to make sure
        # that there is no overlap between two consecutive packages
        if curr_source:  # make sure that list is not empty
            last_package_of_source = curr_source[-1]
            last_end_time = last_package_of_source[0] + last_package_of_source[1]
            if last_end_time > new_arrival_time:
                should_add = False

        if should_add:
            curr_source += [(new_arrival_time, packages[distributed][1])]
            # print('curr_source after add: ', curr_source)
            distributed += 1
        else:
            failed += 1

        i += 1

    print('=== Sources ===')
    print('Source1: ', sources[0])
    print('Source2: ', sources[1])
    print('Source3: ', sources[2])
    return sources, calc_max_end_time(sources)

# Test data
# packages = [[2, 7],
#             [3, 2],
#             [3, 7],
#             [6, 2],
#             [8, 4],
#             [8, 2],
#             [9, 6],
#             [10, 8],
#             [15, 2],
#             [16, 9],
#             [20, 5],
#             [22, 8],
#             [24, 1],
#             [26, 1],
#             [38, 7],
#             [38, 7],
#             [39, 9],
#             [41, 8],
#             [44, 5],
#             [46, 3]]
