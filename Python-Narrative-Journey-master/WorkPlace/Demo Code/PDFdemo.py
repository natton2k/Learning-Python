import PyPDF2

book = open("D:\Python\Mark Lutz - Learning Python, 5th Edition-O'Reilly Media (2013).pdf", 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
page = pdf_reader.getPage(0)

f = open('PDF.pdf', 'wb')
pdf_writter = PyPDF2.PdfFileWriter()
pdf_writter.addPage(page)
pdf_writter.write(f)

book.close()
f.close()
