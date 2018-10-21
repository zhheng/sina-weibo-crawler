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
    return [WCrawler(cookie=cookie, max_num_weibo=0, max_num_fans=30, max_num_follow=30,
                     max_num_page=3, wfilter='all', return_type='json')
            for cookie in list]


if __name__ == '__main__':
    # set to your own cookie
    crawlers = get_crawler()
    # queue = ['https://weibo.cn/yaochen']
    # queue = ['https://weibo.cn/1557721227']

    queue = set(get_user_list())

    visited = set(get_visited_user_list())
    print("[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "] init visited...")

    queue = list(queue - visited)
    print("[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "] init queue...")

    while len(queue) > 0:
        url = queue[0]
        queue = queue[1:]
        if url in visited:
            continue
        if not_visited(url):
            try:
                crawler = crawlers[random.randint(0, len(crawlers) - 1)]

                json_data = crawler.crawl(url)
                save(json_data)
                visited.add(url)
                queue += list(
                    set([user['url'] for user in json_data['follow']] + [user['url'] for user in json_data['fans']]))

                print("[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "] save...")
            except:
                print("[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "] except...")
        time.sleep(random.randint(1, 5))
    pass
