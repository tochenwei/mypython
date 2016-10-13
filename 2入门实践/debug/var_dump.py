from __future__ import print_function
from types import NoneType

__author__ = "Shamim Hasnath"
__copyright__ = "Copyright 2013, Shamim Hasnath"
__license__ = "BSD License"
__version__ = "1.0.1"


TAB_SIZE = 4


infs = []

def display(o, space, num, key, typ):
    st = ""
    l = []
    if key:
        if typ is dict:
            st += " " * space + "['%s'] => "
        else:
            st += " " * space + "%s => "
        l.append(key)
    elif space > 0:
        st += " " * space + "[%d] => "
        l.append(num)
    else:  # at the very start
        st += "#%d "
        l.append(num)

    if type(o) in (tuple, list, dict, int, str, float, long, bool, NoneType, unicode):
        st += "%s(%s) "
        l.append(type(o).__name__)

        if type(o) in (int, float, long, bool, NoneType):
            l.append(o)
        else:
            l.append(len(o))

        if type(o) in (str, unicode):
            st += '"%s"'
            l.append(o)

    elif isinstance(o, object):
        st += "object(%s) (%d)"
        l.append(o.__class__.__name__)
        l.append(len(getattr(o, '__dict__', {})))

    #print(st % tuple(l))
    infs.append(st % tuple(l))

def display_s(o, space, num, key, typ):
    st = ""
    l = []
    if key:
        if typ is dict:
            st += " " * space + "['%s']=>"
        else:
            st += " " * space + "%s=>"
        l.append(key)
    # elif space > 0:
    #     st += " " * space + "[%d] => "
    #     l.append(num)
    # else:  # at the very start
    #     st += "#%d "
    #     l.append(num)

    if type(o) in (tuple, list, dict, int, str, float, long, bool, NoneType, unicode):
        st += "%s"
        # l.append(type(o).__name__)

        if type(o) in (int, float, long, bool, NoneType):
            l.append(o)
        else:
            l.append('')

        if type(o) in (str, unicode):
            st += '"%s"'
            l.append(o)

    elif isinstance(o, object):
        st += "%s"
        l.append(o.__class__.__name__)
        # l.append(len(getattr(o, '__dict__', {})))

    #print(st % tuple(l))
    infs.append(st % tuple(l))


def dump(o, space, num, key, typ):

    if type(o) in (str, int, float, long, bool, NoneType, unicode):
        display(o, space, num, key, typ)

    elif isinstance(o, object):
        display(o, space, num, key, typ)
        num = 0
        if type(o) in (tuple, list, dict):
            typ = type(o)  # type of the container of str, int, long, float etc
        elif isinstance(o, object):
            o = getattr(o, '__dict__', {})
            typ = object
        for i in o:
            space += TAB_SIZE
            if type(o) is dict:
                dump(o[i], space, num, i, typ)
            else:
                dump(i, space, num, '', typ)
            num += 1
            space -= TAB_SIZE

def dump_s(o, space, num, key, typ):

    if type(o) in (str, int, float, long, bool, NoneType, unicode):
        display_s(o, space, num, key, typ)

    elif isinstance(o, object):
        display_s(o, space, num, key, typ)
        num = 0
        if type(o) in (tuple, list, dict):
            typ = type(o)  # type of the container of str, int, long, float etc
        elif isinstance(o, object):
            o = getattr(o, '__dict__', {})
            typ = object
        for i in o:
            space += TAB_SIZE
            if type(o) is dict:
                dump_s(o[i], space, num, i, typ)
            else:
                dump_s(i, space, num, '', typ)
            num += 1
            space -= TAB_SIZE

def _get_space_num(s):
    i = 0
    for c in s:
        if c == ' ':
            i+=1
        else:
            break
    s = s[i:]
    return i,s

def var_dump(*obs):
    """
      shows structured information of a object, list, tuple etc
    """
    global infs
    infs = []
    i = 0
    for x in obs:
        dump(x, 0, i, '', object)
        i += 1
    for inf in infs:
        print(inf)

def var_dump_s(*obs):
    """
      shows structured information of a object, list, tuple etc
    """
    global infs
    infs = []
    i = 0
    for x in obs:
        dump_s(x, 0, i, '', object)
        i += 1
    strs = []
    bsn = 0
    for inf in infs:
        sn, s = _get_space_num(inf)
        if sn > bsn:
            strs.append('{')
        if sn < bsn:
            strs.append('}, ')
        if sn == bsn and sn != 0:
            strs.append(', ')
        strs.append(s)
        bsn = sn
    while bsn > 0:
        strs.append('}')
        bsn = bsn - TAB_SIZE

    return ''.join(strs)