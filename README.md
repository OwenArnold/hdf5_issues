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

## Options

To illustrate issues. CMake has a `BACKWARD_COMPAT_FILE` flag, which defaults to `OFF`. If this is set to `ON`
then the test file will be made with a layout comaptible for reading via version 1.8 of HDF5.

## Notes

Note that the HDF5 find module looks for a CMake `HDF5_ROOT` variable. Building newer versions of HDF5, and 
setting this will allow you to switch HDF5 versions (if different from system). You can optionally provide this
The source for hdf5 is [here](https://bitbucket.hdfgroup.org/scm/hdffv/hdf5.git), and can be generated/built
with CMake. I had to use CPack to create a "complete" directory (header, libraries, etc) that the HDF5 find
module coud process. I simply packaged with cpack then `tar -xvzf` the tarball in place. This could then be 
used as the `HDF5_ROOT` as described above. 

HDF5 now comes with a set of [tools](https://support.hdfgroup.org/HDF5/doc/RM/Tools.html). These are also 
built by default if you build from source. Note that [h5format_compat](https://support.hdfgroup.org/HDF5/doc/RM/Tools.html#Tools-FormatConvert)
can be used to convert datasets from newer HDF5 layout to older ones. For example `h5format_convert new_file.hdf5 -d local_name`

