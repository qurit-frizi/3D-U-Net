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

### Note 
This code does not need the input size of 144x144x144!!

In the following of the code, [144, 144, 144] is the OUTPUT shape that is hard coded in the “predict.py” code and it is not for training.
https://github.com/qurit-frizi/3D-U-Net/blob/8fcd6e1a1b73585f0416236926aa23e90c74e2fd/model/predict.py#L47

If you want, you can either change the needed output shape or put it as an input in the prediction config file (model_predict.yaml) for instance: https://github.com/qurit-frizi/3D-U-Net/blob/122bb35ea7868bf40de194e93db855f5b2fc592e/config/model_predict.yaml#L21

So, for the input Can be of any size as long as its dimensions are multiple of 16’s. So if you have input data with any dimension you just need to pad it to be a multiple of 16’s. For example, for the input size of 192X192X263, you only need to pad its z dimension to be in the size of 192X192X272.
