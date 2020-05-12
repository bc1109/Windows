import PyPDF2
import os

os.chdir('C:\\Users\\admin\BCPY\\taclan docs')

pdf1File = open('16.2 Install Manual Final1.22.20.pdf',
                'rb')  # rb = read binary mode
pdf2File = open(
    '16.2 Operations and Maintenance_Manual  Final_edited1.28.20.pdf', 'rb')
pdf3File = open('VDD Final 1.22.20.pdf', 'rb')
pdf4File = open('FCD-W v2.X VDD Final.pdf', 'rb')
pdf5File = open('MTP Final 1.22.20.pdf', 'rb')
pdf6File = open('SPS Final 1.22.20.pdf', 'rb')
pdf7File = open('SRS Final 1.22.20.pdf', 'rb')
pdf8File = open('TACLAN 16.2 Document Control Process.pdf', 'rb')


reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
reader3 = PyPDF2.PdfFileReader(pdf3File)
reader4 = PyPDF2.PdfFileReader(pdf4File)
reader5 = PyPDF2.PdfFileReader(pdf5File)
reader6 = PyPDF2.PdfFileReader(pdf6File)
reader7 = PyPDF2.PdfFileReader(pdf7File)
reader8 = PyPDF2.PdfFileReader(pdf8File)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader3.numPages):
    page = reader3.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader4.numPages):
    page = reader4.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader5.numPages):
    page = reader5.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader6.numPages):
    page = reader6.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader7.numPages):
    page = reader7.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader8.numPages):
    page = reader8.getPage(pageNum)
    writer.addPage(page)


outputFile = open('TACLAN_ALL_IN_ONE.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
pdf3File.close()
pdf4File.close()
pdf5File.close()
pdf6File.close()
pdf7File.close()
pdf8File.close()
