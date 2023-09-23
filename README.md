# Data Extraction
- From PDF
- From Images
- From Web

## Getting started
GFG Guide: https://www.geeksforgeeks.org/convert-pdf-to-image-using-python.

Open this project root in Powershell and run
```
python -m venv env
.\env\Scripts\Activate.ps1
```

### Install dependecies
#### PDF2Image
```
pip install pdf2image
```

#### Poppler
PDF2Image requires you have poppler downloaded.

Direct download link: https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip

You will need to add the `bin/` directory i.e. `poppler-23.08.0/Library/bin/` to your PATH.

### Run
```
python convert_to_image.py [list of PDF file paths]
```