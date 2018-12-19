import sys
import os
import h5py
import os
import argparse
import re
import semantic_version

parser = argparse.ArgumentParser(description='Script to create test hdf5 file')

positional_args = parser.add_argument_group('Positional arguments')
positional_args.add_argument(
        'OutFilePath', nargs='?',
        help='The full file directory to write to')
optional_args = parser.add_argument_group('Optional arguments')
optional_args.add_argument('-e', '--earliest', action='store_true', default=False,
                               help='Forces h5py to write as backward compatible version')
arguments = parser.parse_args()
if not arguments.OutFilePath:
    raise ValueError("No directory specified")
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

# Check h5py is using 1.10.0 or greater
h5py_info = h5py.version.info
match = re.search("HDF5\s*(\d+\.\d+\.\d+)", h5py_info)
lib_version = match.group(1)
if semantic_version.Version(lib_version) < semantic_version.Version('1.10.0'):
    raise Exception('h5py using old HDF5 version ', lib_version)

# Make test file in parent directory
parent_dir =arguments.OutFilePath
# libver `latest` means 1.10.1 writing
write_ver = 'earliest' if arguments.earliest else 'latest'
f = h5py.File(os.path.join(parent_dir, 'test_file.hdf5'), 'w', libver=write_ver)
# type variable length string
dt = h5py.special_dtype(vlen=str)     
dset = f.create_dataset("dataset", (1,), dtype=dt, data=u"this_is_a_utf8_var_length_string")
f.close()



