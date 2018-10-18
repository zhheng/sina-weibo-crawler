__author__ = 'LiGe'
#encoding:utf-8
import pymongo
import os
import csv

class mongodb(object):
    def __init__(self, ip, port):
        self.ip=ip
        self.port=port
        self.conn=pymongo.MongoClient(ip,port)

    def close(self):
        return self.conn.disconnect()

    def get_conn(self):
        return self.conn


def get_user_list():
    conn = mongodb('127.0.0.1', 27017)
    data_conn = conn.get_conn()
    dc = data_conn.weibo
    return [u['url'] for u in dc.user.find()]


def get_visited_user_list():
    conn = mongodb('127.0.0.1', 27017)
    data_conn = conn.get_conn()
    dc = data_conn.weibo
    return [u['url'] for u in dc.info.find()]


def not_visited(url):
    conn = mongodb('127.0.0.1', 27017)
    data_conn = conn.get_conn()
    dc = data_conn.weibo
    return dc.info.find_one({'url':url}) is None


def save(json_data):
    conn = mongodb('127.0.0.1', 27017)
    data_conn = conn.get_conn()
    dc = data_conn.weibo

    list3 = [user for user in json_data['follow']] + [user for user in json_data['fans']]
    list3.append({"nickname": json_data['nickname'],
                  "num_fans": json_data['num_fans'],
                  "url": json_data['url'],
                  "verify_type": "RED_V"})
    for f in list3:
        if dc.user.find_one({'url': f['url']}) is None:
            dc.user.insert({
                "nickname": f['nickname'],
                "num_fans": f['num_fans'],
                "url": f['url'],
                "verify_type": f['verify_type']
            })

    if dc.info.find_one({'url': json_data['url']}) is None:
        dc.info.insert({
            "uid": json_data['uid'],
            "url": json_data['url'],
            "gender": json_data['gender'],
            "good_at": json_data['good_at'],
            "location": json_data['location'],
            "nickname": json_data['nickname'],
            "num_fans": json_data['num_fans'],
            "num_follow": json_data['num_follow'],
            "num_weibo": json_data['num_weibo'],
            "relationship_status": json_data['relationship_status'],
            "self-intro": json_data['self-intro'],
            "sexual_orientation": json_data['sexual_orientation'],
            "verify_info": json_data['verify_info'],
            "birthday": json_data['birthday'],
            "follow":json_data['follow'],
            "fans":json_data['fans'],
        })
