import os
import sys
from pdf2image import convert_from_path

SYS_ROOT = os.path.abspath('/')
POPPLER_PATH = '/Program Files/poppler/poppler-23.08.0/Library/bin'

def convert_pdf(pdf_path):
    save_path = f'./images/{os.path.basename(pdf_path)}/'
    # Create required directories
    os.makedirs(save_path, exist_ok=True)
    # Store PDF with convert_from_path function
    images = convert_from_path(pdf_path,
        poppler_path = os.path.abspath(POPPLER_PATH))
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(f'./{save_path}/{str(i)}.png', 'PNG')


def convert_multiple_pdf(path_list):
    for path in path_list:
        convert_pdf(path)


args = sys.argv[1:]

if len(args) <= 0:
    print('no args provided')
    print('usage:', sys.argv[0], '[list of files]')
    exit(1)

convert_multiple_pdf(args)
