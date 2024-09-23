import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.interpolate import griddata
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import MultipleLocator

###############################################################################################################################
###########################################< Section n °1 : loading and plotting DATA >########################################
###############################################################################################################################

# Plot N°1
directory1 = "figure_7-b_data"
filenames1 = ["25.txt", "40.txt", "60.txt", "80.txt", "100.txt", "120.txt", "140.txt", "160.txt", 
              "180.txt", "200.txt", "220.txt", "230.txt", "240.txt", "250.txt", "260.txt", "270.txt", 
              "280.txt", "290.txt", "300.txt"]
y_values1 = [25, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 230, 240, 250, 260, 270, 280, 290, 300]

x1 = []
y1 = []
z1 = []

for i, filename in enumerate(filenames1):
    filepath = os.path.join(directory1, filename)
    data = np.loadtxt(filepath)
    mask = (data[:, 0] >= 32) & (data[:, 0] <= 35.8)
    x1.extend(data[mask, 0])
    y1.extend([y_values1[i]] * mask.sum())
    z1.extend(data[mask, 1])

x1 = np.array(x1)
y1 = np.array(y1)
z1 = np.array(z1)

xi1 = np.linspace(32, 35.8, 1000)
yi1 = np.linspace(min(y_values1), max(y_values1), 1000)
zi1 = griddata((x1, y1), z1, (xi1[None,:], yi1[:,None]), method='linear')

fig = plt.figure(figsize=(14, 4))
gs = fig.add_gridspec(1, 1)#, wspace = 0.4)
axis1 = gs.subplots()
im1 = axis1.imshow(zi1, extent=(xi1.min(), xi1.max(), yi1.min(), yi1.max()), origin='lower', cmap='inferno', aspect='auto')#, vmin = 5000, vmax = 35000)
axis1.set_xlim(32.25, 35.5)

# Set the position and size of the right plot
axis1.set_position([0.1, 0.1, 0.35, 0.5])

###############################################################################################################################
#################################################< Section n °2 : managing ticks >#############################################
###############################################################################################################################

# Twin axis and limits
axis12 = axis1.twinx()
axis121 = axis1.twiny()
axis12.set_ylim(25, 300)
axis12.set_xlim(32.25, 35.5)
axis121.set_ylim(25, 300)
axis121.set_xlim(32.25, 35.5)

# How much tick in the x-axis
axis1.locator_params(axis='x', nbins=8)
axis121.locator_params(axis='x', nbins=8)

# Lables

#axis1.set_title('(c)', color = 'k', fontsize=16, x = 0, y = 1.15)
axis1.set_xlabel(r'2$\theta$ (°)', color = 'k', fontsize=14)
axis1.set_ylabel('T (°C)', color = 'k', fontsize=14)
#axis12.set_ylabel('T (°C)', color = 'k', fontsize=14)

# Major ticks
# Plot N°1
axis1.tick_params(axis='y', colors='r', length = 8, width=1.5, labelsize = 10, direction='in')
axis1.tick_params(axis = 'x', colors = 'r', length = 8, width=1.5, labelsize = 10, direction='in')
axis1.yaxis.set_major_formatter(FormatStrFormatter('%.f'))

axis12.tick_params(axis='y', colors='r', length = 8, width=1.5, labelsize = 10, direction='in')
axis12.tick_params(axis='x', colors='r', length = 8, width=1.5, labelsize = 10, direction='in')
axis12.yaxis.set_major_formatter(FormatStrFormatter('%.f'))

axis121.tick_params(axis='y', colors='r', length = 8, width=1.5, labelsize = 10, direction='in')
axis121.tick_params(axis='x', colors='r', length = 8, width=1.5, labelsize = 10, direction='in')

#axis12.set_yticklabels([])

# Minor ticks
# Plot N°1
axis1.xaxis.set_minor_locator(MultipleLocator(0.1))
axis1.yaxis.set_minor_locator(MultipleLocator(10))
axis1.tick_params(which = 'minor', color = 'r', length = 4, width = 1.5, direction = "in")

axis12.xaxis.set_minor_locator(MultipleLocator(0.1))
axis12.yaxis.set_minor_locator(MultipleLocator(10))
axis12.tick_params(which = 'minor', color = 'r', length = 4, width = 1.5, direction = "in")

axis121.xaxis.set_minor_locator(MultipleLocator(0.1))
axis121.yaxis.set_minor_locator(MultipleLocator(10))
axis121.tick_params(which = 'minor', color = 'r', length = 4, width = 1.5, direction = "in")

###############################################################################################################################
###############################################< Section n °3 : managing colorbar >############################################
###############################################################################################################################

cbar = fig.colorbar(im1, ax=[axis1])
# Adjust the horizontal position of the colorbar
cax = cbar.ax
pos = list(cax.get_position().bounds)
pos[0] += 0.01 # move the colorbar to the right by 0.05
cax.set_position(pos)

# Handling colorbar ticks format and the scale factor x10^(-4)
cbar.formatter.set_powerlimits((4, 4))
cbar.formatter.set_useMathText(True) # To go from e-04 to x10^(-4)
cbar.ax.yaxis.offsetText.set_visible(False) # To make the scale factor disappear
cbar.ax.set_title(r'Intensity $\times 10^{4}$ (a.u.)', x= 5.5, y=0.12, rotation = 90)

###############################################################################################################################
#################################################< Section n °4 : texts and arrows >###########################################
###############################################################################################################################

axis1.text(32.56, 50, '(020)', fontsize=12, color='r')
axis1.text(32.85, 232, '(112)', fontsize=12, color='r')

axis1.text(34.02, 232, r'($\overline{2}$12)', fontsize=12, color='r')
axis1.text(34.1, 155, '(300)', fontsize=12, color='r')
axis1.text(34.93, 113, '(120)', fontsize=12, color='r')

# Add an arrow pointing to a certain point in the left plot
x_highlight3 = 32.7
y_highlight3 = 90
axis1.arrow(x_highlight3 - 0.05, y_highlight3 - 20, 0.1, 30,
          head_width=0.03, head_length=10, fc='r', ec='r')
axis1.arrow(x_highlight3 - 0.05, y_highlight3 - 20, 0.16, 28,
          head_width=0.03, head_length=10, fc='r', ec='r')

x_highlight4 = 33.05
y_highlight4 = 240
axis1.arrow(x_highlight4 - 0.05, y_highlight4 - 20, 0.21, -30,
          head_width=0.03, head_length=10, fc='r', ec='r')
axis1.arrow(x_highlight4 - 0.05, y_highlight4 - 20, 0.27, -28,
          head_width=0.03, head_length=10, fc='r', ec='r')

# Add an arrow pointing to a certain point in the right plot
x_highlight3 = 34.2
y_highlight3 = 282
axis1.arrow(x_highlight3 - 0.05, y_highlight3 - 20, -0.3, 21,
          head_width=0.03, head_length=10, fc='r', ec='r')
axis1.arrow(x_highlight3 - 0.05, y_highlight3 - 20, -0.36, 20,
          head_width=0.03, head_length=10, fc='r', ec='r')

x_highlight4 = 34.25
y_highlight4 = 195
axis1.arrow(x_highlight4 - 0.05, y_highlight4 - 20, -0.24, 30,
          head_width=0.03, head_length=10, fc='r', ec='r')
axis1.arrow(x_highlight4 - 0.05, y_highlight4 - 20, -0.3, 28,
          head_width=0.03, head_length=10, fc='r', ec='r')

x_highlight4 = 35.1
y_highlight4 = 155
axis1.arrow(x_highlight4 - 0.05, y_highlight4 - 20, -0.21, 30,
          head_width=0.03, head_length=10, fc='r', ec='r')
axis1.arrow(x_highlight4 - 0.05, y_highlight4 - 20, -0.27, 28,
          head_width=0.03, head_length=10, fc='r', ec='r')

fig.savefig('figure_7-b.png', dpi=300, bbox_inches='tight')
plt.show()
