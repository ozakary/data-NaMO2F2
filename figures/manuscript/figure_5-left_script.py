#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('default')
plt.rcParams["font.family"] = "Arial" # To globaly change the font POLICE
#lt.rcParams["font.weight"] = "bold" # To write all font in bold
#plt.rcParams["axes.labelweight"] = "bold" # To write all labels in bold

data_file = np.loadtxt("figure_5-left_data.txt", skiprows=1)
labels = ['$f$ {$\Delta_{iso}$ ; $^{19}F$}', 
          '$f$ {$\delta_{iso}$ ; $^{93}Nb$}', '$f$ {$C_Q$ ; $^{93}Nb$}', '$f$ {$\eta_Q$ ; $^{93}Nb$}', 
          '$f$ {$\delta_{iso}$ ; $^{23}Na$}', '$f$ {$C_Q$ ; $^{23}Na$}', '$f$ {$\eta_Q$ ; $^{23}Na$}']
colors = ['r', 'b'] #colors = ['r', '#1aaf6c', '#429bf4', '#d42cea', 'g', 'b', 'c'] 
gr_labels = ['ES', 'APO']
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

data_file_2 = np.column_stack([data_file, data_file[:, 1]])
angles += angles[:1]

graph_y = [data_file_2[0, 1:], data_file_2[1, 1:]]

fig, axis = plt.subplots(figsize=(9,9), subplot_kw=dict(polar=True))
for i in  range(len(colors)):
    axis.plot(angles, graph_y[i], color=colors[i], linewidth=1, label=gr_labels[i])
    axis.scatter(angles, graph_y[i], s=15, color=colors[i], zorder=10)
    axis.fill(angles, graph_y[i], color=colors[i], alpha=0.05)
    axis.set_theta_offset(np.pi / 2)
    axis.set_theta_direction(-1)
    axis.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=28)
for label, angle in zip(axis.get_xticklabels(), angles):
    if angle in (0, np.pi):
        label.set_horizontalalignment('center')
    elif 0 < angle < np.pi:
        label.set_horizontalalignment('left')
    else:
        label.set_horizontalalignment('right')
y_tick_labels = ['0%', '20%', '40%', '60%', '80%', '100%'] 
axis.set_ylim(0, 100)
axis.set_yticks([0, 20, 40, 60, 80, 100])
axis.set_yticklabels(y_tick_labels)
ind = y_tick_labels.index('0%')
gridlines = axis.yaxis.get_gridlines()
#gridlines[2].set_color("k")
gridlines[ind].set_linewidth(1)
axis.set_rlabel_position(180/num_vars)
axis.tick_params(axis='y', labelsize=24)

#axis.set_title("NaNbO$_2$F$_2$", fontsize=36, y=1.1, x = -0.25)
#axis.legend(loc='center right', bbox_to_anchor=(1.3, 1.1), fontsize=26)

fig.savefig('figure_5-left.png', dpi=300, bbox_inches='tight')
plt.show()
