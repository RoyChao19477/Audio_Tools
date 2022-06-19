import librosa
import glob
import argparse
import numpy as np
import soundfile as sf
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--source_sr', type=int, required=True,  help='Source (input) sample rate')
parser.add_argument('--result_sr', type=int, required=True,  help='Result (output) sample rate')
parser.add_argument('--source_folder', '-i', type=str, required=True,  help='Source (input) folder path')
parser.add_argument('--result_folder', '-o', type=str, required=True,  help='Result (output) folder path')

args = parser.parse_args()

if args.source_folder[-1] == '/':
    args.source_folder = args.source_folder[:-1]
args.source_folder += "/*.wav"

if args.result_folder[-1] != '/':
    args.result_folder += "/"

for audio in tqdm(glob.glob(args.source_folder)):
    y, sr = librosa.load(audio, sr=args.source_sr)
    y_new = librosa.resample(y, orig_sr=sr, target_sr=args.result_sr)

    save_pth = args.result_folder + audio.rsplit('/', 1)[1]

    sf.write(save_pth, y_new, args.result_sr)
