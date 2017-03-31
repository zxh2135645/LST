__author__ = 'sf713420'
import os
import numpy as np
import nibabel as nib
from scipy.ndimage import label
from nipype.utils.filemanip import save_json, load_json
from copy import deepcopy
import operator

class GetCenterLesion():

    def __init__(self, filename_list):
        self.filename_list = filename_list
        self.centroids = {}
        self.lesion_size = []

    def run_centroids(self):
        for filename in self.filename_list:
            if len(self.filename_list) == 1:
                kappa = 'reference'
            else:
                kappa = os.path.split(filename)[1].split('_')[2]
                if kappa == '1':
                    kappa = kappa + '.0'

            img = nib.load(filename)
            data = img.get_data()

            # print(img.header)
            labeled_img, nlabels = label(data > 0)
            self.lesion_size = np.bincount(labeled_img.ravel())
            # print(self.lesion_size)
            centroid = {}
            centroid['present'] = {}
            centroid['missing'] = {}
            for idx in range(1, len(self.lesion_size)):
                # idx is the index for labeled lesions
                # centroid['present'][idx] = {}
                l = (labeled_img == idx)
                l_coord = np.nonzero(l)
                # print(labeled_img.shape)
                # print(l_coord)

                x = x_sub = l_coord[0]
                y = y_sub = l_coord[1]
                z = z_sub = l_coord[2]
                x_mean = np.mean(x)
                y_mean = np.mean(y)
                z_mean = np.mean(z)

                x_round = int(round(x_mean))
                y_round = int(round(y_mean))
                z_round = int(round(z_mean))
                # print(x_round, y_round, z_round)

                for i in range(self.lesion_size[idx]):
                    if x_round == x[i] and y_round == y[i] and z_round == z[i]:
                        # print("Yes the centroid is in the shape")
                        # print(labeled_img[x_round, y_round, z_round])
                        centroid['present'][idx] = [x_round, y_round, z_round]
                        # centroid['present'][idx]['LesionSize'] = self.lesion_size[idx]
                        break
                    x_sub = np.delete(x_sub, 0)
                    y_sub = np.delete(y_sub, 0)
                    z_sub = np.delete(z_sub, 0)

                if  len(x_sub) == 0 and len(y_sub) == 0 and len(z_sub) == 0:
                    # centroid['missing'][idx] = [x_round, y_round, z_round]
                    # assumption is that there must be voxels in z_round plane
                    print("Oops, this centroid is not located in the lesion shape \n",
                          "The coordinate is (x, y, z): ", [x_round, y_round, z_round], '\n',
                          "lesion size is: ", self.lesion_size[idx], "\n",
                          "The lesion coordinate is: ", l_coord,
                          "\n",
                          "going to the 2nd level")

                    x_in_right = []
                    y_in_right = []
                    miss_coord_right = []
                    x_in_left = []
                    y_in_left = []
                    miss_coord_left = []
                    x_in_up = []
                    y_in_up = []
                    miss_coord_up = []
                    x_in_down = []
                    y_in_down = []
                    miss_coord_down = []
                    for i in range(self.lesion_size[idx]):
                        if z[i] == z_round:
                            if x[i] >= x_round:
                                x_in_right.append(x[i])
                                y_in_right.append(y[i])
                                miss_coord_right.append([x[i], y[i], z[i]])
                            if x[i] <= x_round:
                                x_in_left.append(x[i])
                                y_in_left.append(y[i])
                                miss_coord_left.append((x[i], y[i], z[i]))
                            if y[i] >= y_round:
                                x_in_up.append(x[i])
                                y_in_up.append(y[i])
                                miss_coord_up.append([x[i], y[i], z[i]])
                            if y[i] <= y_round:
                                x_in_down.append(x[i])
                                y_in_down.append(y[i])
                                miss_coord_down.append([x[i], y[i], z[i]])

                    # print(miss_coord)
                    #coord_list = [len(miss_coord_right), len(miss_coord_up), len(miss_coord_left), len(miss_coord_down)]
                    #max_index, max_value = max(enumerate(coord_list), key=operator.itemgetter(1))

                    if len(miss_coord_right) >= len(miss_coord_left):
                        new_miss_coord_lr = miss_coord_right
                        x_in_new_lr = x_in_right
                        y_in_new_lr = y_in_right
                    else:
                        new_miss_coord_lr = miss_coord_left
                        x_in_new_lr = x_in_left
                        y_in_new_lr = y_in_left

                    if len(miss_coord_up) >= len(miss_coord_down):
                        new_miss_coord_ud = miss_coord_up
                        x_in_new_ud = x_in_up
                        y_in_new_ud = y_in_up
                    else:
                        new_miss_coord_ud = miss_coord_down
                        x_in_new_ud = x_in_down
                        y_in_new_ud = y_in_down

                    if len(new_miss_coord_lr) >= len(new_miss_coord_ud):
                        x_in_new = x_in_new_lr
                        y_in_new = y_in_new_lr
                        new_miss_coord = new_miss_coord_lr
                    else:
                        x_in_new = x_in_new_ud
                        y_in_new = y_in_new_ud
                        new_miss_coord = new_miss_coord_ud

                    x_round2 = int(round(np.mean(x_in_new)))
                    y_round2 = int(round(np.mean(y_in_new)))
                    z_round2 = z_round
                    x_sub2 = x_in_new
                    y_sub2 = y_in_new
                    z_sub2 = [z_round2] * len(new_miss_coord)

                    for i in range(len(new_miss_coord)):
                        if x_round2 == x_in_new[i] and y_round2 == y_in_new[i]:
                            centroid['present'][idx] = [x_round2, y_round2, z_round2]
                            # centroid['present'][idx]['LesionSize'] = self.lesion_size[idx]
                            break
                        x_sub2 = np.delete(x_sub2, 0)
                        y_sub2 = np.delete(y_sub2, 0)
                        z_sub2 = np.delete(z_sub2, 0)

                    if len(x_sub2) == 0 and len(y_sub2) == 0 and len(z_sub2) == 0:
                        print("Oops, this centroid is still not in the lesion shape \n",
                              "The coordinate is (x, y, z): ", [x_round2, y_round2, z_round2], '\n',
                              "lesion size is: ", len(new_miss_coord), "\n",
                              "The lesion coordinate is: ", new_miss_coord,
                              "\n",
                              "going to the 3rd level")

                        # Assumption is that there must be voxels in y_round2 axis
                        x_in_right2D = []
                        miss_coord_right2D = []
                        x_in_left2D = []
                        miss_coord_left2D = []
                        y_in_up2D = []
                        miss_coord_up2D = []
                        y_in_down2D = []
                        miss_coord_down2D = []

                        for i in range(len(new_miss_coord)):
                            if y_in_new[i] == y_round2:
                                if x_in_new[i] >= x_round2:
                                    x_in_right2D.append(x_in_new[i])
                                    miss_coord_right2D.append([x_in_new[i], y_in_new[i]])
                                if x_in_new[i] <= x_round2:
                                    x_in_left2D.append(x_in_new[i])
                                    miss_coord_left2D.append([x_in_new[i], y_in_new[i]])
                            if x_in_new[i] == x_round2:
                                if y_in_new[i] >= y_round2:
                                    y_in_up2D.append(y_in_new[i])
                                    miss_coord_up2D.append([x_in_new[i], y_in_new[i]])
                                if y_in_new[i] <= y_round2:
                                    y_in_down2D.append(y_in_new[i])
                                    miss_coord_down2D.append([x_in_new[i], y_in_new[i]])

                        if len(miss_coord_right2D) >= len(miss_coord_left2D):
                            x_in_new2D = x_in_right2D
                            new_miss_coord2D_lr = miss_coord_right2D
                        else:
                            x_in_new2D = x_in_left2D
                            new_miss_coord2D_lr = miss_coord_left2D

                        if len(miss_coord_up2D) >= len(miss_coord_down2D):
                            y_in_new2D = y_in_up2D
                            new_miss_coord2D_ud = miss_coord_up2D
                        else:
                            y_in_new2D = y_in_down2D
                            new_miss_coord2D_ud = miss_coord_down2D

                        if len(x_in_new2D) >= len(y_in_new2D):
                            x_round3 = int(round(np.mean(x_in_new2D)))
                            y_round3 = y_round2
                            z_round3 = z_round2
                            new_miss_coord2D = new_miss_coord2D_lr
                            x_sub3 = x_in_new2D
                            y_sub3 = [y_round3] * len(new_miss_coord2D)
                            z_sub3 = [z_round3] * len(new_miss_coord2D)

                            for i in range(len(new_miss_coord2D)):
                                if x_in_new2D[i] == x_round3:
                                    centroid['present'][idx] = [x_round3, y_round3, z_round3]
                                    print("Congrats! The centroid is found in the 3rd level")
                                    # centroid['present'][idx]['LesionSize'] = self.lesion_size[idx]
                                    break
                                x_sub3 = np.delete(x_sub3, 0)
                                y_sub3 = np.delete(y_sub3, 0)
                                z_sub3 = np.delete(z_sub3, 0)
                        else:
                            x_round3 = x_round2
                            y_round3 = int(round(np.mean(y_in_new2D)))
                            z_round3 = z_round2
                            new_miss_coord2D = new_miss_coord2D_ud
                            x_sub3 = [x_round3] * len(new_miss_coord2D)
                            y_sub3 = y_in_new2D
                            z_sub3 = [z_round3] * len(new_miss_coord2D)

                            for i in range(len(new_miss_coord2D)):
                                if y_in_new2D[i] == y_round3:
                                    centroid['present'][idx] = [x_round3, y_round3, z_round3]
                                    print("Congrats! The centroid is found in the 3rd level")
                                    # centroid['present'][idx]['LesionSize'] = self.lesion_size[idx]
                                    break
                                x_sub3 = np.delete(x_sub3, 0)
                                y_sub3 = np.delete(y_sub3, 0)
                                z_sub3 = np.delete(z_sub3, 0)

                        if len(x_sub3) == 0 and len(y_sub3) == 0 and len(z_sub3) == 0:
                            # centroid['missing'][idx] = {}
                            centroid['missing'][idx] = {'Level1': [x_round, y_round, z_round],
                                                               'Level2': [x_round2, y_round2, z_round2],
                                                               'Level3': [x_round3, y_round3, z_round3]}
                            # centroid['missing'][idx]['LesionSize'] = self.lesion_size[idx]
                            print("Oops, this algorithm did not work. \n",
                                  "The coordinate is (x, y, z): ", [x_round3, y_round3, z_round3], '\n',
                                  "lesion size is: ", self.len(new_miss_coord2D), "\n",
                                  "The lesion coordinate is: ", new_miss_coord2D,
                                  "\n",
                                  "All three levels of centroids are stored in the json file.")

            if len(centroid['present']) == idx:
                print("Great, all the centroids are in the lesion shape! The kappa is: ", kappa)
            elif not centroid['present'] and not centroid['missing']:
                print("There was no lesion found in this scenario. The kappa is: ", kappa)
            else:
                raise ValueError(":( Please try other algorithm to get a valid point of the lesion shape")
            if kappa == 'reference':
                kappa_name = kappa
            else:
                kappa_name = '_kappa_' + kappa

            centroid_temp = deepcopy(centroid)
            self.centroids[kappa_name] = centroid_temp

        return self.centroids

    def make_lga_json(self, centroids = None):
        if centroids is None:
            centroids = self.run_centroids()

        outdir = os.path.split(os.path.split(self.filename_list[0])[0])[0]
        save_json(os.path.join(outdir, "centroid_lga.json"), centroids)
        print("The json file is generated in the directory: ", outdir)

def load_data(lstpath):
    img = nib.load(lstpath)
    data = img.get_data()
    return data

def cal_FP(f, lst_edit):
    kappa_array = np.linspace(0.05, 1.0, 20)
    if len(lst_edit) > 1:
        raise ValueError("More than one lst_edits files, please check")
    elif len(lst_edit) == 0:
        raise ValueError("No lst_edits file is found, please check your folder")
    elif len(lst_edit) == 1:
        lst_edit = ''.join(lst_edit)
    print("The lst_edit is in the directory: ", lst_edit)
    lst_data = load_data(lst_edit)
    # print(np.max(lst_data), np.min(lst_data))
    Lesion = GetCenterLesion(f)
    lesions = Lesion.run_centroids()
    for num in kappa_array:
        num_str = str(num)
        kappa_name = '_kappa_' + num_str
        if len(lesions[kappa_name]['missing']) != 0:
            raise ValueError("There is some centroid missed from the algorithm. "
                             "Please make sure all the center points are found in the lesion.")
        else:
            print("Awesome, all the centroids are present in the lesion.")

        lesion_items = sorted(lesions[kappa_name]['present'].items())
        FP = 0
        TP = 0
        lesions[kappa_name]['FalsePositives'] = []
        lesions[kappa_name]['TruePositives_to_ref'] = []
        for i, coord in lesion_items:
            if lst_data[coord[0], coord[1], coord[2]] == 0:
            # if lst_data[coord['xyz'][0], coord['xyz'][1], coord['xyz'][2]] == 0:
                lesions[kappa_name]['FalsePositives'].append(i)
                FP += 1
            else:
                lesions[kappa_name]['TruePositives_to_ref'].append(i)
                TP += 1

        lesions[kappa_name]['NumOfFP'] = FP
        lesions[kappa_name]['NumOfTP_to_ref'] = TP
    Lesion.make_lga_json(lesions)
    return [FP, TP]

def cal_FN(f, lst_edit):
    kappa_array = np.linspace(0.05, 1.0, 20)
    if len(lst_edit) > 1:
        raise ValueError("More than one lst_edits files, please check")
    elif len(lst_edit) == 0:
        raise ValueError("No lst_edits file is found, please check your folder")

    print("The lst_edit is in the directory: ", lst_edit)
    lga_data = [load_data(f_kappa) for f_kappa in f]
    print("There are {} elements in lga data".format(len(lga_data)))
    # print("Lga 0 is: ", lga_data[0])
    print("Check if it's 1 for mse3727: ", lga_data[0][52,102,47], lga_data[0][52,103,47])

    Lesion = GetCenterLesion(lst_edit)
    lesions = Lesion.run_centroids()
    ref_lesion = 'reference'
    if len(lesions[ref_lesion]['missing']) != 0:
        raise ValueError("There is some centroid missed from the algorithm. "
                             "Please make sure all the center points are found in the lesion.")
    else:
        print("Awesome, all the centroids are present in the lesion.")

    ref_lesion_to_kappas = {}

    for k, num in enumerate(kappa_array):
        num_str = str(num)
        kappa_name = '_kappa_' + num_str
        lesion_items = sorted(lesions[ref_lesion]['present'].items())
        print("Lesion items are: ", lesion_items)
        FN = 0
        TP = 0
        lesions[ref_lesion]['FalseNegatives'] = []
        lesions[ref_lesion]['TruePositives_to_lga'] = []
        for i, coord in lesion_items:
            print(i, coord)
            if lga_data[k][coord[0], coord[1], coord[2]] == 0:
            # if lga_data[coord['xyz'][0], coord['xyz'][1], coord['xyz'][2]] == 0:
                lesions[ref_lesion]['FalseNegatives'].append(i)
                FN += 1
                print("Oops, FN plus 1! FN is: ", FN)
            else:
                lesions[ref_lesion]['TruePositives_to_lga'].append(i)
                TP += 1
                print("Yay! TP plus 1! TP is: ", TP)

        print("FN, TP and kappa are: ", FN, TP, kappa_name)
        lesions[ref_lesion]['NumOfFN'] = FN
        lesions[ref_lesion]['NumOfTP_to_lga'] = TP
        print("After adding FN and TP, the lesion dictionary is: ", lesions)
        lesions_temp = deepcopy(lesions)
        ref_lesion_to_kappas[kappa_name] = lesions_temp
        print("After making a bigger dict to ref_lesion_to_kappas: ", ref_lesion_to_kappas)

    print("After all kappas, the ref_lesion_to_kappas looks: ", ref_lesion_to_kappas)
    outdir = os.path.split(os.path.split(f[0])[0])[0]
    save_json(os.path.join(outdir, "centroid_lst_edit.json"), ref_lesion_to_kappas)
    print("The json file is generated in the directory: ", outdir)
    return [FN, TP]


if __name__ == '__main__':
    from glob import glob
    test_mse = ['mse3727', 'mse4413', 'mse4482', 'mse4739', 'mse4754']
    FPTP = {}
    FNTP = {}
    for mse in test_mse:
        f = sorted(glob('/data/henry7/PBR/subjects/{0}/lst/lga/ms*/_kappa_*/ples_lga_*_rmms*.nii'.format(mse)))
        lst_edit = glob('/data/henry7/PBR/subjects/{0}/mindcontrol/ms*/lst/lst_edits/no_FP_filled_FN*'.format(mse))
        FPTP[mse] = cal_FP(f, lst_edit)
        # for cal_FN debugging
        FNTP[mse] = cal_FN(f, lst_edit)
        # A lot 2nd level centroid in mse4482 and mse4754
        # No lesion for mse3327 when kappa is 1.0
        # No lesion for mse4439 when kappa is or greater than 0.8

    print(FPTP, FNTP)
    """
        outdir = os.path.split(os.path.split(f[0])[0])[0]
        save_json(os.path.join(outdir, "centroid_lga.json"), lesions)
    """



