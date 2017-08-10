""" Python3: Generate a pdf made of specific pages from parent pdf """
import PyPDF2
# Select pages to be used
pages = [int(i) for i in input('Enter Page numbers to cut-out:').split(',')]
# Initialize input pdf file
in_pdf = open(r'/path/to/input.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(in_pdf)   # Reader element
pdf_writer = PyPDF2.PdfFileWriter()         # Writer element
for page in pages:
    pdf_writer.addPage(pdf_reader.getPage(page)) 
# Initialize output pdf file
out_pdf = open(r'/path/to/output.pdf', 'wb')
pdf_writer.write(out_pdf)
# Close I/O pdf files
out_pdf.close()
in_pdf.close()
