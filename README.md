The purpose of this repository is to demonstrate runtime issues with older HDF5 libraries

This repository is meant to serve as a minimal example and in-place testbed for the issues.

1. You will need to have Python3 set as your default python interpreter. 
1. You will need to install the python packages listed in the `requirements.txt` file
1. You will need CMake

Running CMake will:

1. Create a test file using `make_file.py` called `test_file.hdf5` and put it into the build directory
1. Create build environment, which can be "made" i.e. using Make to produce an executable example

Running `cmake --build` (or say make directly) will produce an executable called `hdf5_issues`.

The executable `hdf5_issues` will attempt to use `H5::H5Cpp` to read the file and test features.


