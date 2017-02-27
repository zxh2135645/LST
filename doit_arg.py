__author__ = 'sf713420'

import os
from utils import doit_workflow
import sys
from glob import glob
import numpy as np

if __name__ == '__main__':
    print("Reading file from the path: ", sys.argv[1], "\n")
    data_ref = glob(sys.argv[1])
    print(data_ref)
    """
    FLAIR_T1_name = data_ref[0].split('/')[5]
    output_dir = '/data/henry1/tristan/LST/opt_thresh_results'
    sk_dir = os.path.join(output_dir, FLAIR_T1_name)
    thresh_array = np.linspace(0.05, 1.00, num=20)
    dwf = doit_workflow(data_ref, thresh_array, sink_dir=sk_dir)

    dwf.run()
    """