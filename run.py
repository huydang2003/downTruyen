from getchap import getChap

import os

def saveChap(pathFile, content):
	with open(pathFile, 'w', encoding='utf8') as file:
		file.write(content)

def test():
	getChap(385)

def main():
	st = 385
	en = 394
	nameFolder = 'Phan 2'
	lstChuong = os.listdir(nameFolder)
	# print(lstChuong)
	# return
	for chuong in range(st, en+1):
		nameFile = f"chuong {chuong}.txt"
		if nameFile in lstChuong: continue

		pathFile = f"{nameFolder}/{nameFile}"
		chap = getChap(chuong)

		saveChap(pathFile, chap)
		print(nameFile)

if __name__ == '__main__':
	main()
	# test()


