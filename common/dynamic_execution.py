import importlib
from common.parser import *
from common.validator import *
def import_module_functions(modules):
    '''
    导入函数并加入上下文
    :param modules: 需要导入的模块名
    :return:
    '''
    for module_name in modules:
       imported = importlib.import_module(module_name)
       logging.debug(imported)
       imported_functions_dict = dict(filter(is_function, vars(imported).items()))
       logging.debug('imported_functions_dict:%s'%imported_functions_dict)
       __update_context_config("functions", imported_functions_dict)
def is_function(tup):
    '''
    判断用例是否是函数
    :param tup: 元祖
    :return:
    '''
    name, item = tup
    return isinstance(item, types.FunctionType)
testcase_config={"functions":{}}
def __update_context_config(type,func_dict):
    testcase_config[type]=func_dict

testcase_variables_mapping={}
func_dict={}

def get_eval_value(data):
   '''
   以递归方式计算数据，将计算数据中的每个变量,并执行模板函数
   :param data: 用例结构化数据
   :return: 计算好的用例数据
   '''
   if isinstance(data, (list, tuple)):
       return [get_eval_value(item) or item for item in data]
   if isinstance(data, dict):
       evaluated_data = {}
       for key, value in data.items():
           evaluated_data[key] = get_eval_value(value) or value
           if value != None:
                testcase_variables_mapping.update(evaluated_data)
       return evaluated_data
   if isinstance(data, (int, float)):
       return data
   # data is in string format here
   data = "" if data is None else data.strip()
   if is_variable(data):
       # variable marker: $var
       variable_list = extract_variables(data)
       if variable_list!=[]:
           for variable_name in variable_list:
               value = testcase_variables_mapping.get(variable_name) or data
               return value
   elif is_functon(data):
       # function marker: ${func(1, 2, a=3, b=4)}
       fuction_meta = parse_string_functions(data)
       logging.debug('function_meta:%s'%fuction_meta)
       func_name = fuction_meta['func_name']
       args = fuction_meta.get('args', [])
       kwargs = fuction_meta.get('kwargs', {})
       args = get_eval_value(args)
       kwargs = get_eval_value(kwargs)
       for i in range(len(args)):
           for (key,value) in func_dict.items():
               if isinstance(args[i], dict):
                   args[i]=str(args[i])
               if key==args[i]:
                   args[i]=value
       func_value=testcase_config["functions"][func_name](*args, **kwargs)
       func_dict[data]=func_value
       for (key,value) in testcase_variables_mapping.items():
           for (key1,value1) in func_dict.items():
                if value==key1:
                    testcase_variables_mapping[key]=value1
       return func_value
   else:
       return data