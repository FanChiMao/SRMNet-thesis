# [NCHU thesis] <br />Image Restoration by Selective Residual Block on Improved Hierarchical Encoder-Decoder Networks  
<!-- 利用可選擇性殘差塊在改良式階層編解碼器網路實現影像修復 -->
## Chi-Mao Fan(student)、Tsung-Jung Liu(adviser)  
[![pdf](https://img.shields.io/badge/PDF-Paper-brightgreen)]() 
[![slides](https://img.shields.io/badge/Presentation-Slides-B762C1)](https://docs.google.com/presentation/d/1ZnCirRdhdY5rOoH_mKf1XFmlHRZtCktZ/edit?usp=sharing&ouid=108348190349543369603&rtpof=true&sd=true) 
[![web](https://img.shields.io/badge/Website-Project-orange)](https://tentativegithub.github.io/) 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Ce9NtVfnP9XvjzOrFeMIMo5yegb2Vc-a?usp=sharing) 
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/52Hz/SRMNet_thesis)  

## 🎉 This thesis earn the Taipei Section 2022 Best Dissertation Award  
<details>  
<summary>Certificate (Click to expand)</summary>  
  <img src = "https://i.imgur.com/OC2jL5H.jpg" alt="1" width="300">
  <img src = "https://i.imgur.com/26eMbci.jpg" alt="2" width="300">
</details>

The pdf file of thesis will publish after 3 years (2025)  
<!--范植貿(研究生)、劉宗榮(指導教授)  -->

> Abstract : Image Restoration is a compute vision task which restoring from the degraded images to clean images. With the rapid development of both hardware and software equipment, convolution neural network (CNN) which needs higher equipment requirements gradually replaces the traditional algorithm-based restoration methods, and shine in each domain of compute vision and achieve the impressive performance. However, with the rapid development of hardware equipment, the trend of convolution neural network gradually becomes a clammy situation which stacking huge complex network structures to achieve excellent performances, while ignoring the efficiency of model. In this paper, we based on light hierarchical network architecture: U-Net, and improve from Residual Dense Block (RDB) which is good at image restoration tasks but memory-consuming to an efficient block called Selective Residual Block (SRB). We also improve the hierarchical network structure U-Net by adding the gatepost feature paths which enrich more spatial feature information comparing with the traditional U-Net and have the synergy with SRB. Besides this, we also proposed a loss function which is based on two important metrics in image restoration: peak signal-to-noise (PSNR) and structural similarity index to optimize our model. Finally, proposed network could handle the several restoration tasks such as denoising, deblurring, deraining, dehazing and low-light image enhancement. Furthermore, the performances are good in terms of quantitative metrics and visual quality.
<!--影像修復是一種從劣化圖像，修復成乾淨圖像的一種電腦視覺任務，常見的圖像劣化種類包括: 雜訊、模糊、雨、霧和低光源等等。 隨著電腦軟硬體設備的快速發展，需要較高硬體設備需求的卷積神經網路(CNN)逐漸取代傳統以演算法為基礎的影像修復方法，並在電腦視覺中的各個領域都大放異彩，並到達了令人印象深刻的效果。 但因為硬體設備的快速發展，深度卷積神經網路的發展趨勢逐漸成為堆疊龐大的複雜網路或模塊架構，來達到卓越的效果而忽視網路效率的病態情況。 所以在這篇論文當中，我們將基於輕量型的階層式網路架構: U-Net為基底，並改良自影像修復任務中效果很好，但需消耗較大記憶體容量的殘差密集塊(RDB)，成為一種效率更高、且不會占據過多顯存的模塊稱為選擇性殘差塊(SRB)。 我們還改良了階層式網路架構U-Net，增加了門柱特徵路徑，稱為M-Net+。 我們提出的M-Net+相較於傳統U-Net，可以獲取更豐富的空間特徵資訊，並與SRB作結合達到相輔相成的效果。 除此之外，我們還提出了基於影像修復中相當重要的兩個評估指標: 峰值訊雜比(PSNR)與結構相似性(SSIM)的損失函數來優化我們網路模型。 最終我們提出的網路架構適用於影像修復中的去噪、去模糊、去雨、去霧與低光源的影像增強，並在定量指標與視覺質量上取得了非常不錯的成績。 -->

## Network Architecture  

<table>
  <tr>
    <td colspan="2"><img src = "https://i.imgur.com/ASazV7H.png" alt="SRMNet" width="800"> </td>  
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
conda install -c conda-forge tensorboardx
pip install -r requirements.txt
```

## Quick run  
You can directly test your own images on my spcae of [**HuggingFace**](https://huggingface.co/spaces/52Hz/SRMNet_thesis).  
To test the pre-trained models of SRMNet on your own images, make sure you have downloaded the pre-trained models and place to `./pretrained_model/`.  
After [downloading](pretrained_model/download_models.py) the models, see [**`quick_demo.py`**](quick_demo.py) and run  
```
python quick_demo.py --input_dir sample_images --result_dir sample_results --weights_root pretrained_model --gpu True --task [restoration tasks]
```
**All pre-trained models can be downloaded at [pretrained_model/README.md](pretrained_model/README.md) or [here](https://github.com/FanChiMao/SRMNet-thesis/releases/tag/v0.0).**  

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
```
python train.py
```  

## Test  
To test (evaluate) the quantitative scores of different tasks, see [**`evaluation_code`**](evaluation_code).  

## Results  
We achieved competitive performance on image denoising (gaussian & real-world), image deblurring, image deraining (rainstreak & raindrop), image dehazing and low-light image enhancement. Detailed results can be found in **section 4.3** of my thesis.  

<details>  
<summary><strong>Denoise (gaussian noise) </strong>(click me) </summary>  
<img src = "https://i.imgur.com/y370l6G.png" width="600">  
<img src = "https://i.imgur.com/FQZzaU6.png" width="600">  
</details>  
<details>  
<summary><strong>Denoise (real-world noise)</strong></summary>  
<img src = "https://i.imgur.com/NxBRuqS.png" width="600">  
</details>  
<details>  
<summary><strong>Deblur (motion blur)</strong></summary>  
<img src = "https://i.imgur.com/17DCXMD.png" width="600">  
</details>  
<details>  
<summary><strong>Derain (rain streak)</strong></summary>  
<img src = "https://i.imgur.com/EtYEt6X.png" width="600">  
<img src = "https://i.imgur.com/XIN4Xki.png" width="600">  
</details>  
<details>  
<summary><strong>Derain (raindrop)</strong></summary>  
<img src = "https://i.imgur.com/W2VDfYb.png" width="600">  
</details>  
<details>  
<summary><strong>Dehaze (dense haze)</strong></summary>  
<img src = "https://i.imgur.com/iVNjdjA.png" width="600">  
</details>  
<details>  
<summary><strong>Enhancement (low-light)</strong></summary>  
<img src = "https://i.imgur.com/SnZxW6g.png" width="600">  
</details>  

## Visual Performance  
We achieved competitive performance on image denoising (gaussian & real-world), image deblurring, image deraining (rainstreak & raindrop), image dehazing, low-light image enhancement and image retouching. The following figures are some visual performances for different tasks. More detailed results can also be found in **section 4.3** of my thesis or directly see in the [**interactive website**](https://tentativegithub.github.io/).  

<details>  
<summary><strong>Denoise (gaussian noise) </strong>(click me) </summary>  
<img src = "https://i.imgur.com/nA2XNCA.png">  
<img src = "https://i.imgur.com/VqaMIna.png">  
</details>  
<details>  
<summary><strong>Denoise (real-world noise)</strong></summary>  
<img src = "https://i.imgur.com/EjR675Q.png">  
<img src = "https://i.imgur.com/DDFSnWZ.png">  
</details>  
<details>  
<summary><strong>Deblur (motion blur)</strong></summary>  
<img src = "https://i.imgur.com/qvLDFXV.png">  
<img src = "https://i.imgur.com/NjDZ874.png">  
</details>  
<details>  
<summary><strong>Derain (rain streak)</strong></summary>  
<img src = "https://i.imgur.com/7vSmWKY.png">  
<img src = "https://i.imgur.com/EUc7H4B.png">  
</details>  
<details>  
<summary><strong>Derain (raindrop)</strong></summary>  
<img src = "https://i.imgur.com/fiOG2OH.png">  
<img src = "https://i.imgur.com/PVJM2BX.png">  
</details>  
<details>  
<summary><strong>Dehaze (dense haze)</strong></summary>  
<img src = "https://i.imgur.com/l7cXfPO.png">  
</details>  
<details>  
<summary><strong>Enhancement (low-light)</strong></summary>  
<img src = "https://i.imgur.com/wc93L6t.png">  
</details>  
<details>  
<summary><strong>Retouching</strong></summary>  
<img src = "https://i.imgur.com/9zhMqB6.png">  
<img src = "https://i.imgur.com/XyUeIE2.png">  
</details>  

## Contact  
If you have any question, feel free to contact qaz5517359@gmail.com.  
