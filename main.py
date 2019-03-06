import subprocess,time,pytest,allure
pytest.main(['-v','-l','-s','--alluredir=data\\pytestreport','--clean-alluredir'])
cmd = ['allure','serve','data\\pytestreport','-o','data\\report','--clean']
i = subprocess.Popen(cmd,cwd=r'E:\code\apitest', shell=True,stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                     stderr=subprocess.PIPE, encoding='gb2312')