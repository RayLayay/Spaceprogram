

import urllib.request as ur
import re
import bs4
import sqlite3


baseurl = 'https://movie.douban.com/top250?start='
#savepath = 'D:/Program Files (x86)/pythonpro/pythonProject/data/movie.xls'
savepath = 'D:/Program Files (x86)/pythonpro/pythonProject/data/moviedata.db'


def main():
    #html = askurl(url)
    datalist = getdata(baseurl)
    #print(datalist)
    saveda2(datalist,savepath)


findlink = re.compile(r'<a href="(.*?)">')
findimg = re.compile(r'<img.*src="(.*?)" width="100"/>', re.S)
findtitle = re.compile(r'<span class="title">(.*)</span>')
findbd = re.compile(r'<p class="">(.*?)</p>',re.S)
findrating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findinq = re.compile(r'<span class="inq">(.*)</span>')
findpingjia = re.compile(r'<span>(.*)人评价</span>')


def askurl(url):
    head = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.87 Safari/ 537.36 SE 2.X MetaSr 1.0'
    }

    request = ur.Request(url, headers=head)
    response = ur.urlopen(request)
    html = response.read().decode('utf-8')
    return html


def getdata(baseurl):
    datalist = []
    for i in range(0,25):
        url = baseurl + str(i*25)
        html = askurl(url)
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)
            link = re.findall(findlink,item)[0]
            data.append(link)
            img = re.findall(findimg,item)[0]
            data.append(img)
            titles = re.findall(findtitle,item)
            if len(titles)==2:
                ctitle = titles[0].replace('/','')
                data.append(ctitle)
                otitle = titles[1].replace(' / ',' ')
                data.append(otitle)
            else:
                data.append(titles)
                data.append(' ')
            bd = re.findall(findbd,item)[0]
            bd = re.sub(' \ \ ','',bd)
            bd = re.sub('<br(\s+)?/(\s+)?>','',bd)
            bd = re.sub(' / ','',bd)
            bd = re.sub('\n','',bd)
            bd = re.sub(' ','',bd)
            data.append(bd)
            rating = re.findall(findrating,item)[0]
            data.append(rating)
            inq = re.findall(findinq,item)
            if len(inq) == 0:
                data.append(' ')
            else:
                data.append(inq[0])
            pingjia = re.findall(findpingjia,item)[0]
            data.append(pingjia)

            datalist.append(data)

    return datalist


def saveda2(datalist,savepath):
    conn = sqlite3.connect(savepath)
    sql1='''
        create table movietop
        (link char,
        img char,
        ctitle char,
        otitle char,
        bd char,
        rating char,
        inq char,
        pingjia char);
    '''
    conn.execute(sql1)
    conn.commit()

    for i in range(0,250):
        data1 = datalist[i]
        sql2 = '''
            insert into movietop
                values (data1[0],data1[1],data1[2],data1[3],data1[4],data1[5],data1[6],data1[7])
                '''
        conn.execute(sql2)
        conn.commit()


    conn.close()


if __name__ == '__main__':
    main()

