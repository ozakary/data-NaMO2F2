#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.ticker import MultipleLocator
import statsmodels.api as sm

plt.style.use("default") # set the plot style
plt.rcParams["font.family"] = "Times New Roman" # To globaly change the font POLICE
plt.rcParams["font.weight"] = "bold" # To write all font in bold
plt.rcParams["axes.labelweight"] = "bold" # To write all labels in bold

# Function to convert the slope value to scientific format 
def as_si(x, ndp):
    s = '{x:0.{ndp:d}e}'.format(x=x, ndp=ndp)
    m, e = s.split('e')
    return r'{m:s}\times 10^{{{e:d}}}'.format(m=m, e=int(e))

###############################################################################################################################
###########################################< Section n °1 : loading and plotting DATA >########################################
###############################################################################################################################

# loading the "to be used DATA"
data_1 = np.loadtxt("figure_8_NaNbO2F2_data.txt", skiprows = 1)
data_2 = np.loadtxt("figure_8_NaTaO2F2_data.txt", skiprows = 1)

# Defining figure area and plotting data with y-errorbars on each data point

# DATA n°1
f, axis = plt.subplots(5, 2, figsize=(8, 14), sharex=True)
axis[0, 0].errorbar(data_1[:, 0], data_1[:, 1], yerr = data_1[:, 2], fmt = 'o', linewidth = .8,
             elinewidth = 1, ecolor = 'k', color = 'r', capsize = 4, ms = 5, mec = 'k')
axis[1, 0].errorbar(data_1[:, 0], data_1[:, 3], yerr = data_1[:, 4], fmt = "o", linewidth = .8, 
             elinewidth = 1, ecolor = 'k', color = 'r', capsize = 4, ms = 5, mec = 'k')
axis[2, 0].errorbar(data_1[:, 0], data_1[:, 5], yerr = data_1[:, 6], fmt="o", linewidth = .8, 
            elinewidth = 1, ecolor='k', color = 'r', capsize = 4, ms = 5, mec = 'k')
axis[3, 0].errorbar(data_1[:, 0], data_1[:, 7], yerr = data_1[:, 8], fmt = "o", linewidth = .8, 
             elinewidth = 1, ecolor = 'k', color = 'r', capsize = 4, ms = 5, mec = 'k')
axis[4, 0].errorbar(data_1[:, 0], data_1[:, 9], yerr = data_1[:, 10], fmt="o", linewidth = .8, 
            elinewidth = 1, ecolor='k', color = 'r', capsize = 4, ms = 5, mec = 'k')

# DATA n°2
axis[0, 1].errorbar(data_2[:, 0], data_2[:, 1], yerr = data_2[:, 2], fmt = 'o', linewidth = .8,
                    elinewidth = 1, ecolor = 'k', color = 'c', capsize = 4, ms = 5, mec = 'k')
axis[1, 1].errorbar(data_2[:, 0], data_2[:, 3], yerr = data_2[:, 4], fmt = 'o', linewidth = .8,
                    elinewidth = 1, ecolor = 'k', color = 'c', capsize = 4, ms = 5, mec = 'k')
axis[2, 1].errorbar(data_2[:, 0], data_2[:, 5], yerr = data_2[:, 6], fmt = 'o', linewidth = .8,
                    elinewidth = 1, ecolor = 'k', color = 'c', capsize = 4, ms = 5, mec = 'k')
axis[3, 1].errorbar(data_2[:, 0], data_2[:, 7], yerr = data_2[:, 8], fmt = "o", linewidth = .8, 
             elinewidth = 1, ecolor = 'k', color = 'c', capsize = 4, ms = 5, mec = 'k')
axis[4, 1].errorbar(data_2[:, 0], data_2[:, 9], yerr = data_2[:, 10], fmt="o", linewidth = .8, 
            elinewidth = 1, ecolor='k', color = 'c', capsize = 4, ms = 5, mec = 'k')

# Setting axis twins
ax30x = axis[3, 0].twiny()
ax40x = axis[4, 0].twiny()
ax31x = axis[3, 1].twiny()
ax41x = axis[4, 1].twiny()

ax00 = axis[0, 0].twinx()
ax10 = axis[1, 0].twinx()
ax20 = axis[2, 0].twinx()
ax30 = axis[3, 0].twinx()
ax40 = axis[4, 0].twinx()
ax01 = axis[0, 1].twinx()
ax11 = axis[1, 1].twinx()
ax21 = axis[2, 1].twinx()
ax31 = axis[3, 1].twinx()
ax41 = axis[4, 1].twinx()

# Hiding ticklabels
ax30x.axes.get_xaxis().set_ticklabels([])
ax40x.axes.get_xaxis().set_ticklabels([])
ax31x.axes.get_xaxis().set_ticklabels([])
ax41x.axes.get_xaxis().set_ticklabels([])

ax00.axes.get_yaxis().set_ticklabels([])
ax10.axes.get_yaxis().set_ticklabels([])
ax20.axes.get_yaxis().set_ticklabels([])
ax30.axes.get_yaxis().set_ticklabels([])
ax40.axes.get_yaxis().set_ticklabels([])
ax01.axes.get_yaxis().set_ticklabels([])
ax11.axes.get_yaxis().set_ticklabels([])
ax21.axes.get_yaxis().set_ticklabels([])
ax31.axes.get_yaxis().set_ticklabels([])
ax41.axes.get_yaxis().set_ticklabels([])

# hiding the spines between the different plots of the twin axis
ax00.spines['bottom'].set_visible(False)
ax10.spines['top'].set_visible(False)
ax10.spines['bottom'].set_visible(False)
ax20.spines['top'].set_visible(False)
ax01.spines['bottom'].set_visible(False)
ax11.spines['top'].set_visible(False)
ax11.spines['bottom'].set_visible(False)
ax21.spines['top'].set_visible(False)

# Setting limites of the twin axis

# DATA n°1
ax30x.set_xlim(15, 310)
ax40x.set_xlim(15, 310)

ax00.set_ylim(7.98, 8.10)
ax10.set_ylim(5.38, 5.50)
ax20.set_ylim(7.58, 7.7)
ax30.set_ylim(101.9, 102.4)
ax40.set_ylim(320, 330)

# DATA n°2
ax31x.set_xlim(15, 310)
ax41x.set_xlim(15, 310)

ax01.set_ylim(8.06, 8.18)
ax11.set_ylim(5.42, 5.54)
ax21.set_ylim(7.46, 7.58)
ax31.set_ylim(102.1, 102.6)
ax41.set_ylim(320, 330)

# Managing major ticks of the twin axis
ax30x.tick_params(top = False, labeltop = False, bottom = True, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax40x.tick_params(top = True, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)

ax31x.tick_params(top = False, labeltop = False, bottom = True, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax41x.tick_params(top = True, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)

ax00.tick_params(top = False, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax10.tick_params(top = False, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax20.tick_params(top = False, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax30.tick_params(top = False, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax40.tick_params(top = False, labeltop = False, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)

ax01.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax11.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax21.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax31.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
ax41.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)

# Managing minor ticks of the twin axis
ax30x.xaxis.set_minor_locator(MultipleLocator(10))
ax30x.tick_params(top = False, labeltop = False, bottom = True, labelbottom = False, which = 'minor', length = 4, width = 1.5, direction = "in")
ax40x.xaxis.set_minor_locator(MultipleLocator(10))
ax40x.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")

ax31x.xaxis.set_minor_locator(MultipleLocator(10))
ax31x.tick_params(top = False, labeltop = False, bottom = True, labelbottom = False, which = 'minor', length = 4, width = 1.5, direction = "in")
ax41x.xaxis.set_minor_locator(MultipleLocator(10))
ax41x.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")


ax00.yaxis.set_minor_locator(MultipleLocator(.005))
ax00.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
ax10.yaxis.set_minor_locator(MultipleLocator(.005))
ax10.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
ax20.yaxis.set_minor_locator(MultipleLocator(.005))
ax20.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
ax30.yaxis.set_minor_locator(MultipleLocator(.025))
ax30.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
ax40.yaxis.set_minor_locator(MultipleLocator(.5))
ax40.tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")

ax01.yaxis.set_minor_locator(MultipleLocator(.005))
ax01.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'minor', length = 4, width = 1.5, direction = "in")
ax11.yaxis.set_minor_locator(MultipleLocator(.005))
ax11.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'minor', length = 4, width = 1.5, direction = "in")
ax21.yaxis.set_minor_locator(MultipleLocator(.005))
ax21.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'minor', length = 4, width = 1.5, direction = "in")
ax31.yaxis.set_minor_locator(MultipleLocator(.025))
ax31.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'minor', length = 4, width = 1.5, direction = "in")
ax41.yaxis.set_minor_locator(MultipleLocator(.5))
ax41.tick_params(left = True, labelleft = False, right = False, labelright = False, which = 'minor', length = 4, width = 1.5, direction = "in")

# Adjusting the number of major-ticks of the twin axis
ax30x.locator_params(axis='x', nbins=6)
ax40x.locator_params(axis='x', nbins=6)

ax31x.locator_params(axis='x', nbins=6)
ax41x.locator_params(axis='x', nbins=6)

ax00.locator_params(axis='y', nbins=7)
ax10.locator_params(axis='y', nbins=7)
ax20.locator_params(axis='y', nbins=7)
ax30.locator_params(axis='y', nbins=6)
ax40.locator_params(axis='y', nbins=6)

ax01.locator_params(axis='y', nbins=7)
ax11.locator_params(axis='y', nbins=7)
ax21.locator_params(axis='y', nbins=7)
ax31.locator_params(axis='y', nbins=6)
ax41.locator_params(axis='y', nbins=6)

# Establishing the linear regression

# DATA n°1

# Definnig the regression variables (x, y)
x1 = data_1[:11, 0]
y11 = data_1[:11, 1]
y12 = data_1[:11, 3]
y13 = data_1[:11, 5]
y14 = data_1[:11, 7]

# Calculating the linear regression model
model11 = sm.OLS(y11, sm.add_constant(x1))
results11 = model11.fit()
model12 = sm.OLS(y12, sm.add_constant(x1))
results12 = model12.fit()
model13 = sm.OLS(y13, sm.add_constant(x1))
results13 = model13.fit()
model14 = sm.OLS(y14, sm.add_constant(x1))
results14 = model14.fit()

# extract intercept b and slope m
b11, m11 = results11.params
b12, m12 = results12.params
b13, m13 = results13.params
b14, m14 = results14.params

# plot y = m*x + b
axis[0, 0].axline(xy1=(0, b11), slope = m11, linestyle='-', color='b', linewidth=1)
axis[1, 0].axline(xy1=(0, b12), slope = m12, linestyle='-', color='b', linewidth=1)
axis[2, 0].axline(xy1=(0, b13), slope = m13, linestyle='-', color='b', linewidth=1)
axis[3, 0].axline(xy1=(0, b14), slope = m14, linestyle='-', color='b', linewidth=1)

# Adding text referring to the slope = thermal expansion coefficient and the R-squared value
axis[0, 0].text(x = 50, y = 8.075, s = r"$\alpha_a = {0:s}$".format(as_si(m11, 2)), color = 'b', fontsize = 14)
axis[0, 0].text(x = 50, y = 8.058, s = f'$R^2 = {results11.rsquared:.4f}$', color = 'b', fontsize = 14)
axis[1, 0].text(x = 50, y = 5.495, s = r"$\alpha_b = {0:s}$".format(as_si(m12, 2)), color = 'b', fontsize = 14)
axis[1, 0].text(x = 50, y = 5.478, s = f'$R^2 = {results12.rsquared:.4f}$', color = 'b', fontsize = 14)
axis[2, 0].text(x = 50, y = 7.695, s = r"$\alpha_c = {0:s}$".format(as_si(m13, 2)), color = 'b', fontsize = 14)
axis[2, 0].text(x = 50, y = 7.678, s = f'$R^2 = {results13.rsquared:.4f}$', color = 'b', fontsize = 14)
axis[3, 0].text(x = 50, y = 102.3, s = r"$\alpha_\beta = {0:s}$".format(as_si(m14, 2)), color = 'b', fontsize = 14)
axis[3, 0].text(x = 50, y = 102.225, s = f'$R^2 = {results14.rsquared:.4f}$', color = 'b', fontsize = 14)

# DATA n°2

# Definnig the regression variables (x, y)
x2 = data_2[:11, 0]
y21 = data_2[:11, 1]
y22 = data_2[:11, 3]
y23 = data_2[:11, 5]
y24 = data_2[:11, 7]

# Calculating the linear regression model
model21 = sm.OLS(y21, sm.add_constant(x2))
results21 = model21.fit()
model22 = sm.OLS(y22, sm.add_constant(x2))
results22 = model22.fit()
model23 = sm.OLS(y23, sm.add_constant(x2))
results23 = model23.fit()
model24 = sm.OLS(y24, sm.add_constant(x2))
results24 = model24.fit()

# extract intercept b and slope m
b21, m21 = results21.params
b22, m22 = results22.params
b23, m23 = results23.params
b24, m24 = results24.params

# plot y = m*x + b
axis[0, 1].axline(xy1=(0, b21), slope = m21, linestyle='-', color='b', linewidth=1)
axis[1, 1].axline(xy1=(0, b22), slope = m22, linestyle='-', color='b', linewidth=1)
axis[2, 1].axline(xy1=(0, b23), slope = m23, linestyle='-', color='b', linewidth=1)
axis[3, 1].axline(xy1=(0, b24), slope = m24, linestyle='-', color='b', linewidth=1)

# Adding text referring to the slope = thermal expansion coefficient and the R-squared value
axis[0, 1].text(x = 50, y = 8.155, s = r"$\alpha_a = {0:s}$".format(as_si(m21, 2)), color = 'b', fontsize = 14)
axis[0, 1].text(x = 50, y = 8.138, s = f'$R^2 = {results21.rsquared:.4f}$', color = 'b', fontsize = 14)
axis[1, 1].text(x = 50, y = 5.535, s = r"$\alpha_b = {0:s}$".format(as_si(m22, 2)), color = 'b', fontsize = 14)
axis[1, 1].text(x = 50, y = 5.518, s = f'$R^2 = {results22.rsquared:.4f}$', color = 'b', fontsize = 14)
axis[2, 1].text(x = 50, y = 7.575, s = r"$\alpha_c = {0:s}$".format(as_si(m23, 2)), color = 'b', fontsize = 14)
axis[2, 1].text(x = 50, y = 7.558, s = f'$R^2 = {results23.rsquared:.4f}$', color = 'b', fontsize = 14)
axis[3, 1].text(x = 50, y = 102.5, s = r"$\alpha_\beta = {0:s}$".format(as_si(m24, 2)), color = 'b', fontsize = 14)
axis[3, 1].text(x = 50, y = 102.425, s = f'$R^2 = {results24.rsquared:.4f}$', color = 'b', fontsize = 14)


# Defining the Y-axis limits

# DATA n°1
axis[0, 0].set_xlim(15, 310)
axis[0, 0].set_ylim(7.98, 8.10)
axis[1, 0].set_ylim(5.38, 5.50)
axis[2, 0].set_ylim(7.58, 7.7)
axis[3, 0].set_ylim(101.9, 102.4)
axis[4, 0].set_ylim(320, 330)

# DATA n°2
axis[0, 1].set_ylim(8.06, 8.18)
axis[1, 1].set_ylim(5.42, 5.54)
axis[2, 1].set_ylim(7.46, 7.58)
axis[3, 1].set_ylim(102.1, 102.6)
axis[4, 1].set_ylim(320, 330)

# Labels and graphic texts

# DATA n°1
#axis[0, 0].set_title('NaNbO$_2$F$_2$', fontsize = 25, y = 1.28)
axis[0, 0].set_xlabel('T (°C)', fontsize = 18)
axis[4, 0].set_xlabel('T (°C)', fontsize = 18)
axis[0, 0].set_ylabel(r'a ($\AA$)', fontsize = 18)
axis[1, 0].set_ylabel(r'b ($\AA$)', fontsize = 18)
axis[2, 0].set_ylabel(r'c ($\AA$)', fontsize = 18)
axis[3, 0].set_ylabel(r'$\beta$ (°)', fontsize = 18)
axis[4, 0].set_ylabel(r' V ($\AA^3$)', fontsize = 18)

# DATA n°2
#axis[0, 1].set_title('NaTaO$_2$F$_2$', fontsize = 25, y = 1.28)
axis[0, 1].set_xlabel('T (°C)', fontsize = 18)
axis[4, 1].set_xlabel('T (°C)', fontsize = 18)
axis[0, 1].set_ylabel(r'a ($\AA$)', fontsize = 18)
axis[1, 1].set_ylabel(r'b ($\AA$)', fontsize = 18)
axis[2, 1].set_ylabel(r'c ($\AA$)', fontsize = 18)
axis[3, 1].set_ylabel(r'$\beta$ (°)', fontsize = 18)
axis[4, 1].set_ylabel(r' V ($\AA^3$)', fontsize = 18)
axis[0, 1].yaxis.set_label_position("right")
axis[1, 1].yaxis.set_label_position("right")
axis[2, 1].yaxis.set_label_position("right")
axis[3, 1].yaxis.set_label_position("right")
axis[4, 1].yaxis.set_label_position("right")


# DATA n°1

# hiding the spines between the different plots and setting the label positions
axis[0, 0].spines['bottom'].set_visible(False)
axis[1, 0].spines['top'].set_visible(False)
axis[1, 0].spines['bottom'].set_visible(False)
axis[2, 0].spines['top'].set_visible(False)
axis[0, 0].xaxis.set_label_coords(.5, 1.26)
axis[0, 1].xaxis.set_label_coords(.5, 1.26)

# Adjusting the major ticks
axis[0, 0].xaxis.tick_top() # moving the x axis tick to the top of
axis[0, 0].tick_params(top = True, labeltop = True, bottom = False, labelbottom = False, which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
axis[1, 0].tick_params(which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[2, 0].tick_params(which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[1, 0].get_xaxis().set_visible(False) # hiding the x axis ticks
axis[2, 0].xaxis.tick_bottom() # moving the x axis tick to the bottom
axis[3, 0].xaxis.tick_top() # moving the x axis tick to the top of
axis[3, 0].tick_params(which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)
axis[4, 0].tick_params(which = 'major', length = 8, width = 1.5, direction = "in", labelsize = 14)

# Adjusting the number of major-ticks
axis[0, 0].locator_params(axis='y', nbins=7)
axis[0, 0].locator_params(axis='x', nbins=6)
axis[1, 0].locator_params(axis='y', nbins=7)
axis[1, 0].locator_params(axis='x', nbins=6)
axis[2, 0].locator_params(axis='y', nbins=7)
axis[2, 0].locator_params(axis='x', nbins=6)
axis[3, 0].locator_params(axis='y', nbins=6)
axis[3, 0].locator_params(axis='x', nbins=6)
axis[4, 0].locator_params(axis='y', nbins=6)
axis[4, 0].locator_params(axis='x', nbins=6)

# Adjusting the minor ticks
axis[0, 0].xaxis.set_minor_locator(MultipleLocator(10))
axis[0, 0].yaxis.set_minor_locator(MultipleLocator(.005))
axis[0, 0].tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
axis[1, 0].xaxis.set_minor_locator(MultipleLocator(10))
axis[1, 0].yaxis.set_minor_locator(MultipleLocator(.005))
axis[1, 0].tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
axis[2, 0].xaxis.set_minor_locator(MultipleLocator(10))
axis[2, 0].yaxis.set_minor_locator(MultipleLocator(.005))
axis[2, 0].tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
axis[3, 0].xaxis.set_minor_locator(MultipleLocator(10))
axis[3, 0].yaxis.set_minor_locator(MultipleLocator(.025))
axis[3, 0].tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")
axis[4, 0].xaxis.set_minor_locator(MultipleLocator(10))
axis[4, 0].yaxis.set_minor_locator(MultipleLocator(.5))
axis[4, 0].tick_params(which = 'minor', length = 4, width = 1.5, direction = "in")

# DATA n°2

# hiding the spines between the different plots
axis[0, 1].spines['bottom'].set_visible(False)
axis[1, 1].spines['top'].set_visible(False)
axis[1, 1].spines['bottom'].set_visible(False)
axis[2, 1].spines['top'].set_visible(False)

# Adjusting the major ticks
axis[0, 1].xaxis.tick_top() # moving the x axis tick to the top of
axis[0, 1].tick_params(top = True, labeltop = True, bottom = False, labelbottom = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[0, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[1, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[2, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[3, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[4, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'major', direction = "in", length = 8, width = 1.5, labelsize = 14)
axis[1, 1].get_xaxis().set_visible(False) # hiding the x axis ticks
axis[2, 1].xaxis.tick_bottom() # moving the x axis tick to the bottom
axis[3, 1].xaxis.tick_top() # moving the x axis tick to the top of

# Adjusting the number of major-ticks
axis[0, 1].locator_params(axis='y', nbins=7)
axis[0, 1].locator_params(axis='x', nbins=6)
axis[1, 1].locator_params(axis='y', nbins=7)
axis[1, 1].locator_params(axis='x', nbins=6)
axis[2, 1].locator_params(axis='y', nbins=7)
axis[2, 1].locator_params(axis='x', nbins=6)
axis[3, 1].locator_params(axis='y', nbins=6)
axis[3, 1].locator_params(axis='x', nbins=6)
axis[4, 1].locator_params(axis='y', nbins=6)
axis[4, 1].locator_params(axis='x', nbins=6)

# Adjusting the minor ticks
axis[0, 1].xaxis.set_minor_locator(MultipleLocator(10))
axis[0, 1].yaxis.set_minor_locator(MultipleLocator(.005))
axis[0, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'minor', length = 4, width = 1.5, direction = "in")
axis[1, 1].xaxis.set_minor_locator(MultipleLocator(10))
axis[1, 1].yaxis.set_minor_locator(MultipleLocator(.005))
axis[1, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'minor', length = 4, width = 1.5, direction = "in")
axis[2, 1].xaxis.set_minor_locator(MultipleLocator(10))
axis[2, 1].yaxis.set_minor_locator(MultipleLocator(.005))
axis[2, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'minor', length = 4, width = 1.5, direction = "in")
axis[3, 1].xaxis.set_minor_locator(MultipleLocator(10))
axis[3, 1].yaxis.set_minor_locator(MultipleLocator(.025))
axis[3, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'minor', length = 4, width = 1.5, direction = "in")
axis[4, 1].xaxis.set_minor_locator(MultipleLocator(10))
axis[4, 1].yaxis.set_minor_locator(MultipleLocator(.5))
axis[4, 1].tick_params(right = True, labelright = True, left = False, labelleft = False, which = 'minor', length = 4, width = 1.5, direction = "in")

###############################################################################################################################
###########################################< Section n°2 : Adding breaks and rectangles >######################################
###############################################################################################################################

# DATA n°1
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=axis[0, 0].transAxes, color='k', clip_on=False)
axis[0, 0].plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axis[0, 0].plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axis[1, 0].transAxes)  # switch to the bottom axes
axis[1, 0].plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axis[1, 0].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
axis[1, 0].plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axis[1, 0].plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axis[2, 0].transAxes)  # switch to the bottom axes
axis[2, 0].plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axis[2, 0].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# DATA n°2
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=axis[0, 1].transAxes, color='k', clip_on=False)
axis[0, 1].plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axis[0, 1].plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axis[1, 1].transAxes)  # switch to the bottom axes
axis[1, 1].plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axis[1, 1].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
axis[1, 1].plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axis[1, 1].plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axis[2, 1].transAxes)  # switch to the bottom axes
axis[2, 1].plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axis[2, 1].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# What's cool about this is that now if we vary the distance between
# ax and ax2 via f.subplots_adjust(hspace=...) or plt.subplot_tool(),
# the diagonal lines will move accordingly, and stay right at the tips
# of the spines they are 'breaking'
f.subplots_adjust(wspace=.08, hspace=.14)

#to add the colored rectangles in the plots also the area between the figures
# DATA n°1
xmin, xmax = 220,300
_,top = f.transFigure.inverted().transform(axis[0, 0].transAxes.transform([0,1]))
_,bottom = f.transFigure.inverted().transform(axis[2, 0].transAxes.transform([0,0]))
trans = matplotlib.transforms.blended_transform_factory(axis[0, 0].transData, f.transFigure)
r_1 = matplotlib.patches.Rectangle(xy=(xmin,bottom), width=xmax-xmin, height=top-bottom, transform=trans,
                                 fc='Grey', alpha = .25, ec='C0', lw=0)
f.add_artist(r_1)

# DATA n°2
_,top = f.transFigure.inverted().transform(axis[0, 1].transAxes.transform([0,1]))
_,bottom = f.transFigure.inverted().transform(axis[2, 1].transAxes.transform([0,0]))
trans = matplotlib.transforms.blended_transform_factory(axis[0, 1].transData, f.transFigure)
r_2 = matplotlib.patches.Rectangle(xy=(xmin,bottom), width=xmax-xmin, height=top-bottom, transform=trans,
                                 fc='Grey', alpha = .25, ec='C0', lw=0)
f.add_artist(r_2)

axis[3, 0].axvspan(xmin, xmax, color = 'Grey', alpha = .25)
axis[4, 0].axvspan(xmin, xmax, color = 'Grey', alpha = .25)
axis[3, 1].axvspan(xmin, xmax, color = 'Grey', alpha = .25)
axis[4, 1].axvspan(xmin, xmax, color = 'Grey', alpha = .25)

#plt.tight_layout()

f.savefig('figure_8.png', dpi=300, bbox_inches='tight')
plt.show()
