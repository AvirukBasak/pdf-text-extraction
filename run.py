import sys
sys.path.insert(1, 'solutions')

def run_soln(path):
    if soln == 1:
        from solutions.extract_with_fitz import run_fitz
        return run_fitz(path)

    if soln == 2:
        from solutions.pypdf2_direct import run_pypdf2
        return run_pypdf2(path)

    if soln == 3:
        from solutions.tesseract_ocr import run_tesseract
        return run_tesseract(path, lang='eng')


PDF_FILES_LIST = [
    'TXT Mines and Minerals Act.pdf',
    'TXT Mineral Auction Amendment Rules.pdf',
    'IMG Mines and Minerals Act 1957.pdf',
]

FILE_NOW = f'pdfs/{PDF_FILES_LIST[2]}'

print('possible solutions:')
print('  1. Fitz')
print('  2. PyPDF2')
print('  3. Tesseract OCR')

soln = int(input('enter choice: '))
if soln < 1 or soln > 3:
    print(f'no such solution: {soln}')
    exit(1)

yn = input(f'confirm target pdf \'{FILE_NOW}\' (Y/n): ')
if yn != 'y' and yn != 'n' and yn != '':
    print('invalid confirm, enter \'y\' or \'n\'')
    exit(1)

text = run_soln(FILE_NOW)
print(text)
