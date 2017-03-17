__author__ = 'sf713420'
import os
import numpy as np
import nibabel as nib
from scipy.ndimage import label
from nipype.utils.filemanip import save_json, load_json

class GetCenterLesion():

    def __init__(self, filename_list):
        self.filename_list = filename_list
        self.centroids = {}
        self.lesion_size = []

    def run_centroids(self):
        for filename in self.filename_list:

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
                    for i in range(self.lesion_size[idx]):
                        if z_round == z[i]:
                            if x[i] >= x_round:
                                x_in_right.append(x[i])
                                y_in_right.append(y[i])
                                miss_coord_right.append([x[i], y[i], z[i]])
                            if x[i] <= x_round:
                                x_in_left.append(x[i])
                                y_in_left.append(y[i])
                                miss_coord_left.append((x[i], y[i], z[i]))

                    # print(miss_coord)
                    if len(miss_coord_right) >= len(miss_coord_left):
                        new_miss_coord = miss_coord_right
                        x_in_new = x_in_right
                        y_in_new = y_in_right
                    else:
                        new_miss_coord = miss_coord_left
                        x_in_new = x_in_left
                        y_in_new = y_in_left

                    x_round2 = int(round(np.mean(x_in_new)))
                    y_round2 = int(round(np.mean(y_in_new)))
                    z_round2 = z_round

                    x_sub2 = x_in_new
                    y_sub2 = y_in_new
                    z_sub2 = [z_round2] * len(new_miss_coord)

                    for i in range(len(new_miss_coord)):
                        if x_round2 == x_in_new[i] and y_round2 == y_in_new[i]:
                            centroid['present'][idx] = [x_round2, y_round2, z_round2]
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

                        for i in range(len(new_miss_coord)):
                            if y_in_new[i] == y_round2:
                                if x_in_new[i] >= x_round2:
                                    x_in_right2D.append(x_in_new[i])
                                    miss_coord_right2D.append([x_in_new[i], y_in_new[i]])
                                if x_in_new[i] <= x_round2:
                                    x_in_left2D.append(x_in_new[i])
                                    miss_coord_left2D.append([x_in_new[i], y_in_new[i]])

                        if len(miss_coord_right2D) >= len(miss_coord_left2D):
                            x_in_new2D = x_in_right2D
                            new_miss_coord2D = miss_coord_right2D
                        else:
                            x_in_new2D = x_in_left2D
                            new_miss_coord2D = miss_coord_left2D

                        x_round3 = int(round(np.mean(x_in_new2D)))
                        y_round3 = y_round2
                        z_round3 = z_round2

                        x_sub3 = x_in_new2D
                        y_sub3 = [y_round3] * len(new_miss_coord2D)
                        z_sub3 = [z_round3] * len(new_miss_coord2D)

                        for i in range(len(new_miss_coord2D)):
                            if x_in_new2D[i] == x_round3:
                                centroid['present'][idx] = [x_round3, y_round3, z_round3]
                                break
                            x_sub3 = np.delete(x_sub3, 0)
                            y_sub3 = np.delete(y_sub3, 0)
                            z_sub3 = np.delete(z_sub3, 0)

                        if len(x_sub3) == 0 and len(y_sub3) == 0 and len(z_sub3) == 0:
                            centroid['missing'][idx] = {1: [x_round, y_round, z_round],
                                                        2: [x_round2, y_round2, z_round2],
                                                        3: [x_round3, y_round3, z_round3]}
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

            kappa_name = '_kappa_' + kappa
            self.centroids[kappa_name] = centroid
        return self.centroids

    def make_json(self):
        centroids = self.run_centroids()
        outdir = os.path.split(os.path.split(self.filename_list[0])[0])[0]
        save_json(os.path.join(outdir, "centroid_lga.json"), centroids)
        print("The json file is generated in the directory: ", outdir)

def load_data(lstpath):
    img = nib.load(lstpath)
    data = img.get_data()
    return data

if __name__ == '__main__':
    from glob import glob
    test_mse = ['mse3727', 'mse4413', 'mse4482', 'mse4739', 'mse4754']
    for mse in test_mse:
        np.array(0.05, 1.0, 20)
        f = sorted(glob('/data/henry7/PBR/subjects/{0}/lst/lga/ms*/_kappa_*/ples_lga_*_rmms*.nii'.format(mse)))
        lst_edit = glob('/data/henry7/PBR/subjects/{0}/mindcontrol/ms*/lst/lst_edits/no_FP_filled_FN*'.format(mse))
        if len(lst_edit) > 1:
            raise ValueError("More than one lst_edits files, please check")
        elif len(lst_edit) == 0:
            raise ValueError("No lst_edits file is found, please check your folder")
        elif len(lst_edit) == 1:
            lst_edit = ''.join(lst_edit)
        print(lst_edit)
        data = load_data(lst_edit)
        print(np.max(data), np.min(data))
        Lesion = GetCenterLesion()
        lesions = Lesion.run_centroids()


        """
        Lesion = GetCenterLesion(f)
        lesions = Lesion.run_centroids()
        # A lot 2nd level centroid in mse4482 and mse4754
        # No lesion for mse3327 since kappa is 1.0
        # No lesion for mse4439 since kappa is 0.8
        """
