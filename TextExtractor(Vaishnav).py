from PyPDF2 import PdfReader
import pdfplumber

pdf_path = "killme.pdf"

# Try PyPDF2 first
reader = PdfReader(pdf_path)

for page in reader.pages:
    print(page.extract_text())

with pdfplumber.open(pdf_path) as pdf:
    text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])


'''text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])'''