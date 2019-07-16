import requests
from bs4 import BeautifulSoup


# carrier = 'PS'
# awbs = '566-13937173'
# #awbs = '566-13936182'
# url = 'http://www.cargoupdate.com/tracktrace/?carrier={}&awbs={}'.format(carrier, awbs)
#url='http://bct.az/en/awb_info.asp?id=1486079'
#url = 'http://swiftaviagroup.com/all_cargo/'

#url='http://connect.track-trace.com/for/andrey/aircargo/56613938260'
#url = 'http://www.track-trace.com/my/new/aircargo/56613938260'
#url = 'http://www.cargoupdate.com/tracktrace/?carrier=PS&awbs=566-13936182'
info= requests.get(url)
print(info.status_code) #200
print(info.text)

info_soup = BeautifulSoup(info.text, 'html.parser')
#print(info_soup.prettify())
#print(info_soup.findAll('div', {'class':'tracktracecontainer'}))
#print(info_soup.findAll('body', {'class':'scrolled'}))
#for link in info_soup.findAll('div', {'class':'col-xs-3'}):
for link in info_soup.findAll('nobr'):
	print(link.text)
	# if link.text == 'GYD-KBP':
	# 	print('Viletel v Kiev')
	# else:
	# 	print('Ne zaregestrirovan')	
