import wget
from tqdm import tqdm

def main():
    print('It will cost about 8-10 minutes to download...')
    with tqdm(total=8) as bar:
        wget.download('https://github.com/FanChiMao/SRMNet-thesis/releases/download/v0.0/Deblurring_motionblur.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-thesis/releases/download/v0.0/Dehaze_realworld.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-thesis/releases/download/v0.0/Denoise_gaussian.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-thesis/releases/download/v0.0/Denoise_realworld.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-thesis/releases/download/v0.0/Deraining_raindrop.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-thesis/releases/download/v0.0/Deraining_rainstreak.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-thesis/releases/download/v0.0/LLEnhancement.pth')
        bar.update(1)
        wget.download('https://github.com/FanChiMao/SRMNet-thesis/releases/download/v0.0/Retouching.pth')
        bar.update(1)


if __name__ == '__main__':
    print('Start downloading pretrained models from https://github.com/FanChiMao/SRMNet-thesis/releases/tag/v0.0')
    main()
    print('Done !!')
