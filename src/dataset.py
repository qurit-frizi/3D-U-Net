import numpy as np
import nibabel as nib
from torch.utils.data import Dataset


class PETCTDataset(Dataset):
    

    def __init__(self, paths_to_samples, transforms=None, mode='train'):
        self.paths_to_samples = paths_to_samples
        self.transforms = transforms
        if mode not in ['train', 'test']:
            raise ValueError(f"Argument 'mode' must be 'train' or 'test'. Received {mode}")
        self.mode = mode
        if mode == 'train':
            print(len(paths_to_samples[0]))
            self.num_of_seqs = len(paths_to_samples[0]) - 1
        else:
            self.num_of_seqs = len(paths_to_samples[0])

    def __len__(self):
        return len(self.paths_to_samples)

    def __getitem__(self, index):
        sample = dict()

        id_ = self.paths_to_samples[index][0].parent.stem
        sample['id'] = id_

        img = [self.read_data(self.paths_to_samples[index][i]) for i in range(self.num_of_seqs)]
        img = np.stack(img, axis=-1)
        sample['input'] = img
         
        if self.mode == 'train':
            mask = self.read_data(self.paths_to_samples[index][-1])
            mask = np.expand_dims(mask, axis=3)

            assert img.shape[:-1] == mask.shape[:-1], \
                f"Shape mismatch for the image with the shape {img.shape} and the mask with the shape {mask.shape}."

            sample['target'] = mask

        else:
            sample['affine'] = self.read_data(self.paths_to_samples[index][0], False).affine
        if self.transforms:
            sample = self.transforms(sample)

        return sample

    @staticmethod
    def read_data(path_to_nifti, return_numpy=True):
        """Read a NIfTI image. Return a numpy array (default) or `nibabel.nifti1.Nifti1Image` object"""
        if return_numpy:
            return nib.load(str(path_to_nifti)).get_fdata()
        return nib.load(str(path_to_nifti))
