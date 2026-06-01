"""
pytest 全局配置文件 - 简化版（Allure兼容）
"""
import pytest
from api.login_api import get_uuid, get_token, login

@pytest.fixture
def valid_uuid():
    """获取有效的uuid"""
    uuid = get_uuid()
    if uuid is None:
        pytest.fail("获取uuid失败")
    print(f"\n📋 UUID: {uuid}")
    return uuid

@pytest.fixture(scope="session")
def valid_token():
    """获取有效的token"""
    token = get_token()
    if token is None:
        pytest.fail("获取token失败")
    print(f"\n🔑 Token: {token[:50]}...")
    return token

@pytest.fixture
def get_token_by_type():
    def _get(token_type="valid"):
        if token_type == "valid":
            return get_token()
        elif token_type == "missing":
            return None  # 缺失：不传Authorization头
        elif token_type == "empty":
            return ""  # 空字符串
        elif token_type == "invalid":
            return "invalid-token-12345"  # 无效token
        elif token_type == "expired":
            return "expired-token-12345"  # 过期token（用固定字符串模拟）
        return get_token()
    return _get

@pytest.fixture(autouse=True)
def test_logger(request):
    """自动记录每个用例的开始和结束"""
    case_name = request.node.name
    print(f"\n{'='*50}")
    print(f"📝 开始执行用例: {case_name}")

    yield

    print(f"✅ 用例执行完毕: {case_name}")
    print(f"{'='*50}")

def pytest_configure(config):
    """配置测试标记"""
    config.addinivalue_line("markers", "smoke: 冒烟测试")
    config.addinivalue_line("markers", "negative: 负向测试")

def common_assert(res, business_code=200, msg='成功'):
    actual_code = res.get('code')
    actual_msg = res.get('msg', '')
    assert actual_code == business_code, \
        f"业务code错误: 期望{business_code}, 实际{actual_code}"
    assert msg in actual_msg, \
        f"业务消息错误: 期望包含'{msg}', 实际'{actual_msg}'"



# 修正：直接调用 API 函数测试，而不是 fixture
if __name__ == '__main__':
    print("=== 测试 get_uuid ===")
    uuid = get_uuid()
    print(f"UUID: {uuid}")

    print("\n=== 测试 get_token ===")
    token = get_token()
    print(f"Token: {token[:50] if token else None}...")

    print("\n=== 测试 login ===")
    result = login()
    print(f"登录结果: code={result.get('code')}, msg={result.get('msg')}")