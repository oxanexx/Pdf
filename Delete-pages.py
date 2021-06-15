# Удаление страниц с помощью PyMuPDF
import fitz

input_file = "source/Documentation-Python.pdf"
output_file = "dist/Documentation-Python-rearranged.pdf"


# Определите страницы для сохранения - 1, 2 и 4
file_handle = fitz.open(input_file)
pages_list = [0,1,3]

# Выберите страницы и сохраните вывод
file_handle.select(pages_list)
file_handle.save(output_file)