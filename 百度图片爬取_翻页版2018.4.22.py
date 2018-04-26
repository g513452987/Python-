import urllib.request
import re
import random

uapools = [
'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)',
'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'
]


def ua(uapools):
    thisua = random.choice(uapools)
    # print(uapools)
    headers = ("User-Agent",thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

def baidu(key,page,path):
    '''
    :param key: 搜索关键词
    :param page: 翻页数(超过100可能会报错)
    :param path: 图片保存的地址
    '''
    keyword = urllib.request.quote(key)
    for i in range(page):
        print('正在爬第'+str(i)+'页..')
        ua(uapools)
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+str(keyword)+'&pn='+str(i*20)
        data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
        pat_pic = '{"thumbURL":"(.*?)",'
        pic_url = re.compile(pat_pic).findall(data)
        for n in pic_url:
            all_url.append(n)
        # print(len(all_url))
    all_url_pure = list(set(all_url))
    print(len(all_url_pure))

    for m in range(len(all_url_pure)):
        try:
            urllib.request.urlretrieve(all_url_pure[m],path+str(i)+'_'+str(m)+'.jpg')
        except:
            print('有一张图片下载失败...下载地址为'+all_url_pure[m])
            pass




if __name__ == '__main__':
    #参数1：搜索关键词
    #参数2：翻页数(不用改，超过100可能会报错)
    #参数3：图片保存的地址
    all_url = []
    all_url_pure = []
    baidu('工地安全帽',100,'G:\\Python全栈_CSDN\\百度图片\\')

