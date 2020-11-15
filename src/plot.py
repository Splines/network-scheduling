from copy import deepcopy

import matplotlib.pyplot as plt

from package_simulation import simulate_packages
from round_robin import round_robin

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.suptitle('Scheduling-Verfahren', fontsize=16)


def plot_broken_barh(axes, title, sources, max_end_time):
    axes.set_title(title)
    axes.set_xlabel('Zeit')
    axes.set_ylim(5, 45)
    axes.set_xlim(0, max_end_time)
    axes.broken_barh(sources[0], (30, 9), fc='#F0E156', ec='black')
    axes.broken_barh(sources[1], (20, 9), fc='#F56670', ec='black')
    axes.broken_barh(sources[2], (10, 9), fc='#26CEF0', ec='black')
    axes.set_yticks([15, 25, 35])
    axes.set_yticklabels(['Quelle 3', 'Quelle 2', 'Quelle 1'])


def plot_scatter(axes, title, data):
    axes.set_title(title)
    axes.set_xlabel('Paketgröße')
    axes.set_ylabel('Wartezeit')
    x, y = zip(*data)
    axes.scatter(x, y)


def __init__():
    print('# =============== #')
    print('# Scheduling Plot #')
    print('# =============== #')
    print('© Dominic Plein 11/2020')

    # Packages
    sources, max_end_time = simulate_packages(5, 50, 10)
    plot_broken_barh(ax1, 'Eintreffende Pakete', sources, max_end_time)

    # Round Robin (abbreviated as rr)
    sources_rr, max_end_time_rr, data_rr = round_robin(deepcopy(sources))
    plot_broken_barh(ax2, 'Round-Robin', sources_rr, max_end_time_rr)
    plot_scatter(ax3, 'Round-Robin (Auswertung)', data_rr)

    # Fair Queuing
    # plot_scatter(ax3, data_rr)

    # Plot
    plt.show()


__init__()
