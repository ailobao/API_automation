import pytest
import random
import api.contract_api as contract_api
from conftest import common_assert
from conftest import get_token_by_type
from utils.data_json_loader import load_test_data

class TestContractCases():

    add_cases = load_test_data("contract_data.json").get('add_contract',[])
    query_list_cases = load_test_data("contract_data.json").get('query_contract_list',[])
    remove_cases = load_test_data("contract_data.json").get('contract_remove',[])

    def _common(self, get_token_by_type, test_data):
        token_type = test_data.get("token_type", "valid")
        token = get_token_by_type(token_type)
        params = test_data.get("params", {}).copy()
        return token, params

    @pytest.mark.parametrize("test_data", add_cases)
    def test_add_contract(self, get_token_by_type, test_data):
        token, params = self._common(get_token_by_type, test_data)
        if params.get("contractNo") == "AUTO":
            params["contractNo"] = f"HT{random.randint(100000000, 999999999)}"

        result = contract_api.contract_add(token=token, **params)
        common_assert(result, test_data["expected_code"], test_data["expected_msg"])
        print(f"✅ {test_data['name']} 通过")

    @pytest.mark.parametrize("test_data", query_list_cases)
    def test_query_contract_list(self, get_token_by_type, test_data):
        token, params = self._common(get_token_by_type, test_data)

        result = contract_api.get_contract_list(token=token, **params)
        common_assert(result, test_data["expected_code"], test_data["expected_msg"])
        print(f"✅ {test_data['name']} 通过")

    # 删除：特殊处理id参数名不同
    @pytest.mark.parametrize("test_data", remove_cases)
    def test_delete_contract(self, get_token_by_type, test_data):
        token, params = self._common(get_token_by_type, test_data)

        if params.get("id") == "dynamic":
            list_result = contract_api.get_contract_list(token=token)
            if list_result.get("rows"):
                params["id"] = list_result["rows"][0].get("id")
            else:
                pytest.skip("没有可删除的合同")

        contract_id = params.get("id")
        result = contract_api.contract_remove(token=token, id=contract_id)

        # 测试层根据返回内容判断期望的 code
        expected_code = test_data["expected_code"]
        actual_code = result.get("code")
        actual_msg = result.get("msg", "")

        # 如果期望失败，但 HTTP 状态码是 200，需要根据 msg 内容重新判断
        if expected_code == 500 and actual_code == 200:
            if "缺少" in actual_msg or "失败" in actual_msg:
                actual_code = 500

        assert actual_code == expected_code, f"期望{expected_code}, 实际{actual_code}"

        if test_data.get("expected_msg"):
            assert test_data["expected_msg"] in actual_msg

        print(f"✅ {test_data['name']} 通过")