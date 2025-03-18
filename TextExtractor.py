from xml.etree.ElementTree import tostring
import pdfplumber

def text_extractor(pdf_path):
    try:
        text_path = pdf_path
        text_path = text_path.rstrip(".pdf")+".txt"
        print (text_path)
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        with open(text_path,"w",encoding="utf-8") as f:
            f.write(text)
            
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False