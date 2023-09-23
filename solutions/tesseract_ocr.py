import os
import sys

from pdf2image import convert_from_path
from PIL import Image
import pytesseract


SYS_ROOT = os.path.abspath('/')
POPPLER_PATH = os.path.abspath('/Program Files/poppler/poppler-23.08.0/Library/bin')
TESSERACT_PATH = os.path.abspath('/Program Files/Tesseract-OCR/tesseract.exe')


def convert_pdf_to_image(pdf_path):
    save_path = f'./images/{os.path.basename(pdf_path)}/'
    # Create required directories
    os.makedirs(save_path, exist_ok=True)
    # Store PDF with convert_from_path function
    images = convert_from_path(pdf_path,
        poppler_path = POPPLER_PATH)
    pages = 0
    for i in range(len(images)):
        # Save pages as images in the pdf
        pages += 1
        images[i].save(f'./{save_path}/{str(i)}.png', 'PNG')

    return pages


def run_ocr_on_images(pdf_path, lang, pages):
    # If you don't have tesseract executable in your PATH, include the following
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    print('Tesseract Supported Languages: ', pytesseract.get_languages(config=''))
    # Generate text using OCR
    text = ''
    for i in range(pages):
        text += pytesseract.image_to_string(Image.open(f'./images/{os.path.basename(pdf_path)}/{str(i)}.png'), lang=lang)

    return text


def run_tesseract(pdf_path, lang):
    pages = convert_pdf_to_image(pdf_path)
    return run_ocr_on_images(pdf_path, lang, pages)
