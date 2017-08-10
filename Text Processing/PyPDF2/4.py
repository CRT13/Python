""" Python3: Obtain file-info from pdf file """
#============================== (1) - single file ================================#
import PyPDF2
# Initialize input pdf file
in_pdf = open(r'/path/to/input.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(in_pdf)   # Reader element
pdf_info = pdf_reader.documentInfo
# pdf_info is a dict instance. Use 'key:value' pairs to access basic file-info
#=================================================================================#
#============================= (2) - multiple files ==============================#
import PyPDF2
# Select pdf files to be used (assuming they are in the same directory)
pdfs = [i for i in input('Enter PDF files to choose from: ').split(',')]
pdf_info = []     # file-info list
for pdf in pdfs:
    pdf += '.pdf'
    print('Opening \''+pdf+'\'...')
    in_pdf = open(r'/path/to/input_directory/'+pdf, 'rb')
    pdf_info.append(PyPDF2.PdfFileReader(in_pdf).documentInfo)
# pdf_info is a list instance. Use comprehension/slicing to access basic file-info
#=================================================================================#
