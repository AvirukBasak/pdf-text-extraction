from PyPDF2 import PdfReader

def run_pypdf2(path):
    text = ''
    reader = PdfReader(path)
    for page in reader.pages:
        text += page.extract_text()
    # printing number of pages in pdf file
    print('Page Count:', len(reader.pages))
    return (text)
