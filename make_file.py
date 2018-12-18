import sys
import os
import h5py
import os
import argparse

parser = argparse.ArgumentParser(description='Script to create test hdf5 file')

positional_args = parser.add_argument_group('Positional arguments')
positional_args.add_argument(
        'OutFilePath', nargs='?',
        help='The full file directory to write to')

arguments = parser.parse_args()
if not arguments.OutFilePath:
    raise ValueError("No directory specified")
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")
# Make test file in parent directory
parent_dir =arguments.OutFilePath
f = h5py.File(os.path.join(parent_dir, 'test_file.hdf5'), 'w')
# type variable length string
dt = h5py.special_dtype(vlen=str)     
dset = f.create_dataset("dataset", dtype=dt, data=u"this_is_a_utf8_var_length_string")
f.close()



