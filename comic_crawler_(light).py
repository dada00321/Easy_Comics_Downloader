from modules.basic_scraping_module import get_response, get_soup

from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
import os, time, json

def get_webdriver(headless):
    chrome_options = Options()
    if headless == True:
        chrome_options.add_argument("--headless")
        #chrome_options.headless = True # also works
    wd_path = r"D:\geckodriver\chromedriver.exe"
    driver = wd.Chrome(wd_path, options=chrome_options)
    driver.implicitly_wait(10)
    return driver
    
def scraping_comicBook(comicNum, ep):
    print(f"正在下載 漫畫編號: {comicNum} 第{ep}話")
    max_page = 25
    pages = [f"{ep}-{pageNum}" for pageNum in range(1, max_page+1)]
    
    err_occur = False
    for idx, page in enumerate(pages):
        if err_occur: 
            break
        url = f"https://comicbus.com/online/a-{comicNum}.html?ch={page}"
        print(f"Page {page} is downloading...")
        #print(url)
        driver = get_webdriver(headless=True)
        driver.get(url)
        
        img = driver.find_element_by_id("TheImg")
        imgUrl = img.get_attribute("src")
        
        # get response and then download images
        r = get_response(imgUrl)
        if r != None:
            if not os.path.exists("download_comics"):
                os.mkdir("download_comics")
            if not os.path.exists(f"download_comics\{comicNum}"):
                os.mkdir(f"download_comics\{comicNum}")
            if not os.path.exists(f"download_comics\{comicNum}\第{ep}話"):
                os.mkdir(f"download_comics\{comicNum}\第{ep}話")
            with open(f"download_comics\{comicNum}\第{ep}話\{1+idx}.jpg", "wb") as fp:
                fp.write(r.content)
        else:
            err_occur = True
    driver.quit()
    print(f"漫畫編號:{comicNum} 第{ep}話 下載完成！")
    
if __name__ == "__main__":
    comicNum = 14237 # 輝夜姬 漫畫
    ep = 106 # 第 X 話
    scraping_comicBook(comicNum, ep)
    