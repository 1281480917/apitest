import io
import json
import yaml
import configparser
import logging
from common.dynamic_execution import *
###############################################################################
##   file loader
###############################################################################
def _check_format(file_path, content):
    """ 检查测试用例格式（如果有效）
    """
    # TODO: 替换为JSON模式验证

    if not content:

        # testcase file content is empty

        err_msg = u"Testcase file content is empty: {}".format(file_path)

        logging.error(err_msg)
    elif not isinstance(content, (list, dict)):

        # testcase file content does not match testcase format

        err_msg = u"Testcase file content format invalid: {}".format(file_path)

        logging.error(err_msg)
def load_testcase(file):
    testsuit=load_yaml_file(file)
    moudules=testsuit[0]['config']['import_module_functions']
    import_module_functions(moudules)
    testsuit=get_eval_value(testsuit)
    testsuit.pop(0)
    print(testsuit)
    return testsuit
def load_yaml_file(yaml_file):
    '''
    加载yaml文件并检查文件内容格式
    :param yaml_file:
    :return:
    '''
    with io.open(yaml_file, 'r', encoding='utf-8') as stream:

        yaml_content = yaml.load(stream)
        #logging.info('加载用例文件:%s'%yaml_content)
        _check_format(yaml_file, yaml_content)
        return yaml_content
def load_json_file(json_file):
    '''
    加载yaml文件并检查文件内容格式
    :param json_file:
    :return:
    '''
    with io.open(json_file, encoding='utf-8') as data_file:
        try:
            json_content = json.load(data_file)
        except Exception as e:
            err_msg = u"JSONDecodeError: JSON file format error: {}".format(json_file)
            logging.error(err_msg)
        _check_format(json_file, json_content)
        return json_content
def load_ini_file():
    cfgpath='data/cfg.ini'
    conf=configparser.ConfigParser()
    conf.read(cfgpath,encoding='utf-8')
    print(conf)
    return conf
def test_case_name(file):
    cases=load_testcase(file)
    name_list = []
    for case in cases:
        name = case['test']['name']
        name_list.append(name)
    return name_list
def test_yaml_name(file):
    texts=load_yaml_file(file)
    name_list=[]
    for text in texts:
        name=text['test']['name']
        name_list.append(name)
    return name_list
if __name__ == '__main__':
    #load_testcase(r'data/case/testcases/scenario_A.yaml')
    load_ini_file()