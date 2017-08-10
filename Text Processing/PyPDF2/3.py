"""
Python3: Generate a pdf from a list of pdfs
    The pages are fixed sequentially as PDF(1)[1,2,3...]+PDF(2)[1,2,3,...]+...
    There is no cross-manipulation.
"""
import PyPDF2
# Select pdf files to be used (assuming they are in the same directory)
pdfs = [i for i in input('Enter PDF files to choose from: ').split(',')]
pdf_writer = PyPDF2.PdfFileWriter()             # Writer element
for pdf in pdfs:
    pdf += '.pdf'
    print('Opening \''+pdf+'\'...')
    # Initialize input pdf file
    in_pdf = open(r'/path/to/input_directory/'+pdf, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(in_pdf)   # Reader element
    pages = [int(i)-1 for i in input('Enter Page numbers to cut-out: ').split(',')]
    for page in pages:
        pdf_writer.addPage(pdf_reader.getPage(page))
# Initialize output pdf file
out_pdf = open(r'/path/to/output.pdf', 'wb')
pdf_writer.write(out_pdf)
# Close I/O pdf files
out_pdf.close()
in_pdf.close()
