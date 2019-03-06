from common import loader
from common import dynamic_execution
def api_v1_Account_Login_POST(UserName, Password):
    all_api=loader.load_yaml_file(r'data/case/api/v1/Account.yaml')
    api={}
    api['UserName']=UserName
    api['Password'] = Password
    for i in all_api:
        if i['api'].pop('def')=='api_v1_Account_Login_POST($UserName, $Password)':
                api.update(i['api'])
    api=dynamic_execution.get_eval_value(api)
    api.pop('UserName')
    api.pop('Password')
    print(api)
    return api

def api_v1_Account_LoginOff_GET():
    all_api = loader.load_yaml_file(r'data/case/api/v1/Account.yaml')
    api = {}
    for i in all_api:
        if i['api'].pop('def') == 'api_v1_Account_LoginOff_GET()':
            api.update(i['api'])
    api = dynamic_execution.get_eval_value(api)
    print(api)
    return api
if __name__ == '__main__':
    api_v1_Account_Login_POST(1,2)
    api_v1_Account_LoginOff_GET()