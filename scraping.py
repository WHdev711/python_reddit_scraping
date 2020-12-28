from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime,timedelta
from termcolor import colored
import colorama
colorama.init()


options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3') 
driver = webdriver.Chrome(options=options)
driver1 = webdriver.Chrome(options=options)

url = 'https://www.google.com'
f = open('input_subs.txt','r')
urllist = f.readlines()
output = open('output_temp.txt','w')
for tmp in urllist:
    driver.get(tmp)
    try:
        but_18 = driver.find_elements_by_name('over18')
        but_18[1].click()
    except:
        pass
    print(colored("Starting on URL : "+tmp+"\n",'green'))
    commentlist = driver.find_elements_by_class_name('thing')
    for comment in commentlist:
        try:
            com_url = comment.find_element_by_xpath(".//a[@data-event-action='comments']").get_attribute('href')
            driver1.get(com_url+"?limit=500")
            try:
            	but_19 = driver1.find_elements_by_name('over18')
            	but_19[1].click()
            except:
                pass
            commentarea = driver1.find_element_by_xpath("//div[@class='commentarea']")
            namelist = commentarea.find_elements_by_class_name('tagline')
            for name in namelist:
                try:
                    output.write(name.find_element_by_class_name('author').get_attribute("textContent")+"\n")
                    print("this is comment name",name.find_element_by_class_name('author').get_attribute("textContent"))
                except:
                    pass
        except:
            pass
output.close()
driver.quit()
driver1.quit()

finalresult = open('output_temp.txt','r')
total = finalresult.readlines()
tmp = []
i = 0
for line in total:
    i = i + 1
    tmp.append(line.rstrip("\n"))
a = list(dict.fromkeys(tmp))
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%Y%m%d_%H%M")
output_duplicate = open('output_%s.txt' % timestampStr,'w')
for word in a:
    output_duplicate.write(word+'\n')
output_duplicate.close() 
