""" Python3: Extract text from pdf file and copy into txt file """
import PyPDF2
pdf_pages = []  # Page object container
pdf_text = []   # Page text container
pages = [int(i) for i in input('Enter page numbers to split text for: ').split(',')]
# Initialize input pdf file
in_pdf = open(r'path/to/input.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(in_pdf)   # Reader element
for page in pages:
    pdf_pages.append(pdf_reader.getPage(page-1))
for i in range(len(pdf_pages)):
    try:
        pdf_text.append(pdf_pages[i].extractText())         
    except:
        pdf_text.append('<NO_TEXT_EXTRACTED>')              
        pass
in_pdf.close()
# Initialize output txt file using 'with' context-manager
with open(r'path/to/output.txt','w') as txt_file:
    for page,page_txt in zip(pages,pdf_text):
        txt_file.write('\n=={}==\n'.format(page)+page_txt)  # Insert page-numbers alongwith text
"""
Note
 1. pdf_pages = []  # Every element is a single-page object
    pdf_text = []   # Every element is a single-page text-string
 2. It'd be really helpful if you could suggest a better way to insert page number (without using multiprocessing).
The efficiency is no-way close to 'pdftotext'. This one's just for fun!
"""
