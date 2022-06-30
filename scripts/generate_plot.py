#!/usr/bin/env python

"""
Generate a interface_delta_X vs. ligand_rms_no_super_X plot for all docked structures.
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt

def main(score_csv, xlabel, ylabel, scatter_label, out_file):
    df = pd.read_csv(score_csv)

    plt.figure(figsize=(36, 24), dpi=600)

    score = df[xlabel]

    if ":" in scatter_label:
        scatter_label, crop_start, crop_end = scatter_label.split(":")
        crop_start = None if crop_start == "None" else int(crop_start)
        crop_end = None if crop_end == "None" else int(crop_end)
        
        crop = lambda x: x[crop_start:crop_end]
    else:
        crop = lambda x: x

    labels = list(map(crop, df[scatter_label]))
    rms_to_native = df[ylabel]

    plt.scatter(score, rms_to_native)
    for i, label in enumerate(labels):
        plt.text(score[i], rms_to_native[i], label, fontsize=4.0, horizontalalignment="center", verticalalignment="center")
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(out_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("score_csv")
    parser.add_argument("xlabel")
    parser.add_argument("ylabel")
    parser.add_argument("scatter_label")
    parser.add_argument("out_file")

    args = parser.parse_args()

    main(args.score_csv, args.xlabel, args.ylabel, args.scatter_label, args.out_file)