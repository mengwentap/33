import unittest
test_dir ="C:\\Users\\Administrator\\PycharmProjects\\30day\\day27\\cases"
dis = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

# 创建套件
suit = unittest.TestSuite()
suit.addTest(dis)
run = unittest.TextTestRunner()
run.run(suit)