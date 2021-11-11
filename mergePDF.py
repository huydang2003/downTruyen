from PyPDF2 import PdfFileMerger
import os

pathFIN = 'PDF'
nameOO = "12 Nữ Thần 2"

st = 260
en = 395

merger = PdfFileMerger()
for x in range(st,en+1):
	fileName = f'chuong {x}.pdf'
	filePath = f'{pathFIN}/chuong {x}.pdf'
	merger.append(filePath)
	print(fileName)
merger.write(f"{nameOO}.pdf")
merger.close()

