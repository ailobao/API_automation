import os
import shutil
import pytest

# 清理旧报告
allure_dir = "./reports/allure_results"
if os.path.exists(allure_dir):
    shutil.rmtree(allure_dir)
    print(f"已清理旧报告: {allure_dir}")

# 运行测试
pytest.main([
    'testcases/',
    '--alluredir=./reports/allure_results',
    '-v', '-s'
])

# 生成报告
os.system('allure serve reports/allure_results')