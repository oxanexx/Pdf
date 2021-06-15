# Добавление изображения в многостраничный PDF документ

from pdfrw import PdfReader, PdfWriter, PageMerge

input_file = "source/Documentation-Python.pdf"
output_file = "dist/Documentation-Python-pages-image.pdf"
watermark_file = "source/mshe-logo-512x512.pdf"

# определяем объекты чтения и записи
reader_input = PdfReader(input_file)
writer_output = PdfWriter()
watermark_input = PdfReader(watermark_file)
watermark = watermark_input.pages[0]

# просматривать страницы одну за другой
for current_page in range(len(reader_input.pages)):
    merger = PageMerge(reader_input.pages[current_page])
    merger.add(watermark).render()

# записать измененный контент на диск
writer_output.write(output_file, reader_input)