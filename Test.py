import numpy as np
import nibabel as nib
import itertools


def resize_data(data):
    initial_size_x = data.shape[0]
    initial_size_y = data.shape[1]
    initial_size_z = data.shape[2]

    new_size_x = 176
    new_size_y = 256
    new_size_z = 256

    delta_x = initial_size_x / new_size_x
    delta_y = initial_size_y / new_size_y
    delta_z = initial_size_z / new_size_z

    new_data = np.zeros((new_size_x, new_size_y, new_size_z))

    for x, y, z in itertools.product(range(new_size_x),
                                     range(new_size_y),
                                     range(new_size_z)):
        new_data[x][y][z] = data[int(x * delta_x)][int(y * delta_y)][int(z * delta_z)]

    return new_data


data = nib.load("/home/dthomas/AD/3T_extracted_ad/sub-OAS30212_ses-d3043_T1wBrainExtractionBrain.nii.gz").get_fdata()

resized_data = resize_data(data)
print(resized_data.shape)
img = nib.Nifti1Image(resized_data, np.eye(4))
img.to_filename("asdf.nii.gz")
