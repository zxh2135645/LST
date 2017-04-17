__author__ = 'sf713420'
from nipype.utils.filemanip import load_json
from glob import glob
import numpy as np
import pandas as pd
import csv
import os
from glob import glob
from copy import deepcopy

def cal_lDC(mse_list, flag=None):
    centroids_lst_edit = {}
    centroids_lga = {}
    data_dict = {}
    data_list = [['mse', 'kappa', 'TP_to_ref', 'TP_to_lga', 'FP', 'FN', 'LesionDC']]

    for mse in mse_list:
        dir_lst_edit = ''.join(glob('/data/henry7/PBR/subjects/{0}/lst/lga/ms*/centroid_lst_edit.json'.format(mse)))
        dir_lga = ''.join(glob('/data/henry7/PBR/subjects/{0}/lst/lga/ms*/centroid_lga.json'.format(mse)))
        centroids_lst_edit[mse] = load_json(dir_lst_edit)
        centroids_lga[mse] = load_json(dir_lga)
        # print(centroids_lga[mse])

        kappa_array = np.linspace(0.05, 1.0, 20)
        TP_lga = []
        FP = []
        TP_lst_edit = []
        FN = []
        kappa_name_list = []
        DSC_list = []
        data = [['mse', 'kappa', 'TP_to_ref', 'TP_to_lga', 'FP', 'FN', 'LesionDC']]

        for i, num in enumerate(kappa_array):
            num_str = str(num)
            kappa_name = '_kappa_' + num_str

            TP_lga.append(centroids_lga[mse][kappa_name]['NumOfTP_to_ref'])
            FP.append(centroids_lga[mse][kappa_name]['NumOfFP'])
            TP_lst_edit.append(centroids_lst_edit[mse][kappa_name]['reference']['NumOfTP_to_lga'])
            FN.append(centroids_lst_edit[mse][kappa_name]['reference']['NumOfFN'])
            kappa_name_list.append(kappa_name)

            DSC = (TP_lga[i] + TP_lst_edit[i]) / (TP_lst_edit[i] + TP_lga[i] + FP[i] + FN[i])
            DSC_list.append(DSC)

            data.append([mse, num_str, TP_lga[i], TP_lst_edit[i], FP[i], FN[i], DSC])
            data_list.append([mse, num_str, TP_lga[i], TP_lst_edit[i], FP[i], FN[i], DSC])
            # print(DSC_list)
        print(data)
        data_dict[mse] = deepcopy(data)

    if flag == 'dict':
        return data_dict
    elif flag == 'list':
        return data_list
    else:
        raise NameError("Please input a flag of either dict or list")

def write_lDC_csv(mse_list, data_dict):
    # Output is by default sinking to PBR output directory
    # Each output csv file contains only one mse with iteration through kappa
    for mse in mse_list:
        outdir = ''.join(glob(os.path.join('/data/henry7/PBR/subjects/',mse,'lst/lga/ms*')))
        data = data_dict[mse]
        df = pd.DataFrame(data)
        df.to_csv(os.path.join(outdir, 'Lesion_DC.csv'), header=False, index=False)

        """
        with open('test.csv', 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(data)
        """
def write_lDC_list_csv(data_list, outdir):
    # The list output need to be defined prehand
    # The csv file contains all mses in your test_mse list
    df = pd.DataFrame(data_list)
    df.to_csv(os.path.join(outdir, 'Lesion_DC.csv'), header=False, index=False)

def get_new_metric(lesion_DC, LST_doit):
    df1 = pd.read_csv(lesion_DC)
    print(df1)
    df2 = pd.read_csv(LST_doit)
    df1['VoxelDC'] = df2['DC']
    df1['NewMetric_DC'] = 0.5 * df1['LesionDC'] + 0.5 * df1['VoxelDC']
    outdir = os.path.split(lesion_DC)[0]
    df1.to_csv(os.path.join(outdir, 'final_metric.csv'))
    pass


if __name__ == '__main__':
    # This script is basically calculating lesion based Dice Coefficient and new metrics for lga algorithm

    test_mse = ['mse3727', 'mse4413', 'mse4482', 'mse4739', 'mse4754']
    # data_dict = cal_lDC(test_mse)
    # print(data_dict)
    # print(len(data_dict))
    data_list = cal_lDC(test_mse, flag='list')
    outdir = '/data/henry1/tristan/LST/opt_thresh_results/test_subjects/_bin_thresh_0.3'
    #write_lDC_list_csv(data_list, outdir)

    lesion_DC = os.path.join(outdir, 'Lesion_DC.csv')
    LST_doit = ''.join(glob(os.path.join(outdir, 'LST_doit*.csv')))
    get_new_metric(lesion_DC, LST_doit)










