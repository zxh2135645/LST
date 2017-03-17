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
                    print("Oops, this centroid is not located in the lesion shape",
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
                        print("Oops, this centroid is still not in the lesion shape",
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
                            print("Oops, this algorithm did not work.",
                                  "The coordinate is (x, y, z): ", [x_round3, y_round3, z_round3], '\n',
                                  "lesion size is: ", self.len(new_miss_coord2D), "\n",
                                  "The lesion coordinate is: ", new_miss_coord2D,
                                  "\n",
                                  "All three levels of centroids are stored in the json file.")

            if len(centroid['present']) == idx:
                print("Great, all the centroids are in the lesion shape!")

            kappa_name = '_kappa_' + kappa
            self.centroids[kappa_name] = centroid
        return self.centroids

    def make_json(self):
        outdir = os.path.split(os.path.split(self.filename_list[0])[0])[0]
        save_json(os.path.join(outdir, "centroid_lga.json"), self.centroids)

    def check_missing_points(self):
        #print(self.centroids)
        centroids = run_centroids()
        # TODO

        for i, filename in enumerate(self.filename_list):
            kappa = os.path.split(filename)[1].split('_')[2]
            if kappa == '1':
                kappa = kappa + '.0'
            kappa_name = '_kappa_' + kappa

            if len(run_centroids()) == (len(self.lesion_size) - 1):
                print("Great, all the centroids are in the lesion shape for kappa is: ", kappa)
            else:
                raise ValueError("Please try other algorithm to get a valid point of the lesion shape")


if __name__ == '__main__':
    from glob import glob
    f = sorted(glob('/data/henry7/PBR/subjects/mse4413/lst/lga/ms*/_kappa_*/ples_lga_*_rmms*.nii'))
    lesion = GetCenterLesion(f)
    lesions = lesion.run_centroids()