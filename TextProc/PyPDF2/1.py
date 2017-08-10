""" Python3: Save single page of pdf as a new pdf file """
import PyPDF2
# Initialize input pdf file
in_pdf = open(r'/path/to/input.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(in_pdf)   # Reader element
pdf_writer = PyPDF2.PdfFileWriter()         # Writer element
pdf_writer.addPage(pdf_reader.getPage(n))   # Choose n-th page number
# Initialize output pdf file
out_pdf = open(r'/path/to/output.pdf', 'wb')
pdf_writer.write(out_pdf)
# Close I/O pdf files
out_pdf.close()
in_pdf.close()
