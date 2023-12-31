# PDF Text Extraction
- Fitz
- PyPDF2
- Poppler and Tesseract
- PDFQuery

#### Note
Tesseract is the only one that can handle scanned docs and digitally born PDFs.
However, there may be a lack of accuracy as Tesseract uses OCR.

Other solutions can work with high accuracy on digitally born PDFs (text in PDF) but will fail for scanned PDFs.

#### Note
Multilingual text extraction (in Hindi) is unreliable.


#### Note
If you get this error when using `Fitz` solution:
```
AttributeError: module 'fitz' has no attribute 'open'
```
Then reinstall `PyMuPDF` using:
```
pip uninstall PyMuPDF
pip install PyMuPDF
```


## Gettig Started
Open this project root in Powershell and run
```
python -m venv env
.\env\Scripts\Activate.ps1
```
You MUST use a virtual environment as we'll be installing an ungodly number of packages and dependencies.


## Install dependecies

### PIP
Run the following after activating your environment:
```
python setup.py
```

### Poppler
PDF2Image, which is a dependency of this project, requires you have `Poppler` downloaded.

Poppler direct download link for Windows: https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip

You will need to add the `bin/` directory i.e. `poppler-23.08.0/Library/bin/` to your PATH.

### Tesseract-OCR
Tesseract-OCR direct download link for Windows: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe

On Windows, you'll be able to download the installer.
Select to download additional scripts and Indian languages during insallation.


## Run experiment
- Set `POPPLER_PATH` and `TESSERACT_PATH` in `solutions/tesseract_ocr.py`
- Put your PDF files in `pdfs/`
- List you PDF files by setting `PDF_FILES_LIST` and `FILE_NOW` in `run.py`

Once setup is done, run:
```
python run.py
```

Select a solution and see the text getting extracted and printed.

If you use the `Tesseract` solution, you will also get a printed list of languages installed with `Tesseract-OCR`

Note that text extraction may take a long time depending on number of pages in PDF.
It may take over a minute or two in some cases.


## Direct Download Links
- Poppler for Windows: https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip
- Tesseract-OCR for Windows: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe


## References
- PDF to Image GFG guide: https://www.geeksforgeeks.org/convert-pdf-to-image-using-python
- PyTesseract Docs: https://pypi.org/project/pytesseract
- Tesseract Docs: https://tesseract-ocr.github.io/tessdoc/Installation.html
