#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import statsmodels.api as sm

plt.style.use("default") # set the plot style
plt.rcParams["font.family"] = "Arial" # To globaly change the font POLICE
plt.rcParams["font.weight"] = "bold" # To write all font in bold
plt.rcParams["axes.labelweight"] = "bold" # To write all labels in bold

# Function to convert the slope value to scientific format 
def as_si(x, ndp):
    s = '{x:0.{ndp:d}e}'.format(x=x, ndp=ndp)
    m, e = s.split('e')
    return r'{m:s}\times 10^{{{e:d}}}'.format(m=m, e=int(e))

data_1 = np.loadtxt("figure_S5_data.txt", skiprows = 1, usecols=(1, 2))

fig, ax = plt.subplots(figsize=(7, 7))

# Creating second (x, y) axis and setting thier interval
ax2 = ax.twinx()
ax3 = ax.twiny()
ax3.set_xlim(0, 500)
ax2.set_ylim(-250, 0)

# Adjusting the major ticks
ax.tick_params(which = 'major', direction = "in", length = 10, width = 2, labelsize = 16)

# Adjusting the minor ticks
ax.xaxis.set_minor_locator(MultipleLocator(10))
ax.yaxis.set_minor_locator(MultipleLocator(10))
ax.tick_params(which = 'minor', length = 5, width = 1.5, direction = "in")

# Adjusting the major ticks
ax2.tick_params(which = 'major', direction = "in", length = 10, width = 2, labelsize = 16)
ax3.tick_params(which = 'major', direction = "in", length = 10, width = 2, labelsize = 16)

# Adjusting the minor ticks
ax3.xaxis.set_minor_locator(MultipleLocator(10))
ax2.yaxis.set_minor_locator(MultipleLocator(10))
ax2.tick_params(which = 'minor', length = 5, width = 1.5, direction = "in")
ax3.tick_params(which = 'minor', length = 5, width = 1.5, direction = "in")

ax2.axes.get_yaxis().set_ticklabels([])
ax3.axes.get_xaxis().set_ticklabels([])

ax.plot(data_1[:, 0], data_1[:, 1], '.', color = 'k', ms = 14, mec = 'k')
ax.set_xlabel(r"$\sigma$$_{iso, cal}$ (ppm)", fontsize = 18)
ax.set_ylabel(r"$\delta$$_{iso, exp}$ (ppm)", fontsize = 18)
#ax.set_title("Average F—Ta bond lengths as a function of \n $^{19}$F calculated chemical shifts", fontsize = 22)
ax.set_xlim(0, 500)
ax.set_ylim(-250, 0)
ax.grid(linestyle = (0, (5, 5)), color = "darkgrey", linewidth = 1)

# Establishing the linear regression

# DATA n°1

# Definnig the regression variables (x, y)
x1 = data_1[:, 0]
y11 = data_1[:, 1]


# Calculating the linear regression model
model11 = sm.OLS(y11, sm.add_constant(x1))
results11 = model11.fit()



# extract intercept b and slope m
b11, m11 = results11.params


# plot y = m*x + b
ax.axline(xy1=(0, b11), slope = m11, linestyle='--', color='r', linewidth=2)


text = [r'$\delta$$_{iso}$', r'$\sigma$$_{iso}$']
# Adding text referring to the slope = thermal expansion coefficient and the R-squared value
ax.text(x = 150, y = -30, s = text[0] + "$= {m:.3f}$".format(m=m11) + '$(15)$ ' + text[1] + ' $+$ ' + "${b:.1f}$".format(b=b11) + '$(4.0)$', color = 'r', fontsize = 14)
ax.text(x = 280, y = -50, s = f'$R^2 = {results11.rsquared:.4f}$', color = 'r', fontsize = 14)

# # Addinf text about the points in the graphic (NB-F) or (B-F)
# ax.text(x = 90, y = -180, s = "Terminal", color = 'g', fontsize = 22)
# ax.text(x = 130, y = -70, s = "Bridging", color = 'g', fontsize = 22)

fig.savefig('figure_S5.png', dpi=300, bbox_inches='tight')
plt.show()

print(results11.summary())
