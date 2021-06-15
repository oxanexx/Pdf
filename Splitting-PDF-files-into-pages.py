#Разделение PDF‑файлов на страницы с помощью PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_document = "source/Documentation-Python.pdf"
pdf = PdfFileReader(pdf_document)

for page in range(pdf.getNumPages()):
    pdf_writer = PdfFileWriter()
    current_page = pdf.getPage(page)
    pdf_writer.addPage(current_page)

    outputFilename = "dist/Documentation-Python-page-{}.pdf".format(page + 1)
    with open(outputFilename, "wb") as out:
        pdf_writer.write(out)

        print("created", outputFilename)