

import os
import pandas as pds


def from_ascii(filename):
    df = pds.read_csv(filename, sep=' ', skiprows=6, header=None)
    return df


def filename(diag_name, path, time, species_name, patch):
    return path + os.path.sep + diag_name + '_' + species_name +\
           '_{:02}_'.format(patch) + '{:.6e}'.format(time) + '.txt'
