#!/root/nsd1905/bin/python3
# -*- coding:utf-8 -*-
#爬虫----根据关键词下载百度图片
import re  #正则表达式
import requests  #模拟用户访问网站
def dowmload(html, keyword):  #keyword为用户输入的关键词
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 0  #图片文件
    t = 0  #图片张数
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for durl in pic_url:  #在搜索结果的图片网址中循环下载
        print('正在下载第' + str(t + 1) + '张图片，图片地址:' + str(durl))
        t += 1
        try:
            pic = requests.get(durl, timeout=5)  #网址响应时间不超过5秒,超过视为打不开
        except:  #下载不了就提示
            print('【错误】当前图片无法下载')
            continue
        string = 'pictures\\' + keyword + '_' + str(i) + '.jpg'  #保存图片
        fp = open(string, 'wb')  #打开
        fp.write(pic.content) #content返回的是bytes，二级制型的数据。
        fp.close()
        i += 1
if __name__ == '__main__':
    word = input("请输入关键词: ")
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1530013590757_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=' + word  #百度图片
    result = requests.get(url)   #模拟访问用户想要的网站
    dowmload(result.text, word)
