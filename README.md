# Cryosparc 3D variability plotter

I like the interactive plots cryoSPARC makes of the clustered 3D variability
analysis, but you can't download them (or at least, I couldn't figure out
how to).

## Usage
 1. Install the required packages to a python env.
 2. Download your passthrough files from a clustered 3D var display job. They'll have names like `[project]_[job]_particles_cluster_[cluster-number]_exported.cs`
 3. Hard code where the data files are and how much you want to reduce the plot by (sorry, no argparse)

You want to reduce the particles by a somewhat significant factor. Plotly isn't very good at plotting 70k dots!