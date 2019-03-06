import os
from common import loader
from common.test_runner import test_runner
import allure,pytest,logging
@allure.story('模块')
@pytest.mark.parametrize('testcases',loader.load_yaml_file('data/case/case.yaml'),ids=loader.test_yaml_name('data/case/case.yaml'))
def test_run_single_testcase_success(testcases):
   success, _ = test_runner().run_single_testcase(testcases['test'])
   allure.attach(str(testcases), '测试用例')
   assert success
@allure.story('模块')
@pytest.mark.parametrize('testcases',loader.load_testcase('data/case/testcases/scenario_A.yaml'),ids=loader.test_case_name('data/case/testcases/scenario_A.yaml'))
def test_run_api_testcase_success(testcases):
   success, _ = test_runner().run_work_flow_testcase(testcases['test'])
   allure.attach(str(testcases), '测试用例')
   assert success