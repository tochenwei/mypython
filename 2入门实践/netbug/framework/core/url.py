#coding:utf-8
#抓取网页内容-发送报头
def getUrlContent(url=''):
    import urllib2
    import sys
    from urlparse import urlparse
    if url == None or url == '':
        return ''
    
    r = urlparse(url)
    send_headers = {
     'Host':r.netloc,
     'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Connection':'keep-alive'
    }
      
    req = urllib2.Request(url,headers=send_headers)
    #设置超时时间为15秒
    r = urllib2.urlopen(req,timeout=15)
      
    html = r.read()        #返回网页内容
    #receive_header = r.info()     #返回的报头信息
      
    # sys.getfilesystemencoding() 
    #html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding()) #转码:避免输出出现乱码 
      
    #print receive_header

    return html
'''
@description:根据给出的当前页面url和当前的url
             产生一个完整的url
@return:string
@author:chenwei
'''
def makeFullUrl(currentUrl,url):
    if  url=='' or url == None:
        return url
    if 'http:' in url or 'https:' in url :
        return url
    import re
    if re.match(r"^\/.*",url):
        return url
    import os
    filename = os.path.basename(currentUrl)
    index  = currentUrl.index(filename)
    dirUrl = currentUrl[:index]
    return dirUrl+url
'''
@description:根据当前url,分页参数,下一页的页号产生下一页的链接
@return:string
@author:chenwei
'''
def getNextPageUrl(currentUrl,pageParam,nextPageNum):
    if pageParam not in currentUrl:
        nextPageUrl = currentUrl+'&'+pageParam+'='+str(nextPageNum)
        return nextPageUrl
    else:
        import re
        strinfo = re.compile(pageParam+'=[\d]+')
        nextPageUrl = strinfo.sub(pageParam+'='+str(nextPageNum),currentUrl)
        return nextPageUrl
'''
@description:根据当前url,分页参数,分页的间隔,返回下一页的页号
@return int
@author:chenwei
'''
def getNextPageNum(currentUrl,pageParam,startPageNum=1,pageStep=1):
    if pageParam not in currentUrl:
        return startPageNum+int(pageStep)
    else:
        import urlparse
        result=urlparse.urlparse(currentUrl)
        params=urlparse.parse_qs(result.query,True)
        for index, item in enumerate(params[pageParam]):
            currentPageNum = int(item)
        return currentPageNum+int(pageStep)

