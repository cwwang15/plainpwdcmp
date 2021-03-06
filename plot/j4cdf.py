#!/usr/bin/env python3
"""
Json for CDF Zipf (j4cdf)
"""
import argparse
import json
from typing import TextIO

import numpy
import pandas as pd


def read_data(file: TextIO):
    data = pd.read_csv(file, names=["rank", "freq"])
    raw = list(numpy.array(data[["freq"]]))
    y = [i[0].split('/') for i in raw]
    y = [float(a[0]) / float(a[-1]) for a in y]
    x = [int(i) for i in list(numpy.array(data[['rank']]))]
    return x, y


def wrapper():
    cli = argparse.ArgumentParser("Parse CDF data")
    cli.add_argument("-l", "--label", required=False, dest="label", default=None, type=str,
                     help="how to identify this curve")
    cli.add_argument("-f", "--file", required=False, dest="fd_in", type=argparse.FileType("r"),
                     default=None, help="CDF Zipf result file to be parsed")
    cli.add_argument("-s", "--save", required=True, dest="fd_save", type=str,
                     help="save parsed data here")
    cli.add_argument("--lower", required=False, dest="lower_bound", default=0, type=int,
                     help="guesses less than this will be ignored and will not appear in beautified json file")
    cli.add_argument("--upper", required=False, dest="upper_bound", default=10 ** 18, type=int,
                     help="guesses greater than this will be ignored and will not appear in beautified json file")
    cli.add_argument("-c", "--color", required=False, dest="color", default=None, type=str,
                     help="color of curve, using DEFAULT config if you dont set this flag")
    cli.add_argument("--line-style", required=False, dest="line_style", default="solid", type=str,
                     help="style of line, solid or other")
    cli.add_argument("--marker", required=False, dest="marker", default=None, type=str,
                     choices=["|", "+", "o", ".", ",", "<", ">", "v", "^", "1", "2", "3", "4", "s", "p", "_", "x", "*",
                              "D", 'P', 'h', 'H', 'X'],
                     help="the marker for points of curve, default None")
    cli.add_argument("--marker-size", required=False, dest="marker_size", default=2, type=float,
                     help="marker size")
    cli.add_argument("--mark-every", required=False, dest="mark_every", default=None, type=int, nargs="+",
                     help="show marker every n points")
    cli.add_argument("--line-width", required=False, dest="line_width", default=1.0, type=float,
                     help="width of line, can be float point number")
    cli.add_argument("--show-text", required=False, dest="show_text", action="store_true",
                     help="show text at specified position")
    cli.add_argument("--text-x", required=False, dest="text_x", default=0, type=float,
                     help='x position of text')
    cli.add_argument("--text-y", required=False, dest="text_y", default=0, type=float,
                     help='y position of text')
    cli.add_argument("--text-fontsize", required=False, dest="text_fontsize", default=12, type=int,
                     help='fontsize of text')
    args = cli.parse_args()

    line_style = args.line_style
    if line_style not in {'solid', 'dashed', 'dashdot', 'dotted'}:
        seq = [float(i) for i in line_style.split(" ") if len(i) > 0]
        offset = seq[0]
        onoffseq = seq[1:]
        if len(onoffseq) % 2 != 0:
            raise Exception("onoffseq should have even items!")
        line_style = (offset, tuple(onoffseq))
    x, y = read_data(args.fd_in)
    text_color = args.color if args.color is not None else "black"
    json.dump({
        "label": args.label,
        "total": x[-1],
        "marker": args.marker,
        "marker_size": args.marker_size,
        "mark_every": args.mark_every,
        "color": args.color,
        "line_style": line_style,
        "line_width": args.line_width,
        "x_list": x,
        "y_list": y,
        "text_x": args.text_x,
        "text_y": args.text_y,
        "text_fontsize": args.text_fontsize,
        "text_color": text_color,
        "show_text": args.show_text,
    }, open(args.fd_save, "w"), indent=2)
    pass


if __name__ == '__main__':
    wrapper()
