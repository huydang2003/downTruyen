from fpdf import FPDF
import os
   
   
def initPDF():
	# save FPDF() class into 
	# a variable pdf
	pdf = FPDF()
	# Add a page
	pdf.add_page()
	# set style and size of font 
	# that you want in the pdf
	pdf.add_font("Consolas", fname="font/consolai.ttf", uni=True)
	pdf.set_font("Consolas", size = 20)
	return pdf

pathFIN = 'Phan 2'
pathFOUT = 'PDF'

st = 260
en = 395



lstChuong = os.listdir(pathFOUT)

for x in range(st,en+1):
	with open(f"{pathFIN}/chuong {x}.txt", "r", encoding='utf8') as file:
		pdf = initPDF()
		fileName = f'chuong {x}.pdf'
		if fileName in lstChuong: continue
		for line in file:
			pdf.multi_cell(0, 10, line)

		filePath = f'{pathFOUT}/{fileName}'
		pdf.output(filePath, "F")
		pdf.close()
		print(fileName)