import urllib2
 
requset = urllib2.Request('http://www.xxxxx.com')
try:
    urllib2.urlopen(requset)
except urllib2.URLError, e:
    print e.reason