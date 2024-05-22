import requests,bs4
response = requests.get('https://www.taiwanlottery.com/')
obj = bs4.BeautifulSoup(response.text,'lxml')
print(obj)