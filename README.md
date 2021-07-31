# Card Tool

Tooling for creating Occulta Novellia collectible tokens. Given the correct resources as a TSV file, the card tool will:
- Generate a folder of archives, each of which contains the token metadata data to be stored in IPFS
- A script to add and pin the archives onto IPFS
- A TSV containing the metadata to use with `cardano-node`

Run like
- `python3 ./src/card_tool.py cards.csv`

This will direct the output archives to `./output`.

This tool is only used to generate the character JSON files.

## Details JSON

The `details.json` has the following format:

```
{
  "name": "Draculi",
  "assets": {
    "card": ["card.png"],
    "artwork": ["artwork.png"]
  },
  "card": {
    "number": 1,
    "release_set": "Presale 1",
    "location": "Garden of Residues"
  },
  "progression": {
    "class": "Draculi",
    "stage": 1
  },
  "stats": {
    "slots": 1,
    "health": 10,
    "attack": 3,
    "move": 6
  },
  "attributes": ["Creature", "Snake", "Bite", "Agile", "Swim"],
  "Description": "Draculi hunt in packs, often taking down the enourmous Arinspore despite their small size. Without the presence of an Alpha Draculi, their attacks are often disordered."
}
```

**If `stage` > 1, `slots` will be ignored and should be omitted for clarity.**
**There is a hard limit of 400 characters on the `description` or the card engine will consider the card invalid. This should match the text on the `card.png`.**

Text will be displayed how it is written into the JSON file. Use capitalization where it makes sense.
