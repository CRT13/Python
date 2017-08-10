""" Python3: Display pdf file metadata """
import PyPDF2
def display_metadata(md): 
    return {
            'custom_properties':md.custom_properties,
            'dc_contributor':md.dc_contributor,
            'dc_coverage':md.dc_coverage,
            'dc_creator':md.dc_creator,
            'dc_date':md.dc_date,
            'dc_description':md.dc_description,
            'dc_format':md.dc_format,
            'dc_identifier':md.dc_identifier,
            'dc_language':md.dc_language,
            'dc_publisher':md.dc_publisher,
            'dc_relation':md.dc_relation,
            'dc_rights':md.dc_rights,
            'dc_source':md.dc_source,
            'dc_subject':md.dc_subject,
            'dc_type':md.dc_type,
			#'dc_title':md.dc_title, <- This doesn't work for some files
            'pdf_keywords':md.pdf_keywords,
            'pdf_pdfversion':md.pdf_pdfversion,
            'pdf_producer':md.pdf_producer,
            'xmp_createDate':md.xmp_createDate,
            'xmp_creatorTool':md.xmp_creatorTool,
            'xmp_metadataDate':md.xmp_metadataDate,
            'xmp_modifyDate':md.xmp_modifyDate,
            'xmpmm_documentId':md.xmpmm_documentId,
            'xmpmm_instance':md.xmpmm_instanceId
            }
in_pdf = open(r'C:\Users\CRT13\Desktop\BT-SDT_enhanced.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(in_pdf)	# Reader element
pdf_info = pdf_reader.documentInfo			# file-info
pdf_metadata = pdf_reader.xmpMetadata		# file-metadata
usr_input = int(input('Check for meta-data?(1|0): '))
if pdf_metadata and usr_input:
    print(display_metadata(pdf_metadata))
else:
    print('Sorry, no metadata associated.')