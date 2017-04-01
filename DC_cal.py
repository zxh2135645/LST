__author__ = 'sf713420'
from nipype.utils.filemanip import load_json
from glob import glob
import numpy as np

if __name__ == '__main__':
    test_mse = ['mse3727', 'mse4413', 'mse4482', 'mse4739', 'mse4754']
    centroids_lst_edit = {}
    centroids_lga = {}

    for mse in test_mse:
        dir_lst_edit = ''.join(glob('/data/henry7/PBR/subjects/{0}/lst/lga/ms*/centroid_lst_edit.json'.format(mse)))
        dir_lga = ''.join(glob('/data/henry7/PBR/subjects/{0}/lst/lga/ms*/centroid_lga.json'.format(mse)))
        centroids_lst_edit[mse] = load_json(dir_lst_edit)
        centroids_lga[mse] = load_json(dir_lga)
        print(centroids_lga[mse])

        kappa_array = np.linspace(0.05, 1.0, 20)
        TP_lga = []
        FP = []
        TP_lst_edit = []
        FN = []

        for i, num in enumerate(kappa_array):
            num_str = str(num)
            kappa_name = '_kappa_' + num_str
            kappa_name_list = []
            DSC_list = []

            TP_lga.append(centroids_lga[mse][kappa_name]['NumOfTP_to_ref'])
            FP.append(centroids_lga[mse][kappa_name]['NumOfFP'])
            TP_lst_edit.append(centroids_lst_edit[mse][kappa_name]['reference']['NumOfTP_to_lga'])
            FN.append(centroids_lst_edit[mse][kappa_name]['reference']['NumOfFN'])
            kappa_name_list.append(kappa_name)

            DSC = (TP_lga[i] + TP_lst_edit[i]) / (TP_lst_edit[i] + TP_lga + FP + FN)
            DSC_list.append(DSC)



