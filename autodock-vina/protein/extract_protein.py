#!/usr/bin/env python

"""
Extracts only the protein (HETATM) and chain terminator (TER)
values from a PDB file.

date: 2022-07-01
author: Matthew Feng
"""

import argparse

def main(in_pdb, out_pdb):
    with open(in_pdb) as f, open(out_pdb, "w") as out:
        for line in f:
            row = line.strip().split()
            if row[0] == "ATOM":
                out.write(line)
            elif row[0] == "TER":
                out.write("TER\n")
        out.write("END")
    print(f"[i] `{out_pdb}` successfully created.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("in_pdb_file")
    parser.add_argument("out_pdb_file")

    args = parser.parse_args()
    main(args.in_pdb_file, args.out_pdb_file)
