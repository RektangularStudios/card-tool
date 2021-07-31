import os
import zipfile
import json
from utils import bcolors, safe_filename

def get_character_dict(row):
  dict_file = {
    "occulta_novellia_version": 1,
    "copyright": "Copyright Rektangular Studios Inc.; all rights reserved",
    "name": row["product_name"],
    "card": {
      "number": row["card_number"],
      "release_set": row["card_release_set"],
      "rarity": row["card_rarity"],
    },
    "progression": {
      "class": row["progression_class"],
      "stage": row["progression_stage"],
    },
    "stats": {
      "health": row["health"],
      "attack": row["attack"],
      "move": row["move"],
    },
    "attributes": [],
    "description": row["description"],
  }
  
  # slots isn't always set
  if row["slots"]:
    dict_file["stats"]["slots"] = int(row["slots"])

  # build attributes (there can arbitrarily many)
  for attr in ["faction", "type_1", "type_2", "activated_1", "activated_2", "passive_1", "passive_2"]:
    if row[attr]:
      dict_file["attributes"].append(row[attr])

  return dict_file

def write_character(row, out_dir, resource_dir):
  file_prefix = safe_filename(row["product_name"])
  print("writing character {}.json".format(file_prefix))

  dict_file = get_character_dict(row)

  # write details
  details_path = os.path.join(out_dir, "{}.json".format(file_prefix))
  with open(details_path, 'w') as f:
    doc = json.dump(dict_file, f, indent=2)
