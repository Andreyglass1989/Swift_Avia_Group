import requests
headers = {'id':'20edd1d5-3b9f-4492-9807-b3c5d8146e57', 'token':'bAw8Ng6RujV1wnpjSFzaiJl/2nm2yG94Zz8YdANno7fvJyLdtKMNf3Hv7nNvYsx67p9l5xSyfX6aq4YQVmq6JS+TLKogaQ+QAP4IUu2KLbBOXsWKyCq5KahRf9KmuN6kdgehGAHVUBKq6SmkqQs6RMV2DCOtSa5luQashjz8dvBSPj/RlUzTLw+58qzcAdhNRClfb4mURKhBlEBdckSLeCknFAt10Rue8KO5wbR3B7Ma9X/LW1o3ASHoSq7EyzY=', 'content-type': 'application/json' }
url_today = 'https://acp.privatbank.ua/api/proxy/rest/today?acc=26004054347876'
url_last_day = 'https://acp.privatbank.ua/api/proxy/rest/lastday?acc=26004054347876'

url_today1 = 'https://acp.privatbank.ua/api/proxy/transactions/today?acc=26004054347876'
url_last_day1 = 'https://acp.privatbank.ua/api/proxy/transactions/lastday?acc=26004054347876'

z = requests.get('https://acp.privatbank.ua/api/proxy/transactions?acc=26004054347876&startDate=20-01-2019&endDate=20-02-2019', headers=headers)

z1 = requests.get(url_today, headers=headers)
z2 = requests.get(url_last_day, headers=headers)

z3 = requests.get(url_today1, headers=headers)
z4 = requests.get(url_last_day1, headers=headers)

d = z.json()
a = z3.json()
b = z4.json()
c = z.json()

z5 = c['StatementsResponse']['statements']


for number in range(len(z5)):
	print(number)
	obj = z5[number].values()[0]
	print(obj['BPL_DAT_OD'])
	print(obj['BPL_TIM_P'])
	print(obj['BPL_SUM'])
	print(obj['BPL_CCY'])
	print(obj['BPL_A_MFO_CITY'])
	print(obj['BPL_OSND'])
	print(obj['AUT_CNTR_NAM'])


"""
In [11]: z5.keys()
Out[11]: [u'SAMBJ0209XQA76']

In [12]: z5.values()
Out[12]: 

"""