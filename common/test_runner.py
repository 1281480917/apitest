import requests
from common import difference
import allure
from common.dynamic_execution import *
from common import loader
class test_runner():
    def run_single_testcase(self,testcase):
        '''
        单个接口测试用例执行引擎
        :param testcase:读取到的测试用例
        :return:success:bool用例通过还是不通过，diff_content:预期结果与响应的差异
        '''
        import_module_functions(testcase['import_module_functions'])
        value=get_eval_value(testcase)
        logging.debug('get_eval_value:%s'%value)
        logging.info('执行用例%s'%testcase['name'])
        req_kwargs =testcase['request']
        try:
            url = req_kwargs.pop('url')
            method = req_kwargs.pop('method')
        except KeyError:
            raise logging.error("Params Error")
        logging.info('请求数据:%s'%str(req_kwargs))
        resp_obj = requests.request(url=url, method=method, **req_kwargs)
        logging.info('响应数据;%s'%str(resp_obj.text))
        diff_content = difference.diff_response(resp_obj, testcase['response'],testcase['request']['headers']['Content-Type'])
        logging.info('预期响应与实际响应的差异:%s'%diff_content)
        success = False if diff_content else True
        allure.attach(str(req_kwargs), '请求数据')
        allure.attach(str(testcase['response']),'预期响应')
        allure.attach(str(resp_obj), '实际响应')
        allure.attach(str(diff_content), '预期响应与实际响应的差异')
        return success, diff_content
    def run_work_flow_testcase(self,testcase):
        logging.info('执行用例%s' % testcase['name'])
        req_kwargs = testcase['api']['request']
        host=loader.load_ini_file().get('system','host')
        try:
            url = host+req_kwargs.pop('url')
            method = req_kwargs.pop('method')
        except KeyError:
            raise logging.error("Params Error")
        logging.info('请求数据:%s' % str(req_kwargs))
        resp_obj = requests.request(url=url, method=method, **req_kwargs)
        logging.info('响应数据;%s' % str(resp_obj.text))
        diff_content = difference.diff_response(resp_obj, testcase['api']['response'],
                                                testcase['api']['request']['headers']['Content-Type'])
        logging.info('预期响应与实际响应的差异:%s' % diff_content)
        success = False if diff_content else True
        allure.attach(str(req_kwargs), '请求数据')
        allure.attach(str(testcase['api']['response']), '预期响应')
        allure.attach(str(resp_obj), '实际响应')
        allure.attach(str(diff_content), '预期响应与实际响应的差异')
        return success, diff_content