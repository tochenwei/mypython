#coding:utf-8
def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()   
        m.update(str)
        return m.hexdigest()
    else:
        return ''
def sha1(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        return hashlib.sha1(str).hexdigest()
    else:
        return ''
def crc32(str):
        """
        Generates the crc32 hash of the v.
        @return: str, the str value for the crc32 of the v
        """
        import binascii
        #取crc32的八位数据 %x返回16进制数后转成10进制
        return int('0x%x' % (binascii.crc32(str) & 0xffffffff),16)
