import csv
import PyPDF2
import re

def csv_working():
    data = open('download_link.csv')
    csv_data = list(csv.reader(data))
    url = []
    for row in csv_data:
        url.append(row[2])
    print(''.join(url))


def PDF_working():
    pdf = open('Contact_Email_Information.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf)
    pattern = re.compile(r'[._/\w]+@.[._/\w]+')
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        match = re.search(pattern, page.extractText())
        print(match)


PDF_working()
