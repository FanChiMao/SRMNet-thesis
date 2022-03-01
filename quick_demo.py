import torch
import torchvision.transforms.functional as TF
import torch.nn.functional as F
from PIL import Image
import os
from skimage import img_as_ubyte
from tqdm import tqdm
from natsort import natsorted
from glob import glob
from utils.image_utils import save_img
from utils.model_utils import load_checkpoint
import argparse
from model_arch.SRMNet_SWFF import SRMNet_SWFF
from model_arch.SRMNet import SRMNet

tasks = ['Deblurring_motionblur',
         'Dehaze_realworld',
         'Denoising_gaussian',
         'Denoising_realworld',
         'Deraining_raindrop',
         'Deraining_rainstreak',
         'LLEnhancement',
         'Retouching']

def main():
    parser = argparse.ArgumentParser(description='Quick demo Image Restoration')
    parser.add_argument('--input_dir', default='sample_images', type=str, help='Input images root')
    parser.add_argument('--result_dir', default='sample_results', type=str, help='Results images root')
    parser.add_argument('--weights_root', default='pretrained_model', type=str, help='Weights root')
    parser.add_argument('--gpu', default=True, type=bool, help='Using GPU')
    parser.add_argument('--task', default='Retouching', type=str, help='Restoration task (Above task list)')

    args = parser.parse_args()

    # Prepare testing data
    inp_dir = os.path.join(args.input_dir, args.task)
    files = natsorted(glob(os.path.join(inp_dir, '*.JPG')) + glob(os.path.join(inp_dir, '*.PNG')))
    if len(files) == 0:
        raise Exception("\nNo images in {} \nPlease enter the following tasks: \n\n{}".format(inp_dir, '\n'.join(tasks)))

    out_dir = os.path.join(args.result_dir, args.task)
    os.makedirs(out_dir, exist_ok=True)

    # Build model
    model = define_model(args)
    model.eval()
    if args.gpu:
        model.cuda()

    print('restoring images......')

    mul = 16

    for i, file_ in enumerate(tqdm(files)):
        img = Image.open(file_).convert('RGB')
        input_ = TF.to_tensor(img).unsqueeze(0).cuda()

        # Pad the input if not_multiple_of 8
        h, w = input_.shape[2], input_.shape[3]
        H, W = ((h + mul) // mul) * mul, ((w + mul) // mul) * mul
        padh = H - h if h % mul != 0 else 0
        padw = W - w if w % mul != 0 else 0
        input_ = F.pad(input_, (0, padw, 0, padh), 'reflect')
        with torch.no_grad():
            restored = model(input_)

        restored = torch.clamp(restored, 0, 1)
        restored = restored[:, :, :h, :w]
        restored = restored.permute(0, 2, 3, 1).cpu().detach().numpy()
        restored = img_as_ubyte(restored[0])

        f = os.path.splitext(os.path.split(file_)[-1])[0]
        save_img((os.path.join(out_dir, f + '.png')), restored)

    print(f"Files saved at {out_dir}")
    print('finish !')


def define_model(args):
    # Enhance models
    if args.task in ['LLEnhancement', 'Retouching']:
        model = SRMNet(in_chn=3, wf=96, depth=4)
        weight_path = os.path.join(args.weights_root, args.task + '.pth')
        load_checkpoint(model, weight_path)

    # Restored models
    else:
        model = SRMNet_SWFF(in_chn=3, wf=96, depth=4)
        weight_path = os.path.join(args.weights_root, args.task + '.pth')
        load_checkpoint(model, weight_path)

    return model


if __name__ == '__main__':
    main()
