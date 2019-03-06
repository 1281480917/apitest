from common.parser import *
def diff_response(resp_obj, expected_resp_json,content_type):
    '''
    响应和测试用例差异比较
    :param resp_obj: 实际响应接口的Response实例
    :param expected_resp_json:测试用例中描述的response部分
    :return:diff_content:差异结果
    '''
    resp_info =parse_response_object(resp_obj)
    if content_type=='application/json':
        diff_content=diff_json(resp_info,expected_resp_json)
    # 对比 status_code，将差异存入 diff_content
    # 对比 Headers，将差异存入 diff_content
    # 对比 Body，将差异存入 diff_content

    return diff_content
def diff_json(current_json, expected_json):
    '''
    对比json数据并存入字典
    :param current_json: 原始响应数据json格式
    :param expected_json: 测试用例json格式响应
    :return: json_diff:返回差异
    '''
    json_diff = {}

    for key, expected_value in expected_json.items():
        value = current_json.get(key, None)
        if str(value) != str(expected_value):
            json_diff[key] = {
                '实际响应': value,
                '预期响应': expected_value
            }

    return json_diff