#!/usr/bin/python3

import os
import sys
import pandas as pd
import character_utils
import ipfs_utils

script_dir = os.path.dirname(os.path.realpath(__file__))
out_dir = os.path.join(script_dir, "../output")
resource_dir = os.path.join(script_dir, "../resource")

def main(tsv_path):
  print("reading file at {}".format(tsv_path))
  df = pd.read_csv(tsv_path)
  
  # remove NaNs
  df = df.replace(pd.np.nan, '', regex=True)

  for index, row in df.iterrows():
    character_utils.write_character(row, out_dir, resource_dir)

  # TODO: finish deprecating
  #ipfs_utils.write_ipfs_table(df, out_dir)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    raise ValueError("Expected 1 arg: (TSV path for card specification)")

  main(sys.argv[1])
