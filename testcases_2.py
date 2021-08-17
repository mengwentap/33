import unittest


class TestC(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("执行一次前置条件")
    #
    # def tearDown(self) -> None:
    #     print("执行一次后置处理")

    def test_001(self):
        print("执行用例C001")

    def test_007(self):
        print("执行冒烟用例C007")

    def test_004(self):
        print("执行用例C004")

    def test_002(self):
        print("执行用例C002")

    def test_003(self):
        print("执行用例C003")
class TestD(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("执行一次前置条件")
    #
    # def tearDown(self) -> None:
    #     print("执行一次后置处理")

    def test_001(self):
        print("执行用例D001")

    def test_007(self):
        print("执行冒烟用例D007")

    def test_004(self):
        print("执行用例D004")

    def test_002(self):
        print("执行用例D002")

    def test_003(self):
        print("执行用例D003")
if __name__ == '__main__':
    unittest.main()


    # suit = unittest.TestSuite()
    # suit.addTest(TestA('test_007'))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)


    load = unittest.TestLoader()
    suit1 = load.loadTestsFromTestCase(TestC)
    suit2 = load.loadTestsFromTestCase(TestD)
    suits = unittest.TestSuite([suit1][suit2])
    run = unittest.TextTestRunner()
    run.run(suits)