"""
    Created with PyCharm.
    Description:
    文档注释 一般用于 方法的注释和类的注释
    User: hong yaO
    Date: 2023-07-2023/7/1
    Time: 21:50
"""
import time

from common.random_util import cur_timestamp
from sdk.syn_apis import describeReplicateJobs


class Testsyn:

    def test_describeReplicateJobs(self):
        time = cur_timestamp()
        resp = describeReplicateJobs(t=time)
        assert resp["code"] == 0
