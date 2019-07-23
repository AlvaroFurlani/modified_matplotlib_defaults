import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 400)
y1 = np.sin(x)
y2 = np.exp(-x**2/20) * np.sin(x**2)

# %% Example 1: modified default values
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My x_label', ylabel='My y_label')
plt.legend()
plt.savefig('test_modified_default')

# %% Example 2: modified default values, larger figure size
plt.figure(figsize=(7.0625, 3))
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My x_label', ylabel='My y_label')
plt.legend()
plt.savefig('test_modified_default_larger_figsize')

# %% Example 3: modified default values, without grid
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My x_label', ylabel='My y_label')
plt.legend()
plt.grid(False)
plt.savefig('test_modified_default_no_grid')

# %% Example 4: modified default values, without ticks on the top and right spines
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My x_label', ylabel='My y_label')
plt.legend()
plt.gca().tick_params(top=False, right=False)
plt.savefig('test_modified_default_no_top_right_ticks')

# %% Restore matplotlib defaults
plt.rcdefaults()

# %% Example 5: original default values, without grid
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My x_label', ylabel='My y_label')
plt.legend()
plt.savefig('test_original_default_no_grid.pdf')

# %% Example 6: original default values, with grid
plt.figure()
plt.plot(x, y1, label='Curve 1')
plt.plot(x, y2, label='Curve 2')
plt.gca().set(xlabel='My x_label', ylabel='My y_label')
plt.legend()
plt.grid()
plt.savefig('test_original_default_with_grid.pdf')