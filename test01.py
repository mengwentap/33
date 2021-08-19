import requests
import unittest

from day27.com.sql import Sql
from ddt import ddt, file_data
@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cookies = ""
    @file_data('../data/login2.yaml')
    def test_001(self, accout, password,ex):
        url = "https://testadmin.99yuei.com/login/login.action"
        data = {"account": accout, "password": password}
        res = requests.post(url, data, stream=True, verify=False)
        msg = res.json()["success"]
        self.assertEqual(msg, ex)
        TestCase.cookies = res.cookies


    @file_data('../data/erban.yaml')
    def test_002(self, erban,):
        self.uid =""
        url2="https://testadmin.99yuei.com/admin/userCheckAdmin/getlist.action"
        params ={"pageSize":"10","pageNumber":"1","erbanNoList":erban,"type":"1","_":"1628739333509"}
        res2 =requests.get(url2,params=params,cookies=TestCase.cookies,stream=True, verify=False)
        goldNum= res2.json()['data'][0]['userPurseVo']['goldNum']
        self.uid =res2.json()['data'][0]['users']['uid']
        gold_num1=Sql().sql_data('select gold_num from user_purse where uid = {}'.format(self.uid))[0][0]
        self.assertEqual(goldNum, gold_num1)
if __name__ == '__main__':
    unittest.main()