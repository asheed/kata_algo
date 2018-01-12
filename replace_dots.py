#!/usr/bin/env python
# -*- coding: utf8 -*

import re
def replace_dots(str):
    return re.sub(r"[.]", "-", str)

if __name__ == "__main__":
    print(replace_dots(""))
    print(replace_dots("no dots"))
    print(replace_dots("one.two.three"))
    print(replace_dots("........"))