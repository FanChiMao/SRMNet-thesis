# Datasets  
More details of datasets could be found in __**section 4.1**__ of my thesis.

## Deblur  
- GoPro (train & test):  
  - Training set: [GoPro train](https://drive.google.com/drive/folders/1AsgIP9_X0bg0olu2-1N6karm2x15cJWE)  
  - Validation & Testing set: [GoPro test](https://drive.google.com/drive/folders/1a2qKfXWpNuTGOm2-Jex8kfNSzYJLbqkf)  
- HIDE(test):  
  - Testing set: [HIDE test](https://drive.google.com/drive/folders/1nRsTXj4iTUkTvBhTcGg8cySK8nd3vlhK)  

## Dehaze  
- NH-haze (train):  
  - Training set: [NH-haze](https://data.vision.ee.ethz.ch/cvl/ntire20/nh-haze/)  
- D-haze (test):  
  - Validation & Testing set: [D-haze](https://data.vision.ee.ethz.ch/cvl/ntire19//dense-haze/)  

## Denoise (gaussian)  
- DIV2K (train):  
  - Training & Validation set: [DIV2K train val](https://data.vision.ee.ethz.ch/cvl/DIV2K/)  
- CBSD68 (test):
  - Testing set: [CBSD68](https://github.com/clausmichele/CBSD68-dataset/tree/master/CBSD68/original)  
- Kodak24 (test)
  - Testing set: [Kodak24](http://r0k.us/graphics/kodak/)  
- Set5 (test):
  - Testing set: [Set5](https://www.kaggle.com/ll01dm/set-5-14-super-resolution-dataset)  

## Denoise (realworld)  
- SIDD small (train & test):
  - Training & Validation set: [SIDD train benchmark](https://www.eecs.yorku.ca/~kamel/sidd/dataset.php)
  - Testing set: [SIDD benchmark](https://www.eecs.yorku.ca/~kamel/sidd/dataset.php)  
- DND (test):
  - Testing set: [DND](https://noise.visinf.tu-darmstadt.de/)  
    
## Deraindrop
- DeRainDrop (train & test): 
  - Training & Validation set: [Deraindrop train test](https://drive.google.com/open?id=1e7R76s6vwUJxILOcAsthgDLPSnOrQ49K)  
  - Testing set: [Deraindrop testA testB](https://drive.google.com/open?id=1e7R76s6vwUJxILOcAsthgDLPSnOrQ49K)  
    
## Derainstreak  
- Rain13k (train):  
  - Training set: [Rain13k](https://drive.google.com/drive/folders/1Hnnlc5kI0v9_BtfMytC2LR5VpLAFZtVe?usp=sharing)  
- Test2800 (validation & test):  
  - Testing set: [Test2800](https://drive.google.com/drive/folders/1PDWggNh8ylevFmrjo-JEvlmqsDlWWvZs)  
- Rain100H (test):
  - Testing set: [Rain100H](https://drive.google.com/drive/folders/1PDWggNh8ylevFmrjo-JEvlmqsDlWWvZs)  
- Rain100L (test):
  - Testing set: [Rain100L](https://drive.google.com/drive/folders/1PDWggNh8ylevFmrjo-JEvlmqsDlWWvZs)  
- Test100 (test):
  - Testing set: [Test100](https://drive.google.com/drive/folders/1PDWggNh8ylevFmrjo-JEvlmqsDlWWvZs)  

## LLEnhancement  
- LOL (train & test):  
  - Training & Validation set: [LOL train eval](https://daooshee.github.io/BMVC2018website/)  
  - Testing set: [LOL eval](https://daooshee.github.io/BMVC2018website/)

## Retouching
- MIT-5K (train & test):  
  - Training & Validation set: [MIT-5K](https://drive.google.com/drive/folders/1Jv0_9CnYxh_2ReFaVrwG19O3F7xBtdZT?usp=sharing)  
  - Testing set: [MIT-5K](https://drive.google.com/drive/folders/1Jv0_9CnYxh_2ReFaVrwG19O3F7xBtdZT?usp=sharing)

## Preprocess  
Crop the patches by [**generate_patches.py**](https://github.com/FanChiMao/SRMNet-thesis/blob/main/generate_patches.py) for each dataset according to the following table.  
<img src = "https://i.imgur.com/b93EgXf.png" width="800">  
<img src = "https://i.imgur.com/b93EgXf.png" width="800">  

## Tree  
After downloading datasets from above links and finishing the preprocess. Your directory structure should look like this  

<details>  
<summary>Training tree...</summary>   
  
  ```
  datasets  # datasets root
    ├── train                    # training data root (have training and validation set)  
          ├── DIV2K              # Denoising training dataset
          |    ├── test          # validation set
          |    |    ├── input    # noise images set
          |    |    └── target   # gt images set 
          |    └── train         # training set
          |         ├── input    # noise images set
          |         └── target   # gt images set 
          |
          ├── FiveK              # Retouching training dataset
          |    ├── test
          |    |    ├── input
          |    |    └── target
          |    └── train
          |         ├── input
          |         └── target
          |  
          ├── GoPro              # Deblurring training dataset
          |    ├── test
          |    |    ├── input
          |    |    └── target
          |    └── train
          |         ├── input
          |         └── target
          |  
          ├── LOL                # LLEnhancement training dataset
          |    ├── test
          |    |    ├── input
          |    |    └── target
          |    └── train
          |         ├── input
          |         └── target
          |    
          ├── NH-Haze            # Dehaze training dataset
          |    ├── test
          |    |    ├── input
          |    |    └── target
          |    └── train
          |         ├── input
          |         └── target
          |    
          ├── Rain13k            # Derainstreak training dataset
          |    ├── test
          |    |    ├── input
          |    |    └── target
          |    └── train
          |         ├── input
          |         └── target
          |      
          ├── Raindrop           # Deraindrop training dataset
          |    ├── test
          |    |    ├── input
          |    |    └── target
          |    └── train
          |         ├── input
          |         └── target
          |      
          └── SIDD               # Denoising training dataset
               ├── test
               |    ├── input
               |    └── target
               └── train
                    ├── input
                    └── target
                   
  ```  
  
</details>  
