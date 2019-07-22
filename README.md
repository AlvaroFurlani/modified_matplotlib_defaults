# mod_matplotlib_defaults

### Figure:

* Figure size (**figure.figsize**): change from 6.4 by 4.8 inches to 3.5 by 1.5 inches (comments... 2 columns: 7.0625 in);
* Tight layout (**figure.constrained_layout.use**): change from *False* to *True* (it makes the plot elements to fit on the figure area, removing unecessary white space around the axes). The padding is controlled by **figure.constrained_layout.h_pad** and **figure.constrained_layout.w_pad**, which were changed from 0.04167 (3 points) to 0.01389 (1 point);

### Legend:


* Line width of the graphs (**lines.linewidth**): change from 1.5 to 0.75 points;
* Line width of the edges around markers (**lines.markeredgewidth**): change from 1.0 to 0.2 points;
* Line width of the borders of patch objects (**patch.linewidth**): change from 1.0 to 0.5 points;
* Text font family (**font.family**): change from *sans-serif* to *serif*;
* Text font size (**font.size**): change from 10 to 6 points;
* Line width of axes edge (**axes.linewidth**): change from 0.8 to 0.5 points;
* Display axis grid (**axes.grid**): change from *False* to *True* (to turn off the grids for a specific figure, use *plt.grid(False)* after the figure creation);
* Grid line width (**grid.linewidth**): change from 0.8 to 0.5 points;
* Grid transparency (**grid.alpha**): change from 1.0 to 0.3;
* Draw ticks on the top spine (**xtick.top**): change from *False* to *True* (how to turn it off?);
* Draw ticks on the right spine (**ytick.rigth**): change from *False* to *True* (how to turn it off?);
* Major ticks width (**xtick.major.width** and **ytick.major.width**): change from 0.8 to 0.5 points;
* Ticks direction (**xtick.direction** and **ytick.direction**): change from *out* to *in*;
* Legend location (**legend.loc**): change from *best* to *upper right* (it may provide faster rendering for figures with many graphs);
* Transparency of legend frame (**legend.framealpha**): change from 0.8 to 1;

* Resolution for saving the figure (**savefig.dpi**): change from *figure* (which inherits the resolution from the figure object -- 100 dots per inch) to 600 dots per inch;
