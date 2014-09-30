__author__ = 'neal'
import matplotlib
matplotlib.use('PDF')
matplotlib.rcParams.update({'font.size': 10})

import numpy as np
from pylab import savefig
from matplotlib import pyplot as plt
from csv import reader

data_file_name = ''
plot_file_name = ''
plot_title = ''
x_axis_label = 'Time of Day'

# Load CSV data
data = []
with open(file_name, 'r') as lines:
	rows = reader(lines)
	rows.next()  # header
	for row in rows:
		instance = [get(row, x) for x in xrange(0, len(row))]
		data.append(instance)
data = np.array(data)

# Plot heatmap
plt.figure()
fig, ax = plt.subplots()
ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)
ax.set_xticklabels([i for i in xrange(0, 24)], minor=False)
ax.xaxis.set_tick_params(width=0)
ax.xaxis.tick_bottom()

ax.set_yticks([])
ax.set_yticklabels([])

plt.xlabel(x_axis_label)
plt.title(plot_title)
plt.grid(False)

ax.pcolormesh(data, cmap=plt.cm.hot)
savefig(plot_file_name+'.pdf')


