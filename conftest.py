import pytest


# @pytest.fixture(autouse="true")
# @pytest.fixture(scope="module")

# @pytest.fixture(params=["参数1", "参数2"])
# def myfixture(request):
#     print('执行myfixture,-----------> %s' % request.param)

# @pytest.fixture(params=["参数1", "参数2"])
# def connect_db(request):
#     print("开始连接数据库")
#     yield request.param
#     print("关闭数据库")

@pytest.fixture(scope="module")
def myfixture():
    print("开始计算")
    yield
    print("结束计算")


def pytest_collection_modifyitems(session, config, items):
    """
    解决中文乱码
    :param session:
    :param config:
    :param items:
    :return:
    """
    print(type(items))
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
