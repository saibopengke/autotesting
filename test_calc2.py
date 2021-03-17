import allure
import pytest
import yaml
from pythoncode.Calculator import Calculator


def get_data(filepath):
    with open(filepath) as f:
        datas = yaml.safe_load(f)
        data_add = datas["add"]
        data_sub = datas["sub"]
        data_mul = datas["mul"]
        data_div = datas["div"]
        data_ids = datas["myid"]
        return [data_add, data_sub, data_mul, data_div, data_ids]


@allure.feature("计算器模块")
class TestCalc2:
    """
    第二次练习，加上数据驱动yaml，fixture,控制用例执行顺序，生成allure测试报告
    """

    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expected",
                             get_data("./data.yml")[0],
                             )
    def test_add(self, a, b, expected, myfixture):
        """
        加
        :param a:
        :param b:
        :param expected:
        :param myfixture:
        :return:
        """
        assert expected == self.cal.add(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expected",
                             get_data("./data.yml")[1],
                             )
    def test_sub(self, a, b, expected, myfixture):
        """
        减
        :param a:
        :param b:
        :param expected:
        :param myfixture:
        :return:
        """
        assert expected == self.cal.sub(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expected",
                             get_data("./data.yml")[2])
    def test_mul(self, a, b, expected, myfixture):
        """
        乘
        :param a:
        :param b:
        :param expected:
        :param myfixture:
        :return:
        """
        assert expected == self.cal.mul(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expected",
                             get_data("./data.yml")[3])
    def test_div(self, a, b, expected, myfixture):
        """
        除
        :param a:
        :param b:
        :param expected:
        :param myfixture:
        :return:
        """
        assert expected == self.cal.div(a, b)


if __name__ == '__main__':
    pytest.main()
