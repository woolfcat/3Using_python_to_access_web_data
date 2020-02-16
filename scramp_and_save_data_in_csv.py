#python3，beautifulsoup4

#import所需的包
from bs4 import BeautifulSoup
import requests
import lxml
import csv

#新建data.csv文件，‘w’只读
csv_file=open('data.csv','w')

#csv写入
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary','youtube link'])

#获取网页数据（in text）
html=requests.get('https://coreyms.com/').text

#使用lxml解析器
soup=BeautifulSoup(html,'lxml')

#循环
for article in soup.find_all('article'):
    headline=article.h2.a.text
    summary=article.find('div',class_='entry-content').p.text
 
#如果找不到youtube链接就跳过继续循环，否则找不到会结束循环，需要边写代码边确认循环能走下去
    try:
        yt_src=article.find('iframe',class_='youtube-player')['src']
        yt_id=yt_src.split('/')[4]
        yt_id=yt_id.split('?')[0]
        yt_link=f'https://youtube.com/watch?v={yt_id}'
    except:
        yt_link=None
    csv_writer.writerow([headline,summary,yt_link])

#关闭csv文件
csv_file.close()





###写循环前，确认获取的数据的代码能运行
#before writing the loop, check and make sure your code can be run and get the data you need

article=soup.find('article')

headline=article.h2.a.text
print(headline)

summary=article.find('div',class_='entry-content').p.text
print(summary)

yt_src=article.find('iframe',class_='youtube-player')['src']
yt_id=yt_src.split('/')
print(yt_id)
#看到所需数据在[4]
yt_id=yt_src.split('/')[4]
print(yt_id)
#看到视频id在[0]
yt_id=yt_id.split('?')[0]
yt_link=f'https://youtube.com/watch?v={yt_id}'
print(yt_link)



'''

总结：

运行设备环境：ios（macOS Catalina），win10

1、ios安装anaconda3
重装多次都打不开anaconda3
解决：
--安装目录问题：不能默认安装目录，必须自选安装在应用程序（Applications）里
--权限问题：找到应用程序里的anaconda3，点击右键——显示简介——共享与权限——修改权限

2、win10安装anaconda3后使用beautifulsoup出问题
anaconda3自带beautifulsoup，不需要另外安装，直接从bs4文件import BeautifulSoup(注意大小写)
（我下载了beautifulsoup的安装包/bs4文件夹放到新建的py文件的同一个文件夹内，因此from bs4时会优先搜索py文件所在文件夹里的文件，
但安装包/文件夹都有问题，无法成功使用beautifulsoup。但anaconda3是自带beautifulsoup4的，无需多此一举）


3、多练以熟悉应用
第一次完整的自己写下来时，发现错漏百出！！第二遍还有几处错误。所以要多练！多练！多练！

'''
