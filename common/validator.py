import re,logging
import types
def is_functon(content):
    '''
    如果是函数，则返回true。
    :param content:
    :return:
    '''
    function_regexp = re.compile(r"^\$\{(\w+)\(([\$\w =,]*)\)\}$")
    try:
        matched = function_regexp.match(content)
    except TypeError:
        matched=False

    return True if matched else False
def is_variable(tup):
    '''
    如果是变量，则返回true。
    :param tup:
    :return:
    '''
    item = tup
    if callable(item):
        # function or class
        return False
    if isinstance(item, types.ModuleType):
        # imported module
        return False
    if is_functon(item):
        return False
    return True
