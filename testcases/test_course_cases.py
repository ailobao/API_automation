import pytest
import api.course_api as course_api
from conftest import common_assert
from conftest import get_token_by_type
from utils.data_json_loader import load_test_data


class TestCourseCases():

    add_cases = load_test_data("course_data.json").get("add_course", [])
    query_cases = load_test_data("course_data.json").get("query_course_list", [])
    query_detail_cases = load_test_data("course_data.json").get("query_course", [])
    delete_cases= load_test_data("course_data.json").get("delete_course", [])

    def _call_api(self,get_token_by_type, test_data,api_func):
        token_type = test_data.get("token_type", "valid")
        token = get_token_by_type(token_type)
        result = api_func(token=token, **test_data.get("params", {}))
        common_assert(result, test_data["expected_code"], test_data["expected_msg"])
        print(f"✅ {test_data['name']} 通过")
        return result

    @pytest.mark.parametrize("test_data", add_cases)
    def test_add_course(self, get_token_by_type, test_data):

        self._call_api(get_token_by_type, test_data, course_api.course_add)

    @pytest.mark.parametrize("test_data", query_cases)
    def test_get_course_list(self, get_token_by_type, test_data):
        result = self._call_api(get_token_by_type, test_data, course_api.get_course_list)

        if "expected_total" in test_data:
            actual_total = result.get("total")
            expected_total = test_data["expected_total"]
            assert actual_total == expected_total, \
                f"总数错误: 期望{expected_total}, 实际{actual_total}"

    @pytest.mark.parametrize('test_data', query_detail_cases)
    def test_course_detail(self, get_token_by_type, test_data):
        self._call_api(get_token_by_type, test_data, course_api.get_course_detail)

    @pytest.mark.parametrize("test_data", delete_cases)
    def test_course_delete(self, get_token_by_type, test_data):
        self._call_api(get_token_by_type, test_data, course_api.course_delete)
