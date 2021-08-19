import unittest
import requests
import urllib3
urllib3.disable_warnings()
from day27.com.excel_read import Excel_read


# from ddt import ddt,data,unpack,file_data
# @ddt
# class TestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.cookies = ""
#     @file_data('..data/login2.yaml')
#     def test_001(self, accout, password,ex):
#         url = "https://testadmin.99yuei.com/login/login.action"
#         data = {"account": accout, "password": password}
#         res = requests.post(url, data, stream=True, verify=False)
#         msg = res.json()["success"]
#         self.assertEqual(msg, ex)
#         TestCase.cookies = res.cookies
#
#     def test_002(self):
class TestCase(unittest.TestCase):
    def test_001(self):
        a = Excel_read().getExcel('../data/case.xlsx')
        for i in a:
            url = i.get("url")
            body = i.get("body")
            header = {"Content-Type": "application/x-www-form-urlencoded"}
            res = requests.post(url, data=body, headers=header, stream=True, verify=False)
            msg =res.json()["success"]
            self.assertEqual(msg,"true")

if __name__ == '__main__':
    unittest.main()










