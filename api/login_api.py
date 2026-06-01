# utils/login_api.py
import requests
import config

def get_uuid():
    """获取验证码UUID"""
    resp = requests.get(f'{config.BASE_URL}{config.LOGIN_PATH_CAPTCHAIMAGE}')
    if resp.status_code == 200:
        return resp.json().get('uuid')
    return None


def login(username="admin", password="HM_2023_test", code="2", uuid=None):
    # 如果没有传uuid，自动获取
    if uuid is None:
        uuid = get_uuid()
        if uuid is None:
            return {"code": 500, "msg": "获取验证码失败"}
    # 构建请求数据
    login_data = {
        'username': username,
        'password': password,
        'code': code,
        'uuid': uuid
    }
    # 发送登录请求
    resp = requests.post(f'{config.BASE_URL}{config.LOGIN_PATH}', json=login_data)

    if resp.status_code != 200:
        return {"code": resp.status_code, "msg": "请求失败"}
    return resp.json()


def get_token():
    result = login()
    if result.get("code") == 200:
        return result.get("token")
    return None


if __name__ == '__main__':
    # 测试
    print("=== 测试登录 ===")
    result = login()
    print(f"登录结果: {result}")

    print("\n=== 测试获取Token ===")
    print(f"Token: {get_token()}")