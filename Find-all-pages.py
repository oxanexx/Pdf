#Найти все страницы, где есть слово Python

import fitz

filename = "source/Documentation-Python.pdf"

search_term = "Python"
pdf_document = fitz.open(filename)

for current_page in range(len(pdf_document)):
    page = pdf_document.loadPage(current_page)
    if page.searchFor(search_term):
        print("%s найдено на странице %i" % (search_term, current_page+1))