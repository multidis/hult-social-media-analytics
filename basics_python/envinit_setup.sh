# create a new environment and install necessary packages
# (run these commands in the terminal)
conda create -n "socmedia" python=3.7
conda install pip numpy pandas notebook scipy matplotlib requests

# activate the newly created environment
conda activate socmedia

# launch python notebook
jupyter notebook

# NOTE: for Miniconda installations, if wanting to use Anaconda navigator
conda install anaconda-navigator nb-conda-kernels

