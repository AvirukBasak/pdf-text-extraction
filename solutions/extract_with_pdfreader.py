from pdfreader import SimplePDFViewer

def run_pdfreader(path):
    fd = open(path, 'rb')
    vwr = SimplePDFViewer(fd)
    vwr.navigate()
    vwr.render()
    md = vwr.canvas.text_content
    return '\n'.join(md_list)
