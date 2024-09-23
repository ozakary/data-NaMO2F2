#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FormatStrFormatter
import matplotlib
import statsmodels.api as sm
from matplotlib.ticker import MultipleLocator
plt.style.use("default") # set the plot style
plt.rcParams["font.family"] = "Times New Roman" # To globaly change the font POLICE
plt.rcParams["font.weight"] = "bold" # To write all font in bold
plt.rcParams["axes.labelweight"] = "bold" # To write all labels in bold

###############################################################################################################################
###########################################< Section n °1 : loading and plotting DATA >########################################
###############################################################################################################################

data_1 = np.loadtxt("figure_S16-b_NaNbO2F2_data.txt", skiprows=1)
data_2 = np.loadtxt("figure_S16-b_NaTaO2F2_data.txt", skiprows=1)

fig = plt.figure(figsize=(4, 5))
gs = fig.add_gridspec(1, 1, wspace = 0.4)
axis2 = gs.subplots()

# DATA N°2
axis22 = axis2.twinx()
line_3 = axis2.errorbar(data_1[:, 0], data_1[:, 1], yerr = data_1[:, 2], fmt = 'o', linewidth = .8,
             elinewidth = 1, ecolor = 'k', color = 'r', capsize = 3, ms = 5, mec = 'k')
axis2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

line_4 = axis22.errorbar(data_2[:, 0], data_2[:, 1], yerr = data_2[:, 2], fmt = 'o', linewidth = .8,
             elinewidth = 1, ecolor = 'k', color = 'c', capsize = 3, ms = 5, mec = 'k')


# DATA N°2
axis2.set_xlabel('T (°C)', color = 'k', fontsize=18)
axis2.set_ylabel('V$_P$ ($\AA^3$)', fontsize=20, color='k')
#axis2.set_title('[MO1$_2$O2$_2$F1F2]$^5$$^-$', fontsize = 24, y = 1.1, fontweight = 'bold')

# DATA N°2
axis2.set_ylim(24, 28)
axis2.set_xlim(15, 310)
axis22.set_ylim(24, 28)
axis22.set_xlim(15, 310)

axis122 = axis2.twiny()
axis122.set_xlim(15, 310)

###############################################################################################################################
#################################################< Section n °2 : managing ticks >#############################################
###############################################################################################################################

# Major ticks
# DATA N°2
axis2.tick_params(axis='y', colors='k', length = 10, width=1.5, labelsize = 16, direction='in')
axis2.tick_params(axis = 'x', colors = 'k', length = 10, width=1.5, labelsize = 16, direction='in')
axis2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

axis22.tick_params(axis='y', colors='k', length = 10, width=1.5, labelsize = 16, direction='in')
axis22.tick_params(axis='x', colors='k', length = 10, width=1.5, labelsize = 16, direction='in')
axis22.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

axis122.tick_params(axis='y', colors='k', length = 10, width=1.5, labelsize = 16, direction='in')
axis122.tick_params(axis='x', colors='k', length = 10, width=1.5, labelsize = 16, direction='in')

# Minor ticks
# DATA N°2
axis2.xaxis.set_minor_locator(MultipleLocator(10))
axis2.yaxis.set_minor_locator(MultipleLocator(.1))
axis2.tick_params(which = 'minor', length = 5, width = 1.5, direction = "in")

axis22.xaxis.set_minor_locator(MultipleLocator(10))
axis22.yaxis.set_minor_locator(MultipleLocator(.1))
axis22.tick_params(which = 'minor', length = 5, width = 1.5, direction = "in")

axis122.xaxis.set_minor_locator(MultipleLocator(10))
axis122.yaxis.set_minor_locator(MultipleLocator(.1))
axis122.tick_params(which = 'minor', length = 5, width = 1.5, direction = "in")

axis2.locator_params(axis='x', nbins=6)
axis122.locator_params(axis='x', nbins=6)
###############################################################################################################################
################################################< Section n °3 : Rectangulars >################################################
###############################################################################################################################

# To add the colored rectangles in the plots
# DATA n°2
xmin, xmax = 220,300
_,top = fig.transFigure.inverted().transform(axis2.transAxes.transform([0,1]))
_,bottom = fig.transFigure.inverted().transform(axis2.transAxes.transform([0,0]))
trans = matplotlib.transforms.blended_transform_factory(axis2.transData, fig.transFigure)
r_1 = matplotlib.patches.Rectangle(xy=(xmin,bottom), width=xmax-xmin, height=top-bottom, transform=trans,
                                 fc='grey', alpha = .25, ec='C0', lw=0)
fig.add_artist(r_1)

###############################################################################################################################
#############################################< Section n °4 : Linear regressions >#############################################
###############################################################################################################################
# Establishing the linear regression

# DATA n°2

# Definnig the regression variables (x, y)
x2 = data_2[:11, 0]
y21 = data_1[:11, 1]
y22 = data_2[:11, 1]

# Calculating the linear regression model
model21 = sm.OLS(y21, sm.add_constant(x2))
results21 = model21.fit()
model22 = sm.OLS(y22, sm.add_constant(x2))
results22 = model22.fit()

# extract intercept b and slope m
b21, m21 = results21.params
b22, m22 = results22.params

# plot y = m*x + b
axis2.axline(xy1=(0, b21), slope = m21, linestyle='-', color='b', linewidth=1)
axis22.axline(xy1=(0, b22), slope = m22, linestyle='-', color='b', linewidth=1)

###############################################################################################################################
###############################################< Section n°4 : Triangles and text >############################################
###############################################################################################################################
# Triangles

# DATA n°1
axis2.plot([25, 220, 220], [26, 26, 27], '--', color='b', linewidth=1)
axis22.plot([25, 220, 220], [24.5, 24.5, 25.5], '--', color='b', linewidth=1)

# Rectangles and texts

# DATA n°1
rect_1 = mpatches.Rectangle((150, 26.1), 70, 0.25, alpha=0.25, facecolor='b')
rect_2 = mpatches.Rectangle((150, 24.6), 70, 0.25, alpha=0.25, facecolor='b')
axis2.add_patch(rect_1)
axis22.add_patch(rect_2)
axis2.text(150, 26.15, '~0.9 $\AA^3$', fontsize=16, color='b')
axis22.text(150, 24.65, '~0.8 $\AA^3$', fontsize=16, color='b')

axis2.grid(linestyle=(0, (5, 10)))

#axis2.legend(handles=[line_3[0], line_4[0]], labels=['NaNbO$_2$F$_2$', 'NaTaO$_2$F$_2$'], loc='upper left', fontsize=16)

fig.savefig('figure_S16-b.png', dpi=300, bbox_inches='tight')
plt.show()
