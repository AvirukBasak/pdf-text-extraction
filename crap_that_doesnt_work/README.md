# Data Extraction
- From PDF
- From Images
- From Web

## Conclusion
Output of this is in [output_image_to_text.md](output_image_to_text.md) (Hindi Test).
Another test output is in [output_image_to_text_eng.md](output_image_to_text_eng.md) (English Test).

Multilingual OCR using Tesseract on Hindi is unreliable and useless.

## Gettig Started
Open this project root in Powershell and run
```
python -m venv env
.\env\Scripts\Activate.ps1
```

## Converting PDFs into Images
GFG Guide: https://www.geeksforgeeks.org/convert-pdf-to-image-using-python

### Install dependecies
#### PDF2Image
```
pip install pdf2image
```

#### Poppler
PDF2Image requires you have poppler downloaded.

Direct download link: https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip

You will need to add the `bin/` directory i.e. `poppler-23.08.0/Library/bin/` to your PATH.

### Run in Powershell
```
python convert_to_image.py '.\pdfs\TXT Mineral Auction Amendment Rules.pdf' '.\pdfs\TXT Mines and Minerals Act.pdf'
```

A new directory called images will appear.

## Converting Images into Text

### Install dependecies
#### PyTesseract
Ref: https://pypi.org/project/pytesseract
```
pip install pytesseract
```

#### PIL
```
pip install pillow
```

#### Tesseract
Docs: https://tesseract-ocr.github.io/tessdoc/Installation.html

On Windows, you'll be able to download the installer.
Select to download additional scripts and Indian languages during insallation.

### Run in Powershell
```
python image_to_text.py
```

## Conclusion
Output of this is in [output_image_to_text.md](output_image_to_text.md) (Hindi Test).
Another test output is in [output_image_to_text_eng.md](output_image_to_text_eng.md) (English Test).

Multilingual OCR using Tesseract on Hindi is unreliable and useless.
