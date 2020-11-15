import os

import matplotlib.pyplot as plt


def init_plot():
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1)
    fig.suptitle('Scheduling-Verfahren', fontsize=16)
    return fig, (ax1, ax2, ax3, ax4, ax5)


def show_plot():
    plt.show()


def plot_waiting_time(big_height, y_tick, diff, axes, face_color, edge_color):
    delta = big_height / len(diff)
    i = 0
    for element in diff:
        if element[1] != 0:
            axes.broken_barh([element], (y_tick + big_height / 2 - delta * i - 1.5, 1.5), fc=face_color, ec=edge_color)
        i += 1


def plot_broken_barh(axes, title, sources, max_end_time, diff=None):
    axes.set_title(title)
    axes.set_xlabel('Zeit')
    axes.set_ylim(5, 45)
    axes.set_xlim(0, max_end_time)

    big_height = 8
    axes.broken_barh(sources[0], (35 - big_height / 2, big_height), fc='#F0E156', ec='black')
    axes.broken_barh(sources[1], (25 - big_height / 2, big_height), fc='#F56670', ec='black')
    axes.broken_barh(sources[2], (15 - big_height / 2, big_height), fc='#16BFE0', ec='black')
    if diff:
        plot_waiting_time(big_height, 35, diff[0], axes, '#F2EAA0', '#D1C97D')
        plot_waiting_time(big_height, 25, diff[1], axes, '#F7B1B6', '#DB8489')
        plot_waiting_time(big_height, 15, diff[2], axes, '#8DE1F2', '#77C8D9')
    axes.set_yticks([15, 25, 35])
    axes.set_yticklabels(['Quelle 3', 'Quelle 2', 'Quelle 1'])


def plot_scatter(axes, title, data):
    axes.set_title(title)
    axes.set_xlabel('Paketgröße')
    axes.set_ylabel('Wartezeit')
    x, y = zip(*data)
    axes.scatter(x, y)


def save(fig):
    # plt.tight_layout()
    plt.subplots_adjust(top=0.9, hspace=0.7)
    fig.set_size_inches(12, 13, forward=True)
    fname = os.path.join(os.environ["HOMEPATH"], "Desktop", "Scheduling.svg")
    fig.savefig(fname, transparent=False)
    print('Saved file to: ', fname)
