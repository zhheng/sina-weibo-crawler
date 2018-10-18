#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from mongodb import *
from wcrawler import *
import random
import sys


def get_crawler():
    return [WCrawler(
                cookie='SCF=Ak0iONoGebfHR0NAtTW0CmAZx6EjcwU03z5VAc3lw-EV2_vqH1RWltCEZ9cb3QUtsyVIrqLe49jZQ_YemVADSEw.; SUHB=0cS3DxJFGoM6z_; _T_WM=d2f6835d079626b49080c098489fb2d3; SSOLoginState=1539784958; ALF=1542375494; SUB=_2A252wzCuDeRhGeVP4lUX-CfMyT2IHXVSTFDmrDV6PUJbktAKLVTgkW1NTTnhI5zuavezQaLEG5W0DB558BsG18I4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFyflfjSq9Cbw_FHi695g4y5JpX5K-hUgL.Foep1KMc1h.7eo22dJLoI7yoSJn4P0Mfe7tt', \
                max_num_weibo=0, \
                max_num_fans=20, \
                max_num_follow=20, \
                max_num_page=2, \
                wfilter='all', \
                return_type='json'),
            WCrawler(
                cookie='_T_WM=97ea6d6559090059dc838f6fd8f3c0bd; ALF=1542037139; SCF=AmgqUtXVZtz-IzMlC2KvS0q5yUyW75FdldFmJc9-LTOJOAGtm6lES5EulseTinzZ3ijFxUD0AXbv8FSP-gHdI-A.; SUB=_2A252xmHMDeRhGeBJ7VcQ9ybJyTmIHXVSSQ-ErDV6PUJbktANLRXZkW1NRilphGJnUEN39rursTrHdx7ggQdalgno; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFeZhPUbIIUONDmcPy9uRfo5JpX5K-hUgL.FoqNSo-pS0nfeo-2dJLoIpRLxK-LBo5L12qLxKML12eLBoBLxK-LB-BL1KWbqJqt; SUHB=0G0-GGcPqvU1-A; SSOLoginState=1539445148', \
                max_num_weibo=0, \
                max_num_fans=20, \
                max_num_follow=20, \
                max_num_page=2, \
                wfilter='all', \
                return_type='json')
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
        time.sleep(random.randint(4, 9))
    pass
