#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FormatStrFormatter

plt.style.use('default')
plt.rcParams["font.family"] = "Times New Roman"

data_1 = np.loadtxt("figure_6_right_data.txt", skiprows=1, encoding = "utf-16") # the encoding to read the data files!!!

fig1, axis1 = plt.subplots(1, figsize=(5.5, 4.5))

axis12 = axis1.twinx()
axis1.plot(data_1[:, 0], (data_1[:, 1]*100)/data_1[0, 1], color = 'r')
axis1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axis1.set_ylim(0, 120)
axis1.set_xlim(0, 300)

axis1.set_ylabel('wt (%)', fontsize=22, color='r')
axis1.set_xlabel('T (°C)', fontsize=22, color='k')
axis1.spines['left'].set_color('r')
axis1.spines['right'].set_color('b')
axis1.spines['bottom'].set_color('k')
axis1.spines['top'].set_color('k')

axis1.locator_params(axis='x', nbins=7)
axis1.tick_params(axis='y', colors='r', length = 8, width=1.5, labelsize = 18, direction='in')
axis1.tick_params(axis = 'x', colors = 'k', length = 8, width=1.5, labelsize = 18, direction='in')

axis1.yaxis.set_major_formatter(FormatStrFormatter('%.f'))


axis12.plot(data_1[:, 0], data_1[:, 2]/data_1[:, 1], color = 'b')
axis12.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axis12.set_ylim(-0.1, 0.02)
axis12.set_xlim(0, 300)

axis12.spines['right'].set_color('b')
axis12.spines['left'].set_color('r')
axis12.spines['bottom'].set_color('k')
axis12.spines['top'].set_color('k')

axis12.tick_params(axis='y', colors='b', length = 8, width=1.5, labelsize = 18, direction='in')
axis12.tick_params(axis='x', colors='k', length = 8, width=1.5, labelsize = 18, direction='in')

axis12.set_ylabel('Temp. difference (°C/mg)', fontsize=22, color='b')

axis13 = axis1.twiny()
axis13.set_xlim(0, 300)

axis13.spines['right'].set_color('b')
axis13.spines['left'].set_color('r')
axis13.spines['bottom'].set_color('k')
axis13.spines['top'].set_color('k')

axis13.locator_params(axis='x', nbins=7)
axis13.tick_params(axis='y', colors='b', length = 8, width=1.5, labelsize = 18, direction='in')
axis13.tick_params(axis='x', colors='k', length = 8, width=1.5, labelsize = 18, direction='in')


axis1.grid(linestyle=(0, (5, 10)))
plt.tight_layout()
fig1.savefig('figure_6_right.png', dpi=300, bbox_inches='tight')
plt.show()
