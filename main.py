import unittest
test_dir ="C:\\Users\\Apple\\PycharmProjects\\pythonProject\\30day\\day25\\tecase"
dis = unittest.defaultTestLoader.discover(test_dir,pattern="testcases*.py")

# 创建套件
suit = unittest.TestSuite()
suit.addTest(dis)
run = unittest.TextTestRunner()
run.run(suit)