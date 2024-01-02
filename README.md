# Plotish 

Plotish is a Python module designed to create plots from JSON files, providing a flexible solution for programs generating data visualizations. It various applications can JSON files with data that Plotish interprets and translates into plots using Matplotlib.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)


## Installation

```bash
python3 -m venv .env 
source ./.env/bin/activate
pip install poetry 
poetry install 
```

## Usage 


To use Plotish, run it as a module with the filename of the JSON file you want to plot. An optional second argument can be provided for specifying the output folder.

```bash

python -m plotish filename.json [outfolder]
```

Replace filename.json with the path to your JSON file and [outfolder] with an optional output folder (defaults to 'out').