import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import itertools 
plt.style.use('dark_background')

ax = plt.subplot(111)
color = itertools.cycle( ('#8dd3c7', '#feffb3', '#bfbbd9', '#fa8174', '#81b1d2', '#fdb462', '#b3de69', '#bc82bd', '#ccebc4', '#ffed6f'))

def plot_thang( ax, cutoff, height ):
    x = np.linspace(0., 20., 1000)
    y = height*(1.-(0.5*(np.tanh(x-cutoff) + 1.)))
    ax.fill_between(x, 0., y, color=color.next(), alpha=0.5)

ax.set_xlim(0., 20.)
ax.set_ylim(0., 1.)
ax.set_xlabel('Wavenumber')
ax.set_ylabel('Power')

ax.axvline( x = 2, ymin=0, ymax=1, color='r', alpha=0.8,  lw=10)
plt.savefig('spectrum_scaling_0.png', transparent=True)

plot_thang(ax, 5., 0.8)
ax.annotate(r'$\mathrm{Ra} \sim 10^5$', xy=(4., 0.75), xytext=(6,0.9), size=20, arrowprops=dict(facecolor='white') )
plt.savefig('spectrum_scaling_1.png', transparent=True)
plot_thang(ax, 10., 0.6)
ax.annotate(r'$\mathrm{Ra} \sim 10^6$', xy=(9., 0.55), xytext=(11,0.7), size=20, arrowprops=dict(facecolor='white') )
plt.savefig('spectrum_scaling_2.png', transparent=True)
plot_thang(ax, 15., 0.4)
ax.annotate(r'$\mathrm{Ra} \sim 10^7$', xy=(14., 0.40), xytext=(15,0.5), size=20, arrowprops=dict(facecolor='white') )
plt.savefig('spectrum_scaling_3.png', transparent=True)
plot_thang(ax, 20., 0.2)
ax.annotate(r'$\mathrm{Ra} \sim 10^8$', xy=(16., 0.22), xytext=(16,0.3), size=20, arrowprops=dict(facecolor='white') )
plt.savefig('spectrum_scaling_4.png', transparent=True)
plt.show()
