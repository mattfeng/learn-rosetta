#!/usr/bin/env python

"""
Converts a Rosetta score.sc file to a CSV file.
"""

import argparse
import csv

def get_column_names(line):
    # line should start with "SCORE: "
    cols = line.strip().split()[1:]
    return cols

def main(score_file, out_file):
    with open(score_file) as f, open(out_file, "w") as out:
        writer = csv.writer(out)

        f.readline() # skip first line ("SEQUENCE:")
        cols = get_column_names(f.readline())

        writer.writerow(cols)

        for line in f:
            line = line.strip()
            data = line.split()[1:]
            writer.writerow(data)
    
    print("[i] Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("score_file")
    parser.add_argument("out_file")

    args = parser.parse_args()

    main(args.score_file, args.out_file)