# 利用可選擇性殘差塊在改良式階層編解碼器網路實現影像修復<br>Image Restoration by Selective Residual Block on Improved Hierarchical Encoder-Decoder Networks  
范植貿(研究生)、劉宗榮(指導教授)  

<!-- 這句看不見，一句話的註解 -->
***
> 摘要 : 影像修復是一種從劣化圖像，修復成乾淨圖像的一種電腦視覺任務，常見的圖像劣化種類包括: 雜訊、模糊、雨、霧和低光源等等。 隨著電腦軟硬體設備的快速發展，需要較高硬體設備需求的卷積神經網路(CNN)逐漸取代傳統以演算法為基礎的影像修復方法，並在電腦視覺中的各個領域都大放異彩，並到達了令人印象深刻的效果。 但因為硬體設備的快速發展，深度卷積神經網路的發展趨勢逐漸成為堆疊龐大的複雜網路或模塊架構，來達到卓越的效果而忽視網路效率的病態情況。 所以在這篇論文當中，我們將基於輕量型的階層式網路架構: U-Net為基底，並改良自影像修復任務中效果很好，但需消耗較大記憶體容量的殘差密集塊(RDB)，成為一種效率更高、且不會占據過多顯存的模塊稱為選擇性殘差塊(SRB)。 我們還改良了階層式網路架構U-Net，增加了門柱特徵路徑，稱為M-Net+。 我們提出的M-Net+相較於傳統U-Net，可以獲取更豐富的空間特徵資訊，並與SRB作結合達到相輔相成的效果。 除此之外，我們還提出了基於影像修復中相當重要的兩個評估指標: 峰值訊雜比(PSNR)與結構相似性(SSIM)的損失函數來優化我們網路模型。 最終我們提出的網路架構適用於影像修復中的去噪、去模糊、去雨、去霧與低光源的影像增強，並在定量指標與視覺質量上取得了非常不錯的成績。

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


## Prepare datasets  

## Pretrained models  

## Train  

## Test  

## Results  


