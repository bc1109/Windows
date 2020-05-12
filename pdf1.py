import PyPDF2
import os

os.chdir('C:\\Users\\admin\BCPY')
pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

# reader.numPages      # Gets num of pages

page = reader.getPage(0)


page.extractText()
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
