import matplotlib.pyplot as plt


def init_plot():
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    fig.suptitle('Scheduling-Verfahren', fontsize=16)
    return ax1, ax2, ax3


def show_plot():
    plt.show()


def plot_broken_barh(axes, title, sources, max_end_time, diff=None):
    axes.set_title(title)
    axes.set_xlabel('Zeit')
    axes.set_ylim(5, 45)
    axes.set_xlim(0, max_end_time)

    axes.broken_barh(sources[0], (31, 8), fc='#F0E156', ec='black')
    axes.broken_barh(sources[1], (21, 8), fc='#F56670', ec='black')
    axes.broken_barh(sources[2], (11, 8), fc='#16BFE0', ec='black')
    if diff:
        axes.broken_barh(diff[0], (34, 2), fc='#F2EAA0')
        axes.broken_barh(diff[1], (24, 2), fc='#F7B1B6')
        axes.broken_barh(diff[2], (14, 2), fc='#8DE1F2')
    axes.set_yticks([15, 25, 35])
    axes.set_yticklabels(['Quelle 3', 'Quelle 2', 'Quelle 1'])


def plot_scatter(axes, title, data):
    axes.set_title(title)
    axes.set_xlabel('Paketgröße')
    axes.set_ylabel('Wartezeit')
    x, y = zip(*data)
    axes.scatter(x, y)
