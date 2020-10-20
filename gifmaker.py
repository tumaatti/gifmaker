#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(
    description='Simple way to generate .gif-files from videofiles'
)
parser.add_argument('input', metavar='I', type=str, help='specify input file')
parser.add_argument('output', metavar='O', type=str, help='specify output file')
parser.add_argument(
    'start_time',
    metavar='S',
    type=str,
    help='specify start time of the gif in input file in format 12:33'
)
parser.add_argument(
    'duration',
    metavar='D',
    type=str,
    help='give the duration of the clip'
)

args = parser.parse_args()

palette = '/tmp/palette.png'

filters = 'fps=25,scale=1280:720:flags=lanczos'

os.system(
    f"ffmpeg -v warning -ss {args.start_time} -t {args.duration} -i "
    f"{args.input} -vf '{filters},palettegen' -y {palette}"
)
os.system(
    f"ffmpeg -v warning -ss {args.start_time} -t {args.duration} -i "
    f"{args.input} -i {palette} -lavfi '{filters} [x]; [x][1:v] paletteuse'"
    f"-y {args.output}"
)
