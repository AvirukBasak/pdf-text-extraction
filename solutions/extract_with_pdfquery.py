from pdfquery import PDFQuery

def run_pdfquery(path):
    pdf = PDFQuery(path)
    pdf.load()
    text_ele = pdf.pq('LTTextLineHorizontal')
    text_ls = [ t.text for t in text_ele ]
    return '\n\n'.join(text_ls)
