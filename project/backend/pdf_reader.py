from PyPDF2 import PdfReader #extracting texts from uploaded pdf
def extract_text_from_pdf(pdf_path): #function which is used to extract text from the uploaded fpdf 
    text = "" #initially there is no text therefore it is assigned to empty string
    reader = PdfReader(pdf_path) #it reads the uploaded pdf file and stores in reader variable
    for page in reader.pages: 
        text += page.extract_text() #it extracts the text from each page of the uploaded pdfand add it to text variable
    return text