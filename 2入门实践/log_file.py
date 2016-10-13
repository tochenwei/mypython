# -*- coding: utf-8 -*-
'''
在日志文件里记录日志
'''
import logging
import math

logger = logging.getLogger()
#set loghandler
file = logging.FileHandler("log_file.log")
logger.addHandler(file)
#set formater
#formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
file.setFormatter(formatter) 
#set log level
'''
logging提供多种级别的日志信息，如：NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL等。
'''
logger.setLevel(logging.NOTSET)


for i in range(0,10):
	logger.info(str(i))
