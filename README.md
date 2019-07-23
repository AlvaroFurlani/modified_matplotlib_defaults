# Modified matplotlib default settings

The file *my_mpl_settings* given in this repository is a configuration file that contains modified matplotlib settings for creating publication-ready plots. Download this file, and include it in a directory accessible by the Python file(s) used for producing the plots. The settings in this file override the default settings in the file *matplotlibrc* until the kernel is restarted or the default settings are restored.

Using this approach to modify plotting settings is especially useful when working on multiple projects, and a different set of defaults is applied to each one. In this way, the default values are easily modified for all plots in a given project, and reproducibility is guaranteed when producing the plots in different environments and/or at another time.

Note -- the description below adopts the following convention:
```python
import matplotlib.pyplot as plt
from matplotlib import  rc_file
rc_file('my_mpl_settings') # file containing your settings
```

The modifications to the default values shown in this repository represent my personal preferences; you may need to modify it further to adapt to your own needs/preferences. If you do change any setting in the file *my_mpl_settings*, make sure to run the line of code ```rc_file()``` again.

Moreover, the default matplotlib default settings can be restored through:
```python
plt.rcdefaults()
```

```python
plt.rcParams.update({'figure.figsize': [3.5, 1.5],
                     'font.size': 6, 'font.family': 'serif',
                     'grid.alpha': 0.3, 'grid.linewidth': 0.5,
                     'legend.borderaxespad': 0, 'legend.edgecolor': 'black', 'legend.fancybox': False,
                     'legend.framealpha': 1, 'patch.linewidth': 0.5,
                     'savefig.dpi': 600,
                     'xtick.direction': 'in', 'xtick.top': True, 'xtick.major.width': 0.5,
                     'ytick.direction': 'in', 'ytick.right': True, 'ytick.major.width': 0.5})
```

The following settings have been modified in comparison to the matplotlib default values:

### Figure and axes:

* Figure size (**figure.figsize**): changed from ```6.4 x 4.8``` inches to ```3.5 x 1.5``` inches. This figure size may seem too small in a matplotlib window; however, it is the ideal size for double-column articles (assuming letter paper size). You may need to adjust the  height value when creating the figure object according to your dataset:
```python 
plt.figure(figsize=(3.5, new_height))
```

where ```new_height``` is the desired figure height, in inches. If your figure spans both columns, increase its width from ```3.5``` to ```7.0625``` inches:
```python 
plt.figure(figsize=(7.0625, new_height))
```

* Tight layout (**figure.constrained_layout.use**): changed from ```False``` to ```True```. It adjusts all plots elements so that the white space between the axes and the figure frame is reduced; i.e., the plot itself ocuppies all available space in the figure. The amount of horizontal and vertical padding is controlled by **figure.constrained_layout.h_pad** and **figure.constrained_layout.w_pad**, respectively, which were changed from ```0.04167``` (3 points) to ```0.01389``` (1 point);

* Axis spines width (**axes.linewidth**): changed from ```0.8``` to ```0.5``` points;

* Resolution for saving the figure (**savefig.dpi**): changed from ```figure``` (which inherits the resolution from the figure object -- 100 dots per inch) to ```600``` dots per inch;

* File format of the saved figure (**savefig.format**): changed from ```png``` to ```pdf``` (this parameter is used only if ```fname``` in ```plt.savefig()``` does not contain a file extension and ```format=None```).

### Plots:

* Lines width (**lines.linewidth**): changed from ```1.5``` to ```0.75``` points;

* Markers edge width (**lines.markeredgewidth**): changed from ```1.0``` to ```0.2``` points;

* Patch frame width (**patch.linewidth**): changed from ```1.0``` to ```0.5``` points (this parameter also controls the line width of the legend frame).

### Legend: 

* Legend location (**legend.loc**): changed from ```best``` to ```upper right``` (it may provide faster rendering for figures with many graphs);

* Legend frame transparency (**legend.framealpha**): changed from ```0.8``` to ```1.0``` (i.e., no background elements are seen through the legend frame).

#### Side note:

### Grids and ticks:

* Display major grids (**axes.grid**): changed from ```False``` to ```True```; to turn off the grids for a specific figure, insert the following line of code after the figure creation:
```python
plt.grid(False)
```

* Grid line width (**grid.linewidth**): changed from ```0.8``` to ```0.5``` points;

* Grid transparency (**grid.alpha**): changed from ```1.0``` to ```0.3```;

* Draw ticks on the top and right spines (**xtick.top** and **ytick.rigth**): changed from ```False``` to ```True```; to turn off this behavior for a specific figure, insert one the following lines of code after the figure creation:
```python
plt.gca().tick_params(top=False, right=False) # turn off ticks on both top and right spines
plt.gca().tick_params(top=False) # turn off ticks only on top spine
plt.gca().tick_params(right=False) # turn onff ticks only on right spine
```

* Major ticks width (**xtick.major.width** and **ytick.major.width**): changed from ```0.8``` to ```0.5``` points;

* Ticks direction (**xtick.direction** and **ytick.direction**): changed from ```out``` to ```in```.

### Text:

* Text font family (**font.family**): changed from ```sans-serif``` to ```serif```;

* Text font size (**font.size**): changed from ```10``` to ```6``` points.
