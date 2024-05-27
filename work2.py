# 查詢開獎號碼並自動開啟瀏覽器搜尋該期別方便對照
from selenium import webdriver
from selenium.webdriver.common.by import By
import time , requests
# 使用者輸入
year = input('西元年分')
month = input('月(ex : 5月 => 05)')
day = input('日(ex : 5日 => 05)')
browser = webdriver.Chrome()
# 擷取網頁
url = 'https://api.taiwanlottery.com/TLCAPIWeB/Lottery/SuperLotto638Result?period&month='+year+'-'+month+'&pageNum=1&pageSize=10'
url2 = 'https://www.taiwanlottery.com/lotto/history/history_result'
html = requests.get(url)
browser.get(url2)
# 轉換json檔案
data = html.json()
# 查找元素
period = ''
datalist = data['content']['superLotto638Res']
lottery = year+'-'+month+'-'+day+'T00:00:00'
for i in range(len(datalist)):
    if datalist[i]['lotteryDate'] == lottery:
        period = datalist[i]['period']
        num = datalist[i]['drawNumberSize']
        print('開獎號碼 : ',end='')
        print(*num)
        # 自動輸入開獎期別
        browser.find_element(By.XPATH,'//*[@id="el-id-1024-8"]').send_keys(period)
        browser.find_element(By.XPATH,'//*[@id="__nuxt"]/main/div[1]/div[2]/div/button').click()
        time.sleep(15)
if period == '':
    print('查無此期別')