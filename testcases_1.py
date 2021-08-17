import unittest


class TestA(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("执行一次前置条件")
    #
    # def tearDown(self) -> None:
    #     print("执行一次后置处理")

    def test_001(self):
        print("执行用例001")

    def test_007(self):
        print("执行冒烟用例007")

    def test_004(self):
        print("执行用例004")

    def test_002(self):
        print("执行用例002")

    def test_003(self):
        print("执行用例003")
class TestB(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("执行一次前置条件")
    #
    # def tearDown(self) -> None:
    #     print("执行一次后置处理")

    def test_001(self):
        print("执行用例B001")

    def test_007(self):
        print("执行冒烟用例B007")

    def test_004(self):
        print("执行用例B004")

    def test_002(self):
        print("执行用例B002")

    def test_003(self):
        print("执行用例B003")
if __name__ == '__main__':
    unittest.main()


    # suit = unittest.TestSuite()
    # suit.addTest(TestA('test_007'))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)


    load = unittest.TestLoader()
    suit1 = load.loadTestsFromTestCase(TestA)
    suit2 = load.loadTestsFromTestCase(TestB)
    suits = unittest.TestSuite([suit1][suit2])
    run = unittest.TextTestRunner()
    run.run(suits)