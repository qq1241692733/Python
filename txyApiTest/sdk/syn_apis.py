"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-07-2023/7/1
    Time: 21:53
"""

import requests
from _pytest import config
import json
from common.file_load import load_yaml_file, load_json_file


def describeReplicateJobs(t, seqID="e510f060-1810-11ee-8530-8fc20400e86d"):

    url = 'https://db-api.cloud.tencent.com/api/server-cloud3/dts-supeross/DescribeReplicateJobs'
    header = {
        "cookie": load_json_file('/config/secre.json')["cookie"],
        "x-csrfcode": "1924125362",
        "x-qcloud-user-id": "1307234544",
        "x-seqid": "e510f060-1810-11ee-8530-8fc20400e86d"
    }
    prams = {
        "t": t,
        "seqId": seqID
    }
    data = {"Region":"ap-shanghai","Offset":0,"Limit":20,"Order":"CreateTime","OrderSeq":"DESC"}
    resq = requests.post(url=url, headers=header, params=prams, data=data).json()
    print(resq)
    return resq


