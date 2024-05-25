# 使用者輸入
inp = input('輸入年月日(ex:0990301)')

import requests,bs4
response = requests.get('https://www.taiwanlottery.com/lotto/history/history_result')
obj = bs4.BeautifulSoup(response.text,'lxml')
