#coding:utf-8
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
    try: 
        #设置超时时间为15秒
        r = urllib2.urlopen(req,timeout=5)
          
        html = r.read()        #返回网页内容
        #receive_header = r.info()     #返回的报头信息
          
        # sys.getfilesystemencoding() 
        #html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding()) #转码:避免输出出现乱码 
    except socket.error:
        continue
    #print receive_header

    return html
def WorkInTime(Func, Timeout = 0, *args): 
    '''
    If function cann't finished in time then timeout
    '''
    import signal
    def handler(signum, frame):    
        raise AssertionError

    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(Timeout)
        ret = Func(*args)
        signal.alarm(0)
        return ret
    except AssertionError:
        logger.error("%s conn't finished in %d seconds, timeout!" % (Func.__name__, Timeout))
        return -1

WorkInTime(getUrlContent,'http://www.baidu.com')

