from copy import deepcopy

import plot
from package_simulation import simulate_packages
from round_robin import round_robin

print('# =============== #')
print('# Scheduling Plot #')
print('# =============== #')
print('© Dominic Plein 11/2020')

# Plot
ax1, ax2, ax3 = plot.init_plot()

# Packages
sources, max_end_time = simulate_packages(10, 50, 10)
plot.plot_broken_barh(ax1, 'Eintreffende Pakete', sources, max_end_time)

# Round Robin (abbreviated as rr)
sources_rr, diff_rr, max_end_time_rr, data_rr = round_robin(deepcopy(sources))
ax1.set_xlim(0,max_end_time_rr) # TODO: outsource to plot
plot.plot_broken_barh(ax2, 'Round-Robin', sources_rr, max_end_time_rr, diff_rr)
plot.plot_scatter(ax3, 'Round-Robin (Auswertung)', data_rr)

# Fair Queuing
# plot_scatter(ax3, data_rr)

# Plot
plot.show_plot()
