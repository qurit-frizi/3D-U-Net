# 3D U-Net 
This code was used to compare the 2D detection based approach and 3D U-Net segmentation approach for lymphoma lesion segmentation in Primary mediastinal large B-cell lymphoma and Diffuse large B-cell lymphoma cases. 
## The related paper:
> A cascaded deep network for automated tumor detection and segmentation in clinical PET imaging of diffuse large B-cell lymphoma (https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12032/120323M/A-cascaded-deep-network-for-automated-tumor-detection-and-segmentation/10.1117/12.2612684.short?SSO=1).

## Implementation
A PyTorch implementation of 3D U-Net borrowed from the original code: (https://github.com/iantsen/hecktor)

### Main Requirements
- PyTorch 1.6.0 (cuda 10.2)
- SimpleITK 1.2.4 (ITK 4.13)
- nibabel 3.1.1
- skimage 0.17.2

#### Runing the model 
Training
```sh
python train.py -p config/model_train.yaml
```
Test
```sh
python predict.py -p config/model_predict.yaml
```
