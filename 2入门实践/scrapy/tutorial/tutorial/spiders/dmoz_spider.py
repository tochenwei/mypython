#coding:utf-8
import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            '''
            xpath 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表
            extract序列化该节点为unicode字符串并返回list
            '''
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            '''
            把描述抓取后进行处理，先去除换行和水平制表符，然后去除首尾空格
            '''
            item['desc'] = sel.xpath('text()').extract()
            item['desc'] = ''.join(item['desc'])
            item['desc'] = item['desc'].replace("\r",'').replace("\n",'').replace("\t",'');
            item['desc'] = item['desc'].strip();
            '''
            yield的功能类似于return，但是不同之处在于它返回的是生成器
            生成器是通过一个或多个yield表达式构成的函数，每一个生成器都是一个迭代器（但是迭代器不一定是生成器）。
            
            如果一个函数包含yield关键字，这个函数就会变为一个生成器。

            生成器并不会一次返回所有结果，而是每次遇到yield关键字后返回相应结果，并保留函数当前的运行状态，等待下一次的调用。

            由于生成器也是一个迭代器，那么它就应该支持next方法来获取下一个值。
            '''
            yield item
