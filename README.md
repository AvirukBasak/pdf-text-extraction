# PDF Text Extraction
- Fitz
- PyPDF2
- Poppler and Tesseract

## Note
Multilingual text extraction (in Hindi) is unreliable and useless.


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
python setyp.py
```

### Poppler
PDF2Image, which is a dependency of this project, requires you have `Poppler` downloaded.

Poppler direct download link for Windows: https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip

You will need to add the `bin/` directory i.e. `poppler-23.08.0/Library/bin/` to your PATH.

### Tesseract-OCR
Docs: https://tesseract-ocr.github.io/tessdoc/Installation.html

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


## References
- PDF to Image: https://www.geeksforgeeks.org/convert-pdf-to-image-using-python
- Poppler direct download link for Windows: https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip
- PyTesseract: https://pypi.org/project/pytesseract
- Tesseract Installation: Docs: https://tesseract-ocr.github.io/tessdoc/Installation.html
