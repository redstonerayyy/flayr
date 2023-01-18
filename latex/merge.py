from PyPDF2 import PdfFileMerger, PdfFileReader

def merge():
	merger = PdfFileMerger()

	merger.append(PdfFileReader(open("mnist_survey_accompanying_sheet.pdf", 'rb')))
	merger.append(PdfFileReader(open("mnist_survey_sheet_filled.pdf", 'rb')))

	merger.write("lehrer_document_survey.pdf")