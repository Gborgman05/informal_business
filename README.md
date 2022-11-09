# Informal Business Detection for CSC 480

## Usage

### Get Images
- download google_streetview python module via below or similar
``` 
python3 -m pip install google_streetview
```
- generate google cloud platform developer key [here](https://cloud.google.com/docs/authentication/api-keys)
- adjust coordinates and intervals on line 30
- run pull_img.py
```
python3 pull_img.py
```

### remove rows from a manifest file

- get file path for your current file
- find a unique identifier for the rows you want to replace
- find the number of rows you want to remove
```
python3 rm_data.py
```

## TODO
