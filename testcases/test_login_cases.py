# testcases/test_login_cases.py
import allure
import pytest

import conftest
from api.login_api import login
from utils.data_json_loader import load_test_data

class TestLoginCases:
    cases = list(load_test_data("login_data.json").values())
    @pytest.mark.parametrize("test_data", cases)
    def test_login(self, test_data, valid_uuid):

            if test_data.get("uuid") == "valid":
                uuid = valid_uuid
            else:
                uuid = test_data.get("uuid")

            username = test_data.get("username")
            password = test_data.get("password")
            code = test_data.get("code")
            result = login(
                username=username,
                password=password,
                code=code,
                uuid=uuid
            )
            conftest.common_assert(
                result,
                business_code=test_data["expected_code"],
                msg=test_data["expected_msg"]
            )

            # 成功场景额外验证token
            if test_data["expected_code"] == 200:
                assert result.get("token") is not None
                print(f"✅ 登录成功")
            else:
                print(f"✅ 失败场景验证通过")
