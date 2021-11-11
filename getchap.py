import requests
from bs4 import BeautifulSoup
import re

def getData(url):
	res = requests.get(url)
	data = res.text
	return data

def getTitle(data):
	soup = BeautifulSoup(data, 'html.parser')
	# lay title
	title = soup.title.text.split('- ')[1]	
	return title

def getContent(data):
	soup = BeautifulSoup(data, 'html.parser')
	# lay content
	content = soup.find(id='js-truyenkk-read-content')
	content = str(content).replace('</p>', '\n')
	content = content.replace('<p>', '')
	tm = re.findall(r'<(.*?)>', content)
	for t in tm:
		rm = f'<{t}>'
		content = content.replace(rm, '')
	tt = 'Bạn đang đọc truyện trên 123truyen.com , Chúc bạn đọc truyện vui vẻ!'
	content = content.replace(tt, '')
	tt = '123 Truyện Chấm Com\n -->'
	content = content.replace(tt, '')
	return content

def getChap(chuong):
	url = f'https://123truyen.com/12-nu-than/chuong-{chuong}'
	data = getData(url)
	title = getTitle(data)
	content = getContent(data)
	chap = title + '\n' + content
	return chap

if __name__ == '__main__':
	pass