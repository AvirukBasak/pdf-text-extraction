import fitz

def run_fitz(path):
    text = ''
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return (text)
