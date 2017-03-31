# LST
Determination of the optimal initial threshold.
By running this code, csv files will be geneted with threshold for the computation
of binary lesion maps from 0.05 to 1.00 with increment of 0.05
The outputs are at __/data/henry1/tristan/LST/opt_thresh_results/<FLAIR-T1name>__

The csv file contains columns for the folder of the reference images,
the name of FLAIR images, the initial threshold (kappa), the corresponding
Dice coefficients as well as values for sensitivity and specificity.

Please go to the directory where you pulled this repository.
Then run the following code in the terminal:

    python doit_arg.py [-iter]

This is now specifically made for testing five mses. The outputs are at
__/data/henry7/PBR/subjects/LST/opt_thresh_results/test_subjects__


# Finding Centroids
lga_label.py tries to get centroids of both:
1. lst_edits and map it to lga lesion. By doing this, False Negative (FN) and True Positive (TP1) are calculated.
2. lga lesion mapping it back to lst_edits. By doing this, False Positive (FP) and True Positive (TP2)
are calculated

So far, five subjects have been done with this code, and two json files
 (centroid_lga.json and centroid_lst_edit.json) are generated in the directory:

 __/data/henry7/PBR/subjects/<mseID>/lst/lga/ms*/__

 The next step will do dice coefficient for these subjects:

    Dice Coeffient = 2TP / (2TP + FP + FN)

 which I think can be converted in this case to:

    Dice Coeffient = (TP1 + TP2) / (TP1 + TP2 + FP + FN)





