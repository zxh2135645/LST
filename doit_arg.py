__author__ = 'sf713420'

import os
from nipype.interfaces.base import isdefined
from utils import doit_workflow, flatten
import sys
from glob import glob
import numpy as np
import csv

if __name__ == '__main__':
    #print("Reading file from the path: ", sys.argv[1], "\n")
    #data_ref = glob(sys.argv[1])
    iter = sys.argv[1]
    mse_test = ['mse3727', 'mse4413', 'mse4482', 'mse4739', 'mse4754']
    data_ref = [glob('/data/henry7/PBR/subjects/{0}/lst/lga/ms*/*/*_bin_lesion_map.nii'.format(mse)) for mse in mse_test]
    data_ref = flatten(data_ref)
    print(data_ref,'\n', len(data_ref))


    # FLAIR_T1_name = data_ref[0].split('/')[5]
    output_dir = '/data/henry1/tristan/LST/opt_thresh_results/test_subjects'
    sk_dir = os.path.join(output_dir,
                          # FLAIR_T1_name
                          )
    if iter == '-iter':
        thresh_array = np.linspace(0.05, 1.00, num=20)
    elif isdefined(iter):
        raise ValueError("The option for iterate binary threshold is -iter")

    dwf = doit_workflow(data_ref, thresh_array, sink_dir=sk_dir)
    dwf.run()

    """
    with open(os.path.join(sk_dir, '_bin_thresh_'+thresh_array[i]), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    csvfile.close()
    """