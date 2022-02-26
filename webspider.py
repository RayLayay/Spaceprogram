import urllib.request as ur
import bs4
from requests.api import request
import re
from bs4 import BeautifulSoup
import xlwt


baseurl = 'https://xs.sogou.com/29_0_0_0_heat/'
savepath = 'D:/Program Files (x86)/pythonpro/pythonProject/message.xlsx'

def main():
    data = getdata(baseurl)
    savedata(data,savepath)


def askurl(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'}
    request = ur.Request(url, headers = head)
    response = ur.urlopen(request)
    html = response.read().decode('utf-8')
    return html

findimg = re.compile(r'<img src=(.*)>')
findtitle = re.compile(r'<h3><a href=.*>(.*)</a></h3>')
findwriter = re.compile(r'<div class="d1">(.*)<br/><span class="fl">')
findinq = re.compile(r'<div class="d2">(.*)</div>')

def getdata(url):
    html = askurl(url)
    datalist = []
    soup = bs4.BeautifulSoup(html,'html.parser')
    for item in soup.find_all('div',class_ = "sx-ret fr"):
        item = str(item)
        img = re.findall(findimg,item)
        datalist.append(img)
        title = re.findall(findtitle,item)
        datalist.append(title)
        writer = re.findall(findwriter,item)
        for i in writer:
            i.replace('作者：','')
        datalist.append(writer)
        inq = re.findall(findinq,item)
        for k in inq:
            k.replace('\u3000\u3000','')
        datalist.append(inq)
    
    return datalist


def savedata(data,savepath):
    book = xlwt.Workbook(savepath)
    sheet = book.add_sheet('sheet1')
    column = ['img','title','writer','inq']
    for i in range(0,4):
        sheet.write(0,i,column[i])
        for k in range(0,18):
            sheet.write(k+1,i,data[i][k])
    book.save('message.xls')
    

if __name__ == '__main__':
    main()