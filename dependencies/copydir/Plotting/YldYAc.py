import pySALEPlot as psp
import matplotlib.pyplot as plt
from numpy import arange,sqrt,ma

# Need this for the colorbars we will make on the mirrored plot
from mpl_toolkits.axes_grid1 import make_axes_locatable

# This example plotting script designed to plot yield strength
# and acoustic fluidisation strength in the Chicxulub example

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

def make_colorbars(ax,p,f,units):
    # Create axes either side of the plot to place the colorbars
    divider = make_axes_locatable(ax)
    cx1=divider.append_axes("right", size="5%", pad=0.7)
    cx2=divider.append_axes("left", size="5%", pad=0.7)
    cb1=fig.colorbar(p[0],cax=cx1)
    cb1.set_label(psp.longFieldName(f[0])+units[0])
    cb2=fig.colorbar(p[1],cax=cx2)
    cb2.set_label(psp.longFieldName(f[1])+units[1])
    # Need to set the labels on the left for this colorbar
    cx2.yaxis.tick_left()
    cx2.yaxis.set_label_position('left')


# Make an output directory
dirname='YldYAc'
psp.mkdir_p(dirname)

# Open the datafile
model=psp.opendatfile('Chicxulub/jdata.dat')

# Set the distance units to km
model.setScale('km')

# Set up a pylab figure
fig=plt.figure(figsize=(8,4))

ax=fig.add_subplot(111,aspect='equal')

# Loop over timesteps
for i in arange(0,model.nsteps,2):

    # Set the axis labels
    ax.set_xlabel('r [km]')
    ax.set_ylabel('z [km]')

    # Set the axis limits
    ax.set_xlim([-100,100])
    ax.set_ylim([-50,45])

    # Read the time step 'i' from the datafile: 
    # read two or more fields by making a list of their abbreviations
    step=model.readStep(['Yld','YAc'],i)
    
    # -- the classic iSALEPlot mirrored setup. Plot the second field
    # -- using negative x values
    p1=ax.pcolormesh(model.x,model.y,step.data[0]*1.e-6,
            vmin=0,vmax=1.5e2)
    p2=ax.pcolormesh(-model.x,model.y,step.data[1],
            vmin=0,vmax=1.)

    # Material boundaries
    [ax.contour(model.xc,model.yc,step.cmc[mat],1,colors='k',linewidths=0.5) for mat in [0,1,2]]
    [ax.contour(-model.xc,model.yc,step.cmc[mat],1,colors='k',linewidths=0.5) for mat in [0,1,2]]

    # Tracer lines
#    for u in range(1,model.tracer_numu):
#        tru=model.tru[u]
#        # Plot the tracers in horizontal lines, every 5 lines
#        for l in arange(0,len(tru.xlines),5):
#    
#            # Get the distances between pairs of tracers in xlines
#            dist=get_distances(step,tru.xlines[l])
#            # Mask the xmark values if separation too big... means the line won't be connected here
#            ax.plot(ma.masked_array(step.xmark[tru.xlines[l]][:-1],mask=dist > maxsep*tru.d[0]),
#                    step.ymark[tru.xlines[l]][:-1],
#                    c='#808080',marker='None',linestyle='-',linewidth=0.5)
    
   
    # Add colorbars; only need to do this once
    if i == 0: make_colorbars(ax,[p1,p2],step.plottype,[' MPa',''])

    ax.set_title('{: 5.2f} s'.format(step.time))
    
    # Save the figure
    fig.savefig('{}/YldYAc-{:05d}.png'.format(dirname,i))
    
    # Remove the field, ready for the next timestep to be plotted
    ax.cla()
