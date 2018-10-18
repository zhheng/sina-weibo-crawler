#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from mongodb import *
from wcrawler import *
from mysql import *
import random
import sys


def get_crawler():
    list = get_cookies()
    return [WCrawler(
                cookie=cookie, \
                max_num_weibo=0, \
                max_num_fans=20, \
                max_num_follow=20, \
                max_num_page=2, \
                wfilter='all', \
                return_type='json') for cookie in list
            ]


if __name__ == '__main__':
    # set to your own cookie
    crawlers = get_crawler()
    # queue = ['https://weibo.cn/yaochen']
    # queue = ['https://weibo.cn/1557721227']

    queue = get_user_list()

    visited = set(get_visited_user_list())
    while len(queue) > 0:
        url = queue[0]
        queue = queue[1:]
        if url in visited:
            continue
        if not_visited(url):
            try:
                crawler = crawlers.pop()
                json_data = crawler.crawl(url)
                save(json_data)
                visited.add(url)
                queue += list(
                    set([user['url'] for user in json_data['follow']] + [user['url'] for user in json_data['fans']]))
            except:
                if len(crawlers) == 0:
                    crawlers = get_crawler()
                    crawler = crawlers.pop()
            finally:
                print("[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "] save...")
        time.sleep(random.randint(3, 6))
    pass
