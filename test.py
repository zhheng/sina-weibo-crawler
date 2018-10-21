#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mongodb import *

def set_test():
    return [1,2,3,4,5,4,3,3,7]


l = set(get_visited_user_list())


print(len(l))