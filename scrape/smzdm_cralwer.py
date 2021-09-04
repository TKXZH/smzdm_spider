from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def run():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('./driver/chromedriver', options=chrome_options)
    driver.get("https://www.smzdm.com/top/")
    elem = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/ul/li[1]')
    elem.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    hour3 = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[2]/ul/li[2]')
    hour3.click()

    title_list = driver.find_elements_by_xpath('//*[@id="feed-main-list"]/li[*]/div/h5')
    price_list = driver.find_elements_by_xpath('//*[@id="feed-main-list"]/li[*]/div/div[2]')
    start_list = driver.find_elements_by_xpath('//*[@id="feed-main-list"]/li[*]/div/div[5]/div[1]/span/a/span/span')
    func = lambda a: a.text
    res = zip(map(func, title_list), map(func, price_list), map(func, start_list))
    final_text = ''
    for item in res:
        # 修改此处，过滤认为值的人数
        if int(item[2]) > 40:
            line = '价格:' + item[1] + '。' + '名称:' + item[0] + '。' + '认为值的人数:' + item[2] + '。'
            print(line)
            final_text = final_text + line
    return final_text
