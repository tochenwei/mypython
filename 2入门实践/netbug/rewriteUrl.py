#encoding:utf-8
'''
@description:在有url重写的情况下，根据当前url,分页参数,下一页的页号产生下一页的链接
@return:string
@author:chenwei
'''
def getNextPageUrl(currentUrl,pageParam,nextPageNum):
    if pageParam not in currentUrl:
        return ''
    else:
        import re
        strinfo = re.compile(pageParam+'[\d]+')
        nextPageUrl = strinfo.sub(pageParam+str(nextPageNum),currentUrl)
        return nextPageUrl
'''
@description:在有url重写的情况下，根据当前url,分页参数,分页的间隔,返回下一页的页号
@return int
@author:chenwei
'''
def getNextPageNum(currentUrl,pageParam,startPageNum=1,pageStep=1):
    if pageParam not in currentUrl:
        return startPageNum+int(pageStep)
    else:
        import re
        pattern = re.compile(pageParam+"\d+")
        currentPage = pattern.findall(currentUrl)
        for v in currentPage:
            cPageNum = int(v.replace(pageParam,''))
            nextPageNum = cPageNum + pageStep
        return nextPageNum
        
currentUrl   = 'http://www.baidu.com/article/p_1.html'
pageParam    = 'p_'
startPageNum = 1
pageStep     = 1
nextPageNum = getNextPageNum(currentUrl,pageParam,startPageNum,pageStep)
print getNextPageUrl(currentUrl,pageParam,nextPageNum)
