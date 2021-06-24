## Run these commands in the terminal one by one.

# create a new environment
conda create -n "socmedia" python=3.7

# activate the newly created environment
conda activate socmedia

# install the necessary packages
conda install pip numpy pandas notebook scipy matplotlib requests

# launch python notebook from the new environment
jupyter notebook


## NOTE: for Miniconda installations only, if wanting to use the Anaconda navigator
conda install anaconda-navigator nb-conda-kernels

