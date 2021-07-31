import os
import pandas as pd
import subprocess
from utils import safe_filename

def get_ipfs_hash(file_path):
  # requires that script caller has IPFS installed
  result = subprocess.run(['ipfs', 'add', file_path, '--only-hash', '-q'], stdout=subprocess.PIPE)
  return result.stdout.decode('utf-8').strip()

def write_ipfs_table(tsv_df, out_dir):
  print("writing archive ipfs_hashes.zip")

  row_list = []
  for tsv_index, tsv_row in tsv_df.iterrows():
    file_path = os.path.join(out_dir, "{}.zip".format(safe_filename(tsv_row["name"])))
    ipfs_hash = get_ipfs_hash(file_path)

    row = {
      "name": tsv_row["name"],
      "filename": os.path.basename(file_path),
      "ipfs_hash": ipfs_hash,
    }

    row_list.append(row)
  
  # write TSV
  ipfs_df = pd.DataFrame(row_list)
  ipfs_table_path = os.path.join(out_dir, "ipfs_hashes.tsv")
  ipfs_df.to_csv(ipfs_table_path, sep='\t', index=False)

  generate_ipfs_script(ipfs_df, out_dir)

def generate_ipfs_script(ipfs_df, out_dir):
  with open(os.path.join(out_dir, "ipfs_add.sh"), 'w') as f:
    f.write("#!/usr/bin/env bash\n\n")
    for index, row in ipfs_df.iterrows():
      line = "ipfs add {} --pin=true\n".format(row["filename"])
      f.write(line)
