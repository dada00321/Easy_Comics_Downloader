import requests as rs
from bs4 import BeautifulSoup as bs
import os
# 用來隨機產生 user-agent
from fake_useragent import UserAgent

def get_response(url):
    ua = UserAgent().random
    headers = {"User-Agent": ua}
    #print("ua 產生成功!")
    r = rs.get(url, headers=headers)
    #r = rs.get(url)
    if r.status_code == rs.codes.ok: 
        #print("Successfully get response!")
        r.encoding = "utf-8"
        return r
    else:
        print("Fail to get response.")
        '''
        max_failure_time = 5
        failure_count = 0
        while failure_count <= max_failure_time:
            failure_count += 1
            print(f"第 {failure_count} 次 https請求失敗")
            # retry:
            r = rs.get(url, headers=headers)
            if r.status_code == rs.codes.ok: 
                return r
        print(f"第 {failure_count} 次 https請求失敗")
        #print("無法成功獲取URL!")
        '''
        return None
    
def get_soup(response):
    return bs(response.text, "lxml")
'''
def download_pic(No, imgUrl, busNum):
    r = get_response(imgUrl)
    if r != None:
        if not os.path.exists("BUS"):
            os.mkdir("BUS")
        if not os.path.exists(f"BUS\{busNum}"):
            os.mkdir(f"BUS\{busNum}")
        with open(f"BUS\{busNum}\{No}.jpg", "wb") as fp:
            fp.write(r.content)
    else:
        print(f"車號:{busNum} 第{No}張圖無法爬取!!")
'''