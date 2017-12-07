import pySALEPlot as psp
import matplotlib.pyplot as plt
from numpy import arange,sqrt,ma

# Need this for the colorbars we will make on the mirrored plot
from mpl_toolkits.axes_grid1 import make_axes_locatable

# This plotting script is based on that designed to plot 
# material and temperature in the Chicxulub example

# If viridis colormap is available, use it here
try:
    plt.set_cmap('viridis')
except:
    plt.set_cmap('YlGnBu_r')

# distances between tracers
def get_distances(s,line):
    x=s.xmark[line]
    y=s.ymark[line]
    return sqrt((x[:-1]-x[1:])**2+(y[:-1]-y[1:])**2)

# Define the maximum separation allowed when plotting lines
maxsep=3.

def make_colorbar(ax,p,f):
    # Create axes either side of the plot to place the colorbars
    divider = make_axes_locatable(ax)
    cx=divider.append_axes("left", size="5%", pad=0.7)
    cb=fig.colorbar(p,cax=cx)
    cb.set_label(psp.longFieldName(f))
    # Need to set the labels on the left for this colorbar
    cx.yaxis.tick_left()
    cx.yaxis.set_label_position('left')


# Make an output directory
dirname='DenYld'
psp.mkdir_p(dirname)

# Open the datafile
model=psp.opendatfile('Steinheim_1/jdata.dat')

# Set the distance units to km
model.setScale('km')

# Set up a pylab figure
fig=plt.figure(figsize=(8,4))

ax=fig.add_subplot(111,aspect='equal')

# Loop over timesteps
for i in arange(0,model.nsteps,1):

    # Set the axis labels
    ax.set_xlabel('r [km]')
    ax.set_ylabel('z [km]')

    # Set the axis limits
    ax.set_xlim([-3,3])
    ax.set_ylim([-2,1])

    # Read the time step 'i' from the datafile: 
    # read two or more fields by making a list of their abbreviations
    step=model.readStep(['Yld','Den'],i)
    
    # -- the classic iSALEPlot mirrored setup. Plot the second field
    # -- using negative x values
    p1=ax.pcolormesh(model.x,model.y,step.data[1],
            vmin=0.,vmax=3.e3)
    p2=ax.pcolormesh(-model.x,model.y,step.data[0],
            vmin=0,vmax=5.E7)

    # Material boundaries
    [ax.contour(model.xc,model.yc,step.cmc[mat],1,colors='k',linewidths=0.5) for mat in [0,1,2]]
    [ax.contour(-model.xc,model.yc,step.cmc[mat],1,colors='k',linewidths=0.5) for mat in [0,1,2]]

    # Tracer lines
    for u in range(1,model.tracer_numu):
        tru=model.tru[u]
        
        # Plot the tracers in horizontal lines, every 5 lines
        for l in arange(0,len(tru.xlines),5):
    
            # Get the distances between pairs of tracers in xlines
            dist=get_distances(step,tru.xlines[l])
            # Mask the xmark values if separation too big... means the line won't be connected here
            ax.plot(ma.masked_array(step.xmark[tru.xlines[l]][:-1],mask=dist > maxsep*tru.d[0]),
                    step.ymark[tru.xlines[l]][:-1],
                    c='#808080',marker='None',linestyle='-',linewidth=0.5)
    
   
    # Add colorbars; only need to do this once
    if i == 0: make_colorbar(ax,p2,step.plottype[0])

    ax.set_title('{: 5.2f} s'.format(step.time))
    
    # Save the figure
    fig.savefig('{}/DenYld-{:05d}.png'.format(dirname,i),dpi=300)
    
    # Remove the field, ready for the next timestep to be plotted
    ax.cla()
