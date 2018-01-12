#!/usr/bin/env python
# -*- coding: utf8 -*
def triple_trouble(one, two, three):
    # zipped = zip(one, two, three)
    # ret_str = ''
    # for x in zipped:
    #     ret_str += ''.join(x)
    # return ret_str

    # one line
    return ''.join(''.join(x) for x in zip(one, two, three))


print(triple_trouble("aaa", "bbb", "ccc"))
