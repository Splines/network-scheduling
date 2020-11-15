from copy import deepcopy

import plot
from package_simulation import simulate_packages
from scheduling import round_robin, fair_queuing

print('# =============== #')
print('# Scheduling Plot #')
print('# =============== #')
print('© Dominic Plein 11/2020')

# Plot
fig, (ax1, ax2, ax3, ax4, ax5) = plot.init_plot()

# Packages
sources, max_end_time = simulate_packages(15, 40, 10)
plot.plot_broken_barh(ax1, 'Eintreffende Pakete', sources, max_end_time)

# Round Robin (abbreviated as rr)
sources_rr, diff_rr, max_end_time_rr, data_rr = round_robin(deepcopy(sources))
plot.plot_broken_barh(ax2, 'Round-Robin', sources_rr, max_end_time_rr, diff_rr)
plot.plot_scatter(ax4, 'Round-Robin (Auswertung)', data_rr)

# Fair Queuing (abbreviated as fq)
sources_fq, diff_fq, max_end_time_fq, data_fq = fair_queuing(deepcopy(sources))
plot.plot_broken_barh(ax3, 'Fair Queuing', sources_fq, max_end_time_fq, diff_fq)
plot.plot_scatter(ax5, 'Fair Queuing (Auswertung)', data_fq)

# Plot
ax1.set_xlim(0, max(max_end_time_rr, max_end_time_fq))
plot.save(fig)
plot.show_plot()
