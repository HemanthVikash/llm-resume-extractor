import PyPDF2
from common_imports import *





def extract_text_from_pdf(pdf_path):
    text = ""
    with open(os.path.join(PROJECT_ROOT, pdf_path), 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        
        logger.info(f"Number of pages: {num_pages}")

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text



if __name__ == "__main__":
    PDF_PATH = SETTINGS['source_pdf_file']
    extracted_text = extract_text_from_pdf(pdf_path=PDF_PATH)
    print(extracted_text)
    
