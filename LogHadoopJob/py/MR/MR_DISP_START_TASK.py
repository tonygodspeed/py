#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_DISP_START_TASK"
class MR_DISP_START_TASK(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID',   'type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'i', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'err_type','type':'i', 'mt':r'err_type:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'last_err','type':'i', 'mt':r'last_err:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'run_ret','type':'i', 'mt':r'run_ret:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'task_name','type':'s', 'mt':r'task_name:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'task_ver','type':'s', 'mt':r'task_ver:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_DISP_START_TASK()

if __name__ == '__main__':
    test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8032BCS5|S:DISPATCHER|PROD:KWSHELLEXT|DISVER:1.0.6.9051|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.6.9051|GID:78|CHID:MUSIC8032BCS5|PN:rundll32.exe|MAC:2C600C383BB5|UAC:0|ADMIN:1|ST:1473523203|CFGVER:8|ACT:ACT_DISP_START_TASK|err_type:0|last_err:0|run_ret:0|task_name:1007|task_ver:1.0.1.3|{}|U:>(122.188.16.215)TM:1473523199'
    mr_obj.LocalTest(test_str)
    pass
