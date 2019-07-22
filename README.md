# mod_matplotlib_defaults

### Figure and axes:

* Figure size (**figure.figsize**): changed from 6.4 x 4.8 inches to 3.5 x 1.5 inches. This figure size may seem too small in a matplotlib window; however, it is the ideal size for double-column articles (you may need to adjust the figure height according to your dataset -- use *plt.figure(figsize=(3.5, new_height))*, where *new_height* is the desired figure height in inches). If your figure spans both columns, increase its width from 3.5 to 7.0625 inches (*plt.figure(figsize=(7.0625, new_height))*).

* Tight layout (**figure.constrained_layout.use**): changed from *False* to *True*. It adjusts all plots elements so that the white space between the axes and the figure frame is reduced. The amount of horizontal and vertical padding is controlled by **figure.constrained_layout.h_pad** and **figure.constrained_layout.w_pad**, respectively, which were changed from 0.04167 (3 points) to 0.01389 (1 point);

* Axis spines width (**axes.linewidth**): changed from 0.8 to 0.5 points;

* Resolution for saving the figure (**savefig.dpi**): changed from *figure* (which inherits the resolution from the figure object -- 100 dots per inch) to 600 dots per inch.

### Plots:

* Width of line plots (**lines.linewidth**): change from 1.5 to 0.75 points;

* Width of the edges around markers (**lines.markeredgewidth**): change from 1.0 to 0.2 points;

* Width of the borders of patch objects (**patch.linewidth**): change from 1.0 to 0.5 points.

### Legend: 

* Legend location (**legend.loc**): change from *best* to *upper right* (it may provide faster rendering for figures with many graphs);

* Transparency of legend frame (**legend.framealpha**): change from 0.8 to 1.

### Grids and ticks:

* Display axes grid (**axes.grid**): change from *False* to *True* (to turn off the grids for a specific figure, use *plt.grid(False)* after the figure creation);

* Grid line width (**grid.linewidth**): change from 0.8 to 0.5 points;

* Grid transparency (**grid.alpha**): change from 1.0 to 0.3;

* Draw ticks on the top and right spines (**xtick.top** and **ytick.rigth**): change from *False* to *True* (how to turn it off?);

* Major ticks width (**xtick.major.width** and **ytick.major.width**): change from 0.8 to 0.5 points;

* Ticks direction (**xtick.direction** and **ytick.direction**): change from *out* to *in*.

### Text:

* Text font family (**font.family**): change from *sans-serif* to *serif*;

* Text font size (**font.size**): change from 10 to 6 points.
