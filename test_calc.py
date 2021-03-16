import pytest
from pythoncode.Calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print('开始执行')

    def teardown_class(self):
        print('结束执行')

    @pytest.mark.parametrize("a,b,expected", [
        (3, 5, 8), (3, 2, 5), (100, 200, 300)
    ], ids=["first_num", "second_num", "expected_num"])
    def test_add(self, a, b, expected):
        assert expected == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,expected", [
        (8, 5, 3)
    ])
    def test_sub(self, a, b, expected):
        assert expected == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expected", [
        (3, 2, 6)
    ])
    def test_mul(self, a, b, expected):
        assert expected == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expected", [
        (4, 2, 2)
    ])
    def test_div(self, a, b, expected):
        assert expected == self.cal.div(a, b)
