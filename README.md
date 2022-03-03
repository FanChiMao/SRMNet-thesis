# Image Restoration by Selective Residual Block on Improved Hierarchical Encoder-Decoder Networks  
<!-- 利用可選擇性殘差塊在改良式階層編解碼器網路實現影像修復 -->
范植貿(研究生)、劉宗榮(指導教授)  

***  
> Abstract : Image Restoration is a compute vision task which restoring from the degraded images to clean images. With the rapid development of both hardware and software equipment, convolution neural network (CNN) which needs higher equipment requirements gradually replaces the traditional algorithm-based restoration methods, and shine in each domain of compute vision and achieve the impressive performance. However, with the rapid development of hardware equipment, the trend of convolution neural network gradually becomes a clammy situation which stacking huge complex network structures to achieve excellent performances, while ignoring the efficiency of model. In this paper, we based on light hierarchical network architecture: U-Net, and improve from Residual Dense Block (RDB) which is good at image restoration tasks but memory-consuming to an efficient block called Selective Residual Block (SRB). We also improve the hierarchical network structure U-Net by adding the gatepost feature paths which enrich more spatial feature information comparing with the traditional U-Net and have the synergy with SRB. Besides this, we also proposed a loss function which is based on two important metrics in image restoration: peak signal-to-noise (PSNR) and structural similarity index to optimize our model. Finally, proposed network could handle the several restoration tasks such as denoising, deblurring, deraining, dehazing and low-light image enhancement. Furthermore, the performances are good in terms of quantitative metrics and visual quality.


## Network Architecture  

<table>
  <tr>
    <td colspan="2"><img src = "https://i.imgur.com/nftZOUV.png" alt="SRMNet" width="800"> </td>  
  </tr>
  <tr>
    <td colspan="2"><p align="center"><b>Overall Framework of SRMNet</b></p></td>
  </tr>
  
  <tr>
    <td> <img src = "https://i.imgur.com/z6Vds87.png" width="400"> </td>
    <td> <img src = "https://i.imgur.com/eaLejBK.png" width="400"> </td>
  </tr>
  <tr>
    <td><p align="center"><b>Selective Residual Block (SRB)</b></p></td>
    <td><p align="center"> <b>Resizing Block (Pixel Shuffle)</b></p></td>
  </tr>
</table>

## Installation  
The model is built in PyTorch 1.8.0 and tested on Windows10 environment  
(Python: 3.8, CUDA: 10.2, cudnn: 7.6).  

For installing, follow these intructions
```
conda create -n pytorch python=3.8  
conda activate pytorch  
conda install pytorch=1.8 torchvision cudatoolkit=10.2 -c pytorch  
```

## Prepare datasets  
The preparation of dataset in more detail, see [**datasets/README.md**](datasets/README.md).  
In our experiments, we crop both training & testing data with the size of `256x256` by the code: [**`generate_patches.py`**](generate_patches.py).  
More details aboult different restoration tasks can be found in **section 4.3** of my thesis.  

## Train  
To train the restoration models of SRMNet. You should check the following components are correct:  
<details>  
<summary>training.yaml (Take low-light image enhancement for example)  </summary>   
  
 ```
  # Training configuration
  GPU: [0,1,2,3]

  VERBOSE: False

  MODEL:
    MODE: 'Enhancement'

  # Optimization arguments.
  OPTIM:
    BATCH: 2
    EPOCHS: 200
    # EPOCH_DECAY: [10]
    LR_INITIAL: 2e-4
    LR_MIN: 1e-5
    # BETA1: 0.9

  TRAINING:
    VAL_AFTER_EVERY: 1
    RESUME: False
    TRAIN_PS: 256
    VAL_PS: 256
    TRAIN_DIR: './datasets/train/LOL/train'       # path to training data
    VAL_DIR: './datasets/train/LOL/test' # path to validation data
    SAVE_DIR: './checkpoints'           # path to save models and images
  ```
</details>  

If the data path and above configuration are all correctly setting, just simply run:  
`python train.py`  

## Pretrained models  
For the pretrained models of different tasks, see [**pretrained_model/README.md**](pretrained_model/README.md).  

## Test  

## Results  


