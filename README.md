# LST
Determination of the optimal initial threshold.
By running this code, csv files will be geneted with threshold for the computation
of binary lesion maps from 0.05 to 1.00 with increment of 0.05

The csv file contains columns for the folder of the reference images,
the name of FLAIR images, the initial threshold (kappa), the corresponding
Dice coefficients as well as values for sensitivity and specificity.

Please go to the directory where you pulled this repository.
Then run the following code in the terminal:

    python doit_arg.py "/data/henry1/tristan/LST/opt_thresh_results/<FLAIR-T1name>/*/*_bin_lesion_map.nii"


