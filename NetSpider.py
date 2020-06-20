import requests
import re
import os
import time
#请求网页
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.21 Safari/537.36'}
respon = requests.get('https://www.vmgirls.com/13853.html', headers = headers)

#解析网页
html = respon.text
dir_name = re.findall('<title>(.*?)</title>', html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
print(urls)
#保存图片
for url in urls:
    time.sleep(1)
    #图片名字
    file_name = url.split('/')[-1]
    respon = requests.get(url, headers = headers)
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(respon.content)
