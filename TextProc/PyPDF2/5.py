""" Python3: Reorder pages in a pdf file """
import PyPDF2
def pdf_reorder(s):
    # Initialize input pdf file
	in_pdf = open(s+'.pdf','rb')
    pdf_reader = PyPDF2.PdfFileReader(in_pdf)	# Reader element
    pdf_writer = PyPDF2.PdfFileWriter()			# Writer element
    #pages = pdf_reader.getNumPages()
    #pages_reordered = [int(i) for i in input('Rearranged Sequence: ').split(',',maxsplit=pages-1)]
    pages_reordered = [int(i) for i in input('Rearranged Sequence: ').split(',')]	# Assume the list is a replacement for pages (1,2,3,...)
    for page in pages_reordered:
        pdf_writer.addPage(pdf_reader.getPage(page-1))
    # Initialize output pdf file
	op_pdf = open(s+'2.pdf','wb')
    pdf_writer.write(op_pdf)
	# Close I/O pdf files
    op_pdf.close()
    in_pdf.close()
reorder = bool(input('Reorder? (1|0): '))
if reorder:
    pdf_reorder(r'path/to/input_pdf')	# Don't use '.pdf' extension
# 'input_pdf' will be reordered and saved as 'input_pdf2'