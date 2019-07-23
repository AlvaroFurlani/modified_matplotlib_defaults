import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc_file
rc_file('my_mpl_settings')

x = np.linspace(0, 4*np.pi, 400)
y1 = np.sin(x)
y2 = np.exp(-x**2/20) * np.sin(x**2)

# %% Example 1: modified default values
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My xlabel', ylabel='My ylabel')
plt.savefig('test_modified_default')

# %% Example 2: modified default values, larger figure size
plt.figure(figsize=(3.5, 3))
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My xlabel', ylabel='My ylabel')
plt.legend()
plt.savefig('test_modified_default_larger_figsize')

# %% Example 3: modified default values, without grid
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My xlabel', ylabel='My ylabel')
plt.legend()
plt.grid(False)
plt.savefig('test_modified_default_no_grid')

# %% Example 4: modified default values, without ticks on the top and right spines
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My xlabel', ylabel='My ylabel')
plt.legend()
plt.gca().tick_params(top=False, right=False)
plt.savefig('test_modified_default_no_top_right_ticks')

# %% Example 5: modified default values
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(3.5, 3))
ax1.plot(x, y1, label='Curve 1')
ax1.plot(x, y2, label='Curve 2')
ax1.set(xlabel='My xlabel', ylabel='My ylabel')
ax1.legend()
ax2.plot(x, y1, label='Curve 1')
ax2.plot(x, y2, label='Curve 2')
ax2.set(xlabel='My xlabel', ylabel='My ylabel')
ax2.legend(borderaxespad=0, edgecolor='k', fancybox=False)
plt.savefig('test_modified_default_legends')

# %% Restore matplotlib defaults
plt.rcdefaults()

# %% Example 6: original default values, without grid
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My xlabel', ylabel='My ylabel')
plt.legend()
plt.savefig('test_original_default_no_grid.pdf')

# %% Example 7: original default values, with grid
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My xlabel', ylabel='My ylabel')
plt.legend()
plt.grid()
plt.savefig('test_original_default_with_grid.pdf')