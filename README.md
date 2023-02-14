# Informal Business Detection for CSC 480

## Summary
- Computer Vision solution for AWS DxHub on behalf of the World Bank's effort to identify informal businesses
- This is a project using Google Street View Static API to categorize informal businesses for the World Bank. We used Custom labels for Rekognition to create our classification model which is not available here. 

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

