#!/usr/bin/env python3

"""
Extracts only the ligand values from a PDB file.

date: 2022-07-01
author: Matthew Feng
"""

import argparse

def main(in_pdb, ligand, out_pdb):
    with open(in_pdb) as f, open(out_pdb, "w") as out:
        for line in f:
            row = line.strip().split()
            if ligand in row:
                out.write(line)
        out.write("END")
    print(f"[i] `{out_pdb}` successfully created.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("in_pdb_file")
    parser.add_argument("ligand")
    parser.add_argument("out_pdb_file")

    args = parser.parse_args()
    main(args.in_pdb_file, args.ligand, args.out_pdb_file)
